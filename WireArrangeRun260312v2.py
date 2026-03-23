"""江乙加Eric 最大排線程式""" 
import os
import sys
import datetime
import csv
import math
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QListView, QComboBox, QMenuBar, QMenu,
                                QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, QFileDialog, QDoubleSpinBox, QSpinBox,
                                QLineEdit)
from PySide6.QtCore import Qt, QDateTime, QDate, QUrl, QRect, QPoint
from PySide6.QtGui import (QIcon, QPixmap, QFont, QTextDocument, QPageLayout, QPageSize, QImage, QPen, 
                            QPdfWriter, QTextCursor, QTextTableFormat, QTextCharFormat, QTextImageFormat,
                            QColor, QTextBlockFormat, QTextTableCellFormat, QTextLength, QPainter)
from arrange0312_ui import Ui_Arrange

def resource_path(relative_path):
    """ 取得資源絕對路徑，兼容開發與 PyInstaller 打包模式 """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 運行時的臨時資料夾路徑
        return os.path.join(sys._MEIPASS, relative_path)
    # 開啟開發模式下的路徑
    return os.path.join(os.path.abspath("."), relative_path)

#主畫面
class MyMainWindow(QMainWindow, Ui_Arrange): 
    version = " v1.1"
    Developer = " 江乙加 Eric Chiang"
    ver_date = " 2026-03-11"
    Copyright = f" 2026 {Developer}" #" 2026 " + Developer
    
    """initial"""
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)  # 這一行沒寫，提示絕對出不來
        # --- 【核心修改】預載入 Logo 資源 ---
        self.logo_pixmap = QPixmap(resource_path("Assets/Mylogo.png"))
        self.style_pixmap = QPixmap(resource_path("Assets/Mystyle.png"))
        self.current_lang = "TW" # 開機語言

        self.init_ui_settings() # 設定圖示與預設圖
        self.set_default_value() # 預設值
        self.load_languages() #載入語言
        #if not self.load_settings(): self.current_lang = "TW" # 設定初始語言，這要對應到你的檔名
        self.Switch_language() #切換語言
        self.connect_signals() # 啟動所有按鈕與輸入框的「電線」連線！
        self.coords_calculation() # 座標計算
        self.Process_clear() # 清除紀錄
    """設定視窗圖示與初始排線圖"""
    def init_ui_settings(self):
        self.setWindowIcon(QIcon(self.style_pixmap)) #設定視窗圖示
        if hasattr(self, "Language"):
            self.Language.setIcon(QIcon(resource_path("Assets/Earth.png")))
        
        self.update_image("Arrange.png") # 預設顯示排線示意圖
    """預設值"""
    def set_default_value(self):
        self.in_pa_001.setValue(1.0000)
        self.in_pa_002.setValue(10.7951)
        self.in_pa_003.setValue(10.8723)
        self.in_pa_004.setValue(7.8818)
    """ 自動掃描 Languages 資料夾並載入所有 JSON """
    def load_languages(self):
        self.languages = {}
        lang_dir = resource_path("Languages") # 你的語言包資料夾
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)
            return

        for filename in os.listdir(lang_dir):
            if filename.endswith(".json"):
                lang_key = filename.replace(".json", "") # 例如 "en_US"
                try:
                    with open(os.path.join(lang_dir, filename), 'r', encoding='utf-8') as f:
                        self.languages[lang_key] = json.load(f)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
    """自動選單語言切換"""
    def auto_translate_menu(self, menu_obj: QMenuBar | QMenu, lan_dict: dict):
        """ 
        純文字切換版：只負責更新 QAction/QMenu 的文字內容。
        """
        for action in menu_obj.actions():
            obj_name = action.objectName()
            submenu = action.menu()

            # 1. 處理 QAction 與 QMenu 的名稱連動偵測
            if not obj_name and submenu:
                obj_name = submenu.objectName()

            # 2. 匹配 JSON 並僅更新文字
            if obj_name in lan_dict:
                data = lan_dict[obj_name]
                # 相容兩種格式：如果是字典就拿 "text"，如果是純字串就直接用
                text = data["text"] if isinstance(data, dict) else data
                
                action.setText(text) # 更新 Action 文字
                if submenu:
                    submenu.setTitle(text) # 同步更新選單標題
                    # 遞迴翻譯子選單
                    self.auto_translate_menu(submenu, lan_dict)
    """切換語言"""
    def Switch_language(self):
        if not self.languages: return
        lang = self.languages.get(self.current_lang, {})
        # 1. 視窗標題
        self.setWindowTitle(lang.get("Window_main", {}).get("Winding", "繞線排線計算"))
        # 2. 選單列
        self.auto_translate_menu(self.menuBar(), lang.get("Menubar", {}))
        # 3. 批次處理分類元件 (QLabel, QPushButton, QCombobox, Data1)
        t_default = lang.get("QLabel", {}).get("textFont", {"font_size": 14, "font_family": "Microsoft YaHei"})
        categories = ["QLabel", "QPushButton", "QCombobox", "Data1"]
        for cat in categories:
            cat_data = lang.get(cat, {})
            for obj_name, data in cat_data.items():
                if obj_name == "textFont": continue # 跳過字體設定項
                
                widget = getattr(self, obj_name, None)
                if widget:
                    # 文字設定
                    content = data.get("text", "")
                    if isinstance(widget, QComboBox) and isinstance(content, list):
                        idx = widget.currentIndex()
                        widget.clear()
                        widget.addItems(content)
                        widget.setCurrentIndex(idx)
                    elif hasattr(widget, "setText"):
                        widget.setText(content)
                    
                    # 字體設定
                    f_size = data.get("font_size", t_default.get("font_size"))
                    f_family = data.get("font_family", t_default.get("font_family"))
                    widget.setFont(QFont(f_family, f_size))
    """繁簡英切換"""                
    def switch_language_tc(self):
        self.current_lang = "TW"
        self.Switch_language()   
    def switch_language_sc(self):
        self.current_lang = "CN"
        self.Switch_language()  
    def switch_language_en(self):
        self.current_lang = "EN"
        self.Switch_language()     
    """集中處理所有按鈕與輸入框的連線"""
    def connect_signals(self):
        # --- 使用 lambda 精簡按鈕連線 ---
        # 格式：lambda: self.change_mode("圖片檔名", "模式名稱")
        #按鈕
        self.PB_chart.clicked.connect(lambda: self.change_mode("Arrange.png", "繞線示意"))
        self.PB_chart_A.clicked.connect(lambda: self.change_mode("ArrangeA.png", "方式A"))
        self.PB_chart_B.clicked.connect(lambda: self.change_mode("ArrangeB.png", "方式B"))
        self.PB_chart_C.clicked.connect(lambda: self.change_mode("ArrangeC.png", "方式C"))
        self.PB_Calculate.clicked.connect(self.arrange_calculation)
        self.PB_Clear_process.clicked.connect(self.Process_clear)
        #檔案選項
        self.file_exit.triggered.connect(self.close)
        self.file_reset.triggered.connect(self.set_default_value)
        self.language_tc.triggered.connect(self.switch_language_tc)
        self.language_sc.triggered.connect(self.switch_language_sc)
        self.language_en.triggered.connect(self.switch_language_en)






        # --- 座標連動：改用 editingFinished (Enter 或 離開時觸發) ---
        spinbox_group = [
            self.in_pa_002, self.in_pa_003, self.in_pa_004, # AB, BC, CD 長度
            self.in_pa_005, self.in_pa_006                  # Bx, By 基準點
        ]
        for sb in spinbox_group:
            sb.editingFinished.connect(self.coords_calculation)    
    """通用切換模式功能"""
    def change_mode(self, img_file, mode_name):
        self.update_image(img_file)
        # 讀取並更新文字紀錄 (UI 中為 Process)
        now = datetime.datetime.now().strftime('%H:%M:%S')
        # 直接追加一行，不用先讀取舊文字再拼接
        self.Process.append(f"[{now}] 切換至 {mode_name}")
    """通用換圖助手"""
    def update_image(self, filename):
        path = resource_path(f"Assets/{filename}")
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            self.arrange_image.setPixmap(pixmap)
            self.arrange_image.setScaledContents(True)
        else:
            self.arrange_image.setText(f"找不到檔案: {filename}")
    """座標核心計算法"""
    def coords_calculation(self):
        try:
            # 1. 取得數值
            ab, bc, cd = self.in_pa_002.value(), self.in_pa_003.value(), self.in_pa_004.value()
            bx, by = self.in_pa_005.value(), self.in_pa_006.value()
            # 2. 定義座標映射表
            coord_map = {
                self.Coordinate_AX: bx,
                self.Coordinate_AY: ab + by,
                self.Coordinate_CX: bx + bc,
                self.Coordinate_CY: by,
                self.Coordinate_DX: bx + bc,
                self.Coordinate_DY: by + cd
            }
            # 3. 批量更新
            for widget, val in coord_map.items():
                widget.setValue(val)
            # 4. 紀錄
            self.Process.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] 座標更新完成")
            # 5. 回傳座標資料
            return {
                "A": (bx, ab + by),
                "B": (bx, by),
                "C": (bx + bc, by),
                "D": (bx + bc, by + cd),
                "AB": ab,
                "BC": bc,
                "CD": cd
            }
        except Exception as e:
            print(f"計算錯誤: {e}")
    """計算所有組合"""
    def arrange_calculation(self):
        self.PB_Calculate.setEnabled(False)
        #1. 計算座標
        coords_data = self.coords_calculation()
        if not coords_data: return
        #2. 清除紀錄
        self.Process_clear()
        try:
            # 1. 取得數值
            wire_diam = self.in_pa_001.value() # 直徑
            wire_rad = wire_diam / 2 # 半徑
            cross_sectional_area = math.pi * (wire_rad**2) #線截面積            
            ab_l, bc_l, cd_l = coords_data["AB"], coords_data["BC"], coords_data["CD"]
            ax, ay = coords_data["A"] #coords_Ax, coords_Ay, coords_Dx, coords_Dy = coords_data["A"][0], coords_data["A"][1], coords_data["D"][0], coords_data["D"][1]
            # 2. 排線幾何常數
            layer_pitch =(math.sqrt(3) / 2) * wire_diam #第2層後占用高度
            slope = (ay - coords_data["D"][1]) / (ax - coords_data["D"][0]) # AD斜率,斜率是負的，這條線在座標圖上是「從左上往右下」傾斜的
                       
            """計算相關數據**顯示用**"""
            usable_area = ((ab_l + cd_l) * bc_l) / 2 # 繞線梯形面積
            angle_ADa = math.degrees(math.atan2(ab_l - cd_l, bc_l)) # ∠ADa'
            total_layers_ab = 1 + int((ab_l - wire_diam) / (math.sqrt(3) * wire_rad)) #typeAB 總層數
            total_layers_c = int(ab_l / wire_diam) #typeC總層數
            square_layers_ab = 1 + int((cd_l - wire_diam) / (math.sqrt(3) * wire_rad)) #typeAB 方形層數
            square_layers_c = int(cd_l / wire_diam) #typeC 方形層數
            triangle_layers_ab = total_layers_ab - square_layers_ab #typeAB 三角形層數
            triangle_layers_c = total_layers_c - square_layers_c #typeC 三角形層數
            triangle_Height = ab_l - cd_l # 三角形高
            """----------"""
            # 3. 建立統一字典
            type_list = ["A", "B", "C"]
            self.winding_results = {}
            
            for type_name in type_list:
                turns = 0
                rate = 0.0
                self.winding_results[type_name] = {"total_turns": turns, "fill_rate": rate}
                square_layers = square_layers_c if type_name == "C" else square_layers_ab

                """建立type A方形各層資料{Type: {"層":(0:coordsX, 1:coordsY, 2:Turns, 3:Height)}}"""
                for i in range(1, square_layers + 1):
                    layer_key = f"L{i}"
                    if type_name == "A":
                        map_x = (2 * wire_rad) if i % 2 == 0 else wire_rad
                        map_y = wire_rad + (i - 1) * layer_pitch
                    elif type_name == "B":
                        map_x = wire_rad if i % 2 == 0 else (2 * wire_rad)
                        map_y = wire_rad + (i - 1) * layer_pitch
                    else:
                        map_x = wire_rad    
                        map_y = wire_rad + (i - 1) * wire_diam
                    if type_name == "C":
                        map_turns = int(bc_l / wire_diam)
                        map_height = wire_diam + (i - 1) * wire_diam
                    else:
                        map_turns = int((bc_l - (map_x - wire_rad)) / wire_diam)
                        map_height = wire_diam + (i - 1) * layer_pitch

                    # 寫入字典
                    self.winding_results[type_name][layer_key] = (map_x, map_y, map_turns, map_height)
                    turns += map_turns
                    #self.winding_results[type_name]["total_turns"] = turns
                    # 顯示記錄值
                    self.Process.append(f"方式: {type_name}_ {layer_key}: ({map_x:.4f}, {map_y:.4f}, {map_turns:.0f}, {map_height:.4f})")

                square_last_height = cd_l - self.winding_results[type_name][f"L{square_layers}"][3] # 方形剩餘高度
                """建立type A三角形各層資料{"層":(0:coordsX, 1:coordsY, 2:Turns, 3:Height)}"""
                """
                AD直線方程式 : y - y1 = m(x - x1)
                >>> mx + y + k = 0
                >>> A = -m, B = 1, C = mx1 - y1  
                x1,y1用A(0, 10.7951)座標帶入 : y - 10.7951 = -0.2679(x - 0)
                >>> 0.2679 x + y - 10.7951= 0
                >>>A = 0.2679, B = 1, C = -10.7951
                圓心到CD距離d = |Axi + Byi + C| / √(A^2 + B^2)
                """
                eq_A, eq_B, eq_C = -slope, 1, (slope * ax -ay)
                triangle_layers = triangle_layers_c if type_name == "C" else triangle_layers_ab
                for j in range(1, triangle_layers + 1):
                    layer_num = square_layers + j # 三角形第一層=方形最總層數+1
                    layer_key = f"L{layer_num}"
                    if type_name == "A":
                        map_x = (2 * wire_rad) if layer_num % 2 == 0 else wire_rad
                        map_y = wire_rad + (layer_num - 1) * layer_pitch
                    elif type_name == "B":
                        map_x = wire_rad if layer_num % 2 == 0 else (2 * wire_rad)
                        map_y = wire_rad + (layer_num - 1) * layer_pitch
                    else:
                        map_x = wire_rad    
                        map_y = wire_rad + (layer_num - 1) * wire_diam

                    # 利用 while 迴圈精確計算每一層能塞幾根，直到撞到 AD 斜邊
                    map_turns = 0
                    while True:
                        test_x = map_x + (map_turns * wire_diam)
                        # 點到直線距離公式
                        dist = abs(eq_A * test_x + eq_B * map_y + eq_C) / math.sqrt(eq_A**2 + eq_B**2)
                        # 判斷：不能超過右邊界 C 點，且不能撞到 AD 斜邊
                        if (test_x + wire_rad) > bc_l or dist < wire_rad:
                            break
                        map_turns += 1

                    if map_turns <= 0: break
                    map_height = (wire_diam - square_last_height) + (j - 1) * wire_diam if type_name == "C" else (layer_pitch - square_last_height) + (j - 1) * layer_pitch
                    self.winding_results[type_name][layer_key] = (map_x, map_y, map_turns, map_height)
                    turns += map_turns
                    self.Process.append(f"方式: {type_name}_ {layer_key}: ({map_x:.4f}, {map_y:.4f}, {map_turns:.0f}, {map_height:.4f})")
                self.winding_results[type_name]["total_turns"] = turns  
                rate = (turns * cross_sectional_area * 100) / usable_area # 槽滿率
                self.winding_results[type_name]["fill_rate"] = rate
                self.Process.append(f"方式: {type_name} 總圈數: {turns:.0f} 槽滿率: {rate:.4f}")


            # 1. 找出總圈數最多的方式
            # 使用 max 函式搭配 lambda 來比較字典裡的數值
            best_type = max(self.winding_results, key=lambda t: self.winding_results[t]["total_turns"])
            best_turns = self.winding_results[best_type]["total_turns"]
            best_rate = self.winding_results[best_type]["fill_rate"]

            # 2. 建立總結訊息
            summary_msg = (
            f"🏆 計算完成！最優排列建議：方式 {best_type}\n"
            f"--------------------------------\n"
            f"最大總圈數：{best_turns:.0f} 圈\n"
            f"佔空率：{best_rate:.4f}%\n"
            f"--------------------------------\n"
            f"已自動將 UI 數值更新為最優方案。"
        )

            # 3. 顯示彈出視窗
            QMessageBox.information(self, "最優方案推薦", summary_msg) 

            """更新 UI 顯示"""
            self.Cross_sectional_area.setValue(cross_sectional_area) #線截面積
            self.Usable_area.setValue(usable_area) #繞線面積
        
        except Exception as e:
            print(f"計算錯誤: {e}")
        self.PB_Calculate.setEnabled(True)            
    """清除紀錄"""
    def Process_clear(self):
        self.Process.clear()
        #now = datetime.datetime.now().strftime('%H:%M:%S')
        #self.Process.append(f"[{now}] 紀錄已成功清空。")
    """輸出csv"""
    def export_to_csv(self):
        default_dir = os.path.join(os.getcwd(), "Data")
        if not os.path.exists(default_dir): os.makedirs(default_dir)
        default_filename = f"Winding_Data_{QDateTime.currentDateTime().toString('yyyyMMdd_HHmmss')}.csv"
        initial_path = os.path.join(default_dir, default_filename)
        
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        myWin = MyMainWindow()
        myWin.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"啟動失敗: {e}")
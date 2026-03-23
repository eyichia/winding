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
from arrange0309_ui import Ui_Arrange

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

        self.init_ui_settings()    # 1. 設定圖示與預設圖
        self.set_default_value() # 預設值
        self.connect_signals()     # 2. 啟動所有按鈕與輸入框的「電線」連線！
        self.coords_calculation()
        self.Process_clear()
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
    """集中處理所有按鈕與輸入框的連線"""
    def connect_signals(self):
        # --- 使用 lambda 精簡按鈕連線 ---
        # 格式：lambda: self.change_mode("圖片檔名", "模式名稱")
        self.PB_chart.clicked.connect(lambda: self.change_mode("Arrange.png", "繞線示意"))
        self.PB_chart_A.clicked.connect(lambda: self.change_mode("ArrangeA.png", "方式A"))
        self.PB_chart_B.clicked.connect(lambda: self.change_mode("ArrangeB.png", "方式B"))
        self.PB_chart_C.clicked.connect(lambda: self.change_mode("ArrangeC.png", "方式C"))
        self.PB_Calculate.clicked.connect(self.do_calculation)
        self.PB_Clear_process.clicked.connect(self.Process_clear)

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
    """排列計算"""
    def do_calculation(self):
        #1. 計算座標
        coords_data = self.coords_calculation()
        if not coords_data: return
        #2. 清除紀錄
        self.Process_clear()
        try:
            # 1. 取得數值
            wire_diam = self.in_pa_001.value() # 直徑
            wire_rad = wire_diam / 2 # 半徑
            ab_l, bc_l, cd_l = coords_data["AB"], coords_data["BC"], coords_data["CD"]
            ax, ay = coords_data["A"] #coords_Ax, coords_Ay, coords_Dx, coords_Dy = coords_data["A"][0], coords_data["A"][1], coords_data["D"][0], coords_data["D"][1]
            # 2. 排線幾何常數
            layer_pitch =(math.sqrt(3) / 2) * wire_diam #第2層後占用高度
            slope = (ay - coords_data["D"][1]) / (ax - coords_data["D"][0]) # AD斜率,斜率是負的，這條線在座標圖上是「從左上往右下」傾斜的
            # 3. 建立統一字典
            type_list = ["A", "B", "C"]
            self.winding_results = {}
            total_turns = 0
            
            """計算相關數據**顯示用**"""
            usable_area = ((ab_l + cd_l) * bc_l) / 2 # 繞線梯形面積
            angle_ADa = math.degrees(math.atan2(ab_l - cd_l, bc_l)) # ∠ADa'
            total_layers_AB = 1 + int((ab_l - wire_diam) / (math.sqrt(3) * wire_rad)) #typeAB 總層數
            total_layers_D = int(ab_l / wire_diam) #typeD總層數
            square_layers_AB = 1 + int((cd_l - wire_diam) / (math.sqrt(3) * wire_rad)) #typeAB 方形層數
            square_layers_D = int(cd_l / wire_diam) #typeD 方形層數
            triangle_layers_AB = total_layers_AB - square_layers_AB #typeAB 三角形層數
            triangle_layers_D = total_layers_D - square_layers_D #typeD 三角形層數
            triangle_Height = ab_l - cd_l # 三角形高
            """----------"""

            """建立type A方形各層資料{"層":(0:coordsX, 1:coordsY, 2:Turns, 3:Height)}"""
            for i in range(1, square_layers_AB + 1):
                layer_key = f"L{i}"
                map_x = (2 * wire_rad) if i % 2 == 0 else wire_rad
                map_y = wire_rad + (i - 1) * layer_pitch
                map_turns = int((bc_l - (map_x - wire_rad)) / wire_diam)
                map_height = wire_diam + (i - 1) * layer_pitch
                # 寫入字典
                self.winding_results[layer_key] = (map_x, map_y, map_turns, map_height)
                total_turns += map_turns
                # 顯示記錄值
                self.Process.append(f"已紀錄 {layer_key}: ({map_x:.4f}, {map_y:.4f}, {map_turns:.0f}, {map_height:.4f})")

            square_last_Height = cd_l - self.winding_results[f"L{square_layers_AB}"][3] # 方形剩餘高度
            
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
            for j in range(1, triangle_layers_AB + 1):
                layer_num = square_layers_AB + j # 三角形第一層=方形最總層數+1
                layer_key = f"L{layer_num}"
                map_x = (2 * wire_rad) if layer_num % 2 == 0 else wire_rad
                map_y = wire_rad + (layer_num - 1) * layer_pitch

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
                self.winding_results[layer_key] = (map_x, map_y, map_turns, map_height)
                total_turns += map_turns
                self.Process.append(f"已紀錄 {layer_key}: ({map_x:.4f}, {map_y:.4f}, {map_turns:.0f}, {map_height:.4f})")
            
            """更新 UI 顯示"""
            self.Cross_sectional_area.setValue(math.pi * (wire_rad**2)) #線截面積
            self.Usable_area.setValue(usable_area) #繞線面積
            self.Slot_fill_rate.setValue((total_turns * self.Cross_sectional_area.value() * 100) / self.Usable_area.value())
        except Exception as e:
            print(f"計算錯誤: {e}")
    """計算所有組合"""
    def arrange_calculation(self):
        # 3. 建立統一字典
        type_list = ["A", "B", "C"]
        self.winding_results = {}
        total_turns = 0

    """清除紀錄"""
    def Process_clear(self):
        self.Process.clear()
        #now = datetime.datetime.now().strftime('%H:%M:%S')
        #self.Process.append(f"[{now}] 紀錄已成功清空。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        myWin = MyMainWindow()
        myWin.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"啟動失敗: {e}")
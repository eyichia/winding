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
        self.PB_Calculate.clicked.connect(self.arrange_calculation)
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
    def arrange_calculation(self):
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
            ax, ay = coords_data["A"]
            dx, dy = coords_data["D"]
            #coords_Ax, coords_Ay, coords_Dx, coords_Dy = coords_data["A"][0], coords_data["A"][1], coords_data["D"][0], coords_data["D"][1]
            slope = (ay - dy) / (ax - dx) # AD斜率,斜率是負的，這條線在座標圖上是「從左上往右下」傾斜的

            usable_area = ((ab_l + cd_l) * bc_l) / 2 # 繞線梯形面積
            angle_ADa = math.degrees(math.atan2(ab_l - cd_l, bc_l)) # ∠ADa'
            
            total_layers_AB = 1 + int((ab_l - wire_diam) / (math.sqrt(3) * wire_rad)) #typeAB 總層數
            total_layers_D = int(ab_l / wire_diam) #typeD總層數
            square_layers_AB = 1 + int((cd_l - wire_diam) / (math.sqrt(3) * wire_rad)) #typeAB 方形層數
            square_layers_D = int(cd_l / wire_diam) #typeD 方形層數
            triangle_layers_AB = total_layers_AB - square_layers_AB #typeAB 三角形層數
            triangle_layers_D = total_layers_D - square_layers_D #typeD 三角形層數
            second_layer_height =(math.sqrt(3) / 2) * wire_diam #第2層後占用高度
            #second_layer_height =wire_diam - (2 * (wire_rad- ((wire_rad * math.sqrt(3)) / 2))) #第2層後占用高度
            triangle_Height = ab_l - cd_l # 三角形高
            total_turns = 0
            """建立type A方形各層資料{"層":(0:coordsX, 1:coordsY, 2:Turns, 3:Height)}"""
            square_data_mapA = {}
            for i in range(1, square_layers_AB + 1):
                map_key = f"L{i}"
                map_coordX = (2 * wire_rad) if i % 2 == 0 else wire_rad
                map_coordY = wire_rad + (i - 1) * second_layer_height
                map_turns = int((bc_l - (map_coordX - wire_rad)) / wire_diam)
                map_height = wire_diam + (i - 1) * second_layer_height
                square_data_mapA[map_key] = (map_coordX, map_coordY, map_turns, map_height)
                # 取得資料元組
                data = square_data_mapA[map_key]
                self.Process.append(f"已紀錄 {map_key}: ({data[0]:.4f}, {data[1]:.4f}, {data[2]:.0f}, {data[3]:.4f})")

            square_last_Height = cd_l - square_data_mapA[f"L{square_layers_AB}"][3] # 方形剩餘高度
            """建立type A三角形各層資料{"層":(0:coordsX, 1:coordsY, 2:Turns, 3:Height)}"""
            triangle_data_mapA = {}
            for j in range(1, triangle_layers_AB + 1):
                if j == 1:
                    triangle_occupy_height = second_layer_height - square_last_Height # 三角形占用高度
                else:
                    triangle_occupy_height = occupy_height + second_layer_height

                occupy_height = triangle_occupy_height # 記憶上一筆用高度   
                effective_width = bc_l + (triangle_occupy_height / slope) - wire_rad # 三角形有效寬度
                preset_turns = math.ceil(effective_width / wire_diam) # 預設可繞圈數
                print(f'預設可繞圈數{preset_turns}')
                new_layer = square_layers_AB + j
                map_key = f"L{new_layer}"
                if new_layer % 2 == 0:
                    map_coordX = 2 * wire_rad
                else:
                    map_coordX = wire_rad
                map_coordY = wire_rad + (new_layer - 1) * second_layer_height
                # 檢查最後一圈是否超出範圍
                last_turn_coordX = map_coordX + wire_diam * (preset_turns - 1) # 最後1圈座標X
                last_turn_coordY = map_coordY # 最後1圈座標Y
                if last_turn_coordX + wire_rad > bc_l: # 檢查超出方形邊DC
                    beyond_square_edge = "YES"
                else:
                    beyond_square_edge = "NO"
                print(f'檢查超出方形邊DC{beyond_square_edge}')    
                """
                AD直線方程式 : y - y1 = m(x - x1)
                >>> mx + y + k = 0
                >>> A = -m, B = 1, C = mx1 - y1  
                x1,y1用A(0, 10.7951)座標帶入 : y - 10.7951 = -0.2679(x - 0)
                >>> 0.2679 x + y - 10.7951= 0
                >>>A = 0.2679, B = 1, C = -10.7951
                圓心到CD距離d = |Axi + Byi + C| / √(A^2 + B^2)
                
                """
                equation_A = -slope
                equation_B = 1
                equation_C = slope * ax - ay
                check_value = abs(equation_A * last_turn_coordX + equation_B * last_turn_coordY + equation_C) / math.sqrt(equation_A**2 + equation_B**2)
                #print(abs(equation_A * last_turn_coordX + equation_B * last_turn_coordY + equation_C) ,math.sqrt(equation_A**2 + equation_B**2))    
                print(equation_A ,equation_B ,equation_C ,check_value)    
                if beyond_square_edge == "YES" or check_value < wire_rad: # 超出範圍 圈數-1
                    map_turns = int(preset_turns - 1)
                else:    
                    map_turns = int(preset_turns)
                map_height = triangle_occupy_height
                if map_turns <= 0: break
                triangle_data_mapA[map_key] = (map_coordX, map_coordY, map_turns, map_height)
                # 取得資料元組
                data = triangle_data_mapA[map_key]
                self.Process.append(f"已紀錄 {map_key}: ({data[0]:.4f}, {data[1]:.4f}, {data[2]:.0f}, {data[3]:.4f})")
            





            """畫面顯示"""
            self.Cross_sectional_area.setValue(math.pi * (wire_rad**2)) #線截面積
            self.Usable_area.setValue(usable_area) #繞線面積










        except Exception as e:
            print(f"計算錯誤: {e}")

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
"""江乙加Eric 動平衡計算程式""" 
import os
import sys
import datetime
import csv
import math
import json

def resource_path(relative_path):
    """ 取得資源絕對路徑，兼容開發與 PyInstaller 打包模式 """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 運行時的臨時資料夾路徑
        return os.path.join(sys._MEIPASS, relative_path)
    # 開啟開發模式下的路徑
    return os.path.join(os.path.abspath("."), relative_path)

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QListView, QComboBox, QMenuBar, QMenu,
                                QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, QFileDialog, QDoubleSpinBox, QSpinBox,
                                QLineEdit)
from PySide6.QtCore import Qt, QDateTime, QDate, QUrl, QRect, QPoint
from PySide6.QtGui import (QIcon, QPixmap, QFont, QTextDocument, QPageLayout, QPageSize, QImage, QPen, 
                            QPdfWriter, QTextCursor, QTextTableFormat, QTextCharFormat, QTextImageFormat,
                            QColor, QTextBlockFormat, QTextTableCellFormat, QTextLength, QPainter)
from balance0226_ui import Ui_Balance
from grade_info_ui import Ui_GradeDialog
#向量圖
class VectorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.angle = 0  # 角度
        self.is_active = False # 是否顯示向量
        self.is_add_mass = False
        self.setFixedSize(200, 200)

    def update_angle(self, angle, is_add_mass):
        self.angle = angle
        self.is_add_mass = is_add_mass # 儲存狀態
        self.is_active = True
        self.update() # 觸發重繪

    def paintEvent(self, event):
        if not self.is_active:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing) # 抗鋸齒
        
        # 1. 計算圓盤區域
        width = self.width()
        height = self.height()
        side = min(width, height) - 20
        rect = QRect((width - side) // 2, (height - side) // 2, side, side)
        center = rect.center()

        # 2. 畫背景圓盤
        painter.setPen(QPen(Qt.black, 2)) #框粗細
        painter.setBrush(QColor("#f0f0f0"))
        painter.drawEllipse(rect)

        # 3. 畫十字中心線
        painter.setPen(QPen(QColor("gray"), 1, Qt.DashLine))
        painter.drawLine(center.x(), rect.top(), center.x(), rect.bottom())
        painter.drawLine(rect.left(), center.y(), rect.right(), center.y())

        # 4. 畫角度向量 (紅點)
        # 注意：Qt 的角度 0 度在 3 點鐘方向，且是順時針增加。
        # 工業慣例 0 度通常在 12 點鐘方向，逆時針增加，我們需要轉換：
        # 這裡我們採用標準座標：0度在右，逆時針轉
        rad = math.radians(-self.angle + 90) # 修正為 0 度在上方
        radius = side / 2 - 8 #線長
        point_x = center.x() + radius * math.cos(rad)
        point_y = center.y() - radius * math.sin(rad)

        # 加重用綠色，減重用紅色
        dot_color = QColor("#008000") if self.is_add_mass else QColor("#e74c3c")
        # 畫連線
        #painter.setPen(QPen(Qt.red, 2)) #粗細
        painter.setPen(QPen(dot_color, 2))
        painter.drawLine(center.x(), center.y(), int(point_x), int(point_y))

        # 畫端點
        #painter.setBrush(QColor("red"))
        painter.setBrush(dot_color)
        painter.drawEllipse(QPoint(int(point_x), int(point_y)), 4, 4) #大小

        # 標註角度文字
        painter.setPen(Qt.black)
        painter.setFont(QFont("Arial", 10, QFont.Bold))
        painter.drawText(rect.adjusted(5, 5, -5, -5), Qt.AlignTop | Qt.AlignLeft, f"{self.angle:g}°")
#動平等級說明視窗
class GradeInfoWindow(QDialog, Ui_GradeDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # 載入 Designer 的設計內容
        self.main_win = parent # 記住主視窗，方便拿翻譯資料
        
        # --- 1. 設定字體與樣式 (只針對這個視窗) ---
        self.setStyleSheet("""
            QTableWidget {
                font-family: 'Microsoft YaHei';
                font-size: 10pt;  /* 表格內容字體放大 */
                gridline-color: #dcdde1;
                alternate-background-color: #f5f6fa;
            }
            QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                font-family: 'Microsoft YaHei';
                font-size: 14pt;              /* 表頭字體也同步放大 */
                font-weight: bold;
                padding: 6px;  /*「元件內容」與「元件邊框」之間的留白空間,上下左右6px*/
            }
        """)
        
        # 1. 取得表頭物件
        header = self.tableWidget_Grade.horizontalHeader()
        # 2. 先設定模式為「互動式 (Interactive)」或「固定 (Fixed)」
        # 如果設為 Stretch 或 ResizeToContents，手動設定的寬度會失效
        header.setSectionResizeMode(0, QHeaderView.Interactive) 
        header.setSectionResizeMode(1, QHeaderView.Interactive)
        header.setSectionResizeMode(2, QHeaderView.Interactive)
        # 3. 分別設定具體寬度 (單位是像素 px)
        width = [120, 150 ,600]
        for i in range(2):
            self.tableWidget_Grade.setColumnWidth(i, width[i]) # 設定第一欄寬度為 120
        #self.tableWidget_Grade.setColumnWidth(0, 120) # 設定第一欄寬度為 120
        #self.tableWidget_Grade.setColumnWidth(1, 150) # 設定第二欄寬度為 150
        #self.tableWidget_Grade.setColumnWidth(2, 600) # 設定第三欄寬度為 600

        v_header = self.tableWidget_Grade.verticalHeader() # 取得垂直表頭 (控制行高的物件)
        v_header.setDefaultSectionSize(30) # 設定高度為 30
        #self.tableWidget_Grade.setWordWrap(True) # 開啟自動換行 (這是自動長高的前提條件)
        v_header.setVisible(False) #取消「列號」（1, 2, 3,...
        #v_header.setMinimumSectionSize(10) # 這確保了當內容只有一行時，高度不會縮得比 30 還小
        #v_header.setSectionResizeMode(QHeaderView.ResizeToContents)  # 設定調整模式為「根據內容自動縮放」這會讓 Qt 偵測文字行數，若文字多到 30 像素裝不下，它就會自動長高
                
        self.init_table_data()

    def init_table_data(self):
        # 1. 從主視窗拿翻譯包
        lang_name = self.main_win.current_lang
        lang_dict = self.main_win.languages.get(lang_name, {})
        msg_dict = lang_dict.get("Messages", {})
        self.setWindowTitle(msg_dict.get("grade_title", "動平衡等級說明"))
        # 2. 設定表格標題 (表頭翻譯)
        headers = [
            msg_dict.get("grade_h1", "平衡等級 G"),
            msg_dict.get("grade_h2", "量值 (eper​⋅Ω)"),
            msg_dict.get("grade_h3", "適用設備")
        ]
        self.tableWidget_Grade.setHorizontalHeaderLabels(headers)
        # 3. 獲取表格內容
        # 如果 JSON 裡沒定義，就用原本那份作為預設
        data = lang_dict.get("grade_data", [])

        self.tableWidget_Grade.setRowCount(len(data))
        
        for row, row_content in enumerate(data):
            # row_content 現在是一個 list: [等級, 數值, 描述]
            for col, text in enumerate(row_content):
                item = QTableWidgetItem(str(text))
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.tableWidget_Grade.setItem(row, col, item)
                    
        # 4. 欄位縮放設定 (維持原樣)
        # 讓第三欄自動撐滿
        #self.tableWidget_Grade.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        #self.tableWidget_Grade.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget_Grade.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        # 禁止編輯
        self.tableWidget_Grade.setEditTriggers(QTableWidget.NoEditTriggers)
#主畫面
class MyMainWindow(QMainWindow, Ui_Balance): 
    version = " v1.1"
    Developer = " 江乙加 Eric Chiang"
    ver_date = " 2026-02-26"
    Copyright = f" 2026 {Developer}" #" 2026 " + Developer
    # 單位轉換因素<不同單位需轉換倍率>
    Unit_Eccentricity = {"m": 0.001, "mm": 1, "µm": 1000, "ft": 0.00328084, "in": 0.0393701} #偏心距
    Unit_CentrifugalForce = {"N": 1, "gf": 101.9716213, "lbf": 0.2248089431, "ozf": 3.5969430896} #離心力  
    Unit_CorrectionMass = {"kg": 1, "g": 10**3, "mg": 10**6, "lb": 2.2046226218, "oz": 35.27396195} #修正量

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 1. 建立向量圖實體
        self.vector_graph = VectorWidget()
        
        # 2. 找到你在 Designer 規劃好的容器，並把圖加進去
        if hasattr(self, "container_vector"):
            # 取得該容器的佈局 (Layout)
            layout = self.container_vector.layout()
            if layout is None:
                # 如果你在 Designer 忘了設佈局，這裡手動補一個
                layout = QVBoxLayout(self.container_vector)
            
            # 將向量圖加入佈局中，它會自動對齊並填滿
            layout.addWidget(self.vector_graph)
            layout.setAlignment(Qt.AlignCenter)

        # --- 【核心修改】預載入 Logo 資源 ---
        # 先檢查檔案是否存在，並讀進記憶體
        self.style_image = QImage(resource_path("Assets/Mystyle.png"))
        self.style_pixmap = QPixmap.fromImage(self.style_image)
        self.logo_image = QImage(resource_path("Assets/Mylogo.png"))
        self.logo_pixmap = QPixmap.fromImage(self.logo_image)
        self.setWindowIcon(QIcon(self.style_pixmap)) #設定視窗圖示
        if hasattr(self, "Language"):
            icon_path = resource_path("Assets/Earth.png") # 指向 Assets 資料夾
            self.Language.setIcon(QIcon(icon_path))


        self.init_ui_object_style() #設定Ui物件樣式
        self.init_combobox_data() #設定清單內容
        #self.set_default_value() #數值初始化
        self.connect_signal() #連結會觸發計算的訊號
        self.init_param_list() #參數轉陣列
        self.load_languages() #載入語言
        if not self.load_settings():
            # 設定初始語言，這要對應到你的檔名
            self.current_lang = "TW"
            self.set_default_value() # 原本的硬編碼初始值

        self.Switch_language() #切換語言
        self.do_calculation() # 啟動後立刻計算一次，更新向量圖
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
    
    def save_settings(self):
        # 1. 定義資料夾與路徑
        config_dir = "Config"
        config_path = os.path.join(config_dir, "config.json")
        # 2. 如果資料夾不存在，就建立它
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        """ 將當前 UI 狀態儲存至 config.json """
        settings = {
            "current_lang": self.current_lang,
            "params": {},
            "measurement":{
                "MeasuringCentrifugalForce": self.MeasuringCentrifugalForce.value(),
                "CentrifugalForceLocation": self.CentrifugalForceLocation.value(),
            },
            "units": {
                "Eccentricity": self.EccentricityUnit.currentText(),
                "CentrifugalForce": self.CentrifugalForceUnit.currentText(),
                "CorrectionMass": self.CorrectionMassUnit.currentText()
            }
        }
        
        # 遍歷參數陣列，紀錄數值
        for item in self.all_params:
            p_id = item["id"]
            obj = item["input"]
            if isinstance(obj, QComboBox):
                settings["params"][p_id] = obj.currentText()
            elif hasattr(obj, "value"):
                settings["params"][p_id] = obj.value()

        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"儲存設定失敗: {e}")

    def load_settings(self):
        """ 從 Config/config.json 載入上次的設定 """
        config_path = os.path.join("Config", "config.json")
        
        if not os.path.exists(config_path):
            return False # 沒有紀錄檔，使用預設值
            
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                settings = json.load(f)
            
            self.current_lang = settings.get("current_lang", "TW")
            
            # 1. 填回參數數值
            params = settings.get("params", {})
            for item in self.all_params:
                p_id = item["id"]
                if p_id in params:
                    val = params[p_id]
                    obj = item["input"]
                    if isinstance(obj, QComboBox):
                        obj.setCurrentText(str(val))
                    elif hasattr(obj, "setValue"):
                        obj.setValue(float(val))

            # 2. 填回量測數值
            measurement = settings.get("measurement", {})
            self.MeasuringCentrifugalForce.setValue(measurement.get("MeasuringCentrifugalForce", 0.1))
            self.CentrifugalForceLocation.setValue(measurement.get("CentrifugalForceLocation", 0))
            
            # 3. 填回單位設定
            units = settings.get("units", {})
            self.EccentricityUnit.setCurrentText(units.get("Eccentricity", "µm"))
            self.CentrifugalForceUnit.setCurrentText(units.get("CentrifugalForce", "N"))
            self.CorrectionMassUnit.setCurrentText(units.get("CorrectionMass", "mg"))
            
            return True
        except Exception as e:
            print(f"載入設定失敗: {e}")
            return False
        
    def init_param_list(self):
        # 建立一個陣列，儲存所有「標籤、輸入物件、單位」的組合
        self.all_params = []
        # 假設你有 100 個參數，且在 Designer 命好名了
        for i in range(1, 6):
            lb_name = f"lb_param_{i:03d}"
            in_name = f"in_param_{i:03d}"
        
            # 透過字串抓取物件本身
            lb_obj = getattr(self, lb_name, None)
            in_obj = getattr(self, in_name, None)
        
            if lb_obj and in_obj:
                self.all_params.append({
                    "id": lb_name,
                    "label": lb_obj,
                    "input": in_obj
                })

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

    def Switch_language(self):
        if not self.languages: return
        lang = self.languages.get(self.current_lang, {})
        
        # 1. 視窗標題
        self.setWindowTitle(lang.get("Window_main", {}).get("Balance", "動平衡計算"))

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

    def switch_language_tc(self):
        # 切換語言旗標
        self.current_lang = "TW"
        # 更新介面
        self.Switch_language()   
    
    def switch_language_sc(self):
        # 切換語言旗標
        self.current_lang = "CN"
        # 更新介面
        self.Switch_language()  

    def switch_language_en(self):
        # 切換語言旗標
        self.current_lang = "EN"
        # 更新介面
        self.Switch_language()     

    def show_custom_warning(self, title, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        # 這裡放入你想要的樣式
        msg.setStyleSheet("""
            QMessageBox { background-color: #f8f9fa; border: 2px solid #dc3545; }
            QLabel { color: #721c24; font-family: 'Microsoft YaHei'; font-size: 14pt; }
            QPushButton { background-color: #dc3545; color: white; min-width: 80px; height: 30px; border-in_param_003: 5px; }
        """)
        msg.exec()    

    def init_ui_object_style(self):
        #1 建立物件清單
        all_combobox = [self.in_param_001, self.EccentricityUnit, self.CentrifugalForceUnit,
                        self.CorrectionMassUnit, self.in_param_005]   
        #2 統一設定View，確保 QSS 生效
        for combo in all_combobox:
            combo.setView(QListView()) 
        #3 需文字靠右的combo,等級,修正方式
        for combo in [self.in_param_001, self.in_param_005]:
            combo.setEditable(True)             # 必須先設為可編輯
            combo.lineEdit().setReadOnly(True)  # 設為唯讀，防止使用者亂打字
            combo.lineEdit().setAlignment(Qt.AlignRight) # 真正的靠右對齊！
            
    def init_combobox_data(self):
        self.in_param_001.addItems(str(i) for i in [0.4, 1.0, 2.5, 6.3, 16, 40, 100, 250, 630, 1600, 4000]) #動平衡等級選單
        self.EccentricityUnit.addItems(list(self.Unit_Eccentricity.keys())) #允許偏心距單位選單
        self.CentrifugalForceUnit.addItems(list(self.Unit_CentrifugalForce.keys())) #離心力單位選單
        self.CorrectionMassUnit.addItems(list(self.Unit_CorrectionMass.keys())) #修正量單位選單
        self.in_param_005.addItems(["減質量", "加質量"]) #修正方式
        
        for combo in [self.in_param_001, self.in_param_005]:
            for i in range(combo.count()):
                combo.setItemData(i, Qt.AlignRight, Qt.TextAlignmentRole) #內容靠右
    
    def reset_to_factory(self):
        """ 刪除設定檔並恢復出廠預設值 """
        # 1. 彈出確認視窗
        reply = QMessageBox.question(
            self, 
            self.get_msg("reset_title", "重設確認"), 
            self.get_msg("reset_text", "確定要刪除所有儲存的設定並恢復出廠預設值嗎？"),
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # 2. 刪除設定檔
            config_path = os.path.join("Config", "config.json")
            if os.path.exists(config_path):
                try:
                    os.remove(config_path)
                except Exception as e:
                    print(f"刪除設定檔失敗: {e}")

            # 3. 恢復預設狀態
            self.current_lang = "TW" # 恢復預設語言
            self.set_default_value() # 恢復預設數值
            self.Switch_language()   # 刷新介面文字
            self.do_calculation()    # 重新計算並刷新向量圖
            
            QMessageBox.information(self, self.get_msg("success"), self.get_msg("reset_ok", "已恢復出廠設定"))

    def set_default_value(self):
        #ComboBox 初始值
        self.in_param_001.setCurrentText("6.3")
        self.EccentricityUnit.setCurrentText("µm")
        self.CentrifugalForceUnit.setCurrentText("N")
        self.CorrectionMassUnit.setCurrentText("mg")
        self.in_param_005.setCurrentText("減質量")
        #SpinBox 初始值
        self.in_param_002.setValue(0.63)
        self.in_param_003.setValue(62)
        self.in_param_004.setValue(2000)
        self.MeasuringCentrifugalForce.setValue(0.1)
        self.CentrifugalForceLocation.setValue(0)
            
    def connect_signal(self):
        #按鈕
        self.PB_Calculate.clicked.connect(self.do_calculation)
        #清單
        combo = [self.EccentricityUnit, self.CentrifugalForceUnit, self.CorrectionMassUnit, self.in_param_005]
        for c in combo:
            c.currentIndexChanged.connect(self.do_calculation)
        #數值變更
        spinbox = [self.MeasuringCentrifugalForce, self.CentrifugalForceLocation]    
        for s in spinbox:
            s.valueChanged.connect(self.do_calculation)
        #檔案選項
        self.file_save_csv.triggered.connect(self.export_to_csv)
        self.file_open_csv.triggered.connect(self.import_from_csv)
        self.file_save_txt.triggered.connect(self.export_to_txt)
        self.file_open_txt.triggered.connect(self.import_from_txt)
        self.file_ExportPDF.triggered.connect(self.export_to_pdf)
        self.file_ExportPng.triggered.connect(self.export_to_png)
        self.file_Exit.triggered.connect(self.close)
        self.file_reset.triggered.connect(self.reset_to_factory) # 連結重設功能
        self.language_tc.triggered.connect(self.switch_language_tc)
        self.language_sc.triggered.connect(self.switch_language_sc)
        self.language_en.triggered.connect(self.switch_language_en)
        #關於選項
        self.about_Level.triggered.connect(self.show_grade_info) # 加上這一行
        self.about_Version.triggered.connect(self.show_version) # 加上這一行

    def get_msg(self, key, default=""):
        """ 從當前語言包抓取訊息文字 """
        lang = self.languages.get(self.current_lang, {})
        return lang.get("Messages", {}).get(key, default)
    
    def build_reverse_map(self):
        """ 掃描所有語言檔的分類，建立文字到物件 ID 的地圖 """
        reverse_map = {}
        categories = ["QLabel", "QPushButton", "QCombobox", "Data1"]
        
        for lang_data in self.languages.values():
            for cat in categories:
                cat_data = lang_data.get(cat, {})
                for obj_id, content in cat_data.items():
                    if obj_id == "textFont": continue
                    
                    text_val = content.get("text") if isinstance(content, dict) else content
                    
                    if isinstance(text_val, str):
                        reverse_map[text_val] = obj_id
                    elif isinstance(text_val, list):
                        for idx, item in enumerate(text_val):
                            reverse_map[item] = f"{obj_id}_idx_{idx}"
        return reverse_map
    
    def export_to_csv(self):
        default_dir = os.path.join(os.getcwd(), "Data")
        if not os.path.exists(default_dir): os.makedirs(default_dir)
            
        default_filename = f"Balance_Data_{QDateTime.currentDateTime().toString('yyyyMMdd_HHmmss')}.csv"
        initial_path = os.path.join(default_dir, default_filename)

        file_path, _ = QFileDialog.getSaveFileName(self, self.get_msg("csv_save_title", "Save CSV"), 
                                                    initial_path, "CSV Files (*.csv)")
        if not file_path: return
        
        # 關鍵修正：建立表頭以對應讀取時的 next(reader)
        header = [self.get_msg("header_item", "項目"), self.get_msg("header_value", "數值")]
        data = []
        for item in self.all_params:
            label_text = item["label"].text() # 抓取當前語言文字
            input_obj = item["input"]
            value = input_obj.value() if hasattr(input_obj, "value") else input_obj.currentText()
            # 第一欄存入標籤文字，實現「檔案內容隨語言變」
            data.append([label_text, value])

        try:
            with open(file_path, mode='w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(header) # 務必寫入表頭
                writer.writerows(data)
            QMessageBox.information(self, self.get_msg("success", "Success"), f"{self.get_msg('csv_save_ok')}\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, self.get_msg("fail", "Failed"), f"Save Error: {e}")

    def import_from_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, self.get_msg("csv_open_title"), 
                                                   os.path.join(os.getcwd(), "Data"), "CSV Files (*.csv)")
        if not file_path: return

        # --- 2. 建立【反向翻譯地圖】 (含 KeyError 保險) ---
        reverse_map = self.build_reverse_map()
        for lang_name in ["繁體", "簡體", "En"]:
            lang_data = self.languages.get(lang_name, {})
            for obj_id, content in lang_data.items():
                # 關鍵修正：跳過 grade_data，因為它是巢狀清單，會導致字典 Key 報錯
                if obj_id == "grade_data": 
                    continue
                text_val = content.get("text") if isinstance(content, dict) else content
                if isinstance(text_val, str):
                    reverse_map[text_val] = obj_id
                elif isinstance(text_val, list):
                    for idx, item in enumerate(text_val):
                        reverse_map[item] = f"{obj_id}_idx_{idx}"

        # --- 3. 讀取 CSV 並轉換標籤為 ID ---
        clean_data = {}
        success_read = False
        for enc in ['utf-8-sig', 'cp950', 'utf-8']:
            try:
                with open(file_path, mode='r', encoding=enc) as f:
                    reader = csv.reader(f)
                    next(reader) # 跳過表頭
                    for row in reader:
                        if len(row) >= 2:
                            csv_key, csv_val = row[0].strip(), row[1].strip()
                            standard_id = reverse_map.get(csv_key)
                            if standard_id:
                                clean_data[standard_id] = csv_val
                success_read = True
                break 
            except Exception as e:
                last_error = str(e)
                continue

        if not success_read:
            QMessageBox.critical(self, self.get_msg("error"), f"{self.get_msg('confirm_format')}!") #f"讀取失敗：{last_error}")
            return

        # --- 4. 根據 ID 填回 UI (自動化遍歷) ---
        update_count = 0
        try:
            for item in self.all_params:
                p_id = item["id"] # 這裡會拿到 "lb_param_001"
                if p_id in clean_data:
                    val = clean_data[p_id]
                    in_obj = item["input"]
                    
                    if isinstance(in_obj, QComboBox):
                        # 處理索引對應 (針對加減質量)
                        val_id = reverse_map.get(val)
                        if val_id and "_idx_" in val_id:
                            in_obj.setCurrentIndex(int(val_id.split("_idx_")[1]))
                        else:
                            in_obj.setCurrentText(val)
                    elif isinstance(in_obj, (QDoubleSpinBox, QSpinBox)):
                        in_obj.setValue(float(val))
                    elif isinstance(in_obj, QLineEdit):
                        in_obj.setText(val)
                    update_count += 1

            if update_count > 0:
                self.do_calculation()
                QMessageBox.information(self, self.get_msg("success"), f"{self.get_msg('updated')}!")
            else:
                QMessageBox.warning(self, self.get_msg("error"), f"{self.get_msg('confirm_format')}!")
        except Exception as e:
            QMessageBox.critical(self, self.get_msg("error"), f"Data Error: {e}")

    def export_to_txt(self):
        #self.do_calculation() # 確保數據最新
        
        # 1. 準備路徑
        default_dir = os.path.join(os.getcwd(), "Data")
        if not os.path.exists(default_dir): os.makedirs(default_dir)
        now_str = QDateTime.currentDateTime().toString('yyyyMMdd_HHmmss')
        initial_path = os.path.join(default_dir, f"Balance_Note_{now_str}.txt")

        # 2. 彈出存檔視窗
        file_path, _ = QFileDialog.getSaveFileName(self, self.get_msg("txt_save_title", "Save TXT" ),
                                                   initial_path, "Text Files (*.txt)")
        if not file_path: return

        # 3. 格式化資料內容
        # --- 3. 【自動化核心】遍歷參數陣列生成內容 ---
        lines = []
        for item in self.all_params:
            label_text = item["label"].text() # 抓取當前語言的標籤文字
            input_obj = item["input"]
            
            # 智慧判斷數值獲取方式 (SpinBox 用 value, ComboBox 用 currentText)
            if hasattr(input_obj, "value"):
                value = input_obj.value()
            else:
                value = input_obj.currentText()
                
            lines.append(f"{label_text}: {value}")

        # 4. 寫入檔案
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(lines))
            QMessageBox.information(self, self.get_msg("success", "Success"), f"{self.get_msg('txt_save_ok')}\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, self.get_msg("fail", "Failed"), f"{self.get_msg('save_fail')}{e}")

    def import_from_txt(self):
        # 1. 開啟檔案視窗
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.get_msg("txt_open_title", "開啟文字紀錄"), 
            os.path.join(os.getcwd(), "Data"), "Text Files (*.txt)"
        )
        if not file_path: return

        # --- 1. 建立【反向翻譯地圖】 (邏輯不變，用於跨語言辨識) ---
        reverse_map = self.build_reverse_map()
        for lang_name in ["繁體", "簡體", "En"]:
            lang_data = self.languages.get(lang_name, {})
            for obj_id, content in lang_data.items():
                # 關鍵修正：跳過 grade_data，因為它是巢狀清單，會導致字典 Key 報錯
                if obj_id == "grade_data": 
                    continue
                if isinstance(content, dict):
                    text_val = content.get("text") 
                else:
                    text_val = content
            
                if isinstance(text_val, str):
                    reverse_map[text_val] = obj_id
                elif isinstance(text_val, list):
                    for idx, item in enumerate(text_val):
                        reverse_map[item] = f"{obj_id}_idx_{idx}"

        # --- 2. 讀取並轉換資料 (將 TXT 裡的文字標籤轉回標準 ID) ---
        clean_data = {}
        success_read = False
        for enc in ['utf-8-sig', 'cp950', 'utf-8']:
            try:
                with open(file_path, 'r', encoding=enc) as f:
                    for line in f:
                        if ":" in line:
                            key, value = line.split(":", 1) 
                            key, value = key.strip(), value.strip()
                            standard_id = reverse_map.get(key)
                            if standard_id:
                                clean_data[standard_id] = value
                success_read = True
                break
            except Exception: continue

        if not success_read: return

        # --- 3. 【自動化核心】遍歷陣列填回 UI ---
        update_count = 0
        try:
            for item in self.all_params:
                p_id = item["id"]  # 例如 "lb_param_001"
                in_obj = item["input"]
                
                if p_id in clean_data:
                    val_text = clean_data[p_id]
                    
                    # A. 處理下拉選單 (QComboBox) - 需處理索引轉換
                    if isinstance(in_obj, QComboBox):
                        val_id = reverse_map.get(val_text)
                        if val_id and "_idx_" in val_id:
                            idx = int(val_id.split("_idx_")[1])
                            in_obj.setCurrentIndex(idx)
                        else:
                            in_obj.setCurrentText(val_text)
                    
                    # B. 處理數值輸入框 (QDoubleSpinBox / QSpinBox)
                    elif isinstance(in_obj, (QDoubleSpinBox, QSpinBox)):
                        in_obj.setValue(float(val_text))
                        
                    # C. 處理一般文字框 (QLineEdit)
                    elif isinstance(in_obj, QLineEdit):
                        in_obj.setText(val_text)
                        
                    update_count += 1

            # --- 4. 結果通知 ---
            if update_count > 0:
                self.do_calculation()
                QMessageBox.information(self, self.get_msg("success"), f"{self.get_msg('updated')}!")
            else:
                QMessageBox.warning(self, self.get_msg("error"), f"{self.get_msg('confirm_format')}!")

        except Exception as e:
            QMessageBox.critical(self, self.get_msg("error"), f"Import Error: {e}")

    def export_to_pdf(self):
        #self.do_calculation() # 確保數據最新

        # 1. 準備路徑
        default_dir = os.path.join(os.getcwd(), "Reports")
        if not os.path.exists(default_dir): os.makedirs(default_dir)
        now_str = QDateTime.currentDateTime().toString('yyyyMMdd_HHmmss')
        initial_path = os.path.join(default_dir, f"Balance_Report_{now_str}.pdf")

        # 2. 彈出存檔視窗
        file_path, _ = QFileDialog.getSaveFileName(self, self.get_msg("pdf_save_title", "Save PDF"),
                                                   initial_path, "PDF Files (*.pdf)")
        if not file_path: return

        doc = QTextDocument()
        cursor = QTextCursor(doc)
    
        # --- 3. 定義格式 (與之前一致) ---
        title_fmt = QTextCharFormat()
        title_fmt.setFontPointSize(20)
        title_fmt.setFontWeight(QFont.Bold)
        
        header_txt_fmt = QTextCharFormat()
        header_txt_fmt.setFontPointSize(12)
        header_txt_fmt.setFontWeight(QFont.Bold)
        header_txt_fmt.setForeground(QColor("white"))

        content_txt_fmt = QTextCharFormat()
        content_txt_fmt.setFontPointSize(11)

        footer_char_fmt = QTextCharFormat()
        footer_char_fmt.setFontPointSize(10)
        footer_char_fmt.setFontItalic(True)
        footer_char_fmt.setForeground(QColor("gray"))

        center_align = QTextBlockFormat()
        center_align.setAlignment(Qt.AlignCenter)
        
        left_align = QTextBlockFormat()
        left_align.setAlignment(Qt.AlignLeft)

        # 將圖片加入文件的內部資源，命名為 "internal_logo.png"
        doc.addResource(QTextDocument.ImageResource, QUrl("internal_logo.png"), self.logo_image)
        cursor.insertBlock(left_align) # 插入 Logo (靠左)
        image_format = QTextImageFormat()
        # 關鍵：這裡改用剛才註冊好的內部資源名稱
        image_format.setName("internal_logo.png")
        image_format.setWidth(80)
        image_format.setHeight(80)
        cursor.insertImage(image_format)

        cursor.insertBlock(center_align)
        # 標題也改用翻譯
        cursor.insertText(self.get_msg("PDFReport", "動平衡計算報告"), title_fmt)

        cursor.insertBlock(left_align)
        cursor.insertText(f"\n{self.get_msg('date', '日期')}: {QDateTime.currentDateTime().toString('yyyy-MM-dd')}\n\n", content_txt_fmt)

        # --- 4. 【自動化核心】建立表格內容 ---
        contents = []
        
        # A. 遍歷 all_params 陣列 (輸入參數部分)
        for item in self.all_params:
            label = item["label"].text()
            obj = item["input"]
            # 自動判斷取值方式
            val = obj.currentText() if hasattr(obj, "currentText") else f"{obj.value():g}"
            contents.append((label, val))
        
        # B. 手動加入計算結果 (輸出結果部分)
        # 注意：這裡使用翻譯好的 Text 標籤
        contents.append((self.get_msg("Unbalance_label", "不平衡量 (U)"), f"{self.Unbalance.text()} g·mm"))
        contents.append((self.get_msg("ResidualMass_label", "殘餘質量 (M)"), f"{self.ResidualMass.text()} g"))
        contents.append((self.get_msg("FinalResult_label", "判定結果"), self.FinalResult.text()))

        # --- 5. 繪製表格 ---
        table_fmt = QTextTableFormat()
        table_fmt.setBorder(1)
        table_fmt.setCellPadding(8)
        table_fmt.setColumnWidthConstraints([
            QTextLength(QTextLength.PercentageLength, 45),
            QTextLength(QTextLength.PercentageLength, 55)
        ])

        # 插入表格 (列數 = 資料量 + 1 層表頭)
        table = cursor.insertTable(len(contents) + 1, 2, table_fmt)

        # 設定表頭背景與文字 (使用 get_msg)
        header_bg_fmt = QTextTableCellFormat()
        header_bg_fmt.setBackground(QColor("#2c3e50"))
        
        headers = [self.get_msg("pdf_header_item", "測試項目"), self.get_msg("pdf_header_value", "結果 / 數據")]
        for col, head_text in enumerate(headers):
            cell = table.cellAt(0, col)
            cell.setFormat(header_bg_fmt)
            cell_cursor = cell.firstCursorPosition()
            cell_cursor.setBlockFormat(center_align)
            cell_cursor.insertText(head_text, header_txt_fmt)

        # 填入內容
        for row, (label, value) in enumerate(contents):
            curr_row = row + 1
            table.cellAt(curr_row, 0).firstCursorPosition().insertText(label, content_txt_fmt)
            val_cursor = table.cellAt(curr_row, 1).firstCursorPosition()
            val_cursor.setBlockFormat(center_align)
            
            # 特別處理「判定結果」的顏色
            if label == self.get_msg("FinalResult_label", "判定結果"):
                res_fmt = QTextCharFormat(content_txt_fmt)
                res_fmt.setFontWeight(QFont.Bold)
                # 判斷是 PASS 還是 FAIL (忽略大小寫與語言)
                res_fmt.setForeground(QColor("green") if "PASS" in value.upper() else QColor("red"))
                val_cursor.insertText(value, res_fmt)
            else:
                val_cursor.insertText(value, content_txt_fmt)
                
        cursor.movePosition(QTextCursor.End)
        cursor.insertBlock()
        # 頁尾說明 (可視需求加入翻譯)
        cursor.insertText(f"\n\n\n{self.get_msg('report_footer1', '【備註與說明】')}", footer_char_fmt)
        cursor.insertText(f"\n{self.get_msg('report_footer2', '1. 本報告之計算結果係依據 ISO 1940 規範之公式產出。')}", footer_char_fmt)
        cursor.insertText(f"\n{self.get_msg('report_footer3', '2. 殘餘不平衡量建議值僅供參考，實際操作應考量軸承與支撐剛性。')}", footer_char_fmt)
        cursor.insertText(f"\n{self.get_msg('report_footer4', '3. 測試人員：________________ (簽章)')}", footer_char_fmt)
        cursor.insertBlock(left_align)
        cursor.insertText(f"\n{self.get_msg('report_footer5', '本報告由動平衡計算工具自動生成')}", footer_char_fmt)
        
        # 輸出 PDF
        try:
            printer = QPdfWriter(file_path)
            printer.setPageSize(QPageSize(QPageSize.A4))
            doc.print_(printer)
            QMessageBox.information(self, self.get_msg("success"), f"{self.get_msg('pdf_save_ok')}\n{file_path}")
        except Exception as e:
            # 如果發生任何錯誤 (例如檔案被佔用)，跳到這裡
            QMessageBox.critical(self, self.get_msg("error"), 
                                 f"{self.get_msg('fail')}\n{e}")    

    def export_to_png(self):
        # 0. 建議先執行計算，確保畫面數值是最新的
        self.do_calculation()
        
        # 1. 準備預設資料夾
        default_dir = os.path.join(os.getcwd(), "Reports")
        if not os.path.exists(default_dir):
            os.makedirs(default_dir) # 如果資料夾不存在就建立

        # 2. 準備預設完整路徑 (資料夾 + 檔名)
        # 使用 QDate 加上時間戳記，避免檔名重複
        default_filename = f"Balance_{QDateTime.currentDateTime().toString('yyyyMMdd_HHmmss')}.png"
        initial_path = os.path.join(default_dir, default_filename)

        # 3. 彈出對話框，但「預填」我們準備好的路徑
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "儲存擷取畫面", 
            initial_path,      # 關鍵：預設路徑放這裡！
            "Images (*.png)"
        )
    
        # 如果使用者按了「取消」，就停止執行
        if not file_path: return 
        
        # 1. 擷取原始畫面
        pixmap = self.grab()
        """文字浮水印
        # 2. 建立畫筆，並指定在 pixmap 上畫畫
        painter = QPainter(pixmap)
        # 3. 設定浮水印的「透明度」 (0.0 完全透明 ~ 1.0 不透明)
        painter.setOpacity(0.3) 
        # 4. 設定字體與顏色
        font = QFont("Microsoft YaHei", 20)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QColor("gray")) # 設定顏色為灰色
        # 5. 繪製文字 (例如：公司名稱或開發者)
        watermark_text = "Eric Chiang - 動平衡計算系統"
        # 這裡我們把浮水印畫在右下角，並預留 10 像素的間距
        rect = pixmap.rect().adjusted(-10, -10, -10, -10)
        painter.drawText(rect, Qt.AlignBottom | Qt.AlignRight, watermark_text)
        """
        # 2. 載入 Logo 圖片 (這將是我們的浮水印)
        # 【選項】如果覺得 Logo 太大或太小，可以在這裡調整尺寸
        # 例如：強制縮放到寬度 300 像素，保持比例,原256*256
        logo_pixmap = self.logo_pixmap.scaledToWidth(460, Qt.SmoothTransformation)
        # 3. 建立畫筆，準備在底圖上作畫
        painter = QPainter(pixmap)
        # 開啟抗鋸齒，讓圖片邊緣更平滑
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        # 4. 關鍵：設定透明度 (0.1 非常透明 ~ 1.0 不透明)
        # 建議設定在 0.2 ~ 0.3 之間，效果最好
        painter.setOpacity(0.25)
        # 5. 關鍵：計算「置中」座標
        # 公式：(底圖總寬 - Logo寬) / 2 = 起始 X 座標
        x = (pixmap.width() - logo_pixmap.width()) // 2
        # 公式：(底圖總高 - Logo高) / 2 = 起始 Y 座標
        y = (pixmap.height() - logo_pixmap.height()) // 2
        # 6. 繪製 Logo
        painter.drawPixmap(x, y, logo_pixmap)

        # 結束繪製
        painter.end()
        
        # 3. 儲存圖片
        # 可以透過 quality 參數設定品質 (1-100)，預設為高品質
        if pixmap.save(file_path, "PNG"):
            QMessageBox.information(self, self.get_msg("success"), f"{self.get_msg('png_save_ok')}\n{file_path}")
        else:
            QMessageBox.critical(self, self.get_msg("error"), f"{self.get_msg('png_save_er')}") 

    def show_grade_info(self):
        # 每次都重新實例化，或者手動呼叫 init_table_data 以更新語言
        self.grade_win = GradeInfoWindow(self) # 實例化你做好的視窗
        self.grade_win.show()

    def show_version(self):
        """顯示軟體資訊視窗，且只改變此視窗的字型"""
        """ 顯示動態抓取的精準打包日期 """
        build_info = self.get_version_info() # 取得出生證明內容
        msg = QMessageBox(self)
        msg.setWindowTitle(self.get_msg("about_title", "關於動平衡計算程式"))
        # 加入自定義圖示 ---
        scaled_logo = self.logo_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation) # 載入 logo.png 並縮放到適合大小 (建議 64x64 或 80x80)
        msg.setIconPixmap(scaled_logo)
        # 使用 HTML 語法設定內容
        msg.setText(
            f"<h3>{self.get_msg('soft_name')}{self.version}</h3>"
            f"<p>{self.get_msg('dev_label')}{self.Developer}</p>"
            f"<p>{self.get_msg('date_label')}{self.ver_date}</p>"
            "<hr>"
            f"<p>{self.get_msg('about_desc')}</p>"
            f"<p><i>{self.get_msg('copyright')}{self.Copyright}</i></p>"
        )
        # --- 關鍵：只針對這個視窗設定樣式 ---
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #B5B5B5;
            }
            QLabel {
                font-family: "Microsoft YaHei";
                font-size: 14pt;
                color: black;
            }
            QPushButton {
                border-style: solid; 
	            border-width: 1;
	            background-color: #B5B5B5;
	            border-top-color: white;
	            border-left-color: white;
	            border-bottom-color: black;
	            border-right-color: black;          
                font-family: "Microsoft YaHei";
                font-size: 14pt;
                min-width: 70px;
            }
            QPushButton:pressed {
	            border-style: solid; 
	            border-width: 1;
	            background-color: #999999;
	            border-top-color: black;
	            border-left-color: black;
	            border-bottom-color: white;
	            border-right-color: white;
            }
        """)
        
        msg.exec()

    def get_version_info(self):
        """ 讀取打包時生成的 version.txt """
        # 使用你原本就有的 resource_path 尋找內部檔案
        v_path = resource_path("Assets/version.txt") 
    
        if os.path.exists(v_path):
            try:
                with open(v_path, "r", encoding="utf-8") as f:
                    return f.read().strip()
            except Exception:
                pass
            
        # 如果找不到 (開發模式)，則回傳今天日期作為預設
        return datetime.datetime.now().strftime('%Y-%m-%d (Dev)')        

    def closeEvent(self, event):
        """當視窗準備關閉時會自動觸發這個函式，並套用自定義樣式"""
        # 1. 建立詢問視窗物件 (不使用靜態方法)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(self.get_msg("close_title", "確認離開"))
        msg.setText(self.get_msg("close_text", "您確定要結束動平衡計算程式嗎？"))
        # 2.--- 關鍵：換掉問號圖標 ---
        msg.setIconPixmap(self.logo_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)) # 縮放到適合的大小 (例如 64x64 像素)
        # 3. 設定按鈕（Yes 和 No）
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No) # 設定預設選中的按鈕為 No (防止手快按錯)
        # 4. 套用樣式表 (只針對這個視窗)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #B5B5B5;
            }
            QLabel {
                font-family: "Microsoft YaHei";
                font-size: 14pt;
                color: black;
                padding: 10px;
            }
            QPushButton {
                border-style: solid; 
	            border-width: 1;
	            background-color: #B5B5B5;
	            border-top-color: white;
	            border-left-color: white;
	            border-bottom-color: black;
	            border-right-color: black;          
                font-family: "Microsoft YaHei";
                font-size: 14pt;
                min-width: 80px;
                height: 28px;
            }
            QPushButton:pressed {
	            border-style: solid; 
	            border-width: 1;
	            background-color: #999999;
	            border-top-color: black;
	            border-left-color: black;
	            border-bottom-color: white;
	            border-right-color: white;
            }
        """)

        # 4. 執行並獲取結果
        reply = msg.exec()
        if reply == QMessageBox.Yes:
            # --- 關鍵：離開前存檔 ---
            self.save_settings()
            event.accept()  # 接受關閉事件，程式結束
        else:
            event.ignore()  # 忽略關閉事件，回到程式
        
    def do_calculation(self):
        try:
            # 1. 獲取數值
            G = float(self.in_param_001.currentText()) #動平衡等級
            rotor_kg = self.in_param_002.value() #轉子重量
            in_param_003_mm = self.in_param_003.value() #修正半徑
            speed_rpm = self.in_param_004.value() #最大轉速
            omega = (2 * math.pi * speed_rpm) / 60 #(ω)
            meas_N = self.MeasuringCentrifugalForce.value() #假設離心力
            Angle = self.CentrifugalForceLocation.value() % 360 #假設角度

            if speed_rpm <= 0: #設0時跳出視窗,從Qt minimum > 0時,設小於minimum時按enter會回復成原來的值
                self.show_custom_warning("數值錯誤", "最大轉速必須大於 0!")
                return # 停止計算

            if in_param_003_mm <= 0:
                self.show_custom_warning("數值錯誤", "修正半徑必須大於 0!")
                return

            # 2. 執行計算
            # 2-1不平衡量
            #Unbalance_result = (9.549 * G * rotor_kg * 1000) / speed_rpm
            Unbalance_result = (G * rotor_kg * 1000) / omega
            self.Unbalance.setText(f"{Unbalance_result:g}") #.4f小數4位 ,g自動化簡
            # 2-2殘餘質量
            Mass_result = (Unbalance_result / in_param_003_mm) * 1000
            self.ResidualMass.setText(f"{Mass_result:g}")
            # 2-3偏心距
            factor = self.Unit_Eccentricity.get(self.EccentricityUnit.currentText(), 1)
            Eccentricity_result = (G / omega) * factor
            self.Eccentricity.setText(f"{Eccentricity_result:g}")
            # 2-4離心力
            factor = self.Unit_CentrifugalForce.get(self.CentrifugalForceUnit.currentText(), 1)
            CentrifugalForce_result = rotor_kg * G * 0.001 * omega * factor
            self.CentrifugalForce.setText(f"{CentrifugalForce_result:g}")
            # 2-5修正量
            factor = self.Unit_CorrectionMass.get(self.CorrectionMassUnit.currentText(), 1)
            CorrectionMass_result = (meas_N / (in_param_003_mm * 0.001 * omega**2)) * factor
            self.CorrectionMass.setText(f"{CorrectionMass_result:g}")
            # 2-6修正方式與位置
            is_adding = (self.in_param_005.currentIndex() == 1)
            if is_adding: #[減質量,加質量]=[0,1]
                Angle = (Angle + 180) % 360
            self.CorrectionLocation.setText(f"{Angle:g}")
            # --- 新增：更新動態向量圖 ---
            # --- 關鍵修正：傳入角度與「是否加重」的狀態 ---
            self.vector_graph.update_angle(Angle, is_adding)
            # 2-7判斷結果
            current_mass = (meas_N / (in_param_003_mm * 0.001 * omega**2)) * 10**6
            if current_mass <= Mass_result: #以mg單位比較
                self.FinalResult.setText("PASS")
                self.FinalResult.setStyleSheet("""
                    background-color: green;
                    font-family: Microsoft YaHei;
                    font-size: 14pt; color: black;
                """)
            else:    
                self.FinalResult.setText("FAIL")
                self.FinalResult.setStyleSheet("""
                    background-color: red;
                    font-family: Microsoft YaHei;
                    font-size: 14pt; color: white;
                """)

        except ValueError:
            QMessageBox.critical(self, "輸入錯誤", "請確保輸入的內容為有效數字！")
        except ZeroDivisionError:
            QMessageBox.critical(self, "計算錯誤", "發生除以零的情況，請檢查輸入數值！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # --- 讓 Windows 任務欄顯示獨立圖示的關鍵代碼 ---
    import ctypes
    my_appid = 'mycompany.myproduct.subproduct.version' # 隨便定義一個 ID
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_appid)
    # ------------------------------------------
    try:
        myWin = MyMainWindow()
        myWin.show()
        sys.exit(app.exec())
    except Exception as e:
        # 這行會把真正的錯誤原因印在終端機（黑視窗）上
        print(f"程式啟動失敗，原因: {e}")    

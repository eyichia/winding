# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WireArrangeGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_Arrange(object):
    def setupUi(self, Arrange):
        if not Arrange.objectName():
            Arrange.setObjectName(u"Arrange")
        Arrange.resize(1024, 768)
        Arrange.setMinimumSize(QSize(0, 0))
        Arrange.setMaximumSize(QSize(1024, 768))
        Arrange.setAutoFillBackground(False)
        Arrange.setStyleSheet(u"background-color: #B5B5B5;")
        self.language_tc = QAction(Arrange)
        self.language_tc.setObjectName(u"language_tc")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(10)
        self.language_tc.setFont(font)
        self.language_sc = QAction(Arrange)
        self.language_sc.setObjectName(u"language_sc")
        self.language_sc.setFont(font)
        self.language_en = QAction(Arrange)
        self.language_en.setObjectName(u"language_en")
        self.language_en.setFont(font)
        self.file_exit = QAction(Arrange)
        self.file_exit.setObjectName(u"file_exit")
        self.file_exit.setFont(font)
        self.file_export_csv = QAction(Arrange)
        self.file_export_csv.setObjectName(u"file_export_csv")
        self.about_version = QAction(Arrange)
        self.about_version.setObjectName(u"about_version")
        self.about_version.setFont(font)
        self.file_save_csv = QAction(Arrange)
        self.file_save_csv.setObjectName(u"file_save_csv")
        self.file_save_csv.setFont(font)
        self.file_save_txt = QAction(Arrange)
        self.file_save_txt.setObjectName(u"file_save_txt")
        self.file_save_txt.setFont(font)
        self.file_open_csv = QAction(Arrange)
        self.file_open_csv.setObjectName(u"file_open_csv")
        self.file_open_csv.setFont(font)
        self.file_open_txt = QAction(Arrange)
        self.file_open_txt.setObjectName(u"file_open_txt")
        self.file_open_txt.setFont(font)
        self.file_reset = QAction(Arrange)
        self.file_reset.setObjectName(u"file_reset")
        self.file_reset.setFont(font)
        self.file_export_pdf = QAction(Arrange)
        self.file_export_pdf.setObjectName(u"file_export_pdf")
        self.file_export_xlsx = QAction(Arrange)
        self.file_export_xlsx.setObjectName(u"file_export_xlsx")
        self.centralwidget = QWidget(Arrange)
        self.centralwidget.setObjectName(u"centralwidget")
        self.arrange_image = QLabel(self.centralwidget)
        self.arrange_image.setObjectName(u"arrange_image")
        self.arrange_image.setGeometry(QRect(20, 65, 360, 360))
        self.arrange_image.setStyleSheet(u"QLabel {\n"
"	border-style: solid; \n"
"	border-width: 2;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.arrange_image.setPixmap(QPixmap(u"Assets/Arrange.png"))
        self.arrange_image.setScaledContents(True)
        self.PB_chart = QPushButton(self.centralwidget)
        self.PB_chart.setObjectName(u"PB_chart")
        self.PB_chart.setGeometry(QRect(20, 25, 90, 40))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(14)
        self.PB_chart.setFont(font1)
        self.PB_chart.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_chart_A = QPushButton(self.centralwidget)
        self.PB_chart_A.setObjectName(u"PB_chart_A")
        self.PB_chart_A.setGeometry(QRect(110, 25, 90, 40))
        self.PB_chart_A.setFont(font1)
        self.PB_chart_A.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_chart_B = QPushButton(self.centralwidget)
        self.PB_chart_B.setObjectName(u"PB_chart_B")
        self.PB_chart_B.setGeometry(QRect(200, 25, 90, 40))
        self.PB_chart_B.setFont(font1)
        self.PB_chart_B.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_chart_C = QPushButton(self.centralwidget)
        self.PB_chart_C.setObjectName(u"PB_chart_C")
        self.PB_chart_C.setGeometry(QRect(290, 25, 90, 40))
        self.PB_chart_C.setFont(font1)
        self.PB_chart_C.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.lb_pa_001 = QLabel(self.centralwidget)
        self.lb_pa_001.setObjectName(u"lb_pa_001")
        self.lb_pa_001.setGeometry(QRect(390, 30, 190, 30))
        self.lb_pa_001.setMaximumSize(QSize(16777215, 16777215))
        self.lb_pa_001.setFont(font1)
        self.lb_pa_001.setStyleSheet(u"background-color: transparent;")
        self.lb_pa_001.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_001 = QDoubleSpinBox(self.centralwidget)
        self.in_pa_001.setObjectName(u"in_pa_001")
        self.in_pa_001.setGeometry(QRect(585, 30, 100, 30))
        self.in_pa_001.setFont(font1)
        self.in_pa_001.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.in_pa_001.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.in_pa_001.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_001.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.in_pa_001.setDecimals(4)
        self.in_pa_001.setMinimum(0.000000000000000)
        self.in_pa_001.setMaximum(999.999900000000025)
        self.in_pa_001.setSingleStep(0.000100000000000)
        self.in_pa_001.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.in_pa_001.setValue(0.000000000000000)
        self.un_pa_001 = QLabel(self.centralwidget)
        self.un_pa_001.setObjectName(u"un_pa_001")
        self.un_pa_001.setGeometry(QRect(690, 30, 60, 30))
        self.un_pa_001.setFont(font1)
        self.un_pa_001.setStyleSheet(u"background-color: transparent;")
        self.un_pa_001.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.un_pa_002 = QLabel(self.centralwidget)
        self.un_pa_002.setObjectName(u"un_pa_002")
        self.un_pa_002.setGeometry(QRect(690, 65, 60, 30))
        self.un_pa_002.setFont(font1)
        self.un_pa_002.setStyleSheet(u"background-color: transparent;")
        self.un_pa_002.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lb_pa_002 = QLabel(self.centralwidget)
        self.lb_pa_002.setObjectName(u"lb_pa_002")
        self.lb_pa_002.setGeometry(QRect(390, 65, 190, 30))
        self.lb_pa_002.setMaximumSize(QSize(16777215, 16777215))
        self.lb_pa_002.setFont(font1)
        self.lb_pa_002.setStyleSheet(u"background-color: transparent;")
        self.lb_pa_002.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.un_pa_003 = QLabel(self.centralwidget)
        self.un_pa_003.setObjectName(u"un_pa_003")
        self.un_pa_003.setGeometry(QRect(690, 100, 60, 30))
        self.un_pa_003.setFont(font1)
        self.un_pa_003.setStyleSheet(u"background-color: transparent;")
        self.un_pa_003.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lb_pa_003 = QLabel(self.centralwidget)
        self.lb_pa_003.setObjectName(u"lb_pa_003")
        self.lb_pa_003.setGeometry(QRect(390, 100, 190, 30))
        self.lb_pa_003.setMaximumSize(QSize(16777215, 16777215))
        self.lb_pa_003.setFont(font1)
        self.lb_pa_003.setStyleSheet(u"background-color: transparent;")
        self.lb_pa_003.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.un_pa_004 = QLabel(self.centralwidget)
        self.un_pa_004.setObjectName(u"un_pa_004")
        self.un_pa_004.setGeometry(QRect(690, 135, 60, 30))
        self.un_pa_004.setFont(font1)
        self.un_pa_004.setStyleSheet(u"background-color: transparent;")
        self.un_pa_004.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lb_pa_004 = QLabel(self.centralwidget)
        self.lb_pa_004.setObjectName(u"lb_pa_004")
        self.lb_pa_004.setGeometry(QRect(390, 135, 190, 30))
        self.lb_pa_004.setMaximumSize(QSize(16777215, 16777215))
        self.lb_pa_004.setFont(font1)
        self.lb_pa_004.setStyleSheet(u"background-color: transparent;")
        self.lb_pa_004.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_005 = QDoubleSpinBox(self.centralwidget)
        self.in_pa_005.setObjectName(u"in_pa_005")
        self.in_pa_005.setGeometry(QRect(100, 530, 100, 30))
        self.in_pa_005.setFont(font1)
        self.in_pa_005.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.in_pa_005.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.in_pa_005.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_005.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.in_pa_005.setDecimals(4)
        self.in_pa_005.setMinimum(0.000000000000000)
        self.in_pa_005.setMaximum(999.999000000000024)
        self.in_pa_005.setSingleStep(0.000100000000000)
        self.in_pa_005.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.in_pa_005.setValue(0.000000000000000)
        self.lb_pa_005 = QLabel(self.centralwidget)
        self.lb_pa_005.setObjectName(u"lb_pa_005")
        self.lb_pa_005.setGeometry(QRect(15, 530, 80, 30))
        self.lb_pa_005.setMaximumSize(QSize(16777215, 16777215))
        self.lb_pa_005.setFont(font1)
        self.lb_pa_005.setStyleSheet(u"background-color: transparent;")
        self.lb_pa_005.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(15, 495, 80, 30))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(15, 565, 80, 30))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: transparent;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(15, 600, 80, 30))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: transparent;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_006 = QDoubleSpinBox(self.centralwidget)
        self.in_pa_006.setObjectName(u"in_pa_006")
        self.in_pa_006.setGeometry(QRect(205, 530, 100, 30))
        self.in_pa_006.setFont(font1)
        self.in_pa_006.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.in_pa_006.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.in_pa_006.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_006.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.in_pa_006.setDecimals(4)
        self.in_pa_006.setMinimum(0.000000000000000)
        self.in_pa_006.setMaximum(999.999000000000024)
        self.in_pa_006.setSingleStep(0.000100000000000)
        self.in_pa_006.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.in_pa_006.setValue(0.000000000000000)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 445, 205, 25))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_x = QLabel(self.centralwidget)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setGeometry(QRect(100, 470, 100, 25))
        self.label_x.setMaximumSize(QSize(16777215, 16777215))
        self.label_x.setFont(font1)
        self.label_x.setStyleSheet(u"background-color: transparent;")
        self.label_x.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_y = QLabel(self.centralwidget)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(207, 470, 100, 25))
        self.label_y.setMaximumSize(QSize(16777215, 16777215))
        self.label_y.setFont(font1)
        self.label_y.setStyleSheet(u"background-color: transparent;")
        self.label_y.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PB_Calculate = QPushButton(self.centralwidget)
        self.PB_Calculate.setObjectName(u"PB_Calculate")
        self.PB_Calculate.setGeometry(QRect(535, 285, 150, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_Calculate.sizePolicy().hasHeightForWidth())
        self.PB_Calculate.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(14)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.PB_Calculate.setFont(font2)
        self.PB_Calculate.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(390, 175, 190, 30))
        self.label_1.setMaximumSize(QSize(16777215, 16777215))
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"background-color: transparent;")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 210, 190, 30))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Cross_sectional_area = QDoubleSpinBox(self.centralwidget)
        self.Cross_sectional_area.setObjectName(u"Cross_sectional_area")
        self.Cross_sectional_area.setGeometry(QRect(585, 175, 100, 30))
        self.Cross_sectional_area.setFont(font1)
        self.Cross_sectional_area.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Cross_sectional_area.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Cross_sectional_area.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Cross_sectional_area.setReadOnly(True)
        self.Cross_sectional_area.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Cross_sectional_area.setDecimals(4)
        self.Cross_sectional_area.setMinimum(0.000000000000000)
        self.Cross_sectional_area.setMaximum(999.999900000000025)
        self.Cross_sectional_area.setSingleStep(0.000100000000000)
        self.Cross_sectional_area.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Cross_sectional_area.setValue(0.000000000000000)
        self.Usable_area = QDoubleSpinBox(self.centralwidget)
        self.Usable_area.setObjectName(u"Usable_area")
        self.Usable_area.setGeometry(QRect(585, 210, 100, 30))
        self.Usable_area.setFont(font1)
        self.Usable_area.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Usable_area.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Usable_area.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Usable_area.setReadOnly(True)
        self.Usable_area.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Usable_area.setDecimals(4)
        self.Usable_area.setMinimum(0.000000000000000)
        self.Usable_area.setMaximum(999.999900000000025)
        self.Usable_area.setSingleStep(0.000100000000000)
        self.Usable_area.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Usable_area.setValue(0.000000000000000)
        self.Coordinate_AX = QDoubleSpinBox(self.centralwidget)
        self.Coordinate_AX.setObjectName(u"Coordinate_AX")
        self.Coordinate_AX.setGeometry(QRect(100, 495, 100, 30))
        self.Coordinate_AX.setFont(font1)
        self.Coordinate_AX.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Coordinate_AX.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Coordinate_AX.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Coordinate_AX.setReadOnly(True)
        self.Coordinate_AX.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Coordinate_AX.setDecimals(4)
        self.Coordinate_AX.setMinimum(0.000000000000000)
        self.Coordinate_AX.setMaximum(999.999900000000025)
        self.Coordinate_AX.setSingleStep(0.000100000000000)
        self.Coordinate_AX.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Coordinate_AX.setValue(0.000000000000000)
        self.Coordinate_CX = QDoubleSpinBox(self.centralwidget)
        self.Coordinate_CX.setObjectName(u"Coordinate_CX")
        self.Coordinate_CX.setGeometry(QRect(100, 565, 100, 30))
        self.Coordinate_CX.setFont(font1)
        self.Coordinate_CX.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Coordinate_CX.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Coordinate_CX.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Coordinate_CX.setReadOnly(True)
        self.Coordinate_CX.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Coordinate_CX.setDecimals(4)
        self.Coordinate_CX.setMinimum(0.000000000000000)
        self.Coordinate_CX.setMaximum(999.999000000000024)
        self.Coordinate_CX.setSingleStep(0.000100000000000)
        self.Coordinate_CX.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Coordinate_CX.setValue(0.000000000000000)
        self.Coordinate_AY = QDoubleSpinBox(self.centralwidget)
        self.Coordinate_AY.setObjectName(u"Coordinate_AY")
        self.Coordinate_AY.setGeometry(QRect(205, 495, 100, 30))
        self.Coordinate_AY.setFont(font1)
        self.Coordinate_AY.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Coordinate_AY.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Coordinate_AY.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Coordinate_AY.setReadOnly(True)
        self.Coordinate_AY.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Coordinate_AY.setDecimals(4)
        self.Coordinate_AY.setMinimum(0.000000000000000)
        self.Coordinate_AY.setMaximum(999.999900000000025)
        self.Coordinate_AY.setSingleStep(0.000100000000000)
        self.Coordinate_AY.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Coordinate_AY.setValue(0.000000000000000)
        self.Coordinate_CY = QDoubleSpinBox(self.centralwidget)
        self.Coordinate_CY.setObjectName(u"Coordinate_CY")
        self.Coordinate_CY.setGeometry(QRect(205, 565, 100, 30))
        self.Coordinate_CY.setFont(font1)
        self.Coordinate_CY.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Coordinate_CY.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Coordinate_CY.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Coordinate_CY.setReadOnly(True)
        self.Coordinate_CY.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Coordinate_CY.setDecimals(4)
        self.Coordinate_CY.setMinimum(0.000000000000000)
        self.Coordinate_CY.setMaximum(999.999000000000024)
        self.Coordinate_CY.setSingleStep(0.000100000000000)
        self.Coordinate_CY.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Coordinate_CY.setValue(0.000000000000000)
        self.Coordinate_DX = QDoubleSpinBox(self.centralwidget)
        self.Coordinate_DX.setObjectName(u"Coordinate_DX")
        self.Coordinate_DX.setGeometry(QRect(100, 600, 100, 30))
        self.Coordinate_DX.setFont(font1)
        self.Coordinate_DX.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Coordinate_DX.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Coordinate_DX.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Coordinate_DX.setReadOnly(True)
        self.Coordinate_DX.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Coordinate_DX.setDecimals(4)
        self.Coordinate_DX.setMinimum(0.000000000000000)
        self.Coordinate_DX.setMaximum(999.999000000000024)
        self.Coordinate_DX.setSingleStep(0.000100000000000)
        self.Coordinate_DX.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Coordinate_DX.setValue(0.000000000000000)
        self.Coordinate_DY = QDoubleSpinBox(self.centralwidget)
        self.Coordinate_DY.setObjectName(u"Coordinate_DY")
        self.Coordinate_DY.setGeometry(QRect(205, 600, 100, 30))
        self.Coordinate_DY.setFont(font1)
        self.Coordinate_DY.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Coordinate_DY.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Coordinate_DY.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Coordinate_DY.setReadOnly(True)
        self.Coordinate_DY.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Coordinate_DY.setDecimals(4)
        self.Coordinate_DY.setMinimum(0.000000000000000)
        self.Coordinate_DY.setMaximum(999.999000000000024)
        self.Coordinate_DY.setSingleStep(0.000100000000000)
        self.Coordinate_DY.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Coordinate_DY.setValue(0.000000000000000)
        self.Process = QTextEdit(self.centralwidget)
        self.Process.setObjectName(u"Process")
        self.Process.setGeometry(QRect(395, 345, 300, 320))
        self.Process.setStyleSheet(u"QTextEdit{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.in_pa_002 = QDoubleSpinBox(self.centralwidget)
        self.in_pa_002.setObjectName(u"in_pa_002")
        self.in_pa_002.setGeometry(QRect(585, 65, 100, 30))
        self.in_pa_002.setFont(font1)
        self.in_pa_002.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.in_pa_002.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.in_pa_002.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_002.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.in_pa_002.setDecimals(4)
        self.in_pa_002.setMinimum(0.000000000000000)
        self.in_pa_002.setMaximum(999.999900000000025)
        self.in_pa_002.setSingleStep(0.000100000000000)
        self.in_pa_002.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.in_pa_002.setValue(0.000000000000000)
        self.in_pa_003 = QDoubleSpinBox(self.centralwidget)
        self.in_pa_003.setObjectName(u"in_pa_003")
        self.in_pa_003.setGeometry(QRect(585, 100, 100, 30))
        self.in_pa_003.setFont(font1)
        self.in_pa_003.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.in_pa_003.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.in_pa_003.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_003.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.in_pa_003.setDecimals(4)
        self.in_pa_003.setMinimum(0.000000000000000)
        self.in_pa_003.setMaximum(999.999900000000025)
        self.in_pa_003.setSingleStep(0.000100000000000)
        self.in_pa_003.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.in_pa_003.setValue(0.000000000000000)
        self.in_pa_004 = QDoubleSpinBox(self.centralwidget)
        self.in_pa_004.setObjectName(u"in_pa_004")
        self.in_pa_004.setGeometry(QRect(585, 135, 100, 30))
        self.in_pa_004.setFont(font1)
        self.in_pa_004.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: white;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}")
        self.in_pa_004.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.in_pa_004.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.in_pa_004.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.in_pa_004.setDecimals(4)
        self.in_pa_004.setMinimum(0.000000000000000)
        self.in_pa_004.setMaximum(999.999900000000025)
        self.in_pa_004.setSingleStep(0.000100000000000)
        self.in_pa_004.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.in_pa_004.setValue(0.000000000000000)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(390, 335, 310, 5))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.PB_Clear_process = QPushButton(self.centralwidget)
        self.PB_Clear_process.setObjectName(u"PB_Clear_process")
        self.PB_Clear_process.setGeometry(QRect(535, 675, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_Clear_process.sizePolicy().hasHeightForWidth())
        self.PB_Clear_process.setSizePolicy(sizePolicy)
        self.PB_Clear_process.setFont(font2)
        self.PB_Clear_process.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"	/*border-radius: 15px;*/\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-"
                        "bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 245, 190, 30))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Slot_fill_rate = QDoubleSpinBox(self.centralwidget)
        self.Slot_fill_rate.setObjectName(u"Slot_fill_rate")
        self.Slot_fill_rate.setGeometry(QRect(585, 245, 100, 30))
        self.Slot_fill_rate.setFont(font1)
        self.Slot_fill_rate.setStyleSheet(u"QDoubleSpinBox{\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	border-right-color: white;\n"
"}")
        self.Slot_fill_rate.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.Slot_fill_rate.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Slot_fill_rate.setReadOnly(True)
        self.Slot_fill_rate.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Slot_fill_rate.setDecimals(4)
        self.Slot_fill_rate.setMinimum(0.000000000000000)
        self.Slot_fill_rate.setMaximum(999.999900000000025)
        self.Slot_fill_rate.setSingleStep(0.000100000000000)
        self.Slot_fill_rate.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Slot_fill_rate.setValue(0.000000000000000)
        self.PB_A_export_coordinates = QPushButton(self.centralwidget)
        self.PB_A_export_coordinates.setObjectName(u"PB_A_export_coordinates")
        self.PB_A_export_coordinates.setGeometry(QRect(705, 350, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_A_export_coordinates.sizePolicy().hasHeightForWidth())
        self.PB_A_export_coordinates.setSizePolicy(sizePolicy)
        self.PB_A_export_coordinates.setFont(font2)
        self.PB_A_export_coordinates.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_B_export_coordinates = QPushButton(self.centralwidget)
        self.PB_B_export_coordinates.setObjectName(u"PB_B_export_coordinates")
        self.PB_B_export_coordinates.setGeometry(QRect(705, 400, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_B_export_coordinates.sizePolicy().hasHeightForWidth())
        self.PB_B_export_coordinates.setSizePolicy(sizePolicy)
        self.PB_B_export_coordinates.setFont(font2)
        self.PB_B_export_coordinates.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        self.PB_C_export_coordinates = QPushButton(self.centralwidget)
        self.PB_C_export_coordinates.setObjectName(u"PB_C_export_coordinates")
        self.PB_C_export_coordinates.setGeometry(QRect(705, 450, 150, 40))
        sizePolicy.setHeightForWidth(self.PB_C_export_coordinates.sizePolicy().hasHeightForWidth())
        self.PB_C_export_coordinates.setSizePolicy(sizePolicy)
        self.PB_C_export_coordinates.setFont(font2)
        self.PB_C_export_coordinates.setStyleSheet(u"/*border-width	\u908a\u6846\u7c97\u7d30	1px, 5px\n"
"border-style	\u908a\u6846\u6a23\u5f0f	solid (\u5be6\u7dda), dashed (\u865b\u7dda), dotted (\u9ede\u7dda)\n"
"border-top-width	\u53ea\u8a2d\u5b9a\u4e0a\u65b9\u908a\u6846	2px\n"
"border-radius	\u5713\u89d2\u7a0b\u5ea6	15px (\u534a\u5f91)\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 10; */ \n"
"/* \u5e73\u6642\u7684\u6a23\u5f0f */\n"
"QPushButton {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	border-top-color: white;\n"
"	border-left-color: white;\n"
"	border-bottom-color: black;\n"
"	border-right-color: black;\n"
"}\n"
"\n"
"/* \u6ed1\u9f20\u79fb\u4e0a\u53bb\u6642 (:hover) */\n"
"/*QPushButton:hover {\n"
"    background-color: #e1f5fe;\n"
"}*/\n"
"\n"
"/* \u6309\u4e0b\u53bb\u7684\u77ac\u9593 (:pressed) */\n"
"QPushButton:pressed {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #999999;\n"
"	border-top-color: black;\n"
"	border-left-color: black;\n"
"	border-bottom-color: white;\n"
"	bord"
                        "er-right-color: white;\n"
"}")
        Arrange.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Arrange)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        self.menubar.setFont(font)
        self.menubar.setStyleSheet(u"QMenu {\n"
"	border-style: solid; \n"
"	border-width: 1;\n"
"	background-color: #B5B5B5;\n"
"	/*border-top-color: white;\n"
"	border-left-color: white;*/\n"
"	border-bottom-color: #999999;\n"
"	border-right-color: #999999;\n"
"}")
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.File.setFont(font)
        self.Export = QMenu(self.File)
        self.Export.setObjectName(u"Export")
        self.Export.setFont(font)
        self.Save = QMenu(self.File)
        self.Save.setObjectName(u"Save")
        self.Save.setFont(font)
        self.Open = QMenu(self.File)
        self.Open.setObjectName(u"Open")
        self.Open.setFont(font)
        self.About = QMenu(self.menubar)
        self.About.setObjectName(u"About")
        self.About.setFont(font)
        self.Language = QMenu(self.menubar)
        self.Language.setObjectName(u"Language")
        self.Language.setFont(font)
        Arrange.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Arrange)
        self.statusbar.setObjectName(u"statusbar")
        Arrange.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.in_pa_001, self.in_pa_002)
        QWidget.setTabOrder(self.in_pa_002, self.in_pa_003)
        QWidget.setTabOrder(self.in_pa_003, self.in_pa_004)
        QWidget.setTabOrder(self.in_pa_004, self.in_pa_005)
        QWidget.setTabOrder(self.in_pa_005, self.in_pa_006)
        QWidget.setTabOrder(self.in_pa_006, self.PB_Calculate)
        QWidget.setTabOrder(self.PB_Calculate, self.Process)
        QWidget.setTabOrder(self.Process, self.PB_Clear_process)
        QWidget.setTabOrder(self.PB_Clear_process, self.Cross_sectional_area)
        QWidget.setTabOrder(self.Cross_sectional_area, self.Usable_area)
        QWidget.setTabOrder(self.Usable_area, self.Slot_fill_rate)
        QWidget.setTabOrder(self.Slot_fill_rate, self.PB_chart)
        QWidget.setTabOrder(self.PB_chart, self.PB_chart_A)
        QWidget.setTabOrder(self.PB_chart_A, self.PB_chart_B)
        QWidget.setTabOrder(self.PB_chart_B, self.PB_chart_C)
        QWidget.setTabOrder(self.PB_chart_C, self.Coordinate_AX)
        QWidget.setTabOrder(self.Coordinate_AX, self.Coordinate_AY)
        QWidget.setTabOrder(self.Coordinate_AY, self.Coordinate_CX)
        QWidget.setTabOrder(self.Coordinate_CX, self.Coordinate_CY)
        QWidget.setTabOrder(self.Coordinate_CY, self.Coordinate_DX)
        QWidget.setTabOrder(self.Coordinate_DX, self.Coordinate_DY)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.About.menuAction())
        self.menubar.addAction(self.Language.menuAction())
        self.File.addAction(self.Save.menuAction())
        self.File.addAction(self.Open.menuAction())
        self.File.addAction(self.Export.menuAction())
        self.File.addAction(self.file_exit)
        self.File.addSeparator()
        self.File.addAction(self.file_reset)
        self.Export.addAction(self.file_export_csv)
        self.Export.addAction(self.file_export_pdf)
        self.Export.addAction(self.file_export_xlsx)
        self.Save.addAction(self.file_save_csv)
        self.Save.addAction(self.file_save_txt)
        self.Open.addAction(self.file_open_csv)
        self.Open.addAction(self.file_open_txt)
        self.About.addAction(self.about_version)
        self.Language.addAction(self.language_tc)
        self.Language.addAction(self.language_sc)
        self.Language.addAction(self.language_en)

        self.retranslateUi(Arrange)

        QMetaObject.connectSlotsByName(Arrange)
    # setupUi

    def retranslateUi(self, Arrange):
        Arrange.setWindowTitle(QCoreApplication.translate("Arrange", u"\u6392\u7dda\u8a08\u7b97", None))
        self.language_tc.setText(QCoreApplication.translate("Arrange", u"\u7e41\u9ad4\u4e2d\u6587", None))
        self.language_sc.setText(QCoreApplication.translate("Arrange", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.language_en.setText(QCoreApplication.translate("Arrange", u"English", None))
        self.file_exit.setText(QCoreApplication.translate("Arrange", u"\u7d50\u675f(&X)", None))
#if QT_CONFIG(shortcut)
        self.file_exit.setShortcut(QCoreApplication.translate("Arrange", u"Alt+X", None))
#endif // QT_CONFIG(shortcut)
        self.file_export_csv.setText(QCoreApplication.translate("Arrange", u"CSV(\u9017\u865f\u5206\u9694)(*.csv)", None))
        self.about_version.setText(QCoreApplication.translate("Arrange", u"\u7248\u672c(&V)", None))
#if QT_CONFIG(shortcut)
        self.about_version.setShortcut(QCoreApplication.translate("Arrange", u"Alt+V", None))
#endif // QT_CONFIG(shortcut)
        self.file_save_csv.setText(QCoreApplication.translate("Arrange", u"CSV(\u9017\u865f\u5206\u9694)(*.csv)", None))
        self.file_save_txt.setText(QCoreApplication.translate("Arrange", u"\u6587\u5b57\u6a94(*.txt)", None))
        self.file_open_csv.setText(QCoreApplication.translate("Arrange", u"CSV(\u9017\u865f\u5206\u9694)(*.csv)", None))
        self.file_open_txt.setText(QCoreApplication.translate("Arrange", u"\u6587\u5b57\u6a94(*.txt)", None))
        self.file_reset.setText(QCoreApplication.translate("Arrange", u"\u6062\u5fa9\u51fa\u5ee0\u8a2d\u5b9a", None))
        self.file_export_pdf.setText(QCoreApplication.translate("Arrange", u"PDF", None))
        self.file_export_xlsx.setText(QCoreApplication.translate("Arrange", u"xlsx", None))
        self.arrange_image.setText("")
        self.PB_chart.setText(QCoreApplication.translate("Arrange", u"\u6392\u7dda\u793a\u610f", None))
        self.PB_chart_A.setText(QCoreApplication.translate("Arrange", u"\u65b9\u5f0fA", None))
        self.PB_chart_B.setText(QCoreApplication.translate("Arrange", u"\u65b9\u5f0fB", None))
        self.PB_chart_C.setText(QCoreApplication.translate("Arrange", u"\u65b9\u5f0fC", None))
        self.lb_pa_001.setText(QCoreApplication.translate("Arrange", u"Diameter", None))
        self.un_pa_001.setText(QCoreApplication.translate("Arrange", u"mm", None))
        self.un_pa_002.setText(QCoreApplication.translate("Arrange", u"mm", None))
        self.lb_pa_002.setText(QCoreApplication.translate("Arrange", u"AB length", None))
        self.un_pa_003.setText(QCoreApplication.translate("Arrange", u"mm", None))
        self.lb_pa_003.setText(QCoreApplication.translate("Arrange", u"BC length", None))
        self.un_pa_004.setText(QCoreApplication.translate("Arrange", u"mm", None))
        self.lb_pa_004.setText(QCoreApplication.translate("Arrange", u"CD length", None))
        self.lb_pa_005.setText(QCoreApplication.translate("Arrange", u"B", None))
        self.label_5.setText(QCoreApplication.translate("Arrange", u"A", None))
        self.label_6.setText(QCoreApplication.translate("Arrange", u"C", None))
        self.label_7.setText(QCoreApplication.translate("Arrange", u"D", None))
        self.label_4.setText(QCoreApplication.translate("Arrange", u"Coordinate", None))
        self.label_x.setText(QCoreApplication.translate("Arrange", u"X", None))
        self.label_y.setText(QCoreApplication.translate("Arrange", u"Y", None))
        self.PB_Calculate.setText(QCoreApplication.translate("Arrange", u"\u8a08\u7b97", None))
        self.label_1.setText(QCoreApplication.translate("Arrange", u"Cross-sectional area", None))
        self.label_2.setText(QCoreApplication.translate("Arrange", u"Usable area", None))
        self.PB_Clear_process.setText(QCoreApplication.translate("Arrange", u"\u6e05\u9664", None))
        self.label_3.setText(QCoreApplication.translate("Arrange", u"Slot fill rate", None))
        self.PB_A_export_coordinates.setText(QCoreApplication.translate("Arrange", u"\u532f\u51faA", None))
        self.PB_B_export_coordinates.setText(QCoreApplication.translate("Arrange", u"\u532f\u51faB", None))
        self.PB_C_export_coordinates.setText(QCoreApplication.translate("Arrange", u"\u532f\u51faC", None))
        self.File.setTitle(QCoreApplication.translate("Arrange", u"\u6a94\u6848", None))
        self.Export.setTitle(QCoreApplication.translate("Arrange", u"\u532f\u51fa\u5831\u544a", None))
        self.Save.setTitle(QCoreApplication.translate("Arrange", u"\u5132\u5b58\u53c3\u6578", None))
        self.Open.setTitle(QCoreApplication.translate("Arrange", u"\u958b\u555f\u53c3\u6578", None))
        self.About.setTitle(QCoreApplication.translate("Arrange", u"\u95dc\u65bc", None))
        self.Language.setTitle(QCoreApplication.translate("Arrange", u"\u8a9e\u8a00", None))
    # retranslateUi


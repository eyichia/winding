# 繞線排線計算工具 (Wire Arrangement Calculator) 🧵

![Version](https://img.shields.io/badge/Version-v1.1-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Framework](https://img.shields.io/badge/Framework-PySide6-orange)

這是一個專業的繞線與排線計算應用程式，旨在幫助工程師精確計算導線在不同排列方式（Type A, B, C）下的**總圈數**與**槽滿率**。程式提供即時的座標計算功能，並能產出專業的數據報表。

## ✨ 核心功能

* **多樣化排列計算**：支持三種主流排線方式 (Type A/B/C) 的模擬與對比。
* **精確幾何座標**：自動計算繞線區域 (梯形) 的 A、B、C、D 四點座標，並生成每一圈導線的中心位置。
* **多國語言支援**：內建繁體中文 (TW)、簡體中文 (CN) 與英文 (EN) 切換介面（透過 JSON 語系檔控制）。
* **專業報表輸出**：
    * **PDF 報告**：自動生成包含示意圖、數據摘要與開發資訊的正式文件。
    * **Excel (XLSX) 摘要**：輸出帶有標題與圖示的試算表。
    * **Excel 座標圖**：自動繪製排線路徑座標圖 (Scatter Chart)，模擬導線排列視覺效果。
    * **CSV/TXT**：支援參數的快速匯入與導出。
* **即時日誌系統**：完整記錄操作流程與計算結果。

## 🛠️ 技術棧

* **GUI 框架**：[PySide6](https://doc.qt.io/qtforpython/) (Qt for Python)
* **報表處理**：[openpyxl](https://openpyxl.readthedocs.io/) (Excel 處理與圖表製作)
* **文件輸出**：PySide6.QtGui (PDF 渲染與繪製)
* **數學運算**：Python 標準庫 `math` (點到直線距離、幾何運算)

## 📂 專案結構

```text
.
├── WireArrangeRun260320v4.py  # 主程式邏輯
├── arrange0312_ui.py          # UI 介面定義檔
├── Assets/                    # 圖片資源 (Logo, 示意圖)
├── Languages/                 # 語系 JSON 檔案
├── Sub/
│   └── utils.py               # 通用工具函式 (如：自訂對話框)
└── Reports/                   # 預設報告輸出路徑 (自動建立)
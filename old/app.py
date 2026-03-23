from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_trapezoid():
    # 預設值設為空字串，這樣第一次打開網頁時輸入框是空的
    data = {"upper": "", "lower": "", "height": ""}
    area = None

    if request.method == "POST":
        # 獲取數值
        data["upper"] = request.form.get("upper", "")
        data["lower"] = request.form.get("lower", "")
        data["height"] = request.form.get("height", "")
        
        try:
            # 計算面積
            area = (float(data["upper"]) + float(data["lower"])) * float(data["height"]) / 2
        except ValueError:
            area = "輸入錯誤"
        
    # 將 data 字典整個傳給 HTML
    return render_template("index.html", result=area, data=data)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
app=Flask(__name__)
# __name__代表目前的执行模组

@app.route("/")
# 函式的装饰（Decorator）：以函式为基础，提供附加的功能
def home():
    return "Hello Falsk"

@app.route("/test")
# 代表我们要处理的网络路径
def test():
    return "This is Test"

if __name__=="__main__":
    # 如果以主程式执行
    app.run()
    # 立即启动伺服器
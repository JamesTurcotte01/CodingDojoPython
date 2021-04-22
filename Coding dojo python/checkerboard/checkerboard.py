from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def eightbyfour(num):
    return render_template("index.html", times=num)

@app.route('/<int:num1>/<int:num2>')
def reactive(num1, num2):
    return render_template("index.html", times=num1, timesxx=num2)

if __name__=="__main__":
    app.run(debug=True)
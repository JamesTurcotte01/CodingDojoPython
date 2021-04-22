from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", times=5)	# notice the 2 new named arguments!

@app.route('/play/<x>')
def playnumber(x):
    return render_template("index.html",color="blue" ,times=int(x))

@app.route('/play/<x>/<color>')
def numandcolor(x, color):
    return render_template("index.html", times=int(x), color=color)



if __name__=="__main__":
    app.run(debug=True)

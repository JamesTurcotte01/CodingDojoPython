from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Secret key"

@app.route('/')
def index():
    session['total'] = 0
    return render_template("index.html", total=session['total'])

@app.route('/refresh', methods=['POST'])
def process():
    print(session['total'])
    if session.get('total') != None:
        session['total'] += 1
        print(session['total'])
    return render_template("index.html", total=session['total'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__== "main":
    app.run(debug= True)
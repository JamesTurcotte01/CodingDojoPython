from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def numbersmain():
    return render_template('index.html')


@app.route('/submit')
def submit():
    guess = request.form('guess')
    render_template('index.html', guess = guess)


if __name__== "__main__":
    app.run(debug= True)

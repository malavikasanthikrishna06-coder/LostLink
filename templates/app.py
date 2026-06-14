from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lost')
def lost():
    return render_template('report_lost.html')

@app.route('/found')
def found():
    return render_template('report_found.html')

@app.route('/matches')
def matches():
    return render_template('matches.html')

if __name__ == '__main__':
    app.run(debug=True)

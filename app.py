from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/domestic-violence')
def dv():
    return render_template('dv.html')

if __name__ == "__main__":
    import waitress
    waitress.serve(app, port=5005)
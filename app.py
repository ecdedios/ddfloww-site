import predict
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/domestic-violence')
def dv():
    return render_template('dv.html')

@app.route('/submit_dv', methods=['GET', 'POST'])
def submit_dv():
    if request.method == 'POST':
        feature1 = int(float(request.form['q1']))
        feature2 = int(float(request.form['q2']))
        feature3 = int(float(request.form['q3']))
        feature4 = int(float(request.form['q4']))
        feature5 = int(float(request.form['q5']))
        prediction = predict.predictorizer(feature1,feature2,feature3,feature4,feature5)
        if prediction == '0':
            return render_template('submit_dv.html', prediction='Not Abused', feature1=feature1, feature2=feature2, feature3=feature3, feature4=feature4, feature5=feature5)
        return render_template('submit_dv.html', prediction='Abused', feature1=feature1, feature2=feature2, feature3=feature3, feature4=feature4, feature5=feature5)

        
    return render_template('dv.html')

if __name__ == "__main__":
    import waitress
    waitress.serve(app, port=5005)
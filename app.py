import predict2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/domestic-violence')
def dv():
    return render_template('/domestic-violence/dv.html')

@app.route('/domestic-violence/self-report')
def self_report():
    return render_template('/domestic-violence/self-report.html')

@app.route('/domestic-violence/submit-dv', methods=['GET', 'POST'])
def submit_dv():
    error = None
    if request.method == 'POST':
        if request.form['q1'] == 'x':
            error = 'Missing answer.'
        else:
            feature1 = int(float(request.form['q1']))
            feature2 = int(float(request.form['q2']))
            feature3 = int(float(request.form['q3']))
            feature4 = int(float(request.form['q4']))
            feature5 = int(float(request.form['q5']))
            feature6 = int(float(request.form['q6']))
            feature7 = int(float(request.form['q7']))
            feature8 = int(float(request.form['q8']))
            feature9 = int(float(request.form['q9']))
            prediction = predict2.predictorizer(feature1,
                                                feature2,
                                                feature3,
                                                feature4,
                                                feature5,
                                                feature6,
                                                feature7,
                                                feature8,
                                                feature9)
            return render_template('/domestic-violence/submit_dv.html',
                                    prediction=prediction,
                                    feature1=feature1,
                                    feature2=feature2,
                                    feature3=feature3,
                                    feature4=feature4,
                                    feature5=feature5,
                                    feature6=feature6,
                                    feature7=feature7,
                                    feature8=feature8,
                                    feature9=feature9,)        
        return render_template('/domestic-violence/dv.html', error=error)

if __name__ == "__main__":
    import waitress
    waitress.serve(app, port=5005)
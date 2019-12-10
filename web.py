from flask import Flask, render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakesindex.html')

@app.route('/hello/<name>')
def hello(name):
    if name == "paul":
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)

    return render_template('page.html', name=name)

@app.route('/fuck/<name>')
def hello(name):
    if name == "garry":
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)

    return render_template('page2.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

   
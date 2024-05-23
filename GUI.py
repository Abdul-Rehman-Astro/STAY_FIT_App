from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_pushup')
def run_pushup():
    try:
        subprocess.Popen(['python', r'C:\Users\ABDUL REHMAN\Desktop\StayFIT App\PushUps\PushUps\PushUpCounter-main\PushUpCounter-main\PushUpCounter.py'])
        return 'Pushup Counter will start in 3 seconds.'
    except Exception as e:
        return f'Error starting Pushup Counter: {str(e)}'

@app.route('/run_squat')
def run_squat():
    try:
        subprocess.Popen(['python', r'C:\Users\ABDUL REHMAN\Desktop\StayFIT App\Stayfit\Stayfit\Stay_Fit_with_Abdul\app.py'])
        return 'Squat Counter will start in 3 seconds.'
    except Exception as e:
        return f'Error starting Squat Counter: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)

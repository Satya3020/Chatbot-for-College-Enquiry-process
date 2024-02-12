from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def run_script():
    result = subprocess.run(['python', 'final.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output

if __name__ == '__main__':
    app.run(debug=True)

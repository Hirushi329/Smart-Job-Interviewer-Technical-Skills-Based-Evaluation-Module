from flask import Flask
from TextToSpeech import Execution
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new.html', test_str=dynamic_page() if request.args.get("start") is not None else None)
    # return "Hello world"
    # return render_template('json.html')

def dynamic_page():
    return Execution.run()
    print("log error")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
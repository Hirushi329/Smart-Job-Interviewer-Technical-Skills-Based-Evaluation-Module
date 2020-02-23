#rendering the HTML page which has the button
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")
app.run()
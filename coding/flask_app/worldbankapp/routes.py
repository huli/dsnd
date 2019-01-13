from worldbankapp import app
from flask import render_template
from wrangling_scripts.wrangling import get_data

data = get_data()
print(data)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

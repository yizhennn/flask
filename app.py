#virtualenv flask
#cd flask
#source bin/activate
#python app.py

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
bootstrap= Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')


@app.route("/")
def home():
    paragraphs=['s1', 's2', 's3' ]
    #title = "Flask Web App"
    return render_template('index.html',title="miss hippo",data=paragraphs)

@app.route("/test")
def test():
        return "This is a test!"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)



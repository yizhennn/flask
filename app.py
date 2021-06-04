#virtualenv flask
#cd flask
#cd/Users/Apple/Documents/GitHub/flask
#source bin/activate
#python app.py
from flask import Flask,render_template #,current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import Registerform

#with app.app_context():
app=Flask(__name__)
bootstrap= Bootstrap(app)
db = SQLAlchemy(app)

app.config.from_object(Config)

# basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-KEY'


@app.route("/")
def index():
    return render_template('index.html',title="miss hippo")


@app.route("/register",methods=['GET', 'POST'])
def register():
    form=Registerform()
    
    if form.validate_on_submit():
        return 'Success Submit'

    return render_template('register.html',title="register",form=form)


@app.route("/test")
def test():
        return "This is a test!"

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY']='SECRET_KEY'
    app.run(debug=True,host='0.0.0.0',port=5000)

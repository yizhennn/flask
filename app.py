#virtualenv flask
#cd flask
#source bin/activate
#python app.py#####

from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap= Bootstrap(app)


@app.route("/")
def home():
    paragraphs=['s1', 's2', 's3' ]
    #title = "Flask Web App"
    return render_template('index.html',title="河馬",data=paragraphs)

@app.route("/test")
def test():
        return "This is a test!"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)



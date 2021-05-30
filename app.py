#virtualenv flask
#cd flask
#source bin/activate
#python app.py#####

from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hi! first day from learning flask "

@app.route("/test")
def test():
        return "This is a test!"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=3000)



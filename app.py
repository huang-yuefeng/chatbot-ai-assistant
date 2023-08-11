#from flask import Flask
from flask import Flask, render_template, request
app = Flask(__name__)
app.static_folder = 'static'

#@app.route('/')
#def hello_world():
#    return 'Hello World!'

@app.route("/")
def home():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)

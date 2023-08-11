#from flask import Flask
from flask import Flask, render_template, request
from data_analyst import robot_gpt
app = Flask(__name__)
app.static_folder = 'static'

robot = None
def init_robot(file_path):
    global robot
    if robot == None:
        robot = robot_gpt(file_path)

#@app.route('/')
#def hello_world():
#    return 'Hello World!'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    init_robot("./sample_data/titanic.csv")
    userText = request.args.get('msg')
    return userText

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)

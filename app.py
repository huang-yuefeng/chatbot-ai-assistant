#from flask import Flask
import os
from flask import Flask, render_template, request
from data_analyst import robot_gpt
app = Flask(__name__)
app.static_folder = 'static'

robot = None
def init_robot(file_path):
    global robot
    if robot == None:
        robot = robot_gpt(file_path)

#check iamge type whether is leggal
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),"./sample_data/")
app.config['IMAGE_EXTENSIONS'] = set(['png', 'jpg', 'jpeg','csv'])
app.config['STRUCT_DATA_EXTENSIONS'] = set(['csv'])
def check_type(filename):
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['IMAGE_EXTENSIONS']:
        return "IMAGE"
    elif '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['STRUCT_DATA_EXTENSIONS']:
        return "STRUCT_DATA"
    else:
        return "ILEGGAL"

def extract_text(img):
    #to be implemented
    return 0;

#process image
def process_image(file):
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    text= extract_text(img)
    #will consider any image with text-length below 200 char to be a scene
    if(len(text)<200): 
        #if it is a scence image save to it certain folder and add its tage to tag knowledge base 
        cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'],"photo",filename), img) 
    else: 
        #if image is text-based insert it split its text to paragraph and then add to its knowledge base 
        cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'],"text-based",filename), img)

#process csv
def process_structed(file):
    table = file.read()
    print (table)
    table = table.decode("utf-8")
    print (table)

#smoke test
#@app.route('/')
#def hello_world():
#    return 'Hello World!'

#homepage
@app.route("/")
def home():
    return render_template("index.html")

#return robot answer
@app.route("/get")
def get_bot_response():
    init_robot("./sample_data/titanic.csv")
    userText = request.args.get('msg')
    userText,image_set = robot.run(userText)
    if len(image_set)>0:
        image_name = list(image_set)[0]
        os.system("mv ./"+image_name+" "+app.static_folder+"/"+image_name)
        image_name = "static/"+image_name
        
    else:
        image_name = None
    return [userText,image_name]

#upload images

@app.route("/upload",methods=['POST'])
def uploader():
    if request.method == 'POST':
        uploaded_files =request.files.getlist("file[]")
        for file in uploaded_files:
            if not file:
                continue;
            else:
                file_type = check_type(file.filename)
            if file_type=="IMAGE":
                process_image(file)
            elif file_type=="STRUCT_DATA":
                process_structed(file)
            else:
                print("illegal input file type "+file.filename)

    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)

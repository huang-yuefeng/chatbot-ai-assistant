#from flask import Flask
import os
from flask import Flask, render_template, request
from data_analyst import *
app = Flask(__name__)
app.static_folder = 'static'

#check iamge type whether is leggal
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),"./sample_data/")
app.config['IMAGE_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
app.config['STRUCT_DATA_EXTENSIONS'] = set(['csv', 'xls', 'xlsx'])

def check_type(filename):
    file_type=None
    if '.' in filename:
        file_type = filename.rsplit('.', 1)[1].lower()
    if file_type in app.config['IMAGE_EXTENSIONS']:
        return "IMAGE",file_type
    elif file_type in app.config['STRUCT_DATA_EXTENSIONS']:
        return "STRUCT_DATA",file_type
    else:
        return "ILEGGAL",file_type

def extract_text(img):
    #to be implemented
    return 0;

#process image
def process_image(f, file_type):
    pass
    '''
    img = cv2.imdecode(np.fromstring(f.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    text= extract_text(img)
    #will consider any image with text-length below 200 char to be a scene
    if(len(text)<200): 
        #if it is a scence image save to it certain folder and add its tage to tag knowledge base 
        cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'],"photo",filename), img) 
    else: 
        #if image is text-based insert it split its text to paragraph and then add to its knowledge base 
        cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'],"text-based",filename), img)
    '''

#process csv
GLOBAL_ROBOT = None
def process_structed(f, file_type):
    global GLOBAL_ROBOT
    file_path = "./sample_data/"+f.filename
    f.save(file_path)
    if file_type == "csv":
        GLOBAL_ROBOT = robot_gpt_csv(file_path)
    elif file_type == "xls" or file_type == "xlsx":
        GLOBAL_ROBOT = robot_gpt_excel(file_path)

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
    if(GLOBAL_ROBOT == None):
        userText = "Please select an input csv or excel file first! Then we can have an amazing tour."
        image_name = None
        return [userText,image_name]
    userText = request.args.get('msg')
    userText,image_set = GLOBAL_ROBOT.run(userText)
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
        for f in uploaded_files:
            if not f:
                continue;
            else:
                category,file_type = check_type(f.filename)

                try: 
                    if category=="IMAGE":
                        process_image(f, file_type)
                    elif category=="STRUCT_DATA":
                        process_structed(f, file_type)
                    else:
                        print("illegal input file type "+f.filename)
                except Exception as e:
                    template = "I have encountered an exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(e).__name__, e.args)
                    print (message+f.filename)

    return render_template("index.html")
    
if __name__ == '__main__':
    import pandas as pd
    app.run(host="0.0.0.0", port=5003)

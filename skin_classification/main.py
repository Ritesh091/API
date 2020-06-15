# import libraries
from flask import Flask, jsonify, request
import cv2
import os 
from skin_classify import Skin
import json
from werkzeug.utils import secure_filename
import io
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# define current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))     
model_dir_path = current_dir+"/model"    

imageObj = Skin(model_dir_path)

# image extensions
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]     
app.config['UPLOAD_FOLDER'] = ""
# load model
# model_path = current_dir + "/model/cnn_model2.pkl"                   
#dark = performDetect(imagePath = file)

# function to allow only valid image extensions
def allowed_image(filename):                                          
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    # convert extesions to uppercase and validate
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:      
        return True
    else:
        return False

@app.route('/')
def main():
    return "Server is running!"

@app.route('/getPrediction', methods=['GET', 'POST'])
# function to upload image 
def upload():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']   # request to upload file
        #filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #dark = imageObj.test(image = file.filename)
        if (file.filename) =='':
            return jsonify({"status":False, "message":'No file selected for uploading'}),400
        # allowed valid image file
        if file and allowed_image(file.filename):
            in_memory_file = io.BytesIO()
            #save image in memmory
            file.save(in_memory_file)
            data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            color_image_flag = 1
            #decode the image file
            img = cv2.imdecode(data, color_image_flag)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #img = cv2.imread(img, cv2.COLOR_BGR2RGB)
            dark = imageObj.test(img)

            output = {"status":True, "message":"Prediction generated", "prediction":str(dark[0]), "probability": str(dark[1])}
            return jsonify(output)
        else:
            return jsonify({"status":False, "message":'please enter valid image file'}),400
    else: 
        return jsonify({"status":False, "message":'No file selected for uploading'}),400
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6700, debug = True) 
    
    

  




 

    

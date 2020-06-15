from flask import Flask, jsonify, request
import cv2
import os 
from retail import Retail
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

imageObj = Retail(model_dir_path)

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]     
app.config['UPLOAD_FOLDER'] = ""

def allowed_image(filename):                                          
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    # convert extesions to uppercase and validate
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:      
        return True
    else:
        return False

@app.route('/getPrediction', methods=['GET', 'POST'])
# function to upload image 
def upload():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']   # request to upload file
        if (file.filename) =='':
            return jsonify({"status":False, "message":'No file selected for uploading'}),400
        # allowed valid image file
        if file and allowed_image(file.filename):
            in_memory_file = io.BytesIO()
            #save image in memmory
            file.save(in_memory_file)
            data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            color_image_flag = 3
            #decode the image file
            img = cv2.imdecode(data, color_image_flag)
            dark = imageObj.prediction(img)
            print(dark)

            output = {"status":True, "message":"Prediction generated", "tags":dark, "image":file.filename}
            return jsonify(output)
        else:
            return jsonify({"status":False, "message":'please enter valid image file'}),400
    else: 
        return jsonify({"status":False, "message":'No file selected for uploading'}),400
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6700, debug = False) 
    


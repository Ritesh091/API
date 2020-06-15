from keras.models import load_model
import pandas as pd  
import numpy as np 
import tensorflow as tf
import cv2
from PIL import Image

class Skin:
    def __init__(self,model_dir):
        self.model = load_model(model_dir+'/my_model.h5')
        self.model._make_predict_function()
        self.graph = tf.get_default_graph()

    def test(self,image):
        img = cv2.resize(image, (224,224))
        img = np.expand_dims(img, axis=0)
        with self.graph.as_default():
            result = self.model.predict_proba(img)
            #result1 = self.model.predict_proba(img)
            print(result)
            score = round(result[0][0]*100,2)
            result = np.round(result)
            if (int(result[0][0]) == 0):
                classify = 'Benign'
                score = 100 - score
            else:
                classify = 'Malignant'
        return classify, score
    
if __name__ == '__main__':
    model_dir_path = "/home/riteshjain/Desktop/skin_classification/model/"
    image_path = '/home/riteshjain/anaconda3/Notebook/Skin/Benign/ISIC_0000000.jpg'

    imageObj = Skin(model_dir_path)
    result1 = imageObj.test(image_path)
    print(result1)


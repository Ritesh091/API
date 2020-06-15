
import pandas as pd  
import numpy as np 
import os
import tensorflow as tf
import cv2
from PIL import Image
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
from keras.applications.vgg16 import preprocess_input
from sklearn.externals import joblib 
from keras import backend as K
K.clear_session()

class Retail:
    def __init__(self,model_dir):
        self.model = np.load(model_dir+'/features.npy')
        self.model_1 = VGG16(weights='imagenet', include_top=False)
        #self.model_1._make_predict_function()
        self.data = pd.read_csv(model_dir+'/image_db.csv', index_col = 0)
        self.graph = tf.get_default_graph()

    def feature_extraction(self, image_path):
        #image_path = cv2.imread(image_path)
        img = cv2.resize(image_path,(224,224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        with self.graph.as_default():
            features = self.model_1.predict(img).flatten()
        print(features.shape)
        
        return features

    def test(self, image_path):
        test_features = self.feature_extraction(image_path)
        similarity = cosine_similarity([test_features], self.model)
        similar = (-similarity).argsort()
        for i in similar:
            a = i[:10]

        result = []
        for sim_ in a:
            results = self.data[self.data.index == sim_]['image'].values[0]

            sim = round(similarity[0][sim_]*100, 2)
            json_result = {"image":None, "similarity":None}
            json_result['image'] = results
            json_result['similarity'] = sim
            result.append(json_result)

        return result
    
if __name__ == '__main__':
    model_dir_path = "/home/riteshjain/Desktop/retail_recommendation/model"
    image_path = '/home/riteshjain/Desktop/retail_recommendation/test/'
    imageObj = Retail(model_dir_path)
    for a in os.listdir(image_path):

        
        result1 = imageObj.test(image_path + a)
        print(result1) 


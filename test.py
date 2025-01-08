import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from pathlib import Path

def judge(img):
    model = tf.keras.models.load_model('Brain_Tumor_Model.keras')
    model.summary()
    image_path = file_path = os.path.join(Path.cwd(), img) # "Dataset/Test/Glioma/Te-gl_0014.jpg"

    img = cv2.imread(image_path)
    class_name = ["神经胶质瘤", "脑膜瘤", "健康的", "脑垂体瘤"]
    plt.title("Test Image [Glioma]")
    plt.xticks([])
    plt.yticks([])
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    model_prediction = class_name[result_index]
    return model_prediction

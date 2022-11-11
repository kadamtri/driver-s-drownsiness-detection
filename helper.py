import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
import numpy as np
import cv2

def preprocess(frame):
    frame = np.array(frame)
    image = cv2.resize(frame, (145, 145))
    image = image.astype('float32')
    image /= 255
    image = np.expand_dims(image, axis=0)
    return image

def prediction(frame):
    model = tf.keras.models.load_model('drowiness_new6')
    frame = cv2.resize(frame, (145, 145), interpolation= cv2.INTER_AREA)
    frame = frame.reshape(1, frame.shape[0], frame.shape[1], 3)
    prediction = model.predict(frame)
    pred = prediction.argmax()
    lb.classes_ = np.load('classes.npy')
    output = lb.inverse_transform([pred])
    return output 
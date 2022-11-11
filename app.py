import streamlit as st
import numpy as np
import helper
import cv2
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

st.sidebar.title("App Name")

selectbox = st.sidebar.selectbox(
    'Select the type of input', ('None','Upload Image', 'Take A Shot'))
# Take A Shot
if selectbox == 'Take A Shot':
    Uploaded_file = st.camera_input('Take A Shot')
    if Uploaded_file is not None:
        file_bytes = np.asarray(
            bytearray(Uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = helper.preprocess(frame)
        # st.image(image, caption='Uploaded Image', use_column_width=True)
        # prediction
        output = helper.prediction(frame)
        if (output == 2):
            X = "closed"
        elif (output == 3):
            X = "Open"
        elif (output == 1):
            X = "no_yawn"
        else:
            X = "yawn"
        str_out = 'prediction : ' + str(X)
        st.success(str_out)
# Image Input
if selectbox == 'Upload Image':
    Uploaded_file = st.sidebar.file_uploader(
        "Insert File", type=['.jpg', '.jpeg', '.png'])
    if Uploaded_file is not None:
        file_bytes = np.asarray(
            bytearray(Uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = helper.preprocess(frame)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        # prediction
        output = helper.prediction(frame)
        if (output == 2):
            X = "closed"
        elif (output == 3):
            X = "Open"
        elif (output == 1):
            X = "no_yawn"
        else:
            X = "yawn"
        str_out = 'prediction : ' + str(X)
        st.success(str_out)
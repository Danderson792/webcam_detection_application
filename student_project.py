import cv2
import streamlit as st
import time
from datetime import datetime


st.title('Motion Detector')
start = st.button('Start Camera')



if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        now = datetime.now()
        day_of_week = now.strftime(format('%A'))
        date = now.strftime(format('%I:%M:%S%p'))
        color = st.color_picker

        cv2.putText(img=frame, text=day_of_week, org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=4, color=(76, 0, 153),
                    thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=date, org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=4, color=(76, 0, 153),
                    thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)



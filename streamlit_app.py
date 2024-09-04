#import streamlit as st

#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)


import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Webcam Photo Capture and Celebration")

# Display webcam feed
st.subheader("Capture a photo from your webcam")
run = st.checkbox('Show Webcam')

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    camera.release()

# Capture photo button
if st.button("Capture Photo"):
    if ret:
        st.image(frame, caption="Captured Photo", use_column_width=True)
        
        # Save captured image
        img = Image.fromarray(frame)
        img.save('captured_photo.png')

        # Show celebration balloons
        st.balloons()
    else:
        st.write("Failed to capture photo. Make sure your webcam is working.")

st.write("Press the 'Show Webcam' checkbox to start the webcam and capture a photo.")






import streamlit as st
from PIL import Image, ImageDraw
import moondream as md
import os

# Initialize Moondream model
api_key = os.getenv("MOONDREAM_API_KEY")
model = md.vl(api_key=api_key)

def draw_bounding_box(image, annotation):
    img = image.copy()
    draw = ImageDraw.Draw(img)
    for obj in annotation['objects']:
        x_min, y_min, x_max, y_max = obj['x_min'], obj['y_min'], obj['x_max'], obj['y_max']
        width, height = img.size
        left = x_min * width
        top = y_min * height
        right = x_max * width
        bottom = y_max * height
        draw.rectangle([left, top, right, bottom], outline="red", width=3)
    return img

def object_detection():
    st.title("Detect Objects")
    uploaded_file = st.file_uploader("Upload an image (PNG or JPEG)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        detect_subject = st.text_input("Enter the subject to detect:", "subject")
        if st.button("Detect Objects"):
            with st.spinner("Detecting objects..."):
                detect_result = model.detect(image, detect_subject)
                st.write("**Detected Objects:**", detect_result["objects"])
                annotated_image = draw_bounding_box(image, detect_result)
                st.image(annotated_image, caption='Image with Bounding Box', use_container_width=True)

object_detection()

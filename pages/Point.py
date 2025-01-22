import streamlit as st
from PIL import Image, ImageDraw
import moondream as md
import os

# Initialize Moondream model
api_key = os.getenv("MOONDREAM_API_KEY")
model = md.vl(api_key=api_key)

def draw_points(image, points):
    img = image.copy()
    draw = ImageDraw.Draw(img)
    for point in points:
        x, y = point['x'] * img.width, point['y'] * img.height
        dot_radius = 15
        draw.ellipse([x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius], outline='black', width=2)
        draw.ellipse([x - dot_radius + 2, y - dot_radius + 2, x + dot_radius - 2, y + dot_radius - 2], fill='red')
    return img

def pointing():
    st.title("Point at an Object")
    uploaded_file = st.file_uploader("Upload an image (PNG or JPEG)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        point_subject = st.text_input("Enter the subject to point at:", "subject")
        if st.button("Point at Object"):
            with st.spinner("Pointing at object..."):
                point_result = model.point(image, point_subject)
                st.write("**Points:**", point_result["points"])
                points_image = draw_points(image, point_result["points"])
                st.image(points_image, caption='Image with Points', use_container_width=True)

pointing()

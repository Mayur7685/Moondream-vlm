import streamlit as st
from PIL import Image
import moondream as md
import os

# Initialize Moondream model
api_key = os.getenv("MOONDREAM_API_KEY")
model = md.vl(api_key=api_key)

def question_answering():
    st.title("Ask a Question")
    uploaded_file = st.file_uploader("Upload an image (PNG or JPEG)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        encoded_image = model.encode_image(image)

        user_question = st.text_input("Enter your question about the image:", "What's in this image?")
        if st.button("Ask Question"):
            with st.spinner("Querying the model..."):
                answer = model.query(encoded_image, user_question)["answer"]
                st.write("**Answer:**", answer)

question_answering()

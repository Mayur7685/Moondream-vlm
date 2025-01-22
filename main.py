import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Validate API Key
api_key = os.getenv("MOONDREAM_API_KEY")
if not api_key:
    st.error("API key not found. Please set the MOONDREAM_API_KEY in your .env file.")
    st.stop()

st.title("Moondream Vision Model Demo")
st.write("""
    This application demonstrates various capabilities of the Moondream Vision Model, providing an interactive experience to explore image analysis functionalities. Here's what you can do:
    
    - **Query**: Ask questions about the content of images and get human-like answers.
    - **Caption**: Generate detailed descriptions of scenes within uploaded images.
    - **Object Detection**: Identify and visualize objects within images by drawing bounding boxes around them.
    - **Point**: Locate specific objects or features in images by marking their X, Y coordinates.

    Navigate through the sidebar to explore each feature. Simply upload an image in each section, interact with the model, and see the results in real-time!
    """)

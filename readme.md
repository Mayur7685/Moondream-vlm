<h1 align="center">Moondream Vision Model Demo</h1>  

![moondream](https://github.com/user-attachments/assets/8c4e98db-e9df-45ac-86f9-085e1c6b06e6)

Explore the power of Moondream's Vision-Language Model with this interactive Streamlit app. The app allows you to upload images and use Moondream's cutting-edge capabilities, such as caption generation, image question answering, object detection, and object pointing.  

## Features  
- **Generate Caption**: Upload an image and get an AI-generated caption describing its content.  
- **Ask a Question**: Query the image with natural language questions to retrieve specific information.  
- **Detect Objects**: Identify and annotate objects in the image using bounding boxes.  
- **Point at an Object**: Highlight specific points of interest related to objects in the image.  

## Installation  

### Prerequisites  
1. **Python 3.8 or higher**  
2. **Streamlit**  
3. **Moondream SDK**  

### Clone the Repository  
```bash  
git clone https://github.com/Mayur7685/Moondream-vlm.git  
cd moondream-multipage-app  
```  

### Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Set Up Environment Variables  
1. Create a `.env` file in the project root directory.  
2. Add your Moondream API key:  
```plaintext  
MOONDREAM_API_KEY=your_api_key_here  
```  

## Usage  

### Run the App  
Start the Streamlit app using the following command:  
```bash  
streamlit run moondream_multipage.py  
```  

### Navigate Through the Features  
Use the **sidebar** to switch between different features:  
1. **Introduction**: Learn about the app.  
2. **Generate Caption**: Generate a descriptive caption for an uploaded image.  
3. **Ask a Question**: Ask natural language questions about an image.  
4. **Detect Objects**: Detect and annotate objects in the image.  
5. **Point at an Object**: Highlight specific points of interest in the image.  

## Directory Structure  
```
Moondream-vlm/  
├── main.py                 # main entry file
├── pages
│   ├── Caption.py
│   ├── Query.py
│   ├── Object_Detection.py
│   └── Point.py
├── requirements.txt        # Python dependencies     
└── readme.md               # Project documentation  
```  

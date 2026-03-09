import streamlit as st                 # Streamlit library import for building web UI
import cv2                             # OpenCV library import for image processing
import numpy as np                     # NumPy library for handling image byte arrays
import pandas as pd                    # Pandas for reading CSV and Excel files
from docx import Document              # Library to read DOCX files

from image_preprocessing import preprocess_image
from ocr_text_extractor import extract_text_from_image
from ollama_ai_processor import summarize_document, extract_structured_data
from pdf_to_images import convert_pdf_to_images


st.title("AI Document Scanner")


uploaded_file = st.file_uploader(
    "Upload Document",
    type=["jpg","jpeg","png","pdf","docx","txt","xlsx","csv"]
)

extracted_text = ""                # Initialize variable to hold extracted text

# Function to read text from DOCX files
def read_docx(file):
    doc = Document(file)

    text = ""
    for para in doc.paragraphs:       # loop through each paragraph in the document
        text += para.text + "\n"      # Combine all paragraph text into a single string with newlines
    return text

# Function to read CSV files
def read_csv(file):
    df = pd.read_csv(file)       # Load CSV into pandas dataframe
    return df.to_string()        # Convert dataframe into string so it can be processed as text

# Function to read Excel files
def read_xlsx(file):
    df = pd.read_excel(file)     # Load Excel into pandas dataframe
    return df.to_string()        # Convert dataframe into string so it can be processed as text


#If user has uploaded a file, we will process it based on its type
if uploaded_file:
    
    # Process PDF files
    if uploaded_file.type == "application/pdf":

        with open("temp.pdf","wb") as f:          #save uploaded pdf to a temporary file
            f.write(uploaded_file.read())          

        images = convert_pdf_to_images("temp.pdf")       # Convert PDF pages to images

        for img in images:                       # Loop through each page image
            processed = preprocess_image(img)       # Preprocess image (grayscale, blur, threshold)
            # 🔧 image upscale for better OCR
            processed = cv2.resize(processed, None, fx=2, fy=2) 
            extracted_text += extract_text_from_image(processed)           # Extract text from preprocessed image and append to extracted_text variable

        
    # Process image files (jpg, jpeg, png)
    elif uploaded_file.type.startswith("image"):          

        file_bytes = np.asarray(               # Convert uploaded file bytes into a NumPy array 
            bytearray(uploaded_file.read()),    #
            dtype=np.uint8                      # data type for integer
        )

        image = cv2.imdecode(file_bytes,1)       # Decode image from byte array using OpenCV
        st.image(image,caption="Uploaded Image")      # Show uploaded image in UI


        processed = preprocess_image(image)
        # 🔧 image upscale for better OCR
        processed = cv2.resize(processed, None, fx=2, fy=2)
        extracted_text = extract_text_from_image(processed)

        
    # Process text files
    elif uploaded_file.type == "text/plain":
        extracted_text = uploaded_file.read().decode("utf-8")      # Read text file content and decode from bytes to string


    # Process DOCX files      
    elif uploaded_file.name.endswith(".docx"):
        extracted_text = read_docx(uploaded_file)       # Read DOCX file and extract text


    # Process CSV files
    elif uploaded_file.name.endswith(".csv"):
        extracted_text = read_csv(uploaded_file)        # Read CSV file and convert to string


    # Process Excel files
    elif uploaded_file.name.endswith(".xlsx"):
        extracted_text = read_xlsx(uploaded_file)       # Read Excel file



    # Display extracted text in UI
    st.subheader("Extracted Text")
   
    # Show extracted text in a scrollable text box
    st.text_area("Text extracted from the document will appear here", value=extracted_text, height=300)

     
    #button to download extracted text as a .txt file 
    st.download_button(
        label="Download Extracted Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

    # When user clicks this button AI generates summary
    if st.button("Generate Summary"):
        summary = summarize_document(extracted_text)     # Send extracted text to AI model
        st.subheader("AI Summary")           
        st.write(summary)              # Display AI-generated summary in UI

    # When user clicks this button AI extracts structured data in JSON format

    if st.button("Extract Structured Data"):
        data = extract_structured_data(extracted_text)
        st.subheader("Structured Data")
        st.write(data)      #Show extracted JSON data

        # allow user to download JSON   
        st.download_button(
            label="Download JSON",
            data=str(data),     # Convert JSON data to string for downloading
            file_name="structured_data.json",    
            mime="application/json"    
        )       



st.write("Made with ❤️ by Shivani Saini")

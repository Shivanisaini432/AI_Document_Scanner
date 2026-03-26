# AI Document Scanner

AI Document Scanner is a Python-based application that extracts text from multiple document formats using OCR and processes the extracted content using AI.

The application allows users to upload different types of documents, extract text, generate AI summaries, and extract structured data.

---

# Features

* Upload and scan multiple document formats
* Extract text using OCR
* Generate AI-based document summary
* Extract structured data from documents
* Download extracted text
* Download structured JSON output

---

# Supported File Types

The application supports the following document formats:

* Images (`jpg`, `jpeg`, `png`)
* PDF
* TXT
* DOCX
* CSV
* XLSX

---

# Technologies Used

The project is built using the following technologies:

* Python
* Streamlit for the user interface
* OpenCV for image processing
* PaddleOCR for text extraction
* pandas for reading CSV and Excel files
* python-docx for DOCX processing
* pdf2image for converting PDF pages to images
* Ollama for AI processing

---

# Project Structure

```
AI_Document_Scanner
│
├── app.py
├── image_preprocessing.py
├── ocr_text_extractor.py
├── pdf_to_images.py
├── ollama_ai_processor.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/Shivanisaini432/AI_Document_Scanner.git
```

Move into the project directory:

```
cd AI_Document_Scanner
```

Install all required dependencies:

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Streamlit application:

```
streamlit run app.py
```

After running the command, the application will open in your browser.

---

# How the Application Works

1. User uploads a document
2. System detects the file type
3. OCR extracts text from images or PDF
4. Extracted text is displayed in the interface
5. AI processes the text to generate:

   * Document summary
   * Structured data
6. User can download extracted text or JSON output

---

# Example Workflow

Upload Document
→ Extract Text
→ Generate AI Summary
→ Extract Structured Data
→ Download Text / JSON

---

# Future Improvements

Possible improvements for the project:

* PowerPoint file support
* Automatic document type detection
* Batch document processing
* Export results to PDF or Excel
* Cloud deployment

---

# Author

Shivani Saini

Built using Python, OCR, and AI.


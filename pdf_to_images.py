# """
# Read_PDF.py

# This script extracts text from a scanned PDF file using PaddleOCR.

# Requirements:
# - paddleocr
# - pdf2image
# - poppler (installed and added to system PATH on Windows)

# Author: Shivani
# """

# # Import required libraries
# from paddleocr import PaddleOCR          # OCR engine
# from pdf2image import convert_from_path  # Convert PDF pages to images
# import os                                # For deleting temp image files


# def pdf_to_text(pdf_path: str, lang: str = 'en') -> str:
#     """
#     Convert a scanned PDF into plain text using OCR.

#     Parameters
#     ----------
#     pdf_path : str
#         Path to the input PDF file.
#     lang : str
#         Language code for OCR (default = 'en').

#     Returns
#     -------
#     str
#         Extracted text from all pages combined.
#     """

#     # Step 1: Initialize PaddleOCR model
#     # use_angle_cls=True helps detect rotated text
#     print("Initializing OCR model...")
#     ocr = PaddleOCR(lang=lang, use_angle_cls=True)

#     # Step 2: Convert PDF pages into images
#     print("Converting PDF pages to images...")
#     pages = convert_from_path(pdf_path, dpi=300)

#     all_text = []  # Store text from all pages

#     # Step 3: Loop through each page
#     for i, page in enumerate(pages):
#         print(f"Processing page {i + 1}...")

#         # Temporary image file name
#         img_path = f"__temp_page_{i}.png"

#         # Save PDF page as image
#         page.save(img_path, 'PNG')

#         # Step 4: Perform OCR on image
#         result = ocr.ocr(img_path, cls=True)

#         page_text_lines = []

#         # Step 5: Extract text from OCR result
#         # result format:
#         # [[ [bbox], (text, confidence) ], ...]
#         for page_result in result:
#             for line in page_result:
#                 text = line[1][0]        # Extract detected text
#                 confidence = line[1][1]  # Confidence score
#                 page_text_lines.append(text)

#         # Combine lines for current page
#         all_text.append("\n".join(page_text_lines))

#         # Step 6: Delete temporary image file
#         os.remove(img_path)

#     # Step 7: Combine text from all pages
#     return "\n\n".join(all_text)


# # ===============================
# # MAIN PROGRAM STARTS HERE
# # ===============================

# # 🔹 Direct PDF path
# pdf_path = "Marksheet.pdf"   # Change if needed
# language = "en"              # OCR language

# print("Starting PDF OCR process...\n")

# # Call function
# extracted_text = pdf_to_text(pdf_path, lang=language)

# print("\n========= EXTRACTED TEXT =========\n")
# print(extracted_text)


from pdf2image import convert_from_path
import numpy as np

def convert_pdf_to_images(pdf_path):

    images = convert_from_path(pdf_path)

    image_list = []

    for img in images:

        image_np = np.array(img)

        image_list.append(image_np)

    return image_list
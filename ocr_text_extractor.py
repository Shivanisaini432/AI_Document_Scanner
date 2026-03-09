
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text_from_image(image):

    result = ocr.ocr(image)

    extracted_text = ""

    if result is not None:
        for line in result:
            if line is not None:
                for word in line:
                    extracted_text += word[1][0] + " "

    return extracted_text






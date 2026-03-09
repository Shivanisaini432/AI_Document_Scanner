
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en',
                det_db_thresh=0.3,  # Lower threshold to detect more text regions
                det_db_box_thresh=0.5,  # Lower box threshold to include more text boxes)
)

def extract_text_from_image(image):

    result = ocr.ocr(image)

    extracted_text = ""

    if result is not None:
        for line in result:
            for word in line:
                extracted_text += word[1][0] + " "

    return extracted_text






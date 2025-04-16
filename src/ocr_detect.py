from paddleocr import PaddleOCR

def detect_text(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    result = ocr.ocr(image_path)
    detected = []
    for line in result[0]:
        for word_info in line:
            if isinstance(word_info, tuple):
                detected.append((word_info[0], word_info[1]))
    return detected

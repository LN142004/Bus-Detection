from src.infer import load_model
from src.ocr_detect import detect_text
from src.speak import speak
import cv2

def main():
    model = load_model()
    image_path = "img1 (1).jpg"
    results = model(image_path)

    bbox = results.xyxy[0][0][:4].tolist()
    x1, y1, x2, y2 = map(int, bbox)

    img = cv2.imread(image_path)
    cropped = img[y1:y2, x1:x2]
    crop_path = "cropped.jpg"
    cv2.imwrite(crop_path, cropped)

    detected = detect_text(crop_path)
    bus_number = detected[0][0] if detected else "Unknown"

    speak_text = f"The detected bus number is {bus_number}"
    mp3_file = speak(speak_text)

    print(speak_text)
    return mp3_file

if __name__ == "__main__":
    main()

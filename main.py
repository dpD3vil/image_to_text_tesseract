import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('1.jpg')
text = pytesseract.image_to_string(img)
text = text.rstrip()
print(text)
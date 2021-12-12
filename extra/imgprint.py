import cv2
import easyocr as easyocr
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread("../img/plate.jpg")
reader = easyocr.Reader(['en'])
result = reader.readtext(img)
print(result[0][-2])

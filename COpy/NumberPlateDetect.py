from tkinter import Label, messagebox

import cv2
import numpy as np
import pytesseract
from ConverttoString import con
from totalincoming import record
from message import Message
from tkinter import Tk
class NumDetect:
    def __init__(self, img_name):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        img = cv2.imread(img_name)  ## Reading Image
        # Converting into Gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detecting plate
        plateCascade = cv2.CascadeClassifier("../extra/haarcascade_russian_plate_number.xml")
        nplate = plateCascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in nplate:
            # Crop a portion of plate
            a, b = (int(0.02 * img.shape[0]), int(0.025 * img.shape[1]))
            plate = img[y + a:y + h - a, x + b:x + w - b, :]
            # make image more darker to identify the LPR
            ## iMAGE PROCESSING
            kernel = np.ones((1, 1), np.uint8)
            plate = cv2.dilate(plate, kernel, iterations=1)
            plate = cv2.erode(plate, kernel, iterations=1)
            plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
            (thresh, plate) = cv2.threshold(plate_gray, 120, 255, cv2.THRESH_TOZERO)
            cv2.imwrite('../img/plate.jpg', plate)
            cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)
            cv2.rectangle(img, (x, y - 40), (x + w, y), (51, 51, 255), -1)
            cv2.imshow("Result", img)
            con()
            record()
            cv2.destroyAllWindows()

# NumDetect('../img/car7.png')
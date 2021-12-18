import cv2
import numpy as np
import pytesseract
from ConverttoString import con
from totalincoming import record
class NumDetect:
    def __init__(self, value):

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

        frameWidth = 640  # Frame Width
        franeHeight = 480  # Frame Height

        plateCascade = cv2.CascadeClassifier("../extra/haarcascade_russian_plate_number.xml")
        minArea = 500

        cap = cv2.VideoCapture(0)
        cap.set(3, frameWidth)
        cap.set(4, franeHeight)
        cap.set(10, 150)
        count = 0
        img = None
        imgRoi = None


        def textEdit():
            text = pytesseract.image_to_string(imgRoi)
            print("Detected license plate Number is:", text)


        # value = True
        while value:
            success, img = cap.read()

            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

            for (x, y, w, h) in numberPlates:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow("Result", img)
                a, b = (int(0.02 * img.shape[0]), int(0.025 * img.shape[1]))
                plate = img[y + a:y + h - a, x + b:x + w - b, :]
                key=cv2.waitKey(1)

                if key == ord('s'):
                    kernel = np.ones((1, 1), np.uint8)
                    plate = cv2.dilate(plate, kernel, iterations=1)
                    plate = cv2.erode(plate, kernel, iterations=1)
                    plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
                    (thresh, plate) = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY_INV)
                    # Feed Image to OCR engine
                    read = pytesseract.image_to_string(plate)
                    read = ''.join(e for e in read if e.isalnum())
                    cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)
                    cv2.rectangle(img, (x, y - 40), (x + w, y), (51, 51, 255), -1)
                    cv2.putText(img, read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.imshow('PLate', plate)
                    # Save & display result image
                    cv2.imwrite('../img/plate.jpg', plate)
                    con()
                    record()
                    # record()
                # if key == ord('q'):
                #      cv2.destroyWindow('Result')
                #      cap.release()
            # key = cv2.waitKey(0)
            # if key == ord('q'):
            #     value=False
            #     cv2.destroyWindow('Result')
            #     cap.release()

        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()

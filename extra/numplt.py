import cascade as cascade
import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_num(img_name):
    img = cv2.imread(img_name) ## Reading Image
    # Converting into Gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Detecting plate
    nplate = cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in nplate:
        # Crop a portion of plate
        a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b, :]
        # make image more darker to identify the LPR
        ## iMAGE PROCESSING
        kernel = np.ones((1, 1), np.uint8)
        plate = cv2.dilate(plate, kernel, iterations=1)
        plate = cv2.erode(plate, kernel, iterations=1)
        plate_gray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
        (thresh, plate) = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)
        # Feed Image to OCR engine
        read = pytesseract.image_to_string(plate)
        read = ''.join(e for e in read if e.isalnum())
        print(read)
        # stat = read[0:2]
        # try:
        # # # Fetch the State information
        # #     print('Car Belongs to',states[stat])
        # except:
        #     print('State not recognised!!')
        print(read)
        cv2.rectangle(img, (x,y), (x+w, y+h), (51,51,255), 2)
        cv2.rectangle(img, (x, y - 40), (x + w, y),(51,51,255) , -1)
        cv2.putText(img,read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('PLate',plate)
        # Save & display result image
        cv2.imwrite('../img/plate.jpg', plate)

    cv2.imshow("Result", img)
    cv2.imwrite('result.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Let's make a function call
frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height
cap =cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,franeHeight)
cap.set(10,150)
extract_num(cap)
value=True
while value:
    success , img  = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        loc="D:\IMAGES"+str(count)+".jpg"
        imgaes=cv2.imwrite(loc,imgRoi)
        print(loc)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

        cv2.imshow("Result",img)
        text = pytesseract.image_to_string(r'D:\IMAGES{}.jpg'.format(count))
        print(r'D:\IMAGES{}.jpg'.format(count))
        print("Detected license plate Number is:", text)
        count += 1
    # key = cv2.waitKey(0)
    # if key == ord('q'):
    #     value=False
    #     cv2.destroyWindow('Result')
    #     cap.release()
cap.release()
cv2.destroyAllWindows()



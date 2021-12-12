from tkinter import messagebox

import cv2
import numpy as np
from tkinter import *
import face_recognition
import os
from datetime import datetime
from MainPage import MainPage
from ParkingDisplay import ParkingAvailable


class FaceReco:
    def __init__(self, value):
        self.value = value
        self.path = '../Photo'
        self.images = []
        self.className = []
        mylist = os.listdir(self.path)
        print(mylist)
        for cl in mylist:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.className.append(os.path.splitext(cl)[0])
        self.encodeListKnown = self.findEncodings(self.images)
        print('Encoding Complete')
        self.camera()

    def findEncodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendence(self, name):
        with open('../Record/Attendence.csv', 'r+') as f:
            mydataList = f.readlines()
            namelist = []
            print(mydataList)
            for line in mydataList:
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    def camera (self):
        values= self.value
        self.cap = cv2.VideoCapture(0)
        while values:
            sucess, img = self.cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            cv2.imshow('Webcam', img)
            key=cv2.waitKey(1)
            pro=cv2.getWindowProperty('Webcam',cv2.WND_PROP_VISIBLE)
            if(pro<1):
                messagebox.showinfo("showinfo", "press q to terminate")
            if key==ord('q'):

                cv2.destroyWindow('Webcam')
                self.cap.release()

            else:
                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

                for encodesFace, FaceLoc in zip(encodesCurFrame, facesCurFrame):
                    matches = face_recognition.compare_faces(self.encodeListKnown, encodesFace)
                    faceDis = face_recognition.face_distance(self.encodeListKnown, encodesFace)
                    print(faceDis)
                    matcheIndex = np.argmin(faceDis)

                    if matches[matcheIndex]:
                        name = self.className[matcheIndex].upper()
                        print(name)
                        y1, x2, y2, x1 = FaceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        self.markAttendence(name)
                        messagebox.showinfo("showinfo", "Welcome " + name)
                        MainPage(Tk())
                        ParkingAvailable(Tk())
                        values = False
                        cv2.destroyWindow('Webcam')
                        self.cap.release()



# -*- coding: cp1251 -*-
import cv2
import numpy as np
import dlib
import time
timing = time.time()
filenum = 0
xlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(3)
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=1)
        cv2.rectangle(img=frame, pt1=(x1, y1-35), pt2=(x2, y1-8), color=(0, 0, 0), thickness=-1)
        cv2.rectangle(img=frame, pt1=(x1, y2+8), pt2=(x2, y2+35), color=(0, 0, 0), thickness=-1)
        landmarks = predictor(image=gray, box=face)
        i = 0
        for n in range(36, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(img=frame, center=(x, y), radius=1, color=(0, 255, 0), thickness=1)
            xlist.insert(i, x)
            ylist.insert(i, y)
            i = i + 1
        min_x_l = 1000
        max_x_l = -100
        min_y_l = 1000
        max_y_l = -100
        min_x_r = 1000
        max_x_r = -100
        min_y_r = 1000
        max_y_r = -100
        for i in range(0, 5):
            a = xlist[i]
            b = ylist[i]
            if (a<min_x_l):
                min_x_l = a
            if (a>max_x_l):
                max_x_l = a
            if (b<min_y_l):
                min_y_l = b
            if (b>max_y_l):
                max_y_l = b
        pt1x = min_x_l
        pt1y = min_y_l
        pt2x = max_x_l
        pt2y = min_y_l
        pt3x = max_x_l
        pt3y = max_y_l
        pt4x = min_x_l
        pt4y = max_y_l

        for i in range(6, 11):
            a = xlist[i]
            b = ylist[i]
            if (a<min_x_r):
                min_x_r = a
            if (a>max_x_r):
                max_x_r = a
            if (b<min_y_r):
                min_y_r = b
            if (b>max_y_r):
                max_y_r = b
        pt5x = min_x_r
        pt5y = min_y_r
        pt6x = max_x_r
        pt6y = min_y_r
        pt7x = max_x_r
        pt7y = max_y_r
        pt8x = min_x_r
        pt8y = max_y_r
        crop_img1 = frame[min_y_l:max_y_l, min_x_l:max_x_l]
        crop_img2 = frame[min_y_r:max_y_r, min_x_r:max_x_r]
        if time.time() - timing > 0.0:
            timing = time.time()

        eye10 = cv2.split(crop_img1)[2]
        eye10list = [0]
        eye10clearlist  = [0]
        for i in range(1, 251):
            eye10list.append(0)
        for i in range(1, 251):
            eye10clearlist.append(0)
        for i in range(0, 251):
            for j in range(0, eye10.shape[0]):
                for k in range(0, eye10.shape[1]):
                    if (eye10[j, k] == i):
                        eye10list[i] = eye10list[i] + 1

        eye20 = cv2.split(crop_img2)[1]
        eye20list = [0]
        for i in range(1, 251):
            eye20list.append(0)
        for i in range(0, 251):
            for j in range(0, eye20.shape[0]):
                for k in range(0, eye20.shape[1]):
                    if (eye20[j, k] == i):
                        eye20list[i] = eye20list[i] + 1

        eye30 = cv2.split(crop_img2)[0]
        eye30list = [0]
        for i in range(1, 251):
            eye30list.append(0)
        for i in range(0, 251):
            for j in range(0, eye30.shape[0]):
                for k in range(0, eye30.shape[1]):
                    if (eye30[j, k] == i):
                        eye30list[i] = eye30list[i] + 1

        s10 = 0
        for i in range(1, 251):
            s10 = s10 + eye10list[i]

        s20 = 0
        for i in range(1, 251):
            s20 = s20 + eye20list[i]

        s30 = 0
        for i in range(1, 251):
            s30 = s30 + eye30list[i]

        s = s20 + s30
        s1 = s10 * 100
        per10 = s1 // s
        percent = str(per10)
        text1 = 'exhibition tired man'
        text2 = '% of tiredness'
        output = percent + text2

        font = cv2.FONT_HERSHEY_SIMPLEX
        position1 = (x1+5, y1-16)
        position2 = (x1+5, y2+27)
        fontScale = 0.5
        fontColor = (0, 255, 0)
        lineType = 1

        cv2.putText(frame, text1, position1, font, fontScale, fontColor, lineType)
        cv2.putText(frame, output, position2, font, fontScale, fontColor, lineType)

        cv2.namedWindow("Feel tired?", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Feel tired?", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(winname="Feel tired?", mat=frame)

        if cv2.waitKey(delay=1) == 32:
            filenumstr = str(filenum)
            filetext1 = 'guest number '
            filetext2 = '.jpg'
            filename = filetext1 + filenumstr + filetext2
            cv2.imwrite(filename, frame)
            photo = cv2.imread(filename)
            filenum = filenum + 1
            photowin = 'Your photo!'
            cv2.namedWindow(photowin, WINDOW_NORMAL)
            cv2.imshow(photowin, photo)
            if cv2.waitKey(delay=1) == 13:
                cv2.destroyWindow(photowin)

        if cv2.waitKey(delay=1) == 27:
            break
cap.release()
cv2.destroyAllWindows()

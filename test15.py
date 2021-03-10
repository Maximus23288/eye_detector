import cv2
import dlib
xlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

frame = cv2.imread("face0.png")
gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
faces = detector(gray)
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    landmarks = predictor(image=gray, box=face)
    i = 0
    for n in range(36, 48):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
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

eye10 = cv2.split(crop_img1)[2]
eye10list = [0]
for i in range(1, 251):
    eye10list.append(0)
for i in range(0, 251):
    for j in range(0, eye10.shape[0]):
        for k in range(0, eye10.shape[1]):
            if (eye10[j, k] == i):
                eye10list[i] = eye10list[i] + 1
print (eye10list)

eye20 = cv2.split(crop_img2)[2]
eye20list = [0]
for i in range(1, 251):
    eye20list.append(0)
for i in range(0, 251):
    for j in range(0, eye20.shape[0]):
        for k in range(0, eye20.shape[1]):
            if (eye20[j, k] == i):
                eye20list[i] = eye20list[i] + 1
print (eye20list)

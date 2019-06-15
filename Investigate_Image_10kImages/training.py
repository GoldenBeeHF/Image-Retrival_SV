import numpy as np
import cv2
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import math
import os

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
        help="path to facial landmark predictor")
ap.add_argument("-f", "--folder", required=True,
        help="path training folder")
ap.add_argument("-dst-train", "--file-training", required=True,
        help="path file training")
args = vars(ap.parse_args())

def computeEuclide(x1, x2, y1, y2):
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

path = args["folder"]
allfiles = os.listdir(path)
print allfiles
f1 = open('C:\\Users\\Dell7559\\Desktop\\training.txt', 'a+')

data = []
for file in allfiles:
    if os.path.isdir(path + file):
        data.append(path + file)

for s in data:
    faces = os.listdir(s + "\\")
    for face in faces:
        print (str(s + '\\' + face))
        img = cv2.imread(s + '\\' + face)
        height, width = img.shape[:2]
        thumbnail = img

        gray = cv2.cvtColor(thumbnail, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        
        for rect in rects:
                print rect.left()
                print rect.top()
                print rect.right()
                print rect.bottom()
                print rect.right() - rect.left()
                print rect.bottom()- rect.top()
                cv2.rectangle(thumbnail, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 0), 1)
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
                lstX = []
                lstY = []
                for (x, y) in shape:
                        cv2.circle(thumbnail, (x, y), 1, (0, 0, 255), -1)
                        lstX.append(x)
                        lstY.append(y)

                vector = []
                vector.append(computeEuclide(lstX[0], lstX[16], lstY[0], lstY[16]))
                vector.append(computeEuclide(lstX[36], lstX[39], lstY[36], lstY[39]))
                vector.append(computeEuclide(lstX[42], lstX[45], lstY[42], lstY[45]))
                vector.append(computeEuclide(lstX[39], lstX[42], lstY[39], lstY[42]))
                vector.append(computeEuclide(lstX[31], lstX[35], lstY[31], lstY[35]))
                vector.append(computeEuclide(lstX[48], lstX[54], lstY[48], lstY[54]))
                vector.append(computeEuclide(lstX[19], lstX[39], lstY[19], lstY[39]))
                vector.append(computeEuclide(lstX[24], lstX[42], lstY[24], lstY[42]))
                vector.append(computeEuclide(lstX[19], lstX[36], lstY[19], lstY[36]))
                vector.append(computeEuclide(lstX[24], lstX[45], lstY[24], lstY[45]))
                vector.append(computeEuclide(lstX[19], lstX[24], lstY[19], lstY[24]))
                vector.append(computeEuclide(lstX[31], lstX[39], lstY[31], lstY[39]))
                vector.append(computeEuclide(lstX[35], lstX[42], lstY[35], lstY[42]))
                vector.append(computeEuclide(lstX[33], lstX[39], lstY[33], lstY[39]))
                vector.append(computeEuclide(lstX[33], lstX[42], lstY[33], lstY[42]))
                vector.append(computeEuclide(lstX[31], lstX[33], lstY[31], lstY[33]))
                vector.append(computeEuclide(lstX[33], lstX[35], lstY[33], lstY[35]))
                vector.append(computeEuclide(lstX[31], lstX[51], lstY[31], lstY[51]))
                vector.append(computeEuclide(lstX[35], lstX[51], lstY[35], lstY[51]))
                vector.append(computeEuclide(lstX[31], lstX[48], lstY[31], lstY[48]))
                vector.append(computeEuclide(lstX[35], lstX[54], lstY[35], lstY[54]))
                vector.append(computeEuclide(lstX[8], lstX[48], lstY[8], lstY[48]))
                vector.append(computeEuclide(lstX[8], lstX[54], lstY[8], lstY[54]))
                vector.append(computeEuclide(lstX[21], lstX[39], lstY[21], lstY[39]))
                vector.append(computeEuclide(lstX[22], lstX[42], lstY[22], lstY[42]))
                vector.append(computeEuclide(lstX[21], lstX[36], lstY[21], lstY[36]))
                vector.append(computeEuclide(lstX[22], lstX[45], lstY[22], lstY[45]))
                vector.append(computeEuclide(lstX[27], lstX[39], lstY[27], lstY[39]))
                vector.append(computeEuclide(lstX[21], lstX[27], lstY[21], lstY[27]))
                vector.append(computeEuclide(lstX[27], lstX[42], lstY[27], lstY[42]))
                vector.append(computeEuclide(lstX[22], lstX[27], lstY[22], lstY[27]))
                vector.append(computeEuclide(lstX[17], lstX[36], lstY[17], lstY[36]))
                vector.append(computeEuclide(lstX[24], lstX[45], lstY[24], lstY[45]))
                vector.append(computeEuclide(lstX[33], lstX[50], lstY[33], lstY[50]))
                vector.append(computeEuclide(lstX[33], lstX[52], lstY[33], lstY[52]))
                vector.append(computeEuclide(lstX[7], lstX[57], lstY[7], lstY[57]))
                vector.append(computeEuclide(lstX[8], lstX[57], lstY[8], lstY[57]))
                vector.append(computeEuclide(lstX[9], lstX[57], lstY[9], lstY[57]))
                vector.append(computeEuclide(lstX[3], lstX[48], lstY[3], lstY[48]))
                vector.append(computeEuclide(lstX[13], lstX[54], lstY[13], lstY[54]))
                vector.append(computeEuclide(lstX[3], lstX[7], lstY[3], lstY[7]))
                vector.append(computeEuclide(lstX[9], lstX[13], lstY[9], lstY[13]))
                for i in range(0, len(vector)):
                        f1.write(str(vector[i]) + ' ') 

        cv2.imshow(face, thumbnail)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

f1.close()
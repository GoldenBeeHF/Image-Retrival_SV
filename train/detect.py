import cv2
import sys
import dlib
import copy
import argparse
from imutils import face_utils
import numpy
import math
import os
def computeEuclide(x1, x2, y1, y2):
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
    help="path to facial landmark predictor")
# ap.add_argument("-f", "--folder-train", required=True,
#     help="path folder training")

args = vars(ap.parse_args())

video_capture = cv2.VideoCapture(0)

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# path = args["folder_train"]
# allfiles = os.listdir(path)

# print allfiles

f1 = open('C:\\Users\\Dell7559\\Desktop\\training.txt', 'a+')
dem = 0
# data = []
# for file in allfiles:
#     data.append(path + "\\" + file)

# arrLocation = []
# for s in range(len(data)):
#     arrLocation.append(os.path.basename(os.path.splitext(data[s])[0]))

# arrLocation = map(int, arrLocation)
# arrLocation.sort()
f = open('filename.txt', 'r')
filenames = f.read().split(' ')

for filename in filenames:
# for i in range(len(arrLocation)):
    img = cv2.imread('data_SV/Hinh SV_CNTT/' + filename + ".jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    if len(rects) != 1:
        print filename
        continue
    # if len(rects) > 1:
    #     continue
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # for (x, y) in shape:
        #     cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
        l = int(rect.left() - 20)
        t = int(rect.top() - 20)
        h = int(rect.bottom() - rect.top() + 40)
        w = int(rect.right() - rect.left() + 40)
        crop_img = img[t:t+h,l:l+w]
        height, width = crop_img.shape[:2]
        try:
            scaleW = 150. / width
        except:
            print filename
            continue
        scaleH = height * scaleW

        try:
            crop_img = cv2.resize(crop_img, (150, int(scaleH)), interpolation = cv2.INTER_AREA)
        except:
            print filename
            continue      
        
        gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        rects_crop = detector(gray_crop, 0)
        if len(rects_crop) != 1:
            print filename
            continue
        for rect_crop in rects_crop:
            dem += 1
            shape_crop = predictor(gray_crop, rect_crop)
            shape_crop = face_utils.shape_to_np(shape_crop)
            # cv2.rectangle(, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 0), 2)
            lstX = []
            lstY = []
            for (x, y) in shape_crop:
                # cv2.circle(crop_img, (x, y), 1, (0, 0, 255), -1)
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
            for j in range(0, len(vector)):
                f1.write(str(vector[j]) + ' ')

        cv2.imwrite("C:\\Users\\Dell7559\\Desktop\\dataDetect_SV\\" + filename + ".jpg", img) 
        # cv2.imshow("img", crop_img)
print dem
cv2.waitKey(0)



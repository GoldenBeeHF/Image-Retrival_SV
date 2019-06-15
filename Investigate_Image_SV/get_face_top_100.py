# USAGE
# python video_facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat
# python video_facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --picamera 1

# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
import os
import math
import time
def computeEuclide(x1, x2, y1, y2):
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

class HOG:
    def __init__(self, vector, idImage):
        self.__vector = vector # private attribute
        self.__id = idImage # private attribute
    def getId(self):
        return self.__id
    def getVector(self):
        return self.__vector
class Vector:
    def __init__(self, vector, link):
        self.__vector = vector # private attribute
        self.__link = link # private attribute
    def getVector(self):
        return self.__vector
    def getLink(self):
        return self.__link
    def setVector(self, vector):
        self.__vector = vector
def computeDistanceEuclide(vectorA, vectorB, count):
    dis = 0
    for i in range(0, len(vectorA)):
		count += 1
		dis = dis + math.pow(float(vectorA[i]) - float(vectorB[i]), 2)
    return [math.sqrt(dis), count]

def findMinDistance(vector, lstVector, count):
    vt = 0
    min, count = computeDistanceEuclide(vector, lstVector[0].getVector(), count)
    for i in range(1, len(lstVector)):
        if min > computeDistanceEuclide(vector, lstVector[i].getVector(), count)[0]:
            min, count = computeDistanceEuclide(vector, lstVector[i].getVector(), count)
            vt = i
    return [vt, count]

def computeDistanceByCount(vectorA, vectorB, count):
	dem = 0
	for i in range(0, len(vectorA)):
		if abs(float(vectorA[i]) - float(vectorB[i])) < 3:
			count += 1
			dem += 1
	return [dem, count]

def findMatchDistance(vector, lstVector, count):
	vt = 0
	top = computeDistanceByCount(vector, lstVector[0].getVector(), count)
	for i in range(1, len(lstVector)):
		if top < computeDistanceByCount(vector, lstVector[i].getVector(), count):
			top = computeDistanceByCount(vector, lstVector[i].getVector(), count)
			vt = i
	return [vt, count]

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--path-image", required=True,
# 	help="path of image research")
args = vars(ap.parse_args())
def findTop100(image):
	count = 0
	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	print("[INFO] loading facial landmark predictor...")
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

	f = open('training.txt', 'a+')
	data = f.read()
	arr = data.split()
	print len(arr)
	img = cv2.imread(image)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale frame
	rects = detector(gray, 0)
	if rects != []:
			# loop over the face detections
		for rect in rects:
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			# loop over the (x, y)-coordinates for the facial landmarks
			# and draw them on the image
			l = int(rect.left() - 20)
			t = int(rect.top() - 20)
			h = int(rect.bottom() - rect.top() + 40)
			w = int(rect.right() - rect.left() + 40)
			crop_img = img[t:t+h,l:l+w]
			height, width = crop_img.shape[:2]

			scaleW = 150. / width
			print scaleW
			scaleH = height * scaleW

			try:
				crop_img = cv2.resize(crop_img, (150, int(scaleH)), interpolation = cv2.INTER_AREA)
			except:
				continue      
			gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
			rects_crop = detector(gray_crop, 0)
			for rect_crop in rects_crop:
				shape_crop = predictor(gray_crop, rect_crop)
				shape_crop = face_utils.shape_to_np(shape_crop)
				# cv2.rectangle(img, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 0), 2)
				lstX = []
				lstY = []
				for (x, y) in shape_crop:
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
				
				lstImg = []
				arrCount = []
				arrVector = []
				loop = int(len(arr) / 42)
				for i in range(loop):
					lstImg.append(i)
					count += 1
				for j in range(loop):
					# dem = 0
					v = []
					for i in range(42):
						count += 1
						v.append(arr[i + j * 42])
						# if abs(float(arr[i + j * 42]) - vector[i]) < 4:
						# 	dem = dem + 1
					arrVector.append(v)
					# arrCount.append(dem)
				arrDis = []
				dem = 0
				for vec in arrVector:
					dis, count = computeDistanceEuclide(vec, vector, count)
					arrDis.append(dis)
				
				for i in range(0, len(arrDis) - 1):
					for j in range(i + 1, len(arrDis)):
						count += 1
						if arrDis[i] < arrDis[j]:
							t = arrDis[i]
							arrDis[i] = arrDis[j]
							arrDis[j] = t
							tImg = lstImg[i]
							lstImg[i] = lstImg[j]
							lstImg[j] = tImg

				# for i in range(0, len(arrCount) - 1):
				# 	for j in range(i + 1, len(arrCount)):
				# 		if arrCount[i] <  arrCount[j]:
				# 			t = arrCount[i]
				# 			arrCount[i] = arrCount[j]
				# 			arrCount[j] = t
				# 			tImg = lstImg[i]
				# 			lstImg[i] = lstImg[j]
				# 			lstImg[j] = tImg
				print lstImg
				return [lstImg, count]

def findImageInTree(image):
	count = 0
	lstImage = []
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
	img = cv2.imread(image)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 0)
	if rects != []:
		# loop over the face detections
		for rect in rects:
			# determine the facial landmarks for the face region, then
			# convert the facial landmark (x, y)-coordinates to a NumPy
			# array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			l = rect.left()
			t = rect.top()
			w = rect.right() - l
			h = rect.bottom() - t
			lstX = []
			lstY = []
			for (x, y) in shape:
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

			dis = vector[0]
			for j in range(len(vector)):
				vector[j] = vector[j] / dis

			lstVector = []
			lstRoute = []
			with open("tree/root.txt") as f:
				for line in f:
					temp = line.split()
					v = []
					for i in range(1, len(temp)):
						count += 1
						v.append(temp[i])
					vec = Vector(v, temp[0])
					lstVector.append(vec)
			arrDis = []
			for i in range(0, len(lstVector)):
				arrDis.append(computeDistanceEuclide(vector, lstVector[i].getVector(), count))
			for i in range(0, len(lstVector) - 1):
				for j in range(i + 1, len(lstVector)):
					count += 1
					if arrDis[i][0] > arrDis[j][0]:
						tDis = arrDis[i]
						arrDis[i] = arrDis[j]
						arrDis[j] = tDis
						tVec = lstVector[i]
						lstVector[i] = lstVector[j]
						lstVector[j] = tVec
			lstRoute.append(lstVector)
			countImage = 0
			lstImg = []
			while True:
				currentLocation = 0
				tempFile = open("tree/" + str(lstRoute[len(lstRoute) - 1][currentLocation].getLink()) + ".txt")
				model = tempFile.readline()
				lstV = []
				if model.__contains__('Node'):
					isFirstLine = True
					with open('tree/' + str(lstRoute[len(lstRoute) - 1][currentLocation].getLink()) + '.txt') as f:
						for line in f:
							if isFirstLine == True:
								isFirstLine = False
								continue
							temp = line.split()

							tempVector = []
							for value in range(1, len(temp)):
								count += 1
								tempVector.append(temp[value])
							q = Vector(tempVector, temp[0])
							lstV.append(q)
					arrDis = []
					for i in range(0, len(lstV)):
						arrDis.append(computeDistanceEuclide(vector, lstV[i].getVector(), count))
					for i in range(0, len(lstV) - 1):
						for j in range(i + 1, len(lstV)):
							count += 1
							if arrDis[i][0] > arrDis[j][0]:
								tDis = arrDis[i]
								arrDis[i] = arrDis[j]
								arrDis[j] = tDis
								tVec = lstV[i]
								lstV[i] = lstV[j]
								lstV[j] = tVec
					lstRoute.append(lstV)
				# print 'aaaa'
				# for a in lstRoute:
				# 	print len(a)
				if model.__contains__('Leaf'):
					isFirstLine = True
					lstV = []
					with open("tree/" + str(lstRoute[len(lstRoute) - 1][currentLocation].getLink()) + ".txt") as f:
						for line in f:
							if isFirstLine == True:
								isFirstLine = False
								continue
							temp = line.split()
							
							tempVector = []
							for value in range(1, len(temp)):
								count += 1
								tempVector.append(temp[value])
							q = HOG(tempVector, temp[0])
							lstImg.append(q)
					count += 1
					if len(lstImg) < 1000:
						lstRoute[len(lstRoute) - 1].remove(lstRoute[len(lstRoute) - 1][0])
					count += 1
					if len(lstRoute[len(lstRoute) - 1]) == 0:
						lstRoute.remove(lstRoute[len(lstRoute) - 1])
						lstRoute[len(lstRoute) - 1].remove(lstRoute[len(lstRoute) - 1][0])
						
				if len(lstImg) > 1000:
					break
			lstDistance = []
			for i in range(0, len(lstImg)):
				dis, count = computeDistanceEuclide(lstImg[i].getVector(), vector, count)
				lstDistance.append(dis)
			for i in range(0, len(lstDistance) - 1):
				for j in range(i + 1, len(lstDistance)):
					count += 1
					if lstDistance[i] > lstDistance[j]:
						tDis = lstDistance[i]
						lstDistance[i] = lstDistance[j]
						lstDistance[j] = tDis
						tV = lstImg[i]
						lstImg[i] = lstImg[j]
						lstImg[j] = tV
			# print lstDistance
			dem = 0
			for hog in lstImg:
				count += 1
				lstImage.append(hog.getId())
				dem += 1
				if dem == 100:
					break
	return [lstImage, count]
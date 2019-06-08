import cv2
import sys
import dlib
import copy
import argparse
from imutils import face_utils
import numpy
import math

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
        help="path to facial landmark predictor")
ap.add_argument("-dst", "--dst-folder", required=True,
        help="path destination folder")

args = vars(ap.parse_args())

video_capture = cv2.VideoCapture(0)

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
dem = 0
dstFolder = args["dst_folder"]
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    img = copy.copy(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    crop_img = None
    rects = detector(gray, 0) 

    for rect in rects:
        cv2.rectangle(frame, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 0), 2)
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

        x = int(rect.left() - 20)
        y = int(rect.top() - 20)
        h = int(rect.bottom() - rect.top() + 40)
        w = int(rect.right() - rect.left() + 40)

        crop_img = img[y:y+h,x:x+w]

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        crop_img = cv2.resize(crop_img, (250, 250), interpolation = cv2.INTER_AREA)
        dem = dem + 1
        cv2.imwrite(dstFolder + '\\' + str(dem) + ".jpg", crop_img)
        print str(dem)

    if dem == 20:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
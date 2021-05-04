from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from array import *
from . import Classifier as classify

def Eucledian(x,y):
	x1 = x[0]
	y1 = x[1]
	x2 = y[0]
	y2 = y[1]
	return (((x2-x1)**2) + ((y2-y1)**2))**0.5

def manhattan_distance(a, b):
    return sum(abs(e1-e2) for e1, e2 in zip(a,b))


def RunModel(img):
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor('./home/shape_predictor_68_face_landmarks.dat')

	image = cv2.imread(img)
	#image = imutils.resize(image, width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):

		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		(x, y, w, h) = face_utils.rect_to_bb(rect)
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

		cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

		for (x, y) in shape:
			cv2.circle(image, (x, y), 1, (255, 0,0), -1)

	#cv2.imshow("Output", image)
	#cv2.waitKey(0)
	q1 = shape[52].tolist()
	q2 = shape[58].tolist()
	q3 = shape[49].tolist()
	q4 = shape[55].tolist() 
	q5 = shape[9].tolist()

	queryEu = list()
	queryEu.append(Eucledian(q1,q3))
	queryEu.append(Eucledian(q1,q4))
	queryEu.append(Eucledian(q2,q3))
	queryEu.append(Eucledian(q2,q4))
	queryEu.append(Eucledian(q2,q5))
	#print("Output with Eucledian")
	OUTPUT = classify.Knn(queryEu, 5)
	
	'''
	queryMn = list()
	queryMn.append(manhattan_distance(q1,q3))
	queryMn.append(manhattan_distance(q1,q4))
	queryMn.append(manhattan_distance(q2,q3))
	queryMn.append(manhattan_distance(q2,q4))
	queryMn.append(manhattan_distance(q2,q5))
	'''
	

	'''
	print("Output with Manhattan")
	classify.Knn(queryMn, 5)
	'''
	return OUTPUT
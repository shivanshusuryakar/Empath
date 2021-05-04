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
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):

		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)


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

	OUTPUT = classify.Knn(queryEu, 5)
	
	return OUTPUT
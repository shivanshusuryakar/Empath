#---------------------------------------------------------------------------------------------------
#   Script by:-  VEDANT VINAYAK KULKARNI
#---------------------------------------------------------------------------------------------------

import math
import pandas as pd
from collections import Counter

def Knn(query, k):
    T_L = list()
    T_R = list()
    B_L = list()
    B_R = list()
    B_C = list()

    T_L_q = list()
    T_R_q = list()
    B_L_q = list()
    B_R_q = list()
    B_C_q = list()

    column_names = ['emotion', 'T_L', 'T_R', 'B_L', 'B_R', 'B_C']
    df = pd.read_csv("./home/CleanEucledianNew.csv", names=column_names)
    Emt = df.emotion.to_list()
    T_L = df.T_L.to_list()
    T_R = df.T_R.to_list()
    B_L = df.B_L.to_list()
    B_R = df.B_R.to_list()
    B_C = df.B_C.to_list()


    neighbours = list()
    #Calculation of distance between each value eg: T_L and query T_L
    T_L_q = Iterator_T_L(T_L, query)
    T_R_q = Iterator_T_R(T_R, query)
    B_L_q = Iterator_B_L(B_L, query)
    B_R_q = Iterator_B_R(B_R, query)
    B_C_q = Iterator_B_C(B_C, query)
    

    k_near_T_L = T_L_q[:k]
    k_near_T_R = T_R_q[:k]
    k_near_B_L = B_L_q[:k]
    k_near_B_R = B_R_q[:k]
    k_near_B_C = B_C_q[:k]

    FinalEmt = []
    output = []

    FinalEmt.append(K_near_label_Collector(k_near_T_L, Emt))
    FinalEmt.append(K_near_label_Collector(k_near_T_R, Emt))
    FinalEmt.append(K_near_label_Collector(k_near_B_L, Emt))
    FinalEmt.append(K_near_label_Collector(k_near_B_R, Emt))
    FinalEmt.append(K_near_label_Collector(k_near_B_C, Emt))


    FinalOutput = Mode(FinalEmt[0], output)
    FinalOutput = Mode(FinalEmt[1], output)
    FinalOutput = Mode(FinalEmt[2], output)
    FinalOutput = Mode(FinalEmt[3], output)
    FinalOutput = Mode(FinalEmt[4], output)

    UltimateEmt = Counter(FinalOutput).most_common(1)[0][0]

    Print = ("The Person Looks: {}".format(UltimateEmt))

    return Print




def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def Mode(l,op):
    e = Counter(l).most_common(1)[0][0]
    op.append(e)
    return op

def Iterator_T_L(l, query):
    op = []
    for index,data in enumerate(l):
        if index == 0:
            pass
        else:
            p1 = list()
            p2 = list()
            p1.append(float(query[0]))
            p2.append(float(data))
            x = euclidean_distance(p1,p2)
            op.append((x, index))
    op = sorted(op)    
    return(op)
def Iterator_T_R(l, query):
    op = []
    for index,data in enumerate(l):
        if index == 0:
            pass
        else:
            p1 = list()
            p2 = list()
            p1.append(float(query[1]))
            p2.append(float(data))
            x = euclidean_distance(p1,p2)
            op.append((x, index))
    op = sorted(op)    
    return(op)
def Iterator_B_L(l, query):
    op = []
    for index,data in enumerate(l):
        if index == 0:
            pass
        else:
            p1 = list()
            p2 = list()
            p1.append(float(query[2]))
            p2.append(float(data))
            x = euclidean_distance(p1,p2)
            op.append((x, index))
    op = sorted(op)    
    return(op)

def Iterator_B_R(l, query):
    op = []
    for index,data in enumerate(l):
        if index == 0:
            pass
        else:
            p1 = list()
            p2 = list()
            p1.append(float(query[3]))
            p2.append(float(data))
            x = euclidean_distance(p1,p2)
            op.append((x, index))
    op = sorted(op)    
    return(op)

def Iterator_B_C(l, query):
    op = []
    for index,data in enumerate(l):
        if index == 0:
            pass
        else:
            p1 = list()
            p2 = list()
            p1.append(float(query[4]))
            p2.append(float(data))
            x = euclidean_distance(p1,p2)
            op.append((x, index))
    op = sorted(op)    
    return(op)

def K_near_label_Collector(near_l, emotion_l):
    op = []
    for i in near_l:
        ind = i[1]
        op.append(emotion_l[ind])
    return op

def closest(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(float(lst[i])-K))]
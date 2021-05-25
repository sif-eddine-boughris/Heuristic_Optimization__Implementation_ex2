import pandas
import numpy as np
from copy import deepcopy
import random
def getDataframe(CSV, machine): # give it The csv file return the data frame
    m = []
    for i in range(machine):
        m.append(str('M' + str(i + 1)))
    W = 'w'
    m.append(W)
    DF = pandas.read_csv(str(CSV), usecols=m, sep=',').values
    return DF


#s = getDataframe('instances/instance2/50_20_01.csv', 20)


def get_matrix_with_wieght(Df): #give it the data frame return th matrix with weight
    shape0, shape1 = Df.shape[0], Df.shape[1]
    M = np.zeros((shape0, shape1), dtype=int)
    w = []
    for i in range(Df.shape[0]):
        for j in range(shape1):
            if j ==shape1-1:
                w.append(Df[i, j])
            else:
                M[i, j] = Df[i, j]


    return M, w

#DF, w = get_matrix_with_wieght(s)


#DF, w = Get_Matrix_with_weight('instances/instance2/50_20_01.csv', 20)


def get_completion_matrix(A): # calculate the completion matrix
    shape = A.shape
    D = np.zeros(shape, dtype=int)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i == 0:
                D[i, j] = A[i, j] + D[i, j - 1]
            if j == 0:
                D[i, j] = A[i, j] + D[i - 1, j]
            if i > 0 and j > 0:
                if D[i, j - 1] > D[i - 1, j]:
                    D[i, j] = A[i, j] + D[i, j - 1]
                else:
                    D[i, j] = A[i, j] + D[i - 1, j]
    return D


#b3 = get_completion_matrix(DF)


#print(b3)

def complection_time(A): #get complection time
    D = []
    S = A.shape[1]
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if j == S-1:
                D.append(A[i, j])
    return D


#A2 = complection_time(b3)


def Matrix_info(M, w):#calculate makespan SCT,WCT
    Max = max(M)
    #print('Makespan=', Max)
    Sum1 = sum(M)
    #print('Sum of completion times', Sum1)
    W = [a * b for a, b in zip(M, w)]
    #print('wi·Ci = ', W)
    Sum2 = sum(W)
    #print('Weighted sum of completion times ', Sum2)
    return W, Max, Sum1, Sum2

def WTC(m):#i use this to calculate Sum of completion times, Weighted sum of completion times
   i1,w= get_matrix_with_wieght(m)
   i2= get_completion_matrix(i1)
   i3= complection_time(i2)
   W, Max, Sum1, Sum2 = Matrix_info(i3,w)
   return Sum1,Sum2

#print(Matrix_info(A2, w))

def new_matrix_step(m, init):#here i give it the data frame and the job permutation and give m the new matrix
    m2 = np.zeros(m.shape, dtype=int)
    for i in range(len(m)):
        m2[i] = m[init[i]]
    
    return m2

def Random_permutation(data_frame):#random permutation of the jobs
    RP = np.random.permutation(data_frame).tolist()
    return RP
def transpose_neighbourhood(lis):#give you all the posibal neighbourhood
    list = []
    list1 = []
    lis1 = lis
    list1.append(lis)
    for i in range(len(lis)):
        if i == 0:
            z1 = lis1[i]
            z2 = lis1[i + 1]
            list.append(z2)
            list.append(z1)
            for i in range(2, len(lis)):
                z3 = lis[i]
                list.append(z3)
            list1.append(list)
            list = []


        else:
            if i == len(lis) - 1:
                z4 = lis1[i]
                z5 = lis1[i - 1]
                for i in range(len(lis) - 2):
                    z6 = lis1[i]
                    list.append(z6)
                list.append(z4)
                list.append(z5)
                list1.append(list)
                list = []

            else:
                z7 = lis[i]
                s7 = lis.index(z7)
                # print('s7',s7)
                z8 = lis1[i + 1]
                s8 = lis1.index(z8)
                # print('s8',s8)
                z9 = lis1[i - 1]
                s9 = lis1.index(z9)
                # print('s9',s9)
                left = []
                right = []
                if s7 - 1 == s9:
                    for i in range(s7 - 1):
                        z10 = lis1[i]
                        left.append(z10)
                    left.append(z7)
                    left.append(z9)
                    for i in range(s7 + 1, len(lis)):
                        z11 = lis[i]
                        left.append(z11)
                    list1.append(left)

    new_k = []
    for elem in list1:
        if elem not in new_k:
            new_k.append(elem)
    list1 = new_k
    return list1

def exchange_neighbourhood(lis):#give you all the posibal neighbourhood
    lis1 = [lis]

    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            list2 = deepcopy(lis)
            list2[i], list2[j] = list2[j], list2[i]
            lis1.append(list2)


    return lis1


def insert_neighbourhood(lis):#give you all the posibal neighbourhood
    lis3 = []

    for i in range(len(lis)):
        for j in range(len(lis)):
            lis2 = deepcopy(lis)
            s = lis2[i]
            lis2.remove(lis2[i])
            lis2.insert(j, s)
            lis3.append(lis2)
            lis2 = []


    new_k = []
    for elem in lis3:
        if elem not in new_k:
            new_k.append(elem)
        lis3 = new_k
    return lis3[1:len(lis3)]

def perturbation(list):
    R1=random.randint(0,len(list)-1)
    R2 = random.randint(0, len(list)-1)
    R3 = random.randint(0, len(list)-1)
    R4 = random.randint(0, len(list)-1)
    E1=list[R1]
    E2= list[R2]
    list.remove(E1)
    list.insert(R3,E1)
    list.remove(E2)
    list.insert(R4,E2)
    return list



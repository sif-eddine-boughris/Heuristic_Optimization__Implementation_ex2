from Methods import *




def get_T(m, w):  # calculat Ti
    T = []
    for i in range(m.shape[0]):
        w1 = 1 / w[i]

        P = 0
        J=0
        for j in range(m.shape[1]-1):
            P = P + m[i, j]
            if j ==m.shape[1]-2:
              T.append(round(P*w1, 2))
    return T




def get_index_of_sort_element(t):  # get the list starting sequence
    init = np.argsort(t)
    return init






def new_matrix_step(m, init):#get the new matrix from the Ti sequence
    shape2 = m.shape[1]
    shape1 = len(init)
    m2 = np.zeros((shape1, shape2), dtype=int)

    for i in range(shape1):
        m2[i] = m[init[i]]
    return m2

def get_the_firs_step(z): #get the list of the first 2 element [[x,y],[y,x]]
    for i in range(len(z)):
        if i == 1:
            z0=[]
            z1 = [z[i - 1], z[i]]
            z2 = [z[i], z[i - 1]]
            z0.append(z1)
            z0.append(z2)
    return z0


def get_the_min_wct(s,list): #calculate the wtc of the sequance
    index=0
    wtc= []
    for i in range(len(list)):
        m = new_matrix_step(s, list[i])
        a,b=WTC(m)
        wtc.append(b)
        index= wtc.index(min(wtc))


    return list[index]

def get_posibale_matrix(M,E,P):
    e=[E]
    b = M[:P] + e+ M[P:]
    return b

def get_allPosibale_matrix(M,E):#get the posibale matrix after adding new element in j position
    first =M
    PM = []
    for i in range(len(M)+1):
        M=first
        P= get_posibale_matrix(M,E,i)
        PM.append(P)
        shape=P
    #print (first)
    return PM




def Simplified_RZ_heuristic(file):# give it the file name return the solution sequance
    s = getDataframe('instances/instance2/' + file + '.csv',20 )
    s2, w = get_matrix_with_wieght(s)
    T = get_T(s2, w)
    init = get_index_of_sort_element(T)
    s1 = get_the_firs_step(init)
    s3 = get_the_min_wct(s, s1)
    for i in range(2, len(init)):
        s4 = get_allPosibale_matrix(s3, init[i])
        s5 = get_the_min_wct(s, s4)
        s3 = s5
    return s3

#print(Simplified_RZ_heuristic("test",3))
'''''
import sys
process_arg1=sys.argv[1]
process_arg2=sys.argv[2]
process_arg3=sys.argv[3]
if process_arg1=='SRZH':
    print('Starting the ' + process_arg1 + '...')
    #print(Simplified_RZ_heuristic(process_arg2,int(process_arg3)))
    print(process_arg1 + ' is donne!')
'''


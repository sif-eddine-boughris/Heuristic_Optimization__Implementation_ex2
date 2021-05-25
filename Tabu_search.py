import pandas as pd
import csv
import os
from Methods import *
from Local_search import *
import time
#TC = termination criterion
def Tabu_search(csv,TC):
    Tabu_list=[]
    Tabu_result=[]
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    job = s.shape[0]
    jobs = list(range(0, job))
    jp = Random_permutation(jobs)
    timer = 0
    while timer <= TC :
        tic = time.perf_counter()
        msct1, min1, list1 = best_improvement_Insert(csv, jp)
        toc = time.perf_counter()
        timer = timer+(toc-tic)
        print(timer)
        if Tabu_list.count(list1) > 0:
            jp = list1
            print('exist')
        else:
          Tabu_list.append(list1)
          jp=list1
          Tabu_result.append(min1)

    Min = min(Tabu_result)
    return Min

Algoritm = ['Tabu_search_50','Tabu_search_100']
def RPD(bs,mbs):

    c=100*((float(mbs)-float(bs))/float(bs))
    return c

def creat_experement_csv_file(Algo):
    for i in range(len(Algo)):
        header = ['file', 'bs', 'mbs', 'RPD','RPDS']
        with open('Tabu_exp/' + Algo[i] + '.csv', 'w') as f:
            dw = csv.DictWriter(f, delimiter=',', fieldnames=header)
            dw.writeheader()
        f.close()
#creat_experement_csv_file(Algoritm)

def get_file_names(path):
    l = os.listdir(path)
    li = [x.split('.')[0] for x in l]
    li = li[:-1]
    return li



def add_in_all_file(file, w, column):
    for i in range(len(file)):
        df = pd.read_csv('Tabu_exp/' + file[i] + '.csv')
        df[str(column)] = w
        df.to_csv('Tabu_exp/' + file[i] + '.csv')
        #df.close()

def add_in_one_file(file,w, column):
        df = pd.read_csv('Tabu_exp/' + file + '.csv')
        df[str(column)] = w
        df.to_csv('Tabu_exp/' + file + '.csv',index=False)
        #df.close()

def get_best_solution():
    with open('instances/instances/bestSolutions.txt') as f:
        A = []
        for i in range(61):
            line = f.readline()
            line = line.strip()
            L = line.split(',')
            l=L[1]
            A.append(l)
        A.remove(A[0])
        return A
    f.close


#_______________________________experement 50___________________
def get_experement_Tabu_search_result_50(file_name,bestsolut):
    mbs=[]
    RDp=[]
    RDps=[]
    bs=[]
    file=[]
    step = 5

    for i in range(len(file_name)):
        mbs2 = 0
        bss2 = 0
        RDPs = 0

        if file_name[i][:1] == '5':
            for j in range(step):
                print("working on the file  " + str(file_name[i]) + " step number " + str(j + 1))
                mbs1 = Tabu_search(file_name[i], 150)

                bss = bestsolut[i]
                RDPs = RDPs + (RPD(bss, mbs1))
                if j == 0:
                    mbs2, bss2 = mbs1, bss

                else:
                    if mbs1 < mbs2:
                        mbs2, bss2 = mbs1, bss

                print(i)
                print(mbs2)
            RDp.append(RPD(bss2, mbs2))
            mbs.append(mbs2)
            bs.append(bss2)
            RDps.append(RDPs / step)
            file.append(file_name[i])
        



    print(mbs)
    add_in_one_file('Tabu_search_50', mbs, 'mbs')
    add_in_one_file('Tabu_search_50', RDp, 'RPD')
    add_in_one_file('Tabu_search_50', file, 'file')
    add_in_one_file('Tabu_search_50', bs, 'bs')
    add_in_one_file('Tabu_search_50', RDps, 'RPDS')
    print("the experement Tabu_search is done!")
    
#________________________________________ experement 100______________________________________________
def get_experement_Tabu_search_result_100(file_name,bestsolut):
    mbs=[]
    RDp=[]
    RDps=[]
    bs=[]
    file=[]
    step = 5

    for i in range(0,len(file_name)):
        mbs2 = 0
        bss2 = 0
        RDPs = 0

        if file_name[i][:1] == '1':
            for j in range(step):
                print("working on the file  " + str(file_name[i]) + " step number " + str(j + 1))
                mbs1 = Tabu_search(file_name[i], 300)

                bss = bestsolut[i]
                RDPs = RDPs + (RPD(bss, mbs1))
                if j == 0:
                    mbs2, bss2 = mbs1, bss

                else:
                    if mbs1 < mbs2:
                        mbs2, bss2 = mbs1, bss

                print(i)
                print(mbs2)
            RDp.append(RPD(bss2, mbs2))
            mbs.append(mbs2)
            bs.append(bss2)
            RDps.append(RDPs / step)
            file.append(file_name[i])

    print(mbs)
    add_in_one_file('Tabu_search_100', mbs, 'mbs')
    add_in_one_file('Tabu_search_100', RDp, 'RPD')
    add_in_one_file('Tabu_search_100', file, 'file')
    add_in_one_file('Tabu_search_100', bs, 'bs')
    add_in_one_file('Tabu_search_100', RDps, 'RPDS')
    print("the experement Tabu_search is done!")

#_______________________________________________calling experement

import sys
process_arg1=sys.argv[1]
process_arg2=sys.argv[2]
process_arg3=sys.argv[3]

def loud_bs_filename():
    File_name = get_file_names('instances/instances')
    bestsolution = get_best_solution()
    return File_name,bestsolution


if process_arg1=='Tabu50':
    print('Starting the ' + process_arg1 + '...')
    print( get_experement_Tabu_search_result_50(*loud_bs_filename()))
    print(process_arg1 + 'is donne!')
if process_arg1=='Tabu100':
    print('Starting the ' + process_arg1 + '...')
    print(get_experement_Tabu_search_result_100(*loud_bs_filename()))
    print(process_arg1 + 'is donne!')

if process_arg1=='TS':
    print('Starting the ' + process_arg1 + '...')
    print(Tabu_search(process_arg2,int(process_arg3)))
    print(process_arg1 + 'is donne!')
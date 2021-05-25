from Local_search import *
import pandas as pd
import csv
import os
import time

def ILS(csv,TC):
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    job = s.shape[0]
    jobs = list(range(0, job))
    jp = Random_permutation(jobs)
    msct1, min1, list1 = best_improvement_Insert(csv, jp)
    timer = 0
    while timer <= TC:
        tic = time.perf_counter()
        list2=perturbation(list1)
        msct3, min3, list3 = best_improvement_exchange(csv,list2)
        if min3<min1:
            list1=list3
            Min = min3
            print(Min)
        else:
            list1=list2
            Min = min1
            print(Min)
        toc = time.perf_counter()
        timer = timer + (toc - tic)
        print(timer)


    return Min

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


def RPD(bs,mbs):

    c=100*((float(mbs)-float(bs))/float(bs))
    return c

def add_in_one_file(file, w, column):
 df = pd.read_csv('Q5/' + file + '.csv')
 df[str(column)] = w
 df.to_csv('Q5/' + file + '.csv', index=False)
 # df.close()



def creat_experement_csv_file(Algo):
    for i in range(len(Algo)):
        header = ['file', 'bs', 'mbs', 'RPD','RPDS']
        with open('Q5/' + Algo[i] + '.csv', 'w') as f:
            dw = csv.DictWriter(f, delimiter=',', fieldnames=header)
            dw.writeheader()
        f.close()
Algo=['Q5_tabu','Q5_Ils']
#creat_experement_csv_file(Algo)
file_name=["50_20_01","50_20_02"]
best_solution=["595260","622342"]
#_____________________________________lunch the experement with tabu
def get_experement_Tabu_search_result(file_name,bestsolut):
    mbs=[]
    RDp=[]
    RDps=[]
    bs=[]
    file=[]
    step = 25

    for i in range(len(file_name)):
        mbs2 = 0
        bss2 = 0
        RDPs = 0
        for j in range(step):
            print("working on the file " + str(i + 1) + " step number " + str(j + 1) + '/' + str(step))
            mbs1 = Tabu_search(file_name[i], 1000)
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
    add_in_one_file('Q5_tabu', mbs, 'mbs')
    add_in_one_file('Q5_tabu', RDp, 'RPD')
    add_in_one_file('Q5_tabu', file, 'file')
    add_in_one_file('Q5_tabu', bs, 'bs')
    add_in_one_file('Q5_tabu', RDps, 'RPDS')
    print("the experement Q5_tabu is done!")

#_________________________________lunch the experement with ILS
def get_experement_ILS_result(file_name,bestsolut):
    mbs=[]
    RDp=[]
    RDps=[]
    bs=[]
    file=[]
    step = 25
    for i in range(len(file_name)):
        mbs2 = 0
        bss2 = 0
        RDPs = 0
        for j in range(step):
            print("working on the file " + str(file_name[i]) + " step number " + str(j + 1) + '/' + str(step))
            mbs1 = ILS(file_name[i], 1000)
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
    add_in_one_file('Q5_Ils', mbs, 'mbs')
    add_in_one_file('Q5_Ils', RDp, 'RPD')
    add_in_one_file('Q5_Ils', file, 'file')
    add_in_one_file('Q5_Ils', bs, 'bs')
    add_in_one_file('Q5_Ils', RDps, 'RPDS')
    print("the experement Q5_Ils is done!")




import sys
process_arg1=sys.argv[1]

if process_arg1=='Tabu':
    print('Starting the ' + process_arg1 + '...')
    print(get_experement_Tabu_search_result(file_name,best_solution))
    print(process_arg1 + 'is donne!')
if process_arg1=='Ils':
    print('Starting the ' + process_arg1 + '...')
    print(get_experement_ILS_result(file_name,best_solution))
    print(process_arg1 + 'is donne!')


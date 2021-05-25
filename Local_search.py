from Methods import *
from Simplified_RZ_heuristic import Simplified_RZ_heuristic


def first_improvement_Insert(csv,init_list):#give it the file name ,n° of 20 and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    list_of_nieborhod =insert_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
                break


    return msct,min,new_list


def first_improvement_exchange(csv,init_list):#give it the file name ,n° of 20 and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    list_of_nieborhod =exchange_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
                break


    return msct,min,new_list

def first_improvement_transpose(csv,init_list):#give it the file name ,n° of 20 and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    list_of_nieborhod =transpose_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
                break


    return msct,min,new_list

#-------------------------------------------------------
def best_improvement_Insert(csv,init_list):#give it the file name ,n° of 20 and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    list_of_nieborhod =insert_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
    return msct,min,new_list


def best_improvement_exchange(csv,init_list):#give it the file name ,n° of 20 and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    list_of_nieborhod =exchange_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct

    return msct,min,new_list

def best_improvement_transpose(csv,init_list):#give it the file name ,n° of 20 and the intial sequance return wtc and new list of nighborhod
    s = getDataframe('instances/instance2/' + csv + '.csv', 20)
    list_of_nieborhod =transpose_neighbourhood(init_list)

    msct1, min1 = WTC(new_matrix_step(s, list_of_nieborhod[0]))
    new_list=list_of_nieborhod[0]
    for i in range(len(list_of_nieborhod)):
        m = new_matrix_step(s, list_of_nieborhod[i])
        sct, wtc = WTC(m)
        if i == 0:
            min = min1
            min1 = 0
            msct = msct1
        else:
            if min > wtc:
                min = wtc
                new_list = list_of_nieborhod[i]
                msct = sct
                break
    return msct,min,new_list
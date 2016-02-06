# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 23:34:38 2016

@author: muqia_000
"""

import sys
import math

def findprm(lst):
    flaglst = [1]*(int(math.sqrt(lst[1])))        # initial as 1, flag 0 if not a prime number
    numlst = range(1, int(math.sqrt(lst[1]))+1)   # create number list


    # find prime number in numlst
    flaglst[0] = 0  # 1 is not a prime number
    for flag in range(1, len(numlst)):
        if flaglst[flag] == 1:
            flaglst[numlst[flag]*2-1:len(flaglst):numlst[flag]] = [0]*int(numlst[-1]/numlst[flag]-1)

    prmlst=[]
    for i in range(len(flaglst)):
        if flaglst[i] == 1:
            prmlst.append(numlst[i])

    #return prmlst

    # flag out multiple of prime number in lst
    lst2 = range(lst[0],lst[1]+1)
    flaglst2 = [1]*len(lst2)

    if lst2[0] == 1:
        flaglst2[0] = 0

    for prmele in prmlst:
        if lst2[0]%prmele == 0:
            firstnum = lst2[0]
            firstloc = 0
        else:
            firstnum = prmele+(lst2[0]-lst2[0]%prmele)
            firstloc = firstnum-lst2[0]

        if firstnum == prmele:
            flaglst2[firstloc:len(lst2):prmele] = [0]*int((len(lst2)-firstloc+prmele-1)/prmele)
            flaglst2[firstloc] = 1
        else:
            flaglst2[firstloc:len(lst2):prmele] = [0]*int((len(lst2)-firstloc+prmele-1)/prmele)



    #return flaglst2

    # print prime number
    prm=''
    for i in range(len(flaglst2)):
        if flaglst2[i] == 1:
            #prm.append(lst2[i])
            prm = prm+str(lst2[i])+'\n'

    return prm





list_of_lists = []
for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    list_of_lists.append(new_list)
#print list_of_lists

for i in range(1,list_of_lists[0][0]+1):
    prmlist = list_of_lists[i]
    #print prmlist
    print findprm(prmlist)

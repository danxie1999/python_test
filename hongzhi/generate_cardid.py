#!/usr/bin/python
#coding:utf-8
import os,sys
if len(sys.argv)<2:
    print "usage: %s cardfilename"%sys.argv[0]
    exit()


def generate_checkbit(id):
    orgin="00000000000000000000"
    # id=raw_input("input cardid: ")
    la=range(1,21)
    lb=[]
    lc=[]
    ld=[]
    le=[]
    #id1='{:0>20}'.format(id)
    id1=orgin[:-len(id)]+id
    #print id1,len(id1)
    for i in range(0,20):
        lb.append(id1[21-la[i]-1:21-la[i]])
    #print "lb",lb,len(lb)
    for i in range(20):
        if i%2==0:
            lc.append(2)
        else:
            lc.append(1)
    #print lc,len(lc)
    for i in range(0,20):
        ld.append(int(lb[i])*lc[i])
    #print ld,len(ld)
    sum=0
    for i in range(0,20):
        le.append(ld[i] if ld[i]<10 else int(ld[i]/10)+ld[i]%10)
        sum+=le[i]
    #print "le",le,len(le),sum
    checkbit=0 if sum%10==0 else 10-sum%10
    # print "check bit is %s"%checkbit
    cardid=id+str(checkbit)
    cardid=orgin[:12][:-len(cardid)]+cardid
    return  cardid

with open(sys.argv[1]) as f:
    for line in f.readlines():
        cardid=line.strip()
        print generate_checkbit(cardid)

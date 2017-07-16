#coding=utf-8
import time
import csv
import sys
# from xlwt import *
reload(sys)
start=time.clock()
s=set()


with open("AuthorwithID.csv", 'r') as f:
    reader=csv.reader(f)
    for row in reader:
        # print len(row[2])
        if len(row[2])==8:
            s.add(row[2])
    print s

dict1=dict.fromkeys(s)
# # print type(dict1)
#
for key in dict1:
    dict1[key] =[]
print dict1

s2=set()
address="D:\MS-DATA\PaperAuthorAffiliations\PaperAuthorAffiliations.txt"
# "D:\MS-DATA\PaperAuthorAffiliations\PaperAuthorAffiliations.txt"
f = open(address, 'r')

i=0

line = f.readline().strip('\n')
while line:
    i = i + 1
    print i
    list = line.split()
    # print list
    # if(list[-1]<='4'):
    if(list[1]in s and list[-1]<='5 '):
        # i = i + 1
        # print i
        print list
        dict1[list[1]].append(list[0])
    line=f.readline().strip('\n')
    if not line:
        line =f.readline().strip('\n')
# for row in f:
#     list=row.split()
    # i = i + 1
    # print i

    # if(list[-1]<='4'):
    #     if(list[1]in s):
    #
    #         # print list
    #         # s2.add(list[0])
    #         dict1[list[1]].append(list[0])

ft=open("resultwithnum.txt", "w")
writer = csv.writer(ft)
for key in dict1:
    temp = key,dict1[key],len(dict1[key])
    writer.writerow(temp)
    print temp


end=time.clock()
print 'runing_time:',end-start

# -*- coding:utf-8 -*-
import csv
import time
start=time.clock()
#得到1945-2010之间的论文集
fpy=open("papersetwithyear.txt")
paper_year=dict()
reader=csv.reader(fpy,delimiter='\t')
for line in reader:
    # print line
    if 1945<int(line[-1])<2011:
        paper_year[line[0]]=int(line[-1])

fpy.close()
print paper_year

f=open("paperwithcitelistmodify.txt")

dict=dict()
# print dict
reader=csv.reader(f)
for line in reader:
    if int(line[-1])>0:
        dict[line[0]]=line[-1]
f.close()
print dict    #每篇论文对应的引用数
print len(dict)

ft=open("resultwithnum.txt")
result=open("publishnum&h-index.txt","w")
writer=csv.writer(result)
reader=csv.reader(ft)
for line in reader:
    publishnum=0     #计数作者1945-2010间的发表数
    # print line
    # print line[-1]
    # print line[1].strip('[]')
    listtemp = line[1].strip('[]').split(',')
    list=[]    #list用来存作者在特定时间段发表的论文集
    listyear=[]
    for id in listtemp:
        if id.strip(' \'')in paper_year.keys():
            publishnum=publishnum+1
            listyear.append(paper_year[id.strip(' \'')])#记录所有论文的发表年份
            list.append(id.strip(' \''))
    # print list
    # print sorted(listyear)
    citelist=[]   #citelist用来存作者发表的论文对应的引用数
    for id in list:
        if id in dict.keys():
            citelist.append(int(dict[id]))
    num=1
    if len(citelist)>0:
        for i in sorted(citelist,reverse=True):
            if i>=num:
                num=num+1
            else:
                break
        # print line[0],publishnum,len(list),num-1
        temp=[line[0],publishnum,sum(citelist)/publishnum,min(listyear),num-1]
        writer.writerow(temp)





end=time.clock()
print 'running time:',end-start
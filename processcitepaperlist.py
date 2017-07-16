#coding=utf-8
import csv
import time
start =time.clock()
#得到特定时段的引文集合
citepaperset=set()
f=open("citepapersetwithyear.txt")
reader=csv.reader(f,delimiter='\t')
for line in reader:
    if 1945<int(line[1])<2016:
        citepaperset.add(line[0])
print citepaperset
print len(citepaperset)
f.close()

f=open("paperwithcitelist2015modify.txt",'w')
writer=csv.writer(f)
ft=open("paperwithcitelist2015.txt")
reader=csv.reader(ft)
for line in reader:
    # print line
    # print line[1].strip('[]')
    listtemp=line[1].strip('[]').split(',')
    # print listtemp
    citepaperlist=[]
    for id in listtemp:
        # print  id.strip(' \'')
        if id.strip(' \'') in citepaperset:
            citepaperlist.append(id.strip(' \''))
    temp=[line[0],citepaperlist,len(citepaperlist)]
    writer.writerow(temp)
end =time.clock()
print 'running time:',end-start
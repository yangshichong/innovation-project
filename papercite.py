import csv
import time
start=time.clock()
paperset=set()
f=open("papersetwithyear.txt")
reader=csv.reader(f, delimiter='\t')
for line in reader:
    if('1945'<line[1]<'2016'):
        paperset.add(line[0])
f.close()
print paperset
print len(paperset)
dict=dict.fromkeys(paperset)
for key in dict:
    dict[key]=[]

# print dict

file=open("D:\MS-DATA\PaperReferences\PaperReferences.txt")
reader=csv.reader(file, delimiter='\t')
for line in reader:
    if line[1]in paperset:
        dict[line[1]].append(line[0])


ft=open("paperwithcitelist2015.txt", "w")
writer = csv.writer(ft)
for key in dict:
    temp = key,dict[key],len(dict[key])
    writer.writerow(temp)
    print temp


end=time.clock()
print 'runing_time:',end-start

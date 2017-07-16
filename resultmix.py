#coding=utf-8
import csv
#2015的h-index字典
dict=dict()
ft=open("resultwithh-index2015.txt")
reader=csv.reader(ft)
for line in reader:
    dict[line[0]]=line[1]
print dict
#作者年龄的字典
dictyear={}
ft=open("AuthorwithID.csv")
reader=csv.reader(ft)
for line in reader:
    dictyear[line[2]]=line[1]
print dictyear

f=open("publishnum&h-index.txt")
f1=open("finish.txt","w")
writer=csv.writer(f1)
reader=csv.reader(f)
for line in reader:
    if line[0]in dict.keys():
        temp=line
        temp.append(dict[line[0]])
        temp.insert(1,dictyear[line[0]])
        writer.writerow(temp)

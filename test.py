import csv
f=open("resultall.txt",'r')
ft=open("resultallwithnum.txt",'w')
writer = csv.writer(ft)
i=0
# for line in f:
#     i=i+1
#     print i,line
reader = csv.reader(f)
for row in reader:
    # print row
    list=row[1][1:-1].split()
    row.append(len(list))
    print row
    writer.writerow(row)
    # if len(list)>0:
    #     print list[0][1:-2]




# line =f.readline()
# while line:
#     i = i + 1
#     print i
#     print  line
#     print line.split()
#     # print line.split(',')
#     # print line.split()[0]
#     line = f.readline()


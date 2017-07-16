import csv
ft=open("paperset.txt","w")
# writer=csv.writer(ft)
with open("resultwithnum.txt") as f:
    reader=csv.reader(f)
    for line in reader:
        print line[-1]
        print line[1].strip('[]')
        listtemp=line[1].strip('[]').split(',')
        for id in listtemp:
            print id.strip(' ')
            ft.write(id.strip(' ')+'\n')
        # print line.split()
        # print len(line.split())
import csv
import time
start =time.clock()
paperset=set()
with open("paperset.txt") as f:
    reader=csv.reader(f)
    for line in f:
        if len(line)>1:
            paperset.add(line.strip('\'\n'))

f.close()
print paperset
print len(paperset)


citepaperset=set()
file=open("D:\MS-DATA\PaperReferences\PaperReferences.txt")
reader=csv.reader(file, delimiter='\t')
for line in reader:
    if line[1]in paperset:
        citepaperset.add(line[0])
print citepaperset
print len(citepaperset)


ft=open("citepapersetwithyear.txt","w")
f=open("D:\MS-DATA\Papers\Papers.txt","r")
reader=csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
for line in reader:
    # print line[0]
    if line[0]in citepaperset:
        list=line[0]+'\t'+line[3]
        print list
        ft.write(list+'\n')

end =time.clock()
print 'running time:',end-start
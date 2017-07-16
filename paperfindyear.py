import csv
paperset=set()
f=open("paperset.txt")
ft=open("papersetwithyear.txt","w")

for line in f:
    # print line
    paperset.add(line.strip('\'\n'))
print paperset
print len(paperset)
# for i in paperset:
#     print i
address="F:\MS-DATA\Papers1.txt""D:\MS-DATA\Papers\Papers.txt"
f=open("D:\MS-DATA\Papers\Papers.txt","r")
reader=csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
for line in reader:
    # print line[0]
    if line[0]in paperset:
        list=line[0]+'\t'+line[3]
        print list
        ft.write(list+'\n')

    # print line
    # print line.split('\t')

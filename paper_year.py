# -*- coding:utf-8 -*-
import re
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


for num in range(2,4):
    ft=open(r'F:\result\findPapers' + str(num) + ".txt", 'wb')
    writer = csv.writer(ft)
    i = 0
    total_info = []
    address = "F:\MS-DATA\Papers" + str(num) + ".txt"
    print address
    with open(address, 'rb') as ft:
        # reader = csv.reader(ft)
        reader = csv.reader(ft, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in reader:
            # str=row[0]

            if len(row)>3 and len(row[3]) == 4 and int(row[3]) <= 2010 and int(row[3]) > 1945:
                # print len(row)
                i = i + 1
                print num,'   ',i

                    # for row in total_info:
                        # print row
                writer.writerow(row)
                # total_info.append(row)

            if row=='':
                break


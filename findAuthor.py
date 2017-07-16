import re
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

total_info = []

with open("D:\MS-DATA\PaperAuthorAffiliations\PaperAuthorAffiliations.txt", 'rb') as ft:
    # reader = csv.reader(ft)
    reader= csv.reader(ft, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        # str=row[0]
        print row
        # print row[0]
        row_split=row[0].split('\t')[0:2]
        total_info.append(row_split)

with open("findAuthor.txt", 'wb') as ft:
    writer = csv.writer(ft)
    for row in total_info:
        print row
        writer.writerow(row)
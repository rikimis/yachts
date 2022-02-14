# 4. File converter

import csv

def csv2tsv(file):
  with open(file,'r', encoding='utf-8') as csv_file, open("output.tsv", 'w', newline='', encoding='utf-8') as tsv_file:
    csv_file = csv.reader(csv_file)
    tsv_file = csv.writer(tsv_file, delimiter='\t')
    for row in csv_file:
        tsv_file.writerow(row)


csv2tsv("input.csv")

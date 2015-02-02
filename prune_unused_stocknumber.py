#!/bin/python
# -*- coding: utf-8 -*-

import csv
f = open('stocknumber.csv', 'rb')
cr = csv.reader(f, delimiter=',')
# skip the comment, if no comment, change comment this two lines
cr.next()
cr.next()

discard_lists = ['認購權證', '認售權證', '熊證', '牛證', '認購售權證']

file_lists = []

for row in cr:
    if row[3] in discard_lists:
        continue
    else:
        file_lists.append(row)

fo = open('stocknumber.csv', 'wb')
wr = csv.writer(fo, delimiter=',')
for row in file_lists:
    wr.writerow(row)
#!/bin/python
# -*- coding: utf-8 -*-

import grs
from grs import Stock
import csv
import sys
from os.path import join, isfile
from os import listdir

def main():
    
    DATA_PATH = 'data'
    file_list = [ f for f in listdir(DATA_PATH) if f[-4:] == '.csv' ]

    # print "Validate conflict data..."
    # for filename in file_list:
    #     fin = open(join(DATA_PATH, filename), 'rb')
    #     dates = set()
    #     for row in csv.reader(fin, delimiter=","):
    #         if row[0] in dates:
    #             print '[CONFLICT]', filename, row
    #         else:
    #             dates.add(row[0])

    print "Validate strange data then rewrite all data again"
    for filename in file_list:
        fin = open(join(DATA_PATH, filename), 'rb')
        rows = []
        errorFlag = False
        for row in csv.reader(fin, delimiter=","):
            if len(row) == 9:
                rows.append(row)
            else:
                errorFlag = True
        if errorFlag:
            print '[STRANGE]', filename
            fout = open(join(DATA_PATH, filename), 'wb')
            cw = csv.writer(fout, delimiter=',')
            for row in rows:
                cw.writerow(row)

    # print "Validate missing month..."
    # startFlag = True if len(sys.argv) > 1 else False
    # for filename in file_list:
    #     if startFlag:
    #         if filename == (sys.argv[1]+'.csv'):
    #             startFlag = False
    #         else:
    #             continue
    #     fin = open(join(DATA_PATH, filename), 'rb')
    #     firstFlag = True
    #     for row in csv.reader(fin, delimiter=","):
    #         if firstFlag:
    #             year = int(row[0].split('/')[0])
    #             month = int(row[0].split('/')[1])
    #             firstFlag = False
    #             continue

    #         print filename, row[0], len(row)
    #         newyear = int(row[0].split('/')[0])
    #         newmonth = int(row[0].split('/')[1])

    #         if newyear > year + 1:
    #             print "[YEAR]", filename, row
    #         if newyear == year and newmonth > month + 1:
    #             print "[MONTH]", filename, row

    #         year = newyear
    #         month = newmonth
            
if __name__ == '__main__':
    main()    
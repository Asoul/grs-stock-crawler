#!/bin/python
# -*- coding: utf-8 -*-

from grs import Stock
import csv
import sys


if len(sys.argv) != 3:
  print "usage: python gupiao.py [from_id] [to_id(not_include)]"
  sys.exit(1)

initial_idx = int(sys.argv[1])
initial_month = 240
record_csv_name = 'record.csv'

# record = open(record_csv_name, "ab")
# writer = csv.writer(record, delimiter=',')

# i = initial_idx
# month = initial_month
# while i < int(sys.argv[2]):
#   print "fetch id = ", i, ", month = ", month
#   try:
#     stock = Stock(str(i).zfill(4), month)# may cause not exist error
#     if month > 0: stock.out_putfile(str(i).zfill(4)+'.csv')# may cause index out of range error
#     writer.writerow([str(i).zfill(4), month])
#   except AttributeError:# index out of range
#     print " >> id = ", i, "out of range! month = ", month
#     month -= 12
#   except: # no such id
#     print " >> id = ", i, " not exist"
#     i += 1
#     month = initial_month
#   else:
#     i += 1
#     month = initial_month
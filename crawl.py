#!/bin/python
# -*- coding: utf-8 -*-

import grs
from grs import Stock
import csv
import sys
from os.path import join, isfile

def get_last_row(csv_filename):
    with open(csv_filename,'rb') as f:
        reader = csv.reader(f)
        lastline = reader.next()
        for line in reader:
            lastline = line
        return lastline

def main():

    PATH_OF_DATA = 'data'

    index_lists = []

    ### 從 stocknumber 中讀出看要抓哪幾隻股票的資料
    f = open('stocknumber.csv', 'rb')
    cr = csv.reader(f, delimiter=',')
    for row in cr:
        index_lists.append(row[0])

    skipFlag = True if len(sys.argv) > 1 else False
    tillFlag = True if len(sys.argv) > 2 else False
    for stock_index in index_lists:
        if skipFlag:
            if stock_index != sys.argv[1]:
                continue
            else:
                skipFlag = False
        if tillFlag:
            if stock_index == sys.argv[2]:
                break

        filename = join(PATH_OF_DATA, stock_index+'.csv')
        if isfile(filename):# 如果已經有檔案，就讀出最後一行然後插入在後面
            print stock_index, 'exist!'
            lastline = get_last_row(filename)
            try:
                st = Stock(stock_index)
            except grs.error.StockNoError:
                print stock_index, "not found!"
                continue
            
            try:
                if len(st.raw) == 0:# 近三個月無資料
                    print "近一個月無資料"
                    continue
            except:# len(st.raw) 沒資料可能會 error
                continue

            # 預設不會超過三個月沒有抓資料
            i = 0
            print lastline
            for i in xrange(len(st.raw)):# 從尾巴開始找看差幾筆
                if lastline[0] == st.raw[-(i+1)][0]:
                    break
            print "st.raw[-1]", st.raw[-1]
            print "缺", i, "筆資料"
            fo = open(filename, 'ab')
            cw = csv.writer(fo, delimiter=',')
            for j in range(0, i):# 把後來的都補上
                cw.writerow(st.raw[-i+j])
        else: # 如果沒有檔案，就從頭開始抓
            print stock_index, ' not exist!'
            # 二分搜尋月分, 最大預設 480 個月 (40 年)
            top_month = 481
            bot_month = 0
            
            while top_month != bot_month:
                month = (top_month + bot_month)/2
                print "top: ", top_month, "bottom: ", bot_month, "now:", month
                st = Stock(stock_index, month)
                try:
                    len(st.raw)# 如果 list index out of range 就會 AttributeError
                    bot_month = month
                    if top_month - bot_month == 1:
                        break
                except AttributeError:
                    top_month = month
            st = Stock(stock_index, bot_month)
            st.out_putfile(filename)

if __name__ == '__main__':
    main()    
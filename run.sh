#!/bin/bash
while :
do
    python crawl.py
    #month=`date +%m`
    #day=`date +%d`
    #git add .
    #git commit -m "update to $month/$day"
    #git push
    # 24 x 60 x 60 = 86400
    sleep 80000
done

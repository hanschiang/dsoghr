# -*- coding: utf-8 -*-

import time
import datetime

print "人事資料登錄"

staff_number = raw_input("請輸入員工編號> ")
punch_in_or_out = int(raw_input("上班，請輸入 1 。下班，請輸入 2 > "))

in_or_out = {1: "上班", 2: "下班"}

time_in_sec = time.time()
time_and_date = datetime.datetime.fromtimestamp(time_in_sec).strftime('%Y/%m/%d, %H:%M:%S')

print in_or_out[punch_in_or_out], time_and_date

# -*- coding: utf-8 -*-

import time
import datetime

print "人事資料登錄"

staff_number = raw_input("請輸入員工編號> ")

in_or_out = int(raw_input("上班，請輸入 1 。下班，請輸入 2 > "))

punch_in_or_out = {1: "上班", 2: "下班"}
staff_list = {001: "OB", 002: "Hs", 003: "Ks", 004: "Rb", 005: "pt"}

time_in_sec = time.time()
time_and_date = datetime.datetime.fromtimestamp(time_in_sec).strftime('%Y/%m/%d, %H:%M:%S')

print punch_in_or_out[in_or_out], time_and_date

# 待研究這段的意思，隨便Google找來的code，還沒弄懂就先用了。
target = open("staff_punch_in_record", 'r+')
target.seek(-2, 2)
if target.read(2) == '\n\n':
    target.seek(-1, 1)

target.write(staff_list[staff_number])
target.write(", ")
target.write(punch_in_or_out[in_or_out])
target.write(", ")
target.write(time_and_date)
target.write('\n')
target.close()


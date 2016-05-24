# -*- coding: utf-8 -*-
import time
import datetime
import subprocess

sys_activated = True

# 工號姓名對照
staff_list = {"5001": "An", "5002": "Apple", "5003": "A", "5004": "Day"}


punch_in_or_out = {1: "上班", 2: "下班"}

# 在terminal運作時設定string的顏色
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


sys_activated == True

# 使輸入畫面重複出現>
while sys_activated == True:

    subprocess.call('clear',shell=True)
    print "\n"

    print bcolors.WARNING + "人事資料登錄" + bcolors.ENDC
    print "\n"

    # 讓員工名單照工號順序print。待研究這段的意思，隨便Google找來的code，還沒弄懂就先用了。    
    for staff_number, staff_name in sorted(staff_list.iteritems()):
        print staff_number, staff_name

    print "\n"

    staff_number = raw_input("請輸入員工編號> ")
    check_staff_number = raw_input("請確認資料正確")

    if staff_number in staff_list:
        in_or_out = int(raw_input("1，上班。2，下班。請輸入> "))
        print "\n"

        # 產生時間戳記
        time_in_sec = time.time()
        time_and_date = datetime.datetime.fromtimestamp(time_in_sec).strftime('%Y/%m/%d, %H:%M:%S')

        # 找到最後的字元？待研究這段的意思，隨便Google找來的code，還沒弄懂就先用了。
        target = open("staff_punch_in_record", 'r+')
        target.seek(-2, 2)
        if target.read(2) == '\n\n':
            target.seek(-1, 1)

        # 寫入staff_punch_in_record
        target.write(staff_number)
        target.write(", ")
        target.write(staff_list[staff_number])
        target.write(", ")
        target.write(punch_in_or_out[in_or_out])
        target.write(", ")
        target.write(time_and_date)
        target.write('\n')
        target.close()
        
        # print打卡結果給員工看到
        print staff_list[staff_number], punch_in_or_out[in_or_out], time_and_date
        print "\n"
        
        raw_input("確認無誤請按 Enter >")

    else:
        print bcolors.WARNING + "編號錯誤。請輸入正確的員工編號。" + bcolors.ENDC
        raw_input("按Enter繼續 >")

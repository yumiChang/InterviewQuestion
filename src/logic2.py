# -*- coding: UTF-8 -*-

def get_total_and_last_high(fst_high):
    # 上一次彈跳高度
    last_high = fst_high

    # 目前總經歷長度
    sum = fst_high

    # 加總每一次起跳到落地
    for i in range(1,10):
        sum += last_high
        last_high = last_high/2

    print("總共",sum)
    print("第十次",last_high/2)

#get_total_and_last_high(100)

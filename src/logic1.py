# -*- coding: UTF-8 -*-

def get_new_score(score):
    # 個位數歸零
    num = int(score / 10) * 10

    right_digit = 0
    new_score = score

    # 判斷原分數的下一個5的倍數
    if num + 5 > score:
        right_digit = 5
    else:
        right_digit = 10

    # 差易小於 3, 設定新分數
    if num + right_digit - score <= 3:
        new_score = num + right_digit

    # 新分數小於 40, 則不予加分
    if new_score < 40:
        new_score = score

    print("{} -> {}".format(score, new_score))


# get_new_score(33)
#get_new_score(73)
#get_new_score(63)
#get_new_score(39)
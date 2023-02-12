# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

def get_credit_card_items(screenshot_path):
    driver = webdriver.Chrome()

    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    driver.implicitly_wait(5)

    # 選擇菜單第一個
    btn_menu = driver.find_element(By.XPATH, "//div[text()='產品介紹']")
    btn_menu.click()
    sleep(5)

    # 截圖
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)

    try:
        shot_path = "{}/screenshot_credit_card_items.png".format(screenshot_path)
        shot_success = driver.get_screenshot_as_file(shot_path)

        if shot_success:
            print("信用卡選單 -> 已截圖({})".format(shot_path))
        else:
            print("截圖失敗")
    except Exception as e:
        print("截圖失敗: {}".format(e))

    # 選擇信用卡區塊
    ele_menu_link_list = btn_menu.find_element(By.XPATH, "./../../div[@class='cubre-o-menu__content']/div[@class='cubre-o-menuLinkList']")
    ele_list = ele_menu_link_list.find_element(By.XPATH, "//div[@class='cubre-o-menuLinkList__btn']/div[text()='信用卡']/../../div[@class='cubre-o-menuLinkList__content']")

    # 取得底下的連結
    ct_ele = ele_list.find_elements(By.XPATH, ".//a")
    print("信用卡選單下方共有 {} 個項目".format(str(len(ct_ele))))

    driver.quit()


#get_credit_card_items("../screenshots")


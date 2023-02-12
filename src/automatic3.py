# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

def get_credit_card_stop_items(screenshot_path):
    driver = webdriver.Chrome()

    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    driver.implicitly_wait(5)

    # 選擇菜單第一個
    btn_menu = driver.find_element(By.XPATH, "//div[text()='產品介紹']")
    btn_menu.click()
    sleep(5)

    # 選擇信用卡區塊
    ele_menu_link_list = btn_menu.find_element(By.XPATH, "./../../div[@class='cubre-o-menu__content']/div[@class='cubre-o-menuLinkList']")
    ele_list = ele_menu_link_list.find_element(By.XPATH, "//div[@class='cubre-o-menuLinkList__btn']/div[text()='信用卡']/../../div[@class='cubre-o-menuLinkList__content']")

    # 進入卡片介紹
    ele_list.find_element(By.XPATH, ".//a[text()='卡片介紹']").click()

    # 取得所有 (停發) 卡片
    ele_cards = driver.find_elements(By.XPATH, "//div[contains(text(),'(停發)')]")
    print("共 {} 張卡片停發".format(len(ele_cards)))

    # 建立截圖資料夾
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)

    # 截圖
    card_num = 0;
    shot_fals_num = 0;
    for ele_card in ele_cards:
        try:
            card_num += 1
            shot_success = ele_card.find_element(By.XPATH, "../..").screenshot("{}/停卡{}.png".format(screenshot_path, card_num))

            if not shot_success:
                shot_fals_num+=1
        except Exception as e:
            shot_fals_num+=1
            print("截圖失敗: {}".format(e))

    print("已截圖 {} 張停發卡(路徑:{})".format( card_num-shot_fals_num, screenshot_path))

    driver.quit()


#get_credit_card_stop_items("../screenshots")


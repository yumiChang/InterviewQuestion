# -*- coding: utf-8 -*-
from selenium import webdriver
import os

def get_home_screenshot(screenshot_path):
    driver = webdriver.Chrome()

    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    driver.implicitly_wait(5)

    # 截圖
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)

    try:
        shot_path = "{}/screenshot.png".format(screenshot_path)
        shot_success = driver.get_screenshot_as_file(shot_path)

        if shot_success:
            print("https://www.cathaybk.com.tw/cathaybk/ -> 已截圖({})".format(shot_path))
        else:
            print("截圖失敗")
    except Exception as e:
        print("截圖失敗: {}".format(e))


    driver.quit()

#get_home_screenshot("../screenshots")



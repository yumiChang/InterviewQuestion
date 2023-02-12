# -*- coding: utf-8 -*-
from src import logic1, logic2, automatic1, automatic2, automatic3

def main():
    screenshot_path = "screenshots"

    print("> 程式邏輯 - 第一題")
    logic1.get_new_score(33)
    logic1.get_new_score(73)
    logic1.get_new_score(63)
    logic1.get_new_score(39)
    print("\n")

    print("> 程式邏輯 - 第二題")
    logic2.get_total_and_last_high(100)
    print("\n")

    print("> 自動化測試 - 第一題")
    automatic1.get_home_screenshot(screenshot_path)
    print("\n")

    print("> 自動化測試 - 第二題")
    automatic2.get_credit_card_items(screenshot_path)
    print("\n")

    print("> 自動化測試 - 第三題")
    automatic3.get_credit_card_stop_items(screenshot_path)
    print("\n")

if __name__ == "__main__":
    main()
"""
test move_click
"""
from selenium.webdriver.common.by import By


def test_move_click(key_no_sign):
    key_no_sign.get("https://www.baidu.com/")
    key_no_sign.send_keys(By.ID, "kw", "python")
    key_no_sign.move_click(By.ID, "su", -56, 19)
    # key_no_sign.quit()

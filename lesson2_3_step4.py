from selenium import webdriver
import time
import math


def calc(x: str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # press the button
    browser.find_element_by_css_selector('button').click()

    # accept confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # read x
    x = browser.find_element_by_css_selector('#input_value').text

    # get answer input field
    answer = browser.find_element_by_css_selector('#answer')

    # type answer into input field
    answer.send_keys(calc(x))

    # press submit button
    browser.find_element_by_css_selector("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

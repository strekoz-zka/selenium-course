from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import math
import time

BEST_PRICE = '$100'


def calc(x: str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # wait for price $100
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), BEST_PRICE))

    # press the button Book
    browser.find_element_by_css_selector('#book').click()

    # read x
    x = browser.find_element_by_css_selector('#input_value').text

    # get answer input field
    answer = browser.find_element_by_css_selector('#answer')

    # type answer into input field
    answer.send_keys(calc(x))

    # press submit button
    browser.find_element_by_css_selector('#solve').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

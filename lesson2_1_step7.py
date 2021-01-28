from selenium import webdriver
import time
import math


def calc(x: str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # pick x
    x = browser.find_element_by_css_selector('#treasure').get_attribute('valuex')

    # type mathematical expression into answer field
    browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    # check I'm a robot
    browser.find_element_by_css_selector('#robotCheckbox').click()

    # switch to Robots rule!
    browser.find_element_by_css_selector('[value="robots"]').click()

    # time.sleep(1)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x: str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # pick x
    x = browser.find_element_by_css_selector('#input_value').text

    # scroll down to input field
    answer = browser.find_element_by_css_selector('#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    # type mathematical expression into answer field
    answer.send_keys(calc(x))

    # check I'm a robot
    robot = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()

    # switch to Robots rule!
    rules = browser.find_element_by_css_selector('[value="robots"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rules)
    rules.click()

    # time.sleep(1)

    # Отправляем заполненную форму
    submit_button = browser.find_element_by_css_selector("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

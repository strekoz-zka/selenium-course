from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    num1 = int(browser.find_element_by_css_selector('#num1').text)
    num2 = int(browser.find_element_by_css_selector('#num2').text)
    num = num1 + num2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num))

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

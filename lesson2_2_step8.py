from selenium import webdriver
import time
import os


FIRSTNAME = 'Otto'
LASTNAME = 'Dix'
EMAIL = 'otto@sample.com'
FILENAME = '2_2step8.txt'

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # first name
    browser.find_element_by_css_selector('input[name="firstname"]').send_keys(FIRSTNAME)

    # last name
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys(LASTNAME)

    # email
    browser.find_element_by_css_selector('input[name="email"]').send_keys(EMAIL)

    # find the path to the test file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, FILENAME)

    # attach file
    browser.find_element_by_css_selector('#file').send_keys(file_path)

    # submit form
    browser.find_element_by_css_selector("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

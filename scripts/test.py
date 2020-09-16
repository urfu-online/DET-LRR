import pandas as pd
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui
from selenium.webdriver.support import expected_conditions as EC

file_name = 'IDS.xlsx'
dfs = pd.read_excel(file_name)
data_frame = dfs['ID'].values.tolist()

for item in data_frame:
    SEQUENCE = 'edit_{}'.format(item)
    SEQUENCE_TWO = 'card_{}'.format(item)
    driver = webdriver.Firefox()
    driver.get("https://learn.urfu.ru")
    username = driver.find_element_by_name("login")
    username.send_keys("r.r.repositor")
    password = driver.find_element_by_name("password")
    password.send_keys("123456789")
    submit = driver.find_element_by_name("submit")
    submit.click()

    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hm-user-roleSwitcher')))
    elem.click()
    elem1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hm-user-roleSwitcher-menu > .hm-list-item')))
    elem1.click()

    driver.get("view-source:https://learn.urfu.ru/subject/list/edit/gridmod//subject_id/{}".format(item))


    # WebDriverWait(driver, 10).until(visibility_of_element_located((By.ID, 'grView')))
    # driver.get("https://learn.urfu.ru/subject/list/edit/gridmod//subject_id/2301")
    # WebDriverWait(driver, 10).until(visibility_of_element_located((By.ID, 'grView')))

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite(SEQUENCE)
    pyautogui.hotkey('enter')

    driver.get("view-source:https://learn.urfu.ru/subject/index/card/subject_id/{}".format(item))

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite(SEQUENCE_TWO)
    pyautogui.hotkey('enter')

    driver.close()

    # http = urllib3.PoolManager()
    # url = 'https://learn.urfu.ru/subject/index/card/subject_id/10'
    # myHeaders = urllib3.util.make_headers(basic_auth='r.r.repositor:123456789')
    # r = http.urlopen('GET', 'https://learn.urfu.ru/subject/list/edit/subject_id/2301', headers=myHeaders)
    # html_doc = r.data
    # soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup)
    # strhtm = soup.prettify()
    # for item in soup.find_all('span'):
    #     if "title" in item.attrs:
    #         print(item.text)

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
import shutil
import os
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

file_name = 'IDS.xlsx'
dfs = pd.read_excel(file_name)
data_frame = dfs['ID'].values.tolist()

data = {
    'title': [],
    'programs': [],
    'conditions': [],
    'owner': [],
    'description': []
}
df = pd.DataFrame(data, columns=['title', 'programs', 'conditions', 'owner', 'description'])

# HTML DOWNLOAD
# for item in data_frame:
#     SEQUENCE = 'edit_{}'.format(item)
#     SEQUENCE_TWO = 'card_{}'.format(item)
#     driver = webdriver.Firefox()
#
#     driver.get("https://learn.urfu.ru")
#     username = driver.find_element_by_name("login")
#
#     username.send_keys("r.r.repositor")
#     password = driver.find_element_by_name("password")
#     password.send_keys("123456789")
#     submit = driver.find_element_by_name("submit")
#     submit.click()
#
#     elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hm-user-roleSwitcher')))
#     elem.click()
#     elem1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hm-user-roleSwitcher-menu > .hm-list-item')))
#     elem1.click()
#
#     driver.get("https://learn.urfu.ru/subject/list/edit/gridmod//subject_id/{}".format(item))
#
#     pyautogui.hotkey('ctrl', 's')
#     time.sleep(1)
#     pyautogui.typewrite(SEQUENCE)
#     pyautogui.hotkey('enter')
#     driver.get("https://learn.urfu.ru/subject/index/card/subject_id/{}".format(item))
#     time.sleep(1)
#
#     pyautogui.hotkey('ctrl', 's')
#     time.sleep(1)
#     pyautogui.typewrite(SEQUENCE_TWO)
#     pyautogui.hotkey('enter')
#     time.sleep(1)
#
#     driver.close()

# HTML TO CSV

for item in data_frame:
    html_doc = '/home/alex/Загрузки/card_{}.html'.format(item)
    html_file = '/home/alex/Загрузки/card_{}_files'.format(item)
    # print(html_doc)

    # if os.path.isdir(html_file):
    #     shutil.rmtree(html_file)
    #     print("remove! %s" % html_file)
    # else:  ## Show an error ##
    #     print("Error: %s file not found" % html_file)

    df1 = pd.read_html(html_doc)
    soup = BeautifulSoup(open(html_doc), 'html.parser')
    strhtm = soup.prettify()
    # print(strhtm)
    # df1 = pd.DataFrame(data=df1)
    df2 = df1[0].T
    # print(df2.values.tolist()[1][1])
    for e in soup.find_all('span'):
        if "title" in e.attrs:
            df = df.append({'title': e.text, 'programs': df2.values.tolist()[1][0], 'description': '{} ; {}'.format(df2.values.tolist()[1][1], df2.values.tolist()[1][3])}, ignore_index=True)
    # except:
    #     SEQUENCE_TWO = 'card_{}'.format(item)
    #     driver = webdriver.Firefox()
    #
    #     driver.get("https://learn.urfu.ru/subject/index/card/subject_id/{}".format(item))
    #     time.sleep(1)
    #
    #     pyautogui.hotkey('ctrl', 's')
    #     time.sleep(1)
    #     pyautogui.typewrite(SEQUENCE_TWO)
    #     pyautogui.hotkey('enter')
    #     time.sleep(1)
    #
    #     driver.close()
    #
    #     if os.path.isdir(html_file):
    #         shutil.rmtree(html_file)
    #         print("remove! %s" % html_file)
    #     else:  ## Show an error ##
    #         print("Error: %s file not found" % html_file)

# print(df)
df.to_excel("output.xlsx")

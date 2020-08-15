# Web Scraping

from selenium import webdriver
from selenium.common.exceptions import *

# Data manipulation

import pandas as pd 

# Visualization

import matplotlib.pyplot as plt
import seaborn as sns

webdriver_path = r'C:\Users\svill\Documents\Programación\Varios\chromedriver.exe' # r para que sea raw string
backmarket_url = 'https://www.backmarket.es/'
search_item = 'iPhone X 64gb'

# Select custom Chrome options, hay un fallo y no abre Chrome

'''
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
'''

# Open the Chrome browser

browser = webdriver.Chrome(webdriver_path)
browser.get(backmarket_url)

search_bar = browser.find_element_by_xpath('//*[@id="header"]/div[1]/form/input')
search_bar.send_keys(search_item).submit()
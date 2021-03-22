import logging
import json
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH ="/home/shmyadav90s/Downloads/chromedriver_linux64" 
DRIVER_PATH = r"E:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.google.com')
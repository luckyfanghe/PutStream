
import requests
import sys
import time
from random import choice
from bs4 import BeautifulSoup
from bs4 import NavigableString
from urlparse import urljoin
import csv
import copy
import re
import os
import time
from threading import Timer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import TimeoutException
import smtplib
import email
import urllib2
import urllib


reload(sys)  
sys.setdefaultencoding('utf8')

DELAY = 10

def RequestUrl (baseUrl): 

    try:
        session = requests.Session()
        req = session.get(baseUrl)
        req.raise_for_status()

        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        vidoe_src = soup.find("video", class_="jw-video jw-reset")
        print vidoe_src["scr"]
    except:
        print("Error!!! Please check network state")
        return

def Chrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
      "download.default_directory": r"F:\Test",
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://putstream.com/movie/sarah-s-key?watching=wetgYRZkn6FmOBRLLEtCu5zKp8")
    src = driver.page_source 
    soup = BeautifulSoup(src,"lxml") 
    Src = soup.find("video", class_="jw-video jw-reset")

    driver.get(Src['src'])

    download_url = driver.current_url
    driver.quit()

    download_file(download_url)


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename

if __name__ == '__main__':
    Chrome();

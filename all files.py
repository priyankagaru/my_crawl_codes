# #!/usr/bin/env python
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.common import exceptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# import csv
# from bs4 import BeautifulSoup as bs
# import requests
# import re
# from datetime import date
# from datetime import datetime
#
# from selenium import webdriver
# import itertools
#
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# locale = "en-NG"
# lang = "en"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# url = "http://www.africacharts.com/official-top-50-songs-nigeria/"
# # res = requests.get(url).text
# # print(res)
# # song_list = re.findall(r'column-3"><h3><strong>(.*?)</h3></strong>', res, flags=re.DOTALL) # CHANGE REGEX
# # print(song_list)
# # for s in song_list:
# # data['Title'].append(s.strip())
# # artist_list = re.findall(r'</h3></strong> <h5>(.*?)</h5></td>', res, flags=re.DOTALL) # CHANGE REGEX
# # for a in artist_list:
# # data['Artist'].append(a.strip())
# # data['Extraction Time'].append(day_date_time.strip())
# # data['Locale'].append(locale.strip())
# # data['Language'].append(lang.strip())
# # data['Tag'].append(tag.strip())
# # data['Main Url'].append(url)
# # data['Supported Url'].append('')
# # data['Url'].append(urllst)
# # supported_url = re.findall(r'<td class="column-5">.*?href="(.*?)"', res, flags=re.DOTALL)
# # for my_href in supported_url:
# # data['Supported Url'].append(my_href)
#
# # # return res_list
# file_name = ' Africacharts_MTC.csv'
# make_csv(file_name, data)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # supported_url_list = list()
# # # for i in range(len(supported_url)):
# # # regex_url = re.search(r'<br />\s*<span.*?><a.*?href="https://geo.*?(.*?)"', supported_url[i], flags=re.DOTALL)
# # # if regex_url:
# # # regex_url = "https://geo" + regex_url.group(1)
# # # supported_url_list.append(regex_url)
# # # else:
# # # supported_url_list.append("")
# # res_list = list()
# # for i in range(len(song_list)):
# # artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
# # " &",
# # ",").replace(
# # '&#034;', '"').replace("&#039;", "'")
# # song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# # for j in range(len(feat_list)):
# # if feat_list[j] in artist_list[i]:
# # artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# # if artist_list[i]:
# # res_dict = dict()
# # res_dict.update({"Title": song_list[i]})
# # res_dict.update({"Artist": artist_list[i]})
# # res_dict.update({"Extraction Time": day_date_time})
# # res_dict.update({"Locale": "en-NG"})
# # res_dict.update({"Language": "en"})
# # res_dict.update({"Tag": ""})
# # res_dict.update({"Main Url": url})
# # res_dict.update({"Supported Url": supported_url[i]})
# # res_dict.update({"Url": ""})
# # res_list.append(res_dict)
# # csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# # 'Url']
# # csv_file = "africacharts.csv"
# # with open(csv_file, 'w') as csvfile:
# # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# # writer.writeheader()
# # for data in res_list:
# # writer.writerow(data)
# # # return res_list
# # except:
# # print("africacharts not working")

import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.africacharts.com/official-top-50-songs-nigeria/'
response = requests.get(url)
locale = "en-NG"
lang = "en"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('tr', {'class': True })
urls= []
for each in acts:
 title = each.find_next('h3').text.strip()
 artist = each.find_next('h5').text.strip()
 link = each.find_next('a', href=True, style=True)
 urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append(urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')
file_name = ' Africacharts_MTC.csv'
make_csv(file_name, data)

# # # download in pdf option available
# #
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.by import By
# # #
# # # options = Options()
# # # options.add_argument('--headless') # Runs Chrome in headless mode.
# # # options.add_argument('--no-sandbox') # Bypass OS security model
# # # options.add_argument('start-maximized')
# # # options.add_argument('disable-infobars')
# # # options.add_argument('--disable-extensions')
# # # import re
# # # import urllib
# # # from datetime import datetime
# # # from datetime import date
# # # import csv
# # # import unicodedata
# # # import time
# # # import requests
# # # import os
# # # from selenium import webdriver
# # # import ssl
# # # from bs4 import BeautifulSoup
# # #
# # # ctx = ssl.create_default_context()
# # # ctx.check_hostname = False
# # # ctx.verify_mode = ssl.CERT_NONE
# # # if os.path.exists("out_album.csv"):
# # # os.remove("out_album.csv")
# # # now = datetime.now()
# # # current_time = now.strftime("%H:%M:%S")
# # # date = date.today()
# # # wd = date.weekday()
# # # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# # # day = days[wd]
# # # date = str(date)
# # # date = date.split("-")
# # # month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# # # '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# # # day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# # # feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring", " (Album"]
# # #
# # # url = 'https://snepmusique.com/les-tops/le-top-de-la-semaine/top-albums/'
# # # chromedriver = Service("/usr/local/bin/chromedriver")
# # # op = webdriver.ChromeOptions()
# # # browser = webdriver.Chrome(service=chromedriver, options=op)
# # # browser.get(url)
# # # time.sleep(5)
# # # # res = browser.page_source
# # # # res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# # # res = requests.get(url).text
# # # song_list = re.findall(r'<div class="titre">(.*?)</div>', str(res), flags=re.DOTALL)
# # # artist = re.findall(r'<div class="artiste">(.*?)</div>', str(res))
# # # res_list = list()
# # # for i in range(len(song_list)):
# # # artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# # # ",").replace(
# # # '&#034;', '"').replace("&#039;", "'")
# # # song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# # # for j in range(len(feat_list)):
# # # if feat_list[j] in artist[i]:
# # # artist[i] = artist[i].partition(feat_list[j])[0]
# # # res_dict = dict()
# # # res_dict.update({"Album_Name": song_list[i]})
# # # res_dict.update({"Artist_Name": artist[i]})
# # # res_dict.update({"Extraction Time": day_date_time})
# # # res_dict.update({"Locale": "fr-FR"})
# # # res_dict.update({"Language": "fr"})
# # # res_dict.update({"Entity_URL": url})
# # # res_dict.update({"Detail_URL": ""})
# # # res_dict.update({"Supported_URL": ""})
# # # res_dict.update({"Entity Type": "/music/album"})
# # # res_list.append(res_dict)
# # # csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# # # 'Supported_URL', 'Entity Type']
# # # csv_file = "snep_album.csv"
# # # with open(csv_file, 'w') as csvfile:
# # # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# # # writer.writeheader()
# # # for data in res_list:
# # # writer.writerow(data)
# #
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.common.exceptions import TimeoutException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # options = Options()
# # options.add_argument('--headless') # Runs Chrome in headless mode.
# # options.add_argument('--no-sandbox') # Bypass OS security model
# # options.add_argument('start-maximized')
# # options.add_argument('disable-infobars')
# # options.add_argument('--disable-extensions')
# # import re
# # import time
# # import requests
# # from bs4 import BeautifulSoup as bs
# # from selenium import webdriver
# # import pandas as pd
# # import unicodedata
# # from datetime import datetime
# # from datetime import date
# # import csv
# # import os
# # import itertools
# #
# # def make_csv(filename, data):
# # with open(filename, 'w+') as file:
# # writer = csv.writer(file)
# # writer.writerow(data.keys())
# # writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
# #
# #
# # now = datetime.now()
# # current_time = now.strftime("%H:%M:%S")
# # date = date.today()
# # wd = date.weekday()
# # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# # day = days[wd]
# # date = str(date)
# # date = date.split("-")
# # month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# # '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# # day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# # feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# # url = 'https://snepmusique.com/les-tops/le-top-de-la-semaine/top-albums/'
# # response = requests.get(url)
# # locale = "it-IT"
# # lang = "IT"
# # tag = ""
# # sup_url =""
# # urllst = ""
# # url_name = []
# # author_name = []
# # song_name = []
# # full_list = []
# # first_half = []
# # urllst = []
# # second_half = []
# # data = {
# # 'Title': [],
# # 'Artist':[] ,
# # 'Extraction Time':[],
# # 'Locale': [],
# # 'Language': [],
# # 'Tag': [],
# # 'Main Url': [],
# # 'Supported Url':[],
# # 'Url': [],
# # }
# # timeout =30
# # chromedriver = Service("/usr/local/bin/chromedriver")
# # op = webdriver.ChromeOptions()
# # browser = webdriver.Chrome(service=chromedriver, options=op)
# # browser.get(url)
# # # soup = bs(response.text, 'html.parser')
# # #
# # # acts = soup.find('table').find_all('tr')
# # # print(len(acts))
# # # urls= []
# # # for each in acts:
# # # title = each.find_next('td',{'class': 'c2'}).find_next('div').text.strip()
# # # artist = each.find_next('td',{'class': 'c2'}).find_next('div').find_next('div').text.strip()
# # # link = ''
# # # # urls = link['href']
# # # data['Title'].append(title.strip())
# # # data['Artist'].append(artist.strip())
# # # data['Extraction Time'].append(day_date_time.strip())
# # # data['Locale'].append(locale.strip())
# # # data['Language'].append(lang.strip())
# # # data['Tag'].append(tag.strip())
# # # data['Main Url'].append(url)
# # # data['Supported Url'].append(link)
# # # data['Url'].append(urllst)
# # # # print(f'{title}\n{artist}\n{urls}\n\n')
# # #
# # # file_name = ' FIMI_IT_Album.csv'
# # # make_csv(file_name, data)
# # delay = 1
# # # timeout =20
# # try:
# # WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '///*[@id="news"]/div[2]/div[3]')))
# # print("Page is ready!")
# # except TimeoutException:
# # print("Loading took too much time!")
# # itembox = browser.find_elements(By.CLASS_NAME,'item')
# # print(len(itembox))
# #
# # # itembox = browser.find_elements(By.CLASS_NAME,'chart-section-element')
# # # # print(len(itembox))
# # # for i in itembox:
# # # song = i.find_elements(By.CLASS_NAME,'chart-section-element-title')
# # # for s in song:
# # # title= s.text.strip()
# # # data['Title'].append(title.strip())
# # # author = i.find_elements(By.CLASS_NAME, 'chart-section-element-author')
# # # link =''
# # # for a in author:
# # # artist= a.text.strip()
# # # data['Artist'].append(artist.strip())
# # # data['Extraction Time'].append(day_date_time.strip())
# # # data['Locale'].append(locale.strip())
# # # data['Language'].append(lang.strip())
# # # data['Tag'].append(tag.strip())
# # # data['Main Url'].append(url)
# # # data['Supported Url'].append(link)
# # # data['Url'].append(urllst)
# # # # print(f'{title}\n{artist}\n{urls}\n\n')
# # #
# # # file_name = ' FIMI_IT_Album.csv'
# # make_csv(file_name, data)

#
# !/usr/bin/env python

#
#
# data['Title'].append(s.text.strip())
# for j in itembox1:
# author = j.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/a/div/div/table/tbody/tr[2]/td[1]')
# for a in author:
# print(a.text)
# data['Artist'].append(a.text.strip())
# # data['Supported Url'].append(link)
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url1)
# data['Supported Url'].append('')
# data['Url'].append(urllst)
#
# for my_href in links:
# # print(my_href)
# link = my_href.get_attribute("href")
# print(link)
# data['Supported Url'].append(link)
# x = x+1
# file_name = ' RECOTOP_JP_MTC.csv'
# make_csv(file_name, data)
#
#
# import re
# import time
# import requests
# from bs4 import BeautifulSoup as bs
# from selenium import webdriver
# import pandas as pd
# import unicodedata
# from datetime import datetime
# from datetime import date
# import csv
# import os
# import itertools
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url = 'https://www.recotop.com/topsongs/country/Japan-Top-100-songs/20220131'
# response = requests.get(url)
# locale = "ja-JP"
# lang = "ja"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# timeout = 30
# soup = bs(response.text, 'html.parser')
#
# acts = soup.find_all('table', style='width:100%')
# print(len(acts))
# urls= []
# for each in acts:
# title = each.find_next('tr').text.strip()
# artist = each.find_next('tr').text.strip()
# # link = each.find_next('a', href=True)
# # urls = link['href']
# data['Title'].append(title.strip())
# data['Artist'].append(artist.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# # data['Supported Url'].append(link)
# data['Url'].append(urllst)
# # print(f'{title}\n{artist}\n{urls}\n\n')

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
try:
 res = requests.get("http://www.thebeat99.com/ngt10/").text
 req_list = re.findall(r'.*?<div class="field-content".*?>(.*?)</div>', res, flags=re.DOTALL)
 artist_song_list = list()
 song_list = list()
 artist_list = list()
 itemList = list()
 for i in range(len(req_list)):
 req_list_final = re.findall(r'<p>(.*?)</p>', req_list[i])
 for item in range(len(req_list_final)):
 req_list_final[item] = req_list_final[item].replace(str(item + 1) + ".", "")
 req_list_final[item] = req_list_final[item].replace("&amp;", "&")
 req_list_final[item] = req_list_final[item].replace("\xe2\x80\x93", "-").replace('–', '-')
 itemList = req_list_final[item].split("-")
 artist_list.append(itemList[0])
 song_list.append(itemList[1])
 # artist_list = map(str.strip, artist_list)
 # song_list = map(str.strip, song_list)
 soup = BeautifulSoup(res, "html.parser")
 main_url = soup.find('link', attrs={'rel': re.compile(r'.*canonical.*')})
 main_url = re.search(r'href=[\'"]?([^\'" >]+)', str(main_url))
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-NG"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": main_url.group(1)})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "thebeat99.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # return res_list
except:
 print("the beat99 not working")
#!/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import csv
import re
from datetime import date
from datetime import datetime
from selenium import webdriver

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# browser = webdriver.Firefox()
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# # browser = webdriver.Chrome(executable_path=chromedriver)

url = "http://www.billboard-japan.com/charts/detail?a=hot100"
browser.get(url)
res = browser.page_source
song_list = re.findall(r'<p class="musuc_title">(.*?)</p>', res)
artist_list = re.findall(r'<p class="artist_name">(.*?)</p>', res)
req_artist_list = list()
for i in range(len(artist_list)):
 if "</a>" in artist_list[i]:
 artist_regex = re.search(r'<a.*?>(.*?)</a>', artist_list[i])
 req_artist_list.append(artist_regex.group(1))
 else:
 req_artist_list.append(artist_list[i])
url_list = re.findall(r'<td headers="name" class="name_td">(.*?)<p class="rank">', res, flags=re.DOTALL)
req_url_list = list()
for i in range(len(url_list)):
 url_regex = re.search(r'<a href="(.*?)"', url_list[i])
 if url_regex:
 main_string = "http://www.billboard-japan.com" + url_regex.group(1)
 req_url_list.append(main_string)
 else:
 req_url_list.append("")
res_list = list()

for i in range(len(song_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")

 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not req_url_list[i]:
 req_url_list[i] = url
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": req_url_list[i]})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
browser.close()
csv_file = "billboard_japan.csv"

with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

# http://www.billboard-japan.com/charts/detail?a=hot100

# #!/usr/bin/env python
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.common import exceptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# import csv
# import bs4
# import requests
# import re
# from datetime import date
# from datetime import datetime
#
# from selenium import webdriver
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# main_url = "https://www.chartsurfer.de/musik/single-charts-deutschland/neueinsteiger"
# res = requests.get(main_url).text
# song_list = re.findall(r'<div class="order-2"><div class="ww" style=.*?><a.*?>(.*?)</a>', res)
# artist_list = re.findall(r'<div class="ww"><a class=.*?>(.*?)</a>', res)
# url_list = re.findall(r'<div class="order-2">.*?<a class=.*?href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# url_list[i] = "http://www.chartsurfer.de" + url_list[i]
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# if not url_list[i]:
# url_list[i] = main_url
# if artist_list[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "de-DE"})
# res_dict.update({"Language": "de"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": url_list[i]})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "chartsurfer.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.chartsurfer.de/musik/single-charts-deutschland/neueinsteiger'
response = requests.get(url)
locale = "de-DE"
lang = "DE"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'bg-color2-light p-2 mb-2'})
urls= []
for each in acts:
 title = each.find_next('div', {'class': 'ww'}).text.strip()
 link = each.find_next('a', href=True)
 urls = link['href']
 artist = each.find_next('div', {'class': 'ww'}).find_next('div', {'class': 'ww'}).text.strip()
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://www.chartsurfer.de' + urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')


#
file_name = ' CHARTSURFER_MTC_CHART.csv'
make_csv(file_name, data)
#!/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import csv
from bs4 import BeautifulSoup
import requests
import re
from datetime import date
from datetime import datetime

from selenium import webdriver
import itertools


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
res = requests.get("https://maistocadas.mus.br/musicas-eletronicas/").text
soup = BeautifulSoup(res, "html.parser")
main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
main_url = re.search(r'content=[\'"]?([^\'" >]+)', str(main_url))
song_list = re.findall(r'<SPAN class="musicas" itemprop="name">(.*?)</SPAN>', res)
artist_list = re.findall(r'<span class="artista" itemprop="byArtist">\s*(.*?)\s*</span>', res)
# for i in range(len(artist_list)):
# if "</a>" in artist_list[i]:
# artist_list[i] = re.findall(r'<a.*?>(.*?)</a>', artist_list[i])
# for i in range(len(artist_list)):
# if not isinstance(artist_list[i], str) and len(artist_list[i]) == 1:
# artist_list[i] = ", ".join(artist_list[i])
# if not isinstance(artist_list[i], str) and len(artist_list[i]) == 2:
# artist_list[i] = artist_list[i][0] + " and " + artist_list[i][1]
# url = re.findall(r'<span class="foto">(.*?)</span>', res)
# url_list = list()
# for i in range(len(url)):
# match = re.search(r'href=[\'"]?([^\'" >]+)', url[i])
# match = match.group(1)
# if main_url.group(1)[0:26] not in match:
# match = main_url.group(1)[0:26] + match
# url_list.append(match)
res_list = list()
for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(',#8211;', '').replace("&#8211;", "").replace("&#8211; ",
 "").strip()
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace(
 str(i + 1), "").replace(". ", "").replace(str(i + 2), "").replace("&#8211;", "-").replace("&#8217;",
 "").strip()
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 # if not url_list[i]:
 # url_list[i] = "https://maistocadas.mus.br/musicas-eletronicas/"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": "https://maistocadas.mus.br/musicas-eletronicas/"})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "maistocadas.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # return res_list


 # return res_list
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
#
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import time
# import itertools
# import requests
# from bs4 import BeautifulSoup as bs
# from selenium import webdriver
# import time
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url = 'https://www.mtv.it/playlist/o104ah/hitlist-italia-classifica-singoli/nipkfa'
# response = requests.get(url)
# locale = "it-IT"
# lang = "IT"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# timeout =30
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url)
# delay = 1
# # timeout =20
# try:
# WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[1]/div/div[2]/div[2]/div/div/div/div')))
# print("Page is ready!")
# except TimeoutException:
# print("Loading took too much time!")
# itembox = browser.find_elements(By.CLASS_NAME,'playlist-item-wrapper')
# print(len(itembox))
# # full_list = ','.join(re.split('(?<!\(.),(?!.\))', my_str))
# for i in itembox:
# songs = i.find_elements(By.XPATH,'//*[@id="app"]/main/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/a/div[2]/h2/div[1]')
# for s in songs:
# my_str = s.text
# full_list = ','.join(re.split('(?<!\(.) • (?!.\))', my_str))
# half= len(full_list)//2
# # print(full_list)
# first_half= full_list[:half]
# print(first_half)
# # second_half = full_list[half:]
# # first_half = full_list[middle::0]
# # print(first_half)
# # second_half = full_list[middle:]
#
#
# data['Title'].append(first_half)
# # author = i.find_elements(By.CLASS_NAME, 'header')
# # for a in author:
# data['Artist'].append(second_half)
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# data['Supported Url'].append('')
# data['Url'].append(urllst)
# links = i.find_elements(By.XPATH,'//*[@id="app"]/main/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/a')[1:]
# for my_href in links:
# link = my_href.get_attribute("href")
# data['Supported Url'].append(link)
#
#
# file_name = ' MTV_CLASSIFICHE_MTC.csv'
# make_csv(file_name, data)

import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.mtv.it/playlist/o104ah/hitlist-italia-classifica-singoli/nipkfa'
response = requests.get(url)
locale = "it-IT"
lang = "IT"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'playlist-item-wrapper'})
urls= []
# full_list = {
# 'Song':[],
# 'Author':[],
# }
for each in acts:
 link = each.find_next('a', href=True)
 urls = link['href']
 # print(urls)
 title = each.find_next('div', {'class': 'header'}).text.strip()
 full_list = ','.join(re.split('(?<!\(.) • (?!.\))', title))
 # print(full_list)
 my_list =full_list.split(',')
 print(my_list[0])
 # artist = each.find_next('div', {'class': 'cmn-artist'}).text.strip()
 data['Title'].append(my_list[0].strip())
 data['Artist'].append(my_list[1].strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://www.mtv.it'+ urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' CLASSIFICHE_IT_MTC_.csv'
make_csv(file_name, data)

#!/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import re
import urllib
import requests
from datetime import datetime
from datetime import date
import csv
import bs4
import os
import unicodedata
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# browser = webdriver.Firefox()

if os.path.exists("out.csv"):
 os.remove("out.csv")


def myradio():
 try:
 url = "https://www.obozrevatel.com/music/chart/russkiy-rok/"
 res = requests.get(url).text
 song_list = re.findall(r'<div class="song-item__info">\s*<a.*?>(.*?)</a>', res, flags=re.DOTALL)
 artist_list = re.findall(r'\s*<div class="song-item__subtitle">(.*?)\s*</div>', res, flags=re.DOTALL)
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace("&amp;", "&")
 url_list = re.findall(r'<div class="song-item__info">\s*<a href="(.*?)"', res, flags=re.DOTALL)
 print(url_list)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 artist_list[i] = artist_list[i].strip()
 song_list[i] = song_list[i].strip()
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ru-RU"})
 res_dict.update({"Language": "ru"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "myradio.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("myradio not working")


def radiole():
 try:
 url = "https://www.radiole.com/lista-radiole"
 res = requests.get(url).text
 song_list = re.findall(r'<div class="itm-body">\s*.*?<p>(.*?)</p>', res, flags=re.DOTALL)
 artist_list = re.findall(r'<div class="itm-body">\s*<h2>(.*?)</h2>', res, flags=re.DOTALL)
 artist_list = artist_list[0:len(song_list)]
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 artist_list[i] = artist_list[i].replace("\n", "").replace("\t", "")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "radiole.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("radiole not working")


def acharts():
 try:
 res = requests.get("https://acharts.co/france_singles_top_100").text
 song_list = re.findall(r'<td class="cPrinciple".*?>.*?<span itemprop="name">(.*?)</span></a>', res,
 flags=re.DOTALL)
 artist_list = re.findall(r'<br />\s*<span class="Sub">(.*?)<span class="Sub subStatsDetails">', res,
 flags=re.DOTALL)
 artist_list = artist_list[0:100]
 req_artist_list = list()
 for i in range(len(artist_list)):
 if "and" in artist_list[i]:
 artist_regex1 = re.findall(r'<span itemprop="name">(.*?)</span>', artist_list[i], flags=re.DOTALL)
 artist_regex1 = " and ".join(artist_regex1)
 req_artist_list.append(artist_regex1)
 else:
 artist_regex2 = re.search(r'<span itemprop="name">(.*?)</span>', artist_list[i], flags=re.DOTALL)
 if not artist_regex2:
 req_artist_list.append("")
 else:
 req_artist_list.append(artist_regex2.group(1))
 url_list = re.findall(
 r'<td class="cPrinciple" itemprop="item" itemscope itemtype="http://schema.org/MusicRecording">\s*<a href="(.*?)"',
 res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(artist_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = "https://acharts.co/france_singles_top_100"
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "acharts.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("acharts not working")


def tds():
 try:
 res = requests.get("http://tds.sigletv.net/lista_sigle.php").text
 song_list = re.findall(r'<td class=listcol1><a.*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<td class=listcol1><a href="(.*?)"', res, flags=re.DOTALL)
 for i in range(len(url_list)):
 url_list[i] = "http://tds.sigletv.net/" + url_list[i]
 artist_list = re.findall(r'<td class=listcol1>.*?<td class=listcol3>(.*?)</td>', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 artist_list[i] = artist_list[i].replace("\n", "").replace("\t", "")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = "http://tds.sigletv.net/lista_sigle.php"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "tds.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("tds not working")


def guitarchordworld():
 try:
 res = requests.get("http://www.guitarchordworld.net/p/bangla-top-10-songs-of-month.html").text
 album = re.findall(r"<b>(.*?)\(", res)
 song_list = list()
 artist_list = list()
 for i in range(len(album)):
 album[i] = album[i].replace("&nbsp;", " ").replace("#", "").replace("</b>", "").replace("<b>", "").replace(
 "<br />", "")
 album[i] = album[i].replace("&amp;", "&")
 album[i] = album[i].strip()
 if i != 10:
 album[i] = album[i][1:]
 else:
 album[i] = album[i][2:]
 album[i] = album[i].strip()
 combined_list = album[i].split("-")
 song_list.append(combined_list[0])
 artist_list.append(combined_list[1])
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 req_url_list = list()
 url_list = re.findall(r'<b>(.*?)\)', res)
 for i in range(len(url_list)):
 url_regex = re.search(r'<a href="(.*?)"', url_list[i])
 if not url_regex:
 req_url_list.append("")
 else:
 req_url_list.append(url_regex.group(1))
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not req_url_list[i]:
 req_url_list[i] = "http://www.guitarchordworld.net/p/bangla-top-10-songs-of-month.html"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "bn-bd"})
 res_dict.update({"Language": "bn"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": req_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "guitarchordworld.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("guitarchordworld not working")


def chartsinfrance():
 try:
 url1 = "http://www.chartsinfrance.net/charts/singles.php,p1"
 res1 = requests.get(url1).text
 song_list1 = re.findall(r'<font class="noir11"><a href.*?>(.*?)</a></font></div>', res1, flags=re.DOTALL)
 artist_list1 = re.findall(r'<div class="c1_td5"><font.*?><a.*?>(.*?)</a>', res1, flags=re.DOTALL)
 url_list1 = re.findall(r'<font class="noir11"><a href="(.*?)"', res1, flags=re.DOTALL)
 for i in range(len(url_list1)):
 url_list1[i] = "http://www.chartsinfrance.net" + url_list1[i]
 res_list1 = list()
 for i in range(len(song_list1)):
 artist_list1[i] = artist_list1[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list1[i] = song_list1[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list1[i]:
 artist_list1[i] = artist_list1[i].partition(feat_list[j])[0]
 if not url_list1[i]:
 url_list1[i] = url1
 if artist_list1[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list1[i]})
 res_dict.update({"Artist": artist_list1[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list1[i]})
 res_list1.append(res_dict)
 url2 = "http://www.chartsinfrance.net/charts/singles.php,p2"
 res2 = requests.get(url2).text
 song_list2 = re.findall(r'<font class="noir11"><a href.*?>(.*?)</a></font></div>', res2, flags=re.DOTALL)
 artist_list2 = re.findall(r'<div class="c1_td5"><font.*?><a.*?>(.*?)</a>', res2, flags=re.DOTALL)
 url_list2 = re.findall(r'<font class="noir11"><a href="(.*?)"', res2, flags=re.DOTALL)
 for i in range(len(url_list2)):
 url_list2[i] = "http://www.chartsinfrance.net" + url_list2[i]
 res_list2 = list()
 for i in range(len(song_list2)):
 artist_list2[i] = artist_list2[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list2[i] = song_list2[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list2[i]:
 artist_list2[i] = artist_list2[i].partition(feat_list[j])[0]
 if not url_list2[i]:
 url_list2[i] = url2
 if artist_list2[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list2[i]})
 res_dict.update({"Artist": artist_list2[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list2[i]})
 res_list2.append(res_dict)
 url3 = "http://www.chartsinfrance.net/charts/singles.php,p3"
 res3 = requests.get(url3).text
 song_list3 = re.findall(r'<font class="noir11"><a href.*?>(.*?)</a></font></div>', res3, flags=re.DOTALL)
 artist_list3 = re.findall(r'<div class="c1_td5"><font.*?><a.*?>(.*?)</a>', res3, flags=re.DOTALL)
 url_list3 = re.findall(r'<font class="noir11"><a href="(.*?)"', res3, flags=re.DOTALL)
 for i in range(len(url_list3)):
 url_list3[i] = "http://www.chartsinfrance.net" + url_list3[i]
 res_list3 = list()
 for i in range(len(song_list3)):
 artist_list3[i] = artist_list3[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list3[i] = song_list3[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list3[i]:
 artist_list3[i] = artist_list3[i].partition(feat_list[j])[0]
 if not url_list3[i]:
 url_list3[i] = url3
 if artist_list3[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list3[i]})
 res_dict.update({"Artist": artist_list3[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list3[i]})
 res_list3.append(res_dict)
 url4 = "http://www.chartsinfrance.net/charts/singles.php,p4"
 res4 = requests.get(url4).text
 song_list4 = re.findall(r'<font class="noir11"><a href.*?>(.*?)</a></font></div>', res4, flags=re.DOTALL)
 artist_list4 = re.findall(r'<div class="c1_td5"><font.*?><a.*?>(.*?)</a>', res4, flags=re.DOTALL)
 url_list4 = re.findall(r'<font class="noir11"><a href="(.*?)"', res4, flags=re.DOTALL)
 for i in range(len(url_list4)):
 url_list4[i] = "http://www.chartsinfrance.net" + url_list4[i]
 res_list4 = list()
 for i in range(len(song_list4)):
 artist_list4[i] = artist_list4[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list4[i] = song_list4[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list4[i]:
 artist_list4[i] = artist_list4[i].partition(feat_list[j])[0]
 if not url_list4[i]:
 url_list4[i] = url4
 if artist_list4[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list4[i]})
 res_dict.update({"Artist": artist_list4[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list4[i]})
 res_list4.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "chartsinfrance.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list1:
 writer.writerow(data)
 for data in res_list2:
 writer.writerow(data)
 for data in res_list3:
 writer.writerow(data)
 for data in res_list4:
 writer.writerow(data)
 return res_list1, res_list2, res_list3, res_list4
 except:
 print("chartsinfrance not working")


def africacharts():
 try:
 url = "http://www.africacharts.com/official-top-50-songs-nigeria/"
 res = requests.get(url).text
 song_list = re.findall(r'column-3"><h3><strong>(.*?)</h3></strong>', res, flags=re.DOTALL) # CHANGE REGEX
 artist_list = re.findall(r'</h3></strong> <h5>(.*?)</h5></td>', res, flags=re.DOTALL) # CHANGE REGEX
 supported_url = re.findall(r'<td class="column-5">.*?href="(.*?)"', res, flags=re.DOTALL)
 # supported_url_list = list()
 # for i in range(len(supported_url)):
 # regex_url = re.search(r'<br />\s*<span.*?><a.*?href="https://geo.*?(.*?)"', supported_url[i], flags=re.DOTALL)
 # if regex_url:
 # regex_url = "https://geo" + regex_url.group(1)
 # supported_url_list.append(regex_url)
 # else:
 # supported_url_list.append("")
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-NG"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": supported_url[i]})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "africacharts.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("africacharts not working")


def billboardjapan():
 url = "http://www.billboard-japan.com/charts/detail?a=hot100"
 res = requests.get(url).text
 song_list = re.findall(r'<p class="musuc_title">(.*?)</p>', res)
 artist_list = re.findall(r'<p class="artist_name">(.*?)</p>', res)
 req_artist_list = list()
 for i in range(len(artist_list)):
 if "</a>" in artist_list[i]:
 artist_regex = re.search(r'<a.*?>(.*?)</a>', artist_list[i])
 req_artist_list.append(artist_regex.group(1))
 else:
 req_artist_list.append(artist_list[i])
 url_list = re.findall(r'<td headers="name" class="name_td">(.*?)<p class="rank">', res, flags=re.DOTALL)
 req_url_list = list()
 for i in range(len(url_list)):
 url_regex = re.search(r'<a href="(.*?)"', url_list[i])
 if url_regex:
 main_string = "http://www.billboard-japan.com" + url_regex.group(1)
 req_url_list.append(main_string)
 else:
 req_url_list.append("")
 res_list = list()
 for i in range(len(song_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not req_url_list[i]:
 req_url_list[i] = url
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": req_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "billboard_japan.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def chartsurfer():
 main_url = "https://www.chartsurfer.de/musik/airplay-charts-deutschland/charts"
 res = requests.get(main_url).text
 song_list = re.findall(r'<div class="order-2"><div class="ww" style=.*?><a.*?>(.*?)</a>', res)
 artist_list = re.findall(r'<div class="ww"><a class=.*?>(.*?)</a>', res)
 url_list = re.findall(r'<div class="order-2">.*?<a class=.*?href="(.*?)"', res)
 res_list = list()
 for i in range(len(song_list)):
 url_list[i] = "http://www.chartsurfer.de" + url_list[i]
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = main_url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "chartsurfer.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def classifiche():
 res = requests.get('http://classifiche.mtv.it/hitlist-italia-classifica-singoli/cgmo2j').text
 main_url = "http://classifiche.mtv.it/hitlist-italia-classifica-singoli/cgmo2j"
 res_list = list()
 item_box = re.findall(r'<div class="chart-main">(.*?)</div>', res, flags=re.DOTALL)
 req_url_list = list()
 url_regex1 = re.search(r'<ul class="inner-charts">.*?<a href="(.*?)" class="row-link">', res, flags=re.DOTALL)
 if url_regex1:
 req_url_list.append(url_regex1.group(1))
 else:
 req_url_list.append("")
 url_list = re.findall(r'<div class="chart-main">.*?</div>(.*?)<em>', res, flags=re.DOTALL)
 for i in range(len(url_list)):
 url_regex = re.search(r'<a href="(.*?)"', url_list[i])
 if url_regex:
 req_url_list.append(url_regex.group(1))
 else:
 req_url_list.append("")
 for i in range(len(item_box)):
 song_list = re.search(r'<b>(.*?)</b>', item_box[i]).group(1)
 artist_list = re.search(r'<span>(.*?)</span>', item_box[i])
 if artist_list:
 artist_list = artist_list.group(1)
 else:
 artist_list = ""
 artist_list = artist_list.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list = song_list.replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list:
 artist_list = artist_list.partition(feat_list[j])[0]
 if not req_url_list[i]:
 req_url_list[i] = main_url
 if artist_list:
 res_dict = dict()
 res_dict.update({"Title": song_list})
 res_dict.update({"Artist": artist_list})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": "http://classifiche.mtv.it" + req_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "classifiche.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

#
# def gaana():
#
# res = requests.get("https://gaana.com/album/bengali-top-hits").text
# main_url = "https://gaana.com/album/bengali-top-hits"
# req_list = re.findall(r'<ul id="">(.*?)<div id="relatedalbumdetail".*?>', res)
# for each_item in range(len(req_list)):
# song_list = re.findall(r'<span>(.*?)</span>', req_list[each_item])
# artist_list = re.findall(r'<p>(.*?)</p>', req_list[each_item])
# res_list = list()
# for i in range(len(artist_list)):
# artist_list[i] = artist_list[i].replace("Bengali Top Hits - ", "")
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# if artist_list[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "bn-BD"})
# res_dict.update({"Language": "bn"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": main_url})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": ""})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "gaana.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

#
# def gaanadjbengali():
# res = requests.get("https://gaana.com/playlist/gaana-dj-bengali-top-20").text
# main_url = "https://gaana.com/playlist/gaana-dj-bengali-top-20"
# song_list = re.findall(r'<div class="track_npqitemdetail">\s*<span>(.*?)</span>', res, flags=re.DOTALL)
# artist_list = re.findall(r'<div class="track_npqitemdetail">.*?<a.*?>(.*?)</a>', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# if artist_list[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "bn-BD"})
# res_dict.update({"Language": "bn"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": main_url})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": ""})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "gaana_dj_bengali.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list


# def gaonchart():
 # url = "http://gaonchart.co.kr/main/section/chart/online.gaon"
 # res = requests.get(url).text
 # song_list = re.findall(r'<td class="subject">\s*<p.*?>(.*?)</p>', res, flags=re.DOTALL)
 # artist_list = re.findall(r'<p class="singer".*?>(.*?)<span class="bar">', res, flags=re.DOTALL)
 # res_list = list()
 # for i in range(len(song_list)):
 # artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 # ",").replace(
 # '&#034;', '"').replace("&#039;", "'")
 # song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 # for j in range(len(feat_list)):
 # if feat_list[j] in artist_list[i]:
 # artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 # if artist_list[i]:
 # res_dict = dict()
 # res_dict.update({"Title": song_list[i]})
 # res_dict.update({"Artist": artist_list[i]})
 # res_dict.update({"Extraction Time": day_date_time})
 # res_dict.update({"Locale": "ko-KR"})
 # res_dict.update({"Language": "ko"})
 # res_dict.update({"Tag": ""})
 # res_dict.update({"Main Url": ""})
 # res_dict.update({"Supported Url": ""})
 # res_dict.update({"Url": url})
 # res_list.append(res_dict)
 # res_list = res_list[0:100]
 # csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 # 'Url']
 # csv_file = "gaonchart.csv"
 # with open(csv_file, 'w') as csvfile:
 # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 # writer.writeheader()
 # for data in res_list:
 # writer.writerow(data)
 # return res_list


def itopchartchildren():
 url = "https://itopchart.com/it/it/top-songs/childrens-music/"
 res = requests.get(url).text
 artist_list = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
 song_list = re.findall(r'class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<a class="item_name" href="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": url_list[i]})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "itopchart_childrens.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def itopchartchristian():
 url = "https://itopchart.com/it/it/top-songs/christian-gospel/"
 res = requests.get(url).text
 artist_list = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
 song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL) # CHANGE REGEX
 url_list = re.findall(r'<a class="item_name" href="(.*?)"', res, flags=re.DOTALL) # CHANGE REGEX
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": url_list[i]})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "itopchart_christian.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def itopchartfrench():
 url = "https://itopchart.com/fr/fr/top-songs/french-pop/"
 res = requests.get(url).text
 artist_list = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
 song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<a class="item_name" href="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": url_list[i]})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "itopchart_french.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def letssingit():
 url = "https://www.letssingit.com/charts/japan-singles"
 res = requests.get(url).text
 song_list = re.findall(r'</td><td>(.*?)</td></tr>', res, flags=re.DOTALL)
 req_song_list = list()
 req_artist_list = list()
 url_list = list()
 for i in range(len(song_list)):
 song_regex1 = re.search(r'</td><td><a.*?class=high_profile>(.*?)</a>', song_list[i])
 if not song_regex1:
 song_regex2 = re.search(r'</td><td>(.*?)-', song_list[i]).group(1)
 song_regex2 = song_regex2.strip()
 req_artist_list.append(song_regex2)
 else:
 req_song_list.append(song_regex1.group(1).replace(" lyrics", ""))
 artist_regex1 = re.search(r'</a><br><a href.*?>(.*?)</a>', song_list[i])
 if not artist_regex1:
 artist_regex2 = re.search(r'</td><td>(.*)-(.*)', song_list[i]).group(2)
 artist_regex2 = artist_regex2.strip()
 req_song_list.append(artist_regex2)
 else:
 req_artist_list.append(artist_regex1.group(1))
 url_regex = re.search(r'</td><td><a href="(.*?)"', song_list[i])
 if url_regex:
 url_list.append(url_regex.group(1))
 else:
 url_list.append("")
 res_list = list()
 for i in range(len(req_artist_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 req_song_list[i] = req_song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": req_song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "japan_singles.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def lastfm():
 url1 = "https://www.last.fm/es/tag/rock+en+espanol/tracks"
 res1 = requests.get(url1).text
 song_list1 = re.findall(r'class="chartlist-name".*?>\s*<a.*?>(.*?)</a>', res1, flags=re.DOTALL)
 artist_list1 = re.findall(r'class="chartlist-artist".*?>\s*<a.*?>(.*?)</a>', res1, flags=re.DOTALL)
 url_list1 = re.findall(r'class="chartlist-name".*?>\s*<a\s*href="(.*?)"', res1, flags=re.DOTALL)

 res_list1 = list()
 for i in range(len(artist_list1)):
 artist_list1[i] = artist_list1[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list1[i] = song_list1[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list1[i]:
 artist_list1[i] = artist_list1[i].partition(feat_list[j])[0]
 if not url_list1[i]:
 url_list1[i] = url1
 if artist_list1[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list1[i]})
 res_dict.update({"Artist": artist_list1[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url1})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": 'https://www.last.fm' + url_list1[i]})
 res_list1.append(res_dict)

 url2 = "https://www.last.fm/es/tag/rock+en+espanol/tracks?page=2"
 res2 = requests.get(url2).text
 song_list2 = re.findall(r'class="chartlist-name".*?>\s*<a.*?>(.*?)</a>', res2, flags=re.DOTALL)
 artist_list2 = re.findall(r'class="chartlist-artist".*?>\s*<a.*?>(.*?)</a>', res2, flags=re.DOTALL)
 url_list2 = re.findall(r'class="chartlist-name".*?>\s*<a\s*href="(.*?)"', res1, flags=re.DOTALL)
 # url_regex2 = re.findall(r'<td class="chartlist-play">\s*(.*?)</a>', res2, flags=re.DOTALL)
 res_list2 = list()
 for i in range(len(artist_list2)):
 artist_list2[i] = artist_list2[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list2[i] = song_list2[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list2[i]:
 artist_list2[i] = artist_list2[i].partition(feat_list[j])[0]
 if not url_list2[i]:
 url_list2[i] = url2
 if artist_list2[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list2[i]})
 res_dict.update({"Artist": artist_list2[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url2})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": 'https://www.last.fm' + url_list2[i]})
 res_list2.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "last_fm.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list1:
 writer.writerow(data)
 for data in res_list2:
 writer.writerow(data)
 return res_list1, res_list2


def los40():
 data = requests.get('https://los40.com/lista40/').text
 soup = bs4.BeautifulSoup(data, "html.parser")
 main_url = "https://los40.com/lista40/"
 element = soup.find_all('div', attrs={'class': re.compile(r'.*info_grupo.*')})
 song_list = re.findall(r'<div class="info_grupo">\s*<p>(.*?)</p>', str(element))
 res_list = list()
 artist_list = re.findall(r'<h4>(.*?)</h4>', str(element))
 req_artist_list = list()
 supported_url_list = list()
 for i in range(len(artist_list)):
 artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist_list[i])
 detail_page = re.search(r'<a href="(.*?)"', artist_list[i])
 if not artist_regex:
 req_artist_list.append(artist_list[i])
 else:
 req_artist_list.append(artist_regex.group(1))
 if not detail_page:
 supported_url_list.append("")
 else:
 supported_url_list.append("https://los40.com" + detail_page.group(1))
 req_url_list = list()
 url_list = re.findall(r'<li><a title="votar" class="votar login_votar".*?>(.*?)<span class="button_more".*?>', data,
 flags=re.DOTALL)
 for i in range(len(url_list)):
 url_regex = re.search(r"<a href='(.*?)'", url_list[i])
 if not url_regex:
 req_url_list.append("")
 else:
 req_url_list.append(url_regex.group(1))
 for i in range(len(artist_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(";", ", ")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not supported_url_list[i]:
 supported_url_list[i] = main_url
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": req_url_list[i]})
 res_dict.update({"Url": supported_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "los40.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def maistocadaselectronicas():
 res = requests.get("https://maistocadas.mus.br/musicas-eletronicas/").text
 soup = bs4.BeautifulSoup(res, "html.parser")
 main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
 main_url = re.search(r'content=[\'"]?([^\'" >]+)', str(main_url))
 song_list = re.findall(r'<SPAN class="musicas" itemprop="name">(.*?)</SPAN>', res)
 artist_list = re.findall(r'<span class="artista" itemprop="byArtist">\s*(.*?)\s*</span>', res)
 # for i in range(len(artist_list)):
 # if "</a>" in artist_list[i]:
 # artist_list[i] = re.findall(r'<a.*?>(.*?)</a>', artist_list[i])
 # for i in range(len(artist_list)):
 # if not isinstance(artist_list[i], str) and len(artist_list[i]) == 1:
 # artist_list[i] = ", ".join(artist_list[i])
 # if not isinstance(artist_list[i], str) and len(artist_list[i]) == 2:
 # artist_list[i] = artist_list[i][0] + " and " + artist_list[i][1]
 # url = re.findall(r'<span class="foto">(.*?)</span>', res)
 # url_list = list()
 # for i in range(len(url)):
 # match = re.search(r'href=[\'"]?([^\'" >]+)', url[i])
 # match = match.group(1)
 # if main_url.group(1)[0:26] not in match:
 # match = main_url.group(1)[0:26] + match
 # url_list.append(match)
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(',#8211;', '').replace("&#8211;", "").replace("&#8211; ",
 "").strip()
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace(
 str(i + 1), "").replace(". ", "").replace(str(i + 2), "").replace("&#8211;", "-").replace("&#8217;",
 "").strip()
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 # if not url_list[i]:
 # url_list[i] = "https://maistocadas.mus.br/musicas-eletronicas/"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": "https://maistocadas.mus.br/musicas-eletronicas/"})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "maistocadas.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def maistocadassartanejas():
 res = requests.get("https://maistocadas.mus.br/musicas-sertanejas/").text
 soup = bs4.BeautifulSoup(res, "html.parser")
 main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
 main_url = re.search(r'content=[\'"]?([^\'" >]+)', str(main_url))
 song_list = re.findall(r'<SPAN class="musicas" itemprop="name">\s*(.*?)\s*</span>', res, flags=re.DOTALL)
 artist_list = re.findall(r'<span class="artista" itemprop="byArtist">\s*(.*?)\s*</span>', res, flags=re.DOTALL)
 # for i in range(len(artist_list)):
 # if "</a>" in artist_list[i]:
 # artist_list[i] = re.findall(r'<a.*?>(.*?)</a>', artist_list[i])
 # for i in range(len(artist_list)):
 # if not isinstance(artist_list[i], str) and len(artist_list[i]) == 1:
 # artist_list[i] = ", ".join(artist_list[i])
 # if not isinstance(artist_list[i], str) and len(artist_list[i]) == 2:
 # artist_list[i] = artist_list[i][0] + " and " + artist_list[i][1]
 # url = re.findall(r'<span class="foto">(.*?)</span>', res)
 # url_list = list()
 # for i in range(len(url)):
 # match = re.search(r'href=[\'"]?([^\'" >]+)', url[i])
 # match = match.group(1)
 # if main_url.group(1)[0:26] not in match:
 # match = main_url.group(1)[0:26] + match
 # url_list.append(match)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(',#8211;', '').replace("&#8211; ", "")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace(
 str(i + 1), "").replace("&#8211;", "-").replace(". ", "")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 # if not url_list[i]:
 # url_list[i] = "https://maistocadas.mus.br/musicas-sertanejas/"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": "https://maistocadas.mus.br/musicas-sertanejas/"})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "maistocadas_sartanejas.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

#
# def mix1():
# url = 'https://www.mix1.de/charts/partycharts.htm'
# browser.get(url)
# time.sleep(20)
# res = browser.page_source
# # res = requests.get('https://www.mix1.de/charts/partycharts.htm').text
# song_list = re.findall(r'charts-second-child desktop.*?<a.*?>(.*?)</a>', str(res), re.DOTALL)
# artist_list = re.findall(r'charts-second-child desktop.*?charts-single-interpret">(.*?)</div>', str(res), re.DOTALL)
# url_list = re.findall(r'charts-second-child desktop.*?<a href="(.*?)"', str(res), re.DOTALL)
# supported_url = re.findall(r'charts-second-child desktop.*?</i>\s*<a href="(.*?)"', str(res), re.DOTALL)
# res_list = []
# for i in range(len(artist_list)):
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",") \
# .replace(" And", ",").replace(" &", ",").replace('&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": str(artist_list[i]).strip()})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "de-DE"})
# res_dict.update({"Language": "de"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": supported_url[i]})
# res_dict.update({"Url": url_list[i]})
# res_list.append(res_dict)
# res_list = res_list[0:50]
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "mix_1.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list


def mtvde():
 url = "http://www.mtv.de/charts/c6mc86/single-top-100?expanded=true"
 browser.get(url)
 while True:
 try:
 time.sleep(10)
 more_buttons = browser.find_element_by_css_selector(".btn-border-dark.float-center.loadMoreBtn")
 more_buttons.click()
 except Exception:
 break
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="videoTitle">(.*?)</div>', str(res), flags=re.DOTALL)
 item_box = re.findall(r'<div class="videoTitle">(.*?)<div class="chartItemsBox".*?>', str(res), flags=re.DOTALL)
 last_item = re.search(r'<div class="chartItemsBox" style="order:100">(.*?)<div class="loader".*?>', str(res),
 flags=re.DOTALL).group(1)
 item_box.append(last_item)
 res_list = list()
 for i in range(len(song_list)):
 if "<span>" in item_box[i]:
 artist_list = re.search(r'<span>(.*?)</span>', item_box[i], flags=re.DOTALL).group(1)
 url_list = re.search(r'</span></a></div><a href="(.*?)"', item_box[i], flags=re.DOTALL)
 if url_list:
 url_list = url_list.group(1)
 else:
 url_list = ""
 else:
 artist_list = re.search(r'<div class="artist regular-content">(.*?)</div>', item_box[i],
 flags=re.DOTALL)
 if artist_list:
 artist_list = artist_list.group(1)
 else:
 artist_list = ""
 url_list = ""
 artist_list = artist_list.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list:
 artist_list = artist_list.partition(feat_list[j])[0]
 if not url_list:
 url_list = url
 if artist_list:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "mtv_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def officialcharts():
 res = requests.get('https://www.officialcharts.com/charts/').text
 main_url = re.search(r'<link rel="canonical".*?>(.*?)<link rel="shortcut icon" href="/favicon.ico" />', res,
 flags=re.DOTALL).group(1)
 req_main_url = re.search("(?P<url>https?://[^\s]+)", str(main_url)).group("url")
 req_main_url = req_main_url.replace('"/>', '')
 res_list = list()
 song_list = re.findall(r'<div class="title">\s+<a.*?>(.*?)</a>', res, flags=re.DOTALL)
 artist_list = re.findall(r'<div class="artist">\s+<a.*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<div class="title">\s*<a href="(.*?)"', res, flags=re.DOTALL)
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace("&#39;", "'")
 artist_list[i] = artist_list[i].replace("&amp;", "&")
 for i in range(len(song_list)):
 url_list[i] = url_list[i].replace("&#39;", "'")
 url_list[i] = "https://www.officialcharts.com/" + url_list[i]
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace("&#39;",
 "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = "https://www.officialcharts.com/charts/"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-UK"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "officialcharts.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def oljo():
 url1 = "https://www.oljo.de/radiochart_d/radio100.shtml"
 res1 = requests.get(url1).text
 song_list1 = re.findall(r'<div class="inutilander"><div><strong>(.*?)</strong>', res1, flags=re.DOTALL)
 artist_list1 = re.findall(r'<div class="inutilander"><div><strong>.*?<span class="albtitel">(.*?)\s*&nbsp;</div>',
 res1, flags=re.DOTALL)
 url_list1 = re.findall(
 r'<div class="inutilander"><div><strong>.*?<span class="albtitel">.*?</div></div>(.*?)<img.*?>', res1,
 flags=re.DOTALL)
 req_url_list1 = list()
 req_supported_url_list1 = list()
 req_supported_url_list2 = list()
 for i in range(len(url_list1)):
 url_regex = re.search(r'<div class="videoneuchart"><a href="(.*?)"', url_list1[i], flags=re.DOTALL)
 if url_regex:
 req_url_list1.append(url_regex.group(1))
 else:
 req_url_list1.append("")
 supported_url_regex = re.search(r'<div class="amalinkneuchart2"><a href="(.*?)"', url_list1[i], flags=re.DOTALL)
 if supported_url_regex:
 req_supported_url_list1.append(supported_url_regex.group(1))
 else:
 req_supported_url_list1.append("")
 res_list1 = list()
 for i in range(len(artist_list1)):
 artist_list1[i] = artist_list1[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list1[i] = song_list1[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list1[i]:
 artist_list1[i] = artist_list1[i].partition(feat_list[j])[0]
 if not req_url_list1[i]:
 req_url_list1[i] = url1
 if artist_list1[i]:
 res_dict = dict()
 res_dict.update({"Title": artist_list1[i]})
 res_dict.update({"Artist": song_list1[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": req_supported_url_list1[i]})
 res_dict.update({"Url": req_url_list1[i]})
 res_list1.append(res_dict)
 url2 = "https://www.oljo.de/radiochart_d/radio41100.shtml"
 res2 = requests.get(url2).text
 song_list2 = re.findall(r'<div class="inutilander"><div><strong>(.*?)</strong>', res2, flags=re.DOTALL)
 artist_list2 = re.findall(r'<div class="inutilander"><div><strong>.*?<span class="albtitel">(.*?)\s*&nbsp;</div>',
 res2, flags=re.DOTALL)
 url_list2 = re.findall(
 r'<div class="inutilander"><div><strong>.*?<span class="albtitel">.*?</div></div>(.*?)<img.*?>', res2,
 flags=re.DOTALL)
 req_url_list2 = list()
 for i in range(len(url_list2)):
 url_regex = re.search(r'<div class="videoneuchart"><a href="(.*?)"', url_list2[i], flags=re.DOTALL)
 if url_regex:
 req_url_list2.append(url_regex.group(1))
 else:
 req_url_list2.append("")
 supported_url_regex = re.search(r'<div class="amalinkneuchart2"><a href="(.*?)"', url_list2[i], flags=re.DOTALL)
 if supported_url_regex:
 req_supported_url_list2.append(supported_url_regex.group(1))
 else:
 req_supported_url_list2.append("")
 res_list2 = list()
 for i in range(len(artist_list2)):
 artist_list2[i] = artist_list2[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list2[i] = song_list2[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list2[i]:
 artist_list2[i] = artist_list2[i].partition(feat_list[j])[0]
 if not req_url_list2[i]:
 req_url_list2[i] = url2
 if artist_list2[i]:
 res_dict = dict()
 res_dict.update({"Title": artist_list2[i]})
 res_dict.update({"Artist": song_list2[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": req_supported_url_list2[i]})
 res_dict.update({"Url": req_url_list2[i]})
 res_list2.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "oljo.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list1:
 writer.writerow(data)
 for data in res_list2:
 writer.writerow(data)
 return res_list1, res_list2


def oricon():
 url1 = "https://www.oricon.co.jp/rank/js/w/"
 res1 = requests.get(url1).text
 url_list_all_page = re.findall(r'<div class="block-rank-pager-bottom mt20">(.*?)</div>', res1, flags=re.DOTALL)
 url_regex_all_page = re.findall(r'<li><a href="(.*?)"', url_list_all_page[0])
 for i in range(len(url_regex_all_page)):
 url_regex_all_page[i] = "https://www.oricon.co.jp/" + url_regex_all_page[i]
 artist_list1 = re.findall(r'<p class="name">(.*?)</p>', res1, flags=re.DOTALL)
 song_list1 = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', res1, flags=re.DOTALL)
 url_list1 = re.findall(r'<div class="ribbon">.*?\s*<div class="inner">(.*?)<p class="image"><span>', res1,
 flags=re.DOTALL)
 for i in range(len(url_list1)):
 url_regex = re.search(r'<a href="(.*?)"', url_list1[i])
 if url_regex:
 url_list1[i] = url_regex.group(1)
 url_list1[i] = "https://www.oricon.co.jp" + url_list1[i]
 else:
 url_list1[i] = ""
 res_list1 = list()
 for i in range(len(song_list1)):
 artist_list1[i] = artist_list1[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list1[i] = song_list1[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list1[i]:
 artist_list1[i] = artist_list1[i].partition(feat_list[j])[0]
 if not url_list1[i]:
 url_list1[i] = url1
 if artist_list1[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list1[i]})
 res_dict.update({"Artist": artist_list1[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list1[i]})
 res_list1.append(res_dict)
 url2 = url_regex_all_page[1]
 res2 = requests.get(url2).text
 artist_list2 = re.findall(r'<p class="name">(.*?)</p>', res2, flags=re.DOTALL)
 song_list2 = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', res2, flags=re.DOTALL)
 url_list2 = re.findall(r'<div class="ribbon">.*?\s*<div class="inner">(.*?)<p class="image"><span>', res2,
 flags=re.DOTALL)
 for i in range(len(url_list2)):
 url_regex = re.search(r'<a href="(.*?)"', url_list2[i])
 if url_regex:
 url_list2[i] = url_regex.group(1)
 url_list2[i] = "https://www.oricon.co.jp" + url_list2[i]
 else:
 url_list2[i] = ""
 res_list2 = list()
 for i in range(len(song_list2)):
 artist_list2[i] = artist_list2[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list2[i] = song_list2[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list2[i]:
 artist_list2[i] = artist_list2[i].partition(feat_list[j])[0]
 if not url_list2[i]:
 url_list2[i] = url2
 if artist_list2[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list2[i]})
 res_dict.update({"Artist": artist_list2[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list2[i]})
 res_list2.append(res_dict)
 url3 = url_regex_all_page[2]
 res3 = requests.get(url3).text
 artist_list3 = re.findall(r'<p class="name">(.*?)</p>', res3, flags=re.DOTALL)
 song_list3 = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', res3, flags=re.DOTALL)
 url_list3 = re.findall(r'<div class="ribbon">.*?\s*<div class="inner">(.*?)<p class="image"><span>', res3,
 flags=re.DOTALL)
 for i in range(len(url_list3)):
 url_regex = re.search(r'<a href="(.*?)"', url_list3[i])
 if url_regex:
 url_list3[i] = url_regex.group(1)
 url_list3[i] = "https://www.oricon.co.jp" + url_list3[i]
 else:
 url_list3[i] = ""
 res_list3 = list()
 for i in range(len(song_list3)):
 artist_list3[i] = artist_list3[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list3[i] = song_list3[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list3[i]:
 artist_list3[i] = artist_list3[i].partition(feat_list[j])[0]
 if not url_list3[i]:
 url_list3[i] = url3
 if artist_list3[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list3[i]})
 res_dict.update({"Artist": artist_list3[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list3[i]})
 res_list3.append(res_dict)
 url4 = url_regex_all_page[3]
 res4 = requests.get(url4).text
 artist_list4 = re.findall(r'<p class="name">(.*?)</p>', res4, flags=re.DOTALL)
 song_list4 = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', res4, flags=re.DOTALL)
 url_list4 = re.findall(r'<div class="ribbon">.*?\s*<div class="inner">(.*?)<p class="image"><span>', res4,
 flags=re.DOTALL)
 for i in range(len(url_list4)):
 url_regex = re.search(r'<a href="(.*?)"', url_list4[i])
 if url_regex:
 url_list4[i] = url_regex.group(1)
 url_list4[i] = "https://www.oricon.co.jp" + url_list4[i]
 else:
 url_list4[i] = ""
 res_list4 = list()
 for i in range(len(song_list4)):
 artist_list4[i] = artist_list4[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list4[i] = song_list4[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list4[i]:
 artist_list4[i] = artist_list4[i].partition(feat_list[j])[0]
 if not url_list4[i]:
 url_list4[i] = url4
 if artist_list4[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list4[i]})
 res_dict.update({"Artist": artist_list4[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list4[i]})
 res_list4.append(res_dict)
 url5 = url_regex_all_page[4]
 res5 = requests.get(url5).text
 artist_list5 = re.findall(r'<p class="name">(.*?)</p>', res5, flags=re.DOTALL)
 song_list5 = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', res5, flags=re.DOTALL)
 url_list5 = re.findall(r'<div class="ribbon">.*?\s*<div class="inner">(.*?)<p class="image"><span>', res5,
 flags=re.DOTALL)
 for i in range(len(url_list5)):
 url_regex = re.search(r'<a href="(.*?)"', url_list5[i])
 if url_regex:
 url_list5[i] = url_regex.group(1)
 url_list5[i] = "https://www.oricon.co.jp" + url_list5[i]
 else:
 url_list5[i] = ""
 res_list5 = list()
 for i in range(len(url_list5)):
 artist_list5[i] = artist_list5[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list5[i] = song_list5[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list5[i]:
 artist_list5[i] = artist_list5[i].partition(feat_list[j])[0]
 if not url_list5[i]:
 url_list5[i] = url5
 if artist_list5[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list5[i]})
 res_dict.update({"Artist": artist_list5[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list5[i]})
 res_list5.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "oricon.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data1 in res_list1:
 writer.writerow(data1)
 for data2 in res_list2:
 writer.writerow(data2)
 for data3 in res_list3:
 writer.writerow(data3)
 for data4 in res_list4:
 writer.writerow(data4)
 for data5 in res_list5:
 writer.writerow(data5)
 return res_list1, res_list2, res_list3, res_list4, res_list5


def raaga():
 res = requests.get("https://www.raaga.com/tamil/top10").text
 song_list = re.findall(r'<span title.*?><input onclick.*?>(.*?)</span>', res, flags=re.DOTALL)
 artist_list = re.findall(r'<p><span>Singers.*?</span><a title.*?>(.*?)</p>', res, flags=re.DOTALL)
 required_artist_list = list()
 for each_item in range(len(song_list)):
 song_list[each_item] = song_list[each_item].replace("&nbsp;", "")
 for each_item in range(len(artist_list)):
 if "," in artist_list[each_item]:
 artist_list[each_item] = artist_list[each_item].split(",")
 artist_list[each_item][0] = artist_list[each_item][0].replace("</a>", "")
 artist_list_regex = re.search(r'<a title.*?>(.*?)</a>', artist_list[each_item][1], flags=re.DOTALL).group(1)
 required_artist_list.append(artist_list[each_item][0] + " and " + artist_list_regex)
 else:
 artist_list[each_item] = artist_list[each_item].replace("</a>", "")
 required_artist_list.append(artist_list[each_item])
 req_url_list = list()
 # first_url = re.search(r'<ul class="top_ten_list">\s+<li>\s+<a href="(.*?)"', res, flags=re.DOTALL).group(1)
 # req_url_list.append(first_url)
 url_list = re.findall(r'<li>\s+<a href="(.*?)<div class="image_wrap_big top10_imagewrap_box">', res,
 flags=re.DOTALL)
 for i in range(-9, 0, 1):
 req_url_list.append(url_list[i])
 for i in range(len(req_url_list)):
 req_url_list[i] = req_url_list[i].replace(' class="history-ajaxy">\r\n', '')
 req_url_list[i] = req_url_list[i].replace('"', '')
 req_url_list[i] = req_url_list[i].strip()
 res_list = list()
 for i in range(len(required_artist_list)):
 required_artist_list[i] = required_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(
 " &", ",").replace('&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in required_artist_list[i]:
 required_artist_list[i] = required_artist_list[i].partition(feat_list[j])[0]
 if not req_url_list[i]:
 req_url_list[i] = "https://www.raaga.com/tamil/top10"
 if required_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": required_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ta-IN"})
 res_dict.update({"Language": "ta"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": req_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "raaga.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def radiomirchikannada():
 url = "https://www.radiomirchi.com/more/kannada-top-20/"
 res = requests.get(url).text
 song_list = re.findall(r'\s*<div class="header">\s*<h2>(.*?)</h2>', res)
 artist_list = re.findall(r'\s*<div class="header">\s*<h2>.*?</h2>\s*<h3>.*?<br>\s*(.*?)</h3>', res)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "radiomirchi_kannada.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def radiomirchimalayalam():
 url = "https://www.radiomirchi.com/more/malayalam-top-20/"
 res = requests.get(url).text
 song_list = re.findall(r'\s*<div class="header">\s*<h2>(.*?)</h2>', res)
 artist_list = re.findall(r'\s*<div class="header">\s*<h2>.*?</h2>\s*<h3>.*?<br>\s*(.*?)</h3>', res)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "radiomirchi_malayalam.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def radiomirchimore():
 url = "https://www.radiomirchi.com/more/mirchi-top-20/"
 res = requests.get(url).text
 song_list = re.findall(r'\s*<div class="header">\s*<h2>(.*?)</h2>', res)
 artist_list = re.findall(r'\s*<div class="header">\s*<h2>.*?</h2>\s*<h3>.*?<br>\s*(.*?)</h3>', res)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "radiomirchi_more.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def radiomirchitamil():
 url = "https://www.radiomirchi.com/more/tamil-top-20/"
 res = requests.get(url).text
 song_list = re.findall(r'\s*<div class="header">\s*<h2>(.*?)</h2>', res)
 artist_list = re.findall(r'\s*<div class="header">\s*<h2>.*?</h2>\s*<h3>.*?<br>\s*(.*?)</h3>', res)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ta-IN"})
 res_dict.update({"Language": "ta"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "radiomirchi_tamil.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def radiomirchibangla():
 url = "https://www.radiomirchi.com/more/bangla-top-10/"
 res = requests.get(url).text
 song_list = re.findall(r'\s*<div class="header">\s*<h2>(.*?)</h2>', res)
 artist_list = re.findall(r'\s*<div class="header">\s*<h2>.*?</h2>\s*<h3>.*?<br>\s*(.*?)</h3>', res)
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "bn-BD"})
 res_dict.update({"Language": "bn"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "radiomirchi_bangla.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

 # def recochokusingle():
 url = "https://recochoku.jp/ranking/single/weekly/"
 res = requests.get(url).text
 song_list = re.findall(r'<br/>\s*<a.*?class="ttl">(.*?)</a>\s*<p><a.*?>', res)
 artist_list = re.findall(r'<br/>\s*<a.*?class="ttl">.*?</a>\s*<p><a.*?>(.*?)</a></p>', res, flags=re.DOTALL)
 url_list = re.findall(r'<br/>\s*<a href="(.*?)class="ttl">.*?</a>\s*<p><a.*?>.*?</a></p>', res)
 for i in range(len(url_list)):
 url_list[i] = url_list[i].replace('"', '')
 url_list[i] = "https://recochoku.jp" + url_list[i]
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "recochoku_single_weekly.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

 # def recochokuweekly():
 url = "https://recochoku.jp/genreranking/j-pop/weekly/"
 res = requests.get(url).text
 song_list = re.findall(r'<br/>\s*<a.*?class="ttl">(.*?)</a>\s*<p><a.*?>', res)
 artist_list = re.findall(r'<br/>\s*<a.*?class="ttl">.*?</a>\s*<p><a.*?>(.*?)</a></p>', res, flags=re.DOTALL)
 url_list = re.findall(r'<br/>\s*<a href="(.*?)class="ttl">.*?</a>\s*<p><a.*?>.*?</a></p>', res)
 for i in range(len(url_list)):
 url_list[i] = url_list[i].replace('"', '')
 url_list[i] = "https://recochoku.jp" + url_list[i]
 res_list = list()
 for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "recochoku_weekly.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def rhapsody():
 res = requests.get("https://us.napster.com/chart/tracks").text
 soup = bs4.BeautifulSoup(res, "html.parser")
 main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
 req_main_url = re.search("(?P<url>https?://[^\s]+)", str(main_url)).group("url")
 req_main_url = req_main_url.replace('"', '')
 song_list = re.findall(r'<div class="name play-link js-play-link-in-track">(.*?)</div>', res, flags=re.DOTALL)
 artist_list = re.findall(r'<div class="artist-name js-artist-name">(.*?)</div>', res, flags=re.DOTALL)
 req_song_list = list()
 req_artist_list = list()
 for each_song in range(len(song_list)):
 regex = re.search(r'<a href.*?">(.*?)</a>', song_list[each_song])
 req_song_list.append(regex.group(1))
 for each_artist in range(len(artist_list)):
 regex = re.search(r'<a class="artist-link" href=.*?>(.*?)</a>', artist_list[each_artist], flags=re.DOTALL)
 if not regex:
 regex = re.search(r'<span>(.*?)</span>', artist_list[each_artist], flags=re.DOTALL)
 regex = regex.group(1)
 regex = regex.strip()
 req_artist_list.append(regex)
 res_list = list()
 url_list = re.findall(
 r'<script type="application/ld\+json">\s*{&quot;@context&quot;:&quot;http://schema\.org&quot;,&quot;@type&quot;:&quot;MusicRecording&quot;,&quot;name&quot;:&quot;.*?&quot;url&quot;:&quot;(.*?)&quot;',
 res, flags=re.DOTALL)
 for i in range(len(req_artist_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 req_song_list[i] = req_song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = "https://us.napster.com/chart/tracks"
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": req_song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "rhapsody.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def thebeat99():
 try:
 res = requests.get("http://www.thebeat99.com/ngt10/").text
 req_list = re.findall(r'.*?<div class="views-field views-field-body".*?>(.*?)</div>', res, flags=re.DOTALL)
 artist_song_list = list()
 song_list = list()
 artist_list = list()
 itemList = list()
 for i in range(len(req_list)):
 req_list_final = re.findall(r'<p>(.*?)</p>', req_list[i])
 for item in range(len(req_list_final)):
 req_list_final[item] = req_list_final[item].replace(str(item + 1) + ".", "")
 req_list_final[item] = req_list_final[item].replace("&amp;", "&")
 req_list_final[item] = req_list_final[item].replace("\xe2\x80\x93", "-").replace('–', '-')
 itemList = req_list_final[item].split("-")
 artist_list.append(itemList[0])
 song_list.append(itemList[1])
 # artist_list = map(str.strip, artist_list)
 # song_list = map(str.strip, song_list)
 soup = bs4.BeautifulSoup(res, "html.parser")
 main_url = soup.find('link', attrs={'rel': re.compile(r'.*canonical.*')})
 main_url = re.search(r'href=[\'"]?([^\'" >]+)', str(main_url))
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-NG"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": main_url.group(1)})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "thebeat99.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("the beat99 not working")

def top4011():
 try:
 res = requests.get("https://top40-charts.com/chart.php?cid=11").text
 soup = bs4.BeautifulSoup(res, "html.parser")
 main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
 req_main_url = re.search("(?P<url>https?://[^\s]+)", str(main_url)).group("url")
 req_main_url = req_main_url.replace('"', '')
 song_list = re.findall(r'<B><a.*?>(.*?)</a></b></div>', res, flags=re.DOTALL)
 artist_list = re.findall(r'</a></b></div><a.*?>(.*?)</a></td></tr></table>', res, flags=re.DOTALL)
 url_list = re.findall(r'<B><a(.*?)</a></b></div>', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(url_list)):
 match = re.search(r'href=[\'"]?([^\'" >]+)', url_list[i]).group(1)
 match = req_main_url[0:24] + match
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not match:
 match = "https://top40-charts.com/chart.php?cid=11"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": match})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "top40_11.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("top40_11 not working")

def top4043():
 try:
 res = requests.get("https://top40-charts.com/chart.php?cid=43").text
 soup = bs4.BeautifulSoup(res, "html.parser")
 main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
 req_main_url = re.search("(?P<url>https?://[^\s]+)", str(main_url)).group("url")
 req_main_url = req_main_url.replace('"', '')
 song_list = re.findall(r'<B><a.*?>(.*?)</a></b></div>', res, flags=re.DOTALL)
 artist_list = re.findall(r'</a></b></div><a.*?>(.*?)</a></td></tr></table>', res, flags=re.DOTALL)
 url_list = re.findall(r'<B><a(.*?)</a></b></div>', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(url_list)):
 match = re.search(r'href=[\'"]?([^\'" >]+)', url_list[i]).group(1)
 match = req_main_url[0:24] + match
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not match:
 match = "https://top40-charts.com/chart.php?cid=43"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": match})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "top40_43.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except:
 print("top40_43 not working")

def urdutop10():
 url = "http://www.top10songs.org/best-urdu-songs-albums.html"
 res = requests.get(url).text
 all_details = re.findall(r'<td width.*?>(.*?)</td>', res, flags=re.DOTALL)
 all_details = all_details[4:]
 song_list = list()
 artist_list = list()
 for i in range(len(all_details)):
 if i % 4 == 0:
 song_list.append(all_details[i])
 if i % 4 == 2:
 artist_list.append(all_details[i])
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace(
 "&#8211; ", "-")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ur-PK"})
 res_dict.update({"Language": "ur"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "urdu_top10.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def vagalume():
 res = requests.get("https://www.vagalume.com.br/top100/musicas/geral").text
 main_url = re.search(r'</title>(.*?)<link rel.*?>', res)
 req_main_url = main_url.group().replace('"', "").replace("/>", "")
 req_main_url = re.search('(?<=link rel=canonical href=)(.*)', req_main_url)
 song = re.findall(r'<a class="w1.*?>(.*?)</a>', res)
 url_list = re.findall(r'<a class="w1 h22" href=(.*?)>', res)
 song_list = list()
 for i in range(len(song)):
 clean = re.sub(r'<.+>', '', song[i])
 song_list.append(clean)
 artist = re.findall(r'<p class=styleBlack>(.*?)<p>', res)
 res_list = list()
 for i in range(len(artist)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 url_list[i] = "https://www.vagalume.com.br" + url_list[i]
 if not url_list[i]:
 url_list[i] = "https://www.vagalume.com.br/top100/musicas/geral"
 if artist[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "vagalume.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def gpmusic():
 url = "http://player.gpmusic.co/playlists/62413"
 browser.get(url)
 time.sleep(20)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list, artist_list = [], []
 soup_obj = bs(res, "html.parser").findAll("li", {"class": "tile track extended ui-draggable ui-draggable-handle"})
 for i in soup_obj:
 song_list.append(i.find("span", {"class": "title"}).text)
 artist_list.append(i.find("span", {"class": "artist"}).text)
 res_list = list()
 for i in range(len(song_list)):
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": ""})
 res_dict.update({"Locale": "bn-BD"})
 res_dict.update({"Language": "bn"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 print(res_list)
 print(len(res_list))
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "gpmusic_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def hotmusic():
 url = "https://www.hotmusiccharts.com/th/itunes"
 browser.get(url)
 time.sleep(10)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'internal-artist.*?>(.*?)</a></div>', res, flags=re.DOTALL)
 song_list = re.findall(r'song-title.*?>(.*?)</a></div>', res)
 url_list = re.findall(r'song-title.*? href="(.*?)"', res, flags=re.DOTALL)
 supported_url_list = re.findall(r"'outbound-artist','(.*?)'", res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 url_list[i] = "https://www.hotmusiccharts.com" + url_list[i]
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "th-TH"})
 res_dict.update({"Language": "th"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "hot_music_charts1_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def hotmusiccharts():
 url = "https://www.hotmusiccharts.com/ng/itunes"
 browser.get(url)
 time.sleep(10)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'internal-artist.*?>(.*?)</a></div>', res, flags=re.DOTALL)
 song_list = re.findall(r'song-title.*?>(.*?)</a></div>', res)
 url_list = re.findall(r'song-title.*? href="(.*?)"', res, flags=re.DOTALL)
 supported_url_list = re.findall(r"'outbound-artist','(.*?)'", res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 url_list[i] = "https://www.hotmusiccharts.com" + url_list[i]
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 if not url_list[i]:
 url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-NG"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "hot_music_charts_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def hotchartmp3():
 url = ["http://hotcharts.ru/mp3/top/clicks/week/", "http://hotcharts.ru/mp3/top/clicks/week/2",
 "http://hotcharts.ru/mp3/top/clicks/week/3", "http://hotcharts.ru/mp3/top/clicks/week/4"]
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "hotchart_mp3_topchart.csv"
 if os.path.exists("hotchart_mp3_topchart.csv"):
 os.remove("hotchart_mp3_topchart.csv")
 for j in range(len(url)):
 browser.get(url[j])
 time.sleep(20)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 req_song_list = list()
 song_list = re.findall(r'<div class="song_title visible">.*?</a>.*?<span.*?>(.*?)</span>', res,
 flags=re.DOTALL)
 artist = re.findall(r'<div class="song_title visible">.*?<span.*?>(.*?)</span>', res, flags=re.DOTALL)
 url_list = re.findall(r'<div class="song_title visible">.*?</a>.*?<a href="(.*?)"', res,
 flags=re.DOTALL)
 # print(len(song_list))
 # print(len(artist))
 # print(len(url_list))
 # print(url_list)
 # res_list = list()
 res_list = []
 for i in range(len(song_list)):
 url_list[i] = "http://hotcharts.ru" + url_list[i]
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 if not url_list[i]:
 url_list[i] = url[j]
 if artist[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ru-RU"})
 res_dict.update({"Language": "ru"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


def hungama():
 url = "https://www.hungama.com/videos/explore/trending-videos-5318/"
 res = requests.get(url).text
 song_list = re.findall(r'<div class="leftbox">\s*<a.*?>(.*?)</a>', res, flags=re.DOTALL)
 res_list = list()
 url_list = re.findall(r'<div class="leftbox">\s*<a.*?href="(.*?)"', res, flags=re.DOTALL)
 # for i in range(len(url_list)):
 # url_regex = url_list[i].partition('<a id="pajax_a" href="')
 # url_list[i] = url_regex[2]
 for i in range(len(url_list)):
 sub_res = requests.get(url_list[i]).text
 artist = re.search(r'<span>Singers:</span>(.*?)<br>', sub_res, flags=re.DOTALL)
 if not artist:
 artist1 = re.search(r'<span>Artist:</span>(.*?)<br>', sub_res, flags=re.DOTALL)
 if not artist1:
 artist = ""
 else:
 artist_regex = re.findall(r'<a.*?>(.*?)</a>', artist1.group(1), flags=re.DOTALL)
 artist = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 else:
 artist_regex = re.findall(r'<a.*?>(.*?)</a>', artist.group(1), flags=re.DOTALL)
 artist = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 artist = artist.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist:
 artist = artist.partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "hungama_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def hungamabengali():
 url = "https://www.hungama.com/all/latest-tracks-52/3355/"
 res = requests.get(url).text
 song_list = re.findall(r'<div class="leftbox">\s*<a.*?>(.*?)</a>', res, flags=re.DOTALL)
 res_list = list()
 url_list = re.findall(r'<a id="pajax_a" class="art-ttl" href="(.*?)"', res, flags=re.DOTALL)
 for i in range(len(url_list)):
 song_list[i] = song_list[i].strip()
 sub_res = requests.get(url_list[i]).text
 artist = re.search(r'<td nowrap>Singer - </td>(.*?)<tr>', sub_res, flags=re.DOTALL)
 if not artist:
 artist1 = re.search(r'<span>Artist:</span>(.*?)<br>', sub_res, flags=re.DOTALL)
 if not artist1:
 artist = ""
 else:
 artist_regex = re.findall(r'<a.*?>(.*?)</a>', artist1.group(1), flags=re.DOTALL)
 artist = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 else:
 artist_regex = re.findall(r'<a.*?>(.*?)</a>', artist.group(1), flags=re.DOTALL)
 artist = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 artist = artist.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist:
 artist = artist.partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "bn-BD"})
 res_dict.update({"Language": "bn"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "hungama_bengali_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def saavn():
 url = "https://www.jiosaavn.com/featured/weekly-top-songs/Vzehd0ZQty4_"
 browser.get(url)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'<em class="meta">(.*?)</em>', res, flags=re.DOTALL)
 song_list = re.findall(r'<span class="title"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<meta property="music:song" content="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist_regex = re.findall(r'class="".*?>(.*?)</a>', artist_list[i])
 artist_regex = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 artist_regex = artist_regex.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_regex:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_regex})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ur-Pk"})
 res_dict.update({"Language": "ur"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "jiosaavn1_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

 # def jiosaavn():
 url = "https://www.jiosaavn.com/featured/weekly-top-songs"
 browser.get(url)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'<abbr class="spacer">(.*?)</em>', res, flags=re.DOTALL)
 song_list = re.findall(r'<span class="title"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<meta property="music:song" content="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist_regex = re.findall(r'class="".*?>(.*?)</a>', artist_list[i])
 artist_regex = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 artist_regex = artist_regex.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_regex:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_regex})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "jiosaavn_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


# def melon():
# url = [
# "https://www.melon.com/search/song/index.htm?q=top&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=top&params%5Bsort%5D=date&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=1",
# "http://www.melon.com/search/song/index.htm?q=top&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=top&params%5Bsort%5D=date&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=51"]
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "melon_topchart.csv"
# if os.path.exists("melon_topchart.csv"):
# os.remove("melon_topchart.csv")
# for j in range(len(url)):
# browser.get(url[j])
# time.sleep(20)
# res = browser.page_source
# res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
# req_song_list = list()
# song_list = re.findall(r'class="fc_gray" title="(.*?)">', res, flags=re.DOTALL)
# artist = re.findall(r'<div id="artistName" class="ellipsis".*?class="fc_mgray">(.*?)</a>', res, re.DOTALL)
# # url_list = re.findall(r"<a.*?'web_song','SONG','SO','top','(.*?)'", res)
# # url_list = url[j]
# req_url_list = list()
# res_list = list()
# for i in range(len(song_list)):
# # req_url_list[i] = url_list
# # req_url_list[i] = "https://www.melon.com/song/detail.htm?songId=" + req_url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",") \
# .replace(" &", ",").replace('&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for k in range(len(feat_list)):
# if feat_list[k] in artist[i]:
# artist[i] = artist[i].partition(feat_list[k])[0]
# # if not url_list[i]:
# # url_list[i] = url[j]
# if artist[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": url[j]})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)


def musicme():
 url = ["https://www.musicme.com/#/classements-titres/electro-dance/",
 "https://www.musicme.com/#/classements-titres/electro-dance/2.html",
 "https://www.musicme.com/#/classements-titres/electro-dance/3.html",
 "https://www.musicme.com/#/classements-titres/electro-dance/4.html",
 "https://www.musicme.com/#/classements-titres/electro-dance/5.html",
 "https://www.musicme.com/#/classements-titres/electro-dance/6.html"]

 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "musicme1_topchart.csv"
 if os.path.exists("musicme1_topchart.csv"):
 os.remove("musicme1_topchart.csv")
 for j in range(len(url)):
 browser.get(url[j])
 time.sleep(20)
 browser.switch_to.frame(1)
 iframe_source = browser.page_source
 py_soup = bs(iframe_source, 'html.parser')
 body = py_soup.find('body')
 div_list1 = body.find_all('div', {"class": "track-title"})
 div_list1.pop(0)
 song_list = list()
 artist = list()
 for data in div_list1:
 song_list.append("") if data.getText() is None else song_list.append(data.getText())
 div_list2 = body.find_all('div', {"class": "track-artist"})
 div_list2.pop(0)
 for data in div_list2:
 new_str = data.getText().replace("/", ",")
 artist.append("") if new_str is None else artist.append(new_str)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 res_dict = dict()
 res_dict.update({"Title": str(song_list[i])})
 res_dict.update({"Artist": str(artist[i])})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": str(url[j])})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


def musicme1():
 url = ["https://www.musicme.com/#/classements-titres/variete-francaise/",
 "https://www.musicme.com/#/classements-titres/variete-francaise/2.html",
 "https://www.musicme.com/#/classements-titres/variete-francaise/3.html",
 "https://www.musicme.com/#/classements-titres/variete-francaise/4.html",
 "https://www.musicme.com/#/classements-titres/variete-francaise/5.html",
 "https://www.musicme.com/#/classements-titres/variete-francaise/6.html"]

 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "musicme_topchart.csv"
 if os.path.exists("musicme_topchart.csv"):
 os.remove("musicme_topchart.csv")
 for j in range(len(url)):
 browser.get(url[j])
 time.sleep(10)
 browser.switch_to.frame(1)
 iframe_source = browser.page_source
 py_soup = bs(iframe_source, 'html.parser')
 body = py_soup.find('body')
 div_list1 = body.find_all('div', {"class": "track-title"})
 div_list1.pop(0)
 song_list = list()
 artist = list()
 for data in div_list1:
 song_list.append("") if data.getText() is None else song_list.append(data.getText())
 div_list2 = body.find_all('div', {"class": "track-artist"})
 div_list2.pop(0)
 for data in div_list2:
 new_str = data.getText().replace(" /", ",")
 artist.append("") if new_str is None else artist.append(new_str)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 if artist[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url[j]})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


def recotop():
 url = "https://www.recotop.com/"
 browser.get(url)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 song_list = re.findall(
 r'<mat-card-title _ngcontent-c12="" class="track-title mat-card-title">(.*?)</mat-card-title>', res,
 flags=re.DOTALL)
 artist = re.findall(
 r'<mat-card-subtitle _ngcontent-c12="" class="track-sub mat-card-subtitle">(.*?)</mat-card-subtitle>', res,
 flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 if artist[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-US"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "recotop_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

 # def recochokuranking():
 url = "https://recochoku.jp/ranking/single/daily/"
 browser.get(url)
 browser.get(url)
 # time.sleep(30)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 album, artist, link = [], [], []
 soup_obj = bs(res, "html.parser").find("ul", {"class": "js-viewchange-wrap"})
 data_list = bs(str(soup_obj), "html.parser").findAll("div", {"class": "c-product-list__item"})
 for i in data_list:
 album.append(i.find("div", {"class": "c-product-list__title c-el"}).text)
 artist.append(i.find("div", {"class": "c-product-list__artist c-el"}).text)

 link.append('https://recochoku.jp' + i.find("a", {"class": "c-product-list__link"})['href'])
 # print(len(link))
 # print(len(album))
 # print(len(artist))
 res_list = list()
 for i in range(len(album)):
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Title": album[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": ""})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": link[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "recochoku_ranking_single_daily_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def shazam():
 url = "https://www.shazam.com/charts/top-200/japan"
 browser.get(url)
 time.sleep(30)
 while True:
 try:
 more_buttons = browser.find_element_by_class_name("shz-text-btn")
 more_buttons.click()
 except Exception:
 break
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 item_box = browser.find_elements_by_class_name('ellip')
 song_list = list()
 artist_list = list()
 url_list = list()
 item_box = item_box[0:400]
 for i in range(len(item_box)):
 if i % 2 == 0:
 song_list.append(item_box[i].text.encode('utf-8'))
 else:
 artist_list.append(item_box[i].text.encode('utf-8'))
 for i in range(len(song_list)):
 links = browser.find_elements_by_partial_link_text(song_list[i])
 for link in links:
 url_list.append(str(link.get_attribute("href")).replace('u', ''))
 req_url_list = re.findall(r'<div class="title" data-track-title="">.*?<a href="(.*?)"', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 if not req_url_list[i]:
 req_url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": req_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "shazam_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def soompi():
 url = "https://www.soompi.com/article/1383277wpp/red-velvet-maintains-lead-with-psycho-soompis-k-pop-music-chart-2020-february-week-3"
 browser.get(url)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'<td class="other"><span>(.*?)</span>', res, flags=re.DOTALL)
 further_artist = re.findall(r'<span>Artist/Band: </span>\s*(.*?)\s*</div>', res)
 artist_list.extend(further_artist)
 song_list = re.findall(r'<td class="title">\s*<span>(.*?)</span>', res, flags=re.DOTALL)
 further_songs = re.findall(r'<span class="item-title">\s*(.*?)\s*</span>', res)
 song_list.extend(further_songs)
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ko-KR"})
 res_dict.update({"Language": "ko"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "soompi_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def taazi():
 url = "http://taazi.com/music/top"
 browser.get(url)
 SCROLL_PAUSE_TIME = 0.5
 last_height = browser.execute_script("return document.body.scrollHeight")
 while True:
 browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(SCROLL_PAUSE_TIME)
 new_height = browser.execute_script("return document.body.scrollHeight")
 if new_height == last_height:
 break
 last_height = new_height
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 artist_list = re.findall(r'class="text-muted ng-binding".*?>(.*?)</a>', res, flags=re.DOTALL)
 artist_list = artist_list[0:100]
 song_list = re.findall(r'<div class="item-title text-ellipsis">\s*<a.*?>(.*?)</a>', res, flags=re.DOTALL)
 song_list = song_list[0:100]
 url_list = re.findall(r'class="ng-binding" href="(.*?)"', res, flags=re.DOTALL)
 url_list = url_list[0:100]
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})

 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ur-PK"})
 res_dict.update({"Language": "ur"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "taazi_topchart.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def genfm():
 url = ["http://www.987genfm.com/about/chart-ganas/?l=2", "http://www.987genfm.com/about/chart-ganas/2/?l=2",
 "http://www.987genfm.com/about/chart-ganas/3/?l=2", "http://www.987genfm.com/about/chart-ganas/4/?l=2",
 "http://www.987genfm.com/about/chart-ganas/5/?l=2"]

 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "987genfm_topchart.csv"
 if os.path.exists("987genfm_topchart.csv"):
 os.remove("987genfm_topchart.csv")
 for j in range(len(url)):
 browser.get(url[j])
 time.sleep(20)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<span class="song-title">(.*?)</span>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<span class="song-artist">(.*?)</span>', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 if artist[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "id-ID"})
 res_dict.update({"Language": "id"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url[j]})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


def europafm():
 url = "http://electrafm.com/top-10-mejores-canciones-musica-electronica/agosto-15-de-2016/"
 # res = urllib.urlopen(url).read()
 res = requests.get(url).text
 song_list, artist_list = [], []
 soup_obj = bs(res, "html.parser").findAll("span", {"class": "nombre-cancion color-n"})
 for i in soup_obj:
 song_list.append(re.findall(r'itemprop="name">(.*?) - <span', str(i), re.DOTALL)[0])
 artist_list.append(i.find("span", {"itemprop": "byArtist"}).text)
 res_list = list()
 for i in range(len(song_list)):
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": ""})
 res_dict.update({"Language": ""})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ''})
 res_list.append(res_dict)
 # print(res_list)
 # print(len(res_list))
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "itopchart_electrafm.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def hotmusicchartsmx():
 url = "https://www.hotmusiccharts.com/mx/itunes/100"
 browser.get(url)
 time.sleep(10)
 res = browser.page_source
 # res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'internal-artist.*?>(.*?)</a></div>', res, flags=re.DOTALL)
 song_list = re.findall(r'song-title.*?>(.*?)</a></div>', res)
 url_list = re.findall(r'song-title.*?href="(.*?)"', res, flags=re.DOTALL)
 # supported_url_list = re.findall(r"'outbound-artist','(.*?)'", res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 url_list[i] = "https://www.hotmusiccharts.com" + url_list[i]
 if not url_list[i]:
 url_list[i] = url
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ''})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "hot_music_charts_mx.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


def saavn_pk():
 url = "http://www.saavn.com/s/featured/urdu/Weekly_Top_Songs"
 browser.get(url)
 res = browser.page_source
 res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 artist_list = re.findall(r'<em class="meta">(.*?)</em>', res, flags=re.DOTALL)
 song_list = re.findall(r'<span class="title"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
 url_list = re.findall(r'<meta property="music:song" content="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist_regex = re.findall(r'class="".*?>(.*?)</a>', artist_list[i])
 artist_regex = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 artist_regex = artist_regex.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist_regex:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_regex})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ur-PK"})
 res_dict.update({"Language": "ur"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "saavan_pk.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list


print("**************************************************************")
radiole_func = radiole()
print("https://www.radiole.com/lista-radiole")
print(radiole_func)
print(len(radiole_func))
# print("**************************************************************")
# a_charts = acharts()
# print("https://acharts.co/france_singles_top_100")
# print(a_charts)
# print(len(a_charts))
print("**************************************************************")
tds_func = tds()
print("http://tds.sigletv.net/lista_sigle.php")
print(tds_func)
print(len(tds_func))
print("**************************************************************")
guitar_chord_world = guitarchordworld()
print("http://www.guitarchordworld.net/p/bangla-top-10-songs-of-month.html")
print(guitar_chord_world)
print(len(guitar_chord_world))
print("**************************************************************")
charts_in_france_1, charts_in_france_2, charts_in_france_3, charts_in_france_4 = chartsinfrance()
print("http://www.chartsinfrance.net/charts/singles.php,p1")
print(charts_in_france_1)
print(len(charts_in_france_1))
print(charts_in_france_2)
print(len(charts_in_france_2))
print(charts_in_france_3)
print(len(charts_in_france_3))
print(charts_in_france_4)
print(len(charts_in_france_4))
# print("**************************************************************")
# africa_charts = africacharts()
# print("http://www.africacharts.com/official-top-50-songs-nigeria/")
# print(africa_charts)
# print(len(africa_charts))
# print("**************************************************************")
billboard_japan = billboardjapan()
print("http://www.billboard-japan.com/charts/detail?a=hot100")
print(billboard_japan)
print(len(billboard_japan))
print("**************************************************************")
chart_surfer = chartsurfer()
print("https://www.chartsurfer.de/musik/airplay-charts-deutschland/charts")
print(chart_surfer)
print(len(chart_surfer))
print("**************************************************************")
classi_fiche = classifiche()
print("http://classifiche.mtv.it/hitlist-italia-classifica-singoli/cgmo2j")
print(classi_fiche)
print(len(classi_fiche))
print("****************************************************************")
# gaana_bengali = gaana()
# print("https://gaana.com/album/bengali-top-hits")
# print(gaana_bengali)
# print(len(gaana_bengali))
# print("****************************************************************")
# gaana_dj_bengali = gaanadjbengali()
# print("https://gaana.com/playlist/gaana-dj-bengali-top-20")
# print(gaana_dj_bengali)
# print(len(gaana_dj_bengali))
print("****************************************************************")
# gaon_chart = gaonchart()
# print("http://gaonchart.co.kr/main/section/chart/online.gaon")
# print(gaon_chart)
# print(len(gaon_chart))
# print("****************************************************************")
itopchart_children = itopchartchildren()
print("https://itopchart.com/it/it/top-songs/childrens-music/") # checkwhy data not present in out.csv
print(itopchart_children)
print(len(itopchart_children))
print("****************************************************************")
itopchart_christian = itopchartchristian()
print("https://itopchart.com/it/it/top-songs/christian-gospel/")
print(itopchart_christian)
print(len(itopchart_christian))
print("****************************************************************")
itopchart_french = itopchartfrench()
print("https://itopchart.com/fr/fr/top-songs/french-pop/")
print(itopchart_french)
print(len(itopchart_french))
print("****************************************************************")
# lets_sing_it = letssingit()
# print("https://www.letssingit.com/charts/japan-singles")
# print(lets_sing_it)
# print(len(lets_sing_it))
print("****************************************************************")
last_fm_page1, last_fm_page2 = lastfm()
print("https://www.last.fm/es/tag/rock+en+espanol/tracks")
print(last_fm_page1)
print(len(last_fm_page1))
print(last_fm_page2)
print(len(last_fm_page2))
print("****************************************************************")
# los_40 = los40()
# print("https://los40.com/lista40/")
# print(los_40)
# print(len(los_40))
# print("****************************************************************")
# maistocadas_electronicas = maistocadaselectronicas()
# print("https://maistocadas.mus.br/musicas-eletronicas/")
# print(maistocadas_electronicas)
# print(len(maistocadas_electronicas))
# print("****************************************************************")
# maistocadas_sartanejas = maistocadassartanejas()
# print("https://maistocadas.mus.br/musicas-sertanejas/")
# print(maistocadas_sartanejas)
# print(len(maistocadas_sartanejas))
print("****************************************************************")
# mix_1 = mix1()
# print("https://www.mix1.de/charts/partycharts.htm")
# print(mix_1)
# print(len(mix_1))
print("****************************************************************")
# mtv_de = mtvde()
# print("http://www.mtv.de/charts/c6mc86/single-top-100?expanded=true")
# print(mtv_de)
# print(len(mtv_de))
print("****************************************************************")
official_charts = officialcharts()
print("https://www.officialcharts.com/charts/")
print(official_charts)
print(len(official_charts))
print("****************************************************************")
oljo_func1, oljo_func2 = oljo()
print("https://www.oljo.de/radiochart_d/radio100.shtml/www.oljo.de/radiochart_d/radio41100.shtml")
print(oljo_func1)
print(len(oljo_func1))
print(oljo_func2)
print(len(oljo_func2))
print("****************************************************************")
# oricon_page1, oricon_page2, oricon_page3, oricon_page4, oricon_page5 = oricon()
# print("https://www.oricon.co.jp/rank/js/w/2018-07-23/")
# print(oricon_page1)
# print(len(oricon_page1))
# print(oricon_page2)
# print(len(oricon_page2))
# print(oricon_page3)
# print(len(oricon_page3))
# print(oricon_page4)
# print(len(oricon_page4))
# print(oricon_page5)
# print(len(oricon_page5))
print("*****************************************************************")
# raaga_func = raaga()
# print("https://www.raaga.com/tamil/top10")
# print(raaga_func)
# print(len(raaga_func))
print("****************************************************************")
radiomirchi_kannada = radiomirchikannada()
print("https://www.radiomirchi.com/more/kannada-top-20/")
print(radiomirchi_kannada)
print(len(radiomirchi_kannada))
print("****************************************************************")
radiomirchi_malayalam = radiomirchimalayalam()
print("https://www.radiomirchi.com/more/malayalam-top-20/")
print(radiomirchi_malayalam)
print(len(radiomirchi_malayalam))
print("****************************************************************")
radiomirchi_more = radiomirchimore()
print("https://www.radiomirchi.com/more/mirchi-top-20/")
print(radiomirchi_more)
print(len(radiomirchi_more))
print("****************************************************************")
radiomirchi_tamil = radiomirchitamil()
print("https://www.radiomirchi.com/more/tamil-top-20/")
print(radiomirchi_tamil)
print(len(radiomirchi_tamil))
print("****************************************************************")
radiomirchi_bangla = radiomirchibangla()
print("https://www.radiomirchi.com/more/bangla-top-10/")
print(radiomirchi_bangla)
print(len(radiomirchi_bangla))
print("****************************************************************")
# recochoku_single = recochokusingle()
# print("https://recochoku.jp/ranking/single/weekly/")
# print(recochoku_single)
# print(len(recochoku_single))
# print("****************************************************************")
# recochoku_weekly = recochokuweekly()
# print("https://recochoku.jp/genreranking/j-pop/weekly/")
# print(recochoku_weekly)
# print(len(recochoku_weekly))
print("****************************************************************")

rhapsody_func = rhapsody()
print("https://us.napster.com/chart/tracks")
print(rhapsody_func)
print(len(rhapsody_func))
print("****************************************************************")
# the_beat99 = thebeat99()
# print("http://www.thebeat99.com/ngt10/")
# print(the_beat99)
# print(len(the_beat99))
# print("****************************************************************")
top40_11 = top4011()
print("https://top40-charts.com/chart.php?cid=11")
print(top40_11)
try:
 print(len(top40_11))
except:
 print("0 length")
print("****************************************************************")
top40_43 = []
top40_43 = top4043()
print("https://top40-charts.com/chart.php?cid=43")
print(type(top40_43))
if(len(top40_43)!=0):
 print(len(top40_43))
print("****************************************************************")
urdu_top10 = urdutop10()
print("http://www.top10songs.org/best-urdu-songs-albums.html")
print(urdu_top10)
print(len(urdu_top10))
print("****************************************************************")
vagalume_func = vagalume()
print("https://www.vagalume.com.br/top100/musicas/geral")
print(vagalume_func)
print(len(vagalume_func))
# print("****************************************************************")
# gp_music = gpmusic()
# print("http://player.gpmusic.co/playlists/62413")
# print(gp_music)
# print(len(gp_music))
# # print("***************************************************************")
hot_music = hotmusic()
print("https://www.hotmusiccharts.com/th/itunes")
print(hot_music)
print(len(hot_music))
print("***************************************************************")
hot_music_charts = hotmusiccharts()
print("https://www.hotmusiccharts.com/ng/itunes")
print(hot_music_charts)
print(len(hot_music_charts))
# print("***************************************************************")
# hotchartmp3()
# print("http://hotcharts.ru/mp3/top/clicks/week/")
# print("***************************************************************")
# hungama_func = hungama()
# print("https://www.hungama.com/videos/explore/trending-videos-5318/")
# print(hungama_func)
# print(len(hungama_func))
print("****************************************************************")
hungama_bengali = hungamabengali()
print("https://www.hungama.com/all/latest-tracks-52/3355/")
print(hungama_bengali)
print(len(hungama_bengali))
print("***************************************************************")
# saavn_func = saavn()
# print("https://www.jiosaavn.com/featured/weekly-top-songs/Vzehd0ZQty4_")
# print(saavn_func)
# print(len(saavn_func))
# print("***************************************************************")
# jio_saavn = jiosaavn()
# print("https://www.jiosaavn.com/featured/weekly-top-songs")
# print(jio_saavn)
# print(len(jio_saavn))
# print("***************************************************************")
# melon()
# print(
# "https://www.melon.com/search/song/index.htm?q=top&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=top&params%5Bsort%5D=date&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=1")
print("***************************************************************")
# musicme()
# print("https://www.musicme.com/#/classements-titres/electro-dance/")
# print("***************************************************************")

# recotop_func = recotop()
# print("https://www.recotop.com/")
# print(recotop_func)
# print(len(recotop_func))
# print("****************************************************************")
# #recochoku_ranking = recochokuranking()
# print("https://recochoku.jp/ranking/single/daily/")
# print(recochoku_ranking)
# print(len(recochoku_ranking))
# print("***************************************************************")
# shazam_func = shazam()
# print("https://www.shazam.com/charts/top-200/japan")
# print(shazam_func)
# print(len(shazam_func))
# print("***************************************************************")
# soompi_func = soompi()
# print("https://www.soompi.com/article/1372795wpp/iu-maintains-no-1-with-blueming-soompis-k-pop-music-chart-2019-december-week-3")
# print(soompi_func)
# print(len(soompi_func))
# print("***************************************************************")
# taazi_func = taazi()
# print("https://taazi.com/music/top")
# print(taazi_func)
# print(len(taazi_func))
print("***************************************************************")
# genfm()
# print("http://www.987genfm.com/about/chart-ganas/?l=2")
# print("***************************************************************")
# europafm_func = europafm()
# print("https://www.europafm.com/listas-musicales/")
# print(europafm_func)
# print(len(europafm_func))
print("***************************************************************")
hot_music_charts_mx = hotmusicchartsmx()
print("https://www.hotmusiccharts.com/mx/itunes/100")
print(hot_music_charts_mx)
print(len(hot_music_charts_mx))
print("***************************************************************")
saavn_func_pk = saavn_pk()
print("https://www.jiosaavn.com/featured/weekly-top-songs/Vzehd0ZQty4_")
print(saavn_func_pk)
print(len(saavn_func_pk))

fout = open("out.csv", "a")
# for line in open("myradio.csv"):
# fout.write(line)
# os.remove("myradio.csv")
for line in open("radiole.csv"):
 fout.write(line)
os.remove("radiole.csv")
# for line in open("acharts.csv"):
# fout.write(line)
# os.remove("acharts.csv")
for line in open("tds.csv"):
 fout.write(line)
os.remove("tds.csv")
for line in open("guitarchordworld.csv"):
 fout.write(line)
os.remove("guitarchordworld.csv")
for line in open("chartsinfrance.csv"):
 fout.write(line)
os.remove("chartsinfrance.csv")
# for line in open("africacharts.csv"): #wrong title artist url fetched are not of that
# fout.write(line)
# os.remove("africacharts.csv")
# for line in open("gaana.csv"):
# fout.write(line)
# os.remove("gaana.csv")
for line in open("billboard_japan.csv"):
 fout.write(line)
os.remove("billboard_japan.csv")
for line in open("chartsurfer.csv"):
 fout.write(line)
os.remove("chartsurfer.csv")
for line in open("classifiche.csv"):
 fout.write(line)
os.remove("classifiche.csv")
# for line in open("gaana_dj_bengali.csv"):
# fout.write(line)
# os.remove("gaana_dj_bengali.csv")
# for line in open("gaonchart.csv"):
# fout.write(line)
# os.remove("gaonchart.csv")
# for line in open("itopchart_childrens.csv"): # checkwhy detailed url has supported url
# fout.write(line)
# os.remove("itopchart_childrens.csv")
for line in open("itopchart_christian.csv"):
 fout.write(line)
os.remove("itopchart_christian.csv")
for line in open("itopchart_french.csv"): # checkwhy detailed url has supported url
 fout.write(line)
os.remove("itopchart_french.csv")
# for line in open("japan_singles.csv"): #through crawzall
# fout.write(line)
# os.remove("japan_singles.csv")
for line in open("last_fm.csv"):
 fout.write(line)
os.remove("last_fm.csv")
# for line in open("los40.csv"):
# fout.write(line)
# os.remove("los40.csv")
# for line in open("maistocadas.csv"):
# fout.write(line)
# os.remove("maistocadas.csv")
# for line in open("maistocadas_sartanejas.csv"):
# fout.write(line)
# os.remove("maistocadas_sartanejas.csv")
# for line in open("mix_1.csv"):
# fout.write(line)
# os.remove("mix_1.csv")
# for line in open("mtv_topchart.csv"):
# fout.write(line)
# os.remove("mtv_topchart.csv")
for line in open("officialcharts.csv"):
 fout.write(line)
os.remove("officialcharts.csv")
for line in open("oljo.csv"):
 fout.write(line)
os.remove("oljo.csv")
# for line in open("oricon.csv"): //unscape_html entities are coming
# fout.write(line)
# os.remove("oricon.csv")
# for line in open("raaga.csv"):
# fout.write(line)
# os.remove("raaga.csv")
for line in open("radiomirchi_kannada.csv"):
 fout.write(line)
os.remove("radiomirchi_kannada.csv")
for line in open("radiomirchi_malayalam.csv"):
 fout.write(line)
os.remove("radiomirchi_malayalam.csv")
for line in open("radiomirchi_more.csv"):
 fout.write(line)
os.remove("radiomirchi_more.csv")
for line in open("radiomirchi_tamil.csv"):
 fout.write(line)
os.remove("radiomirchi_tamil.csv")
for line in open("radiomirchi_bangla.csv"):
 fout.write(line)
os.remove("radiomirchi_bangla.csv")
# for line in open("recochoku_single.csv"):
# fout.write(line)
# os.remove("recochoku_single.csv")
# for line in open("recochoku_weekly.csv"):
# fout.write(line)
# os.remove("recochoku_weekly.csv")
for line in open("rhapsody.csv"):
 fout.write(line)
os.remove("rhapsody.csv")
# for line in open("thebeat99.csv"):
# fout.write(line)
# os.remove("thebeat99.csv")
for line in open("top40_11.csv"):
 fout.write(line)
os.remove("top40_11.csv")
for line in open("top40_43.csv"):
 fout.write(line)
os.remove("top40_43.csv")
for line in open("urdu_top10.csv"):
 fout.write(line)
os.remove("urdu_top10.csv")
for line in open("vagalume.csv"):
 fout.write(line)
os.remove("vagalume.csv")
# for line in open("gpmusic_topchart.csv"):
# fout.write(line)
# os.remove("gpmusic_topchart.csv")
for line in open("hot_music_charts1_topchart.csv"):
 fout.write(line)
os.remove("hot_music_charts1_topchart.csv")
for line in open("hot_music_charts_topchart.csv"):
 fout.write(line)
os.remove("hot_music_charts_topchart.csv")
# for line in open("../venv/hotchart_mp3_topchart.csv"):
# fout.write(line)
# os.remove("../venv/hotchart_mp3_topchart.csv")
# for line in open("../venv/hungama_topchart.csv"):
# fout.write(line)
# os.remove("../venv/hungama_topchart.csv")
for line in open("hungama_bengali_topchart.csv"):
 fout.write(line)
os.remove("hungama_bengali_topchart.csv")
# for line in open("../venv/jiosaavn1_topchart.csv"):
# fout.write(line)
# os.remove("../venv/jiosaavn1_topchart.csv")
# for line in open("../venv/jiosaavn_topchart.csv"):
# fout.write(line)
# os.remove("../venv/jiosaavn_topchart.csv")
# for line in open("../venv/melon_topchart.csv"):
# fout.write(line)
# os.remove("../venv/melon_topchart.csv")
# for line in open("../venv/musicme1_topchart.csv"):
# fout.write(line)
# os.remove("../venv/musicme1_topchart.csv")
# for line in open("musicme_topchart.csv"):
# fout.write(line)
# os.remove("musicme_topchart.csv")
# for line in open("../venv/recotop_topchart.csv"):
# fout.write(line)
# os.remove("../venv/recotop_topchart.csv")
# for line in open("../venv/recochoku_ranking_single_daily_topchart.csv"):
# fout.write(line)
# os.remove("../venv/recochoku_ranking_single_daily_topchart.csv")
# for line in open("shazam_topchart.csv"): #run individual -fetching incorrect title and artist
# fout.write(line)
# os.remove("shazam_topchart.csv")
# for line in open("soompi_topchart.csv"):
# fout.write(line)
# os.remove("soompi_topchart.csv")
# for line in open("taazi_topchart.csv"): //run individual as we don't get all records here
# fout.write(line)
# os.remove("taazi_topchart.csv")
# for line in open("987genfm_topchart.csv"):
# fout.write(line)
# os.remove("987genfm_topchart.csv")
# for line in open("europafm_topchart.csv"):
# fout.write(line)
# os.remove("europafm_topchart.csv")
for line in open("hot_music_charts_mx.csv"):
 fout.write(line)
os.remove("hot_music_charts_mx.csv")
for line in open("saavan_pk.csv"):
 fout.write(line)
os.remove("saavan_pk.csv")
fout.close()
# #!/usr/bin/env python
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.common import exceptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# import csv
# from bs4 import BeautifulSoup as bs
# import requests
# import re
# from datetime import date
# from datetime import datetime
# import pandas as pd
# from selenium import webdriver
# import itertools
#
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url1 = 'https://gaana.com/playlist/gaana-dj-bengali-top-20'
# response = requests.get(url1)
# locale = "bn-BD"
# lang = "bn"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# # timeout =30
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url1)
# delay = 20
# # timeout =20
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # delay = 20
# try:
# WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/section[3]/ul[10]')))
# print("Page is ready!")
# except TimeoutException:
# print("Loading took too much time!")
# itembox1 = browser.find_elements(By.CLASS_NAME,'_row')
# # print(len(itembox1))
# # for i in itembox1:
# # print(i.text)
#
#
# for i in itembox1:
# WebDriverWait(browser, delay, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located((By.CLASS_NAME,'_tra')))
# songs = i.find_elements(By.CLASS_NAME,'_tra')
# for s in songs:
# print(s.text)
# data['Title'].append(s.text.strip())
# author = i.find_elements(By.CLASS_NAME, '_art')
# for a in author:
# print(a.text)
# data['Artist'].append(a.text.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url1)
# data['Supported Url'].append('')
# data['Url'].append(urllst)
# links = i.find_elements(By.CLASS_NAME,'_tra')
# for my_href in links:
# # print(my_href)
# link = my_href.get_attribute("href")
# print(link)
# data['Supported Url'].append(link)
# # # return res_list
# df = pd.DataFrame(data)
# df.to_csv('gaanaDJ_DJ_bengali_MTC.csv', index= False)
# # file_name = ' gaanaDJ_DJ_bengali_MTC.csv'
# # make_csv(file_name, data)


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://gaana.com/playlist/gaana-dj-bengali-top-20'
response = requests.get(url)
locale = "bn-BD"
lang = "bn"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': '_grp'})
urls= []
for each in acts:
 link = each.find_next('a', href=True)
 urls = link['href']
 title = each.find_next('a', {'class': '_tra t_over _plyCr'}).text.strip()[0:]
 artist = each.find_next('div', {'class': '_art t_over'}).text.strip()[0:]

 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://gaana.com'+ urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' gaanaDJ_DJ_bengali_MTC.csv'
make_csv(file_name, data)
# #!/usr/bin/env python
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.common import exceptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# import csv
# from bs4 import BeautifulSoup as bs
# import requests
# import re
# from datetime import date
# from datetime import datetime
#
# from selenium import webdriver
# import itertools
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# # chromedriver = Service("/usr/local/bin/chromedriver")
# # op = webdriver.ChromeOptions()
# # browser = webdriver.Chrome(service=chromedriver, options=op)
# # def gaana():
#
# # res = requests.get("https://gaana.com/album/bengali-top-hits").text
# # main_url = "https://gaana.com/album/bengali-top-hits"
# url = 'https://gaana.com/album/bengali-top-hits'
# response = requests.get(url)
# locale = "bn-BD"
# lang = "bn"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# # timeout =30
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url)
# delay = 20
# # timeout =20
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# delay = 20
# try:
# WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/section[3]/ul[10]')))
# print("Page is ready!")
# except TimeoutException:
# print("Loading took too much time!")
# itembox1 = browser.find_elements(By.CLASS_NAME,'list_data')
# # print(len(itembox1))
# # for i in itembox1:
# # print(i.text)
#
# for i in itembox1:
# songs = i.find_elements(By.CLASS_NAME,'_tra')
# for s in songs:
# print(s.text)
# data['Title'].append(s.text.strip())
# author = i.find_elements(By.CLASS_NAME, '_art')
# for a in author:
# print(a.text)
# data['Artist'].append(a.text.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# data['Supported Url'].append('')
# data['Url'].append(urllst)
# links = i.find_elements(By.CLASS_NAME,'_tra')[0:1]
# for my_href in links:
# # print(my_href)
# link = my_href.get_attribute("href")
# data['Supported Url'].append(link)
# # # return res_list
# file_name = ' gaana_bengali_MTC.csv'
# make_csv(file_name, data)

# def gaanadjbengali():
# res = requests.get("https://gaana.com/playlist/gaana-dj-bengali-top-20").text
# main_url = "https://gaana.com/playlist/gaana-dj-bengali-top-20"
# song_list = re.findall(r'<div class="track_npqitemdetail">\s*<span>(.*?)</span>', res, flags=re.DOTALL)
# artist_list = re.findall(r'<div class="track_npqitemdetail">.*?<a.*?>(.*?)</a>', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# if artist_list[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "bn-BD"})
# res_dict.update({"Language": "bn"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": main_url})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": ""})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "gaana_dj_bengali.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# # return res_list
import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://gaana.com/album/bengali-top-hits'
response = requests.get(url)
locale = "bn-BD"
lang = "bn"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': '_grp'})
urls= []
for each in acts:
 link = each.find_next('a', href=True)
 urls = link['href']
 title = each.find_next('a', {'class': '_tra t_over _plyCr'}).text.strip()[0:]
 artist = each.find_next('div', {'class': '_art t_over'}).text.strip()[0:]

 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://gaana.com'+ urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' gaana_bengali_MTC.csv'
make_csv(file_name, data)

# !/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import csv
import bs4
import requests
import re
from datetime import date
from datetime import datetime

from selenium import webdriver

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
url = "http://gaonchart.co.kr/main/section/chart/online.gaon"
res = requests.get(url).text
song_list = re.findall(r'<td class="subject">\s*<p.*?>(.*?)</p>', res, flags=re.DOTALL)
artist_list = re.findall(r'<p class="singer".*?>(.*?)<span class="bar">', res, flags=re.DOTALL)
res_list = list()
for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ko-KR"})
 res_dict.update({"Language": "ko"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url})
 res_list.append(res_dict)
res_list = res_list[0:100]
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "gaonchart_mtc.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# return res_list
# import csv
# import re
# import time
# import unicodedata
# import os
# from datetime import date
# from datetime import datetime
#
# from selenium import webdriver
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# # browser = webdriver.Firefox()
# chromedriver = "/usr/local/google/home/pritishc/Downloads/chromedriver"
# browser = webdriver.Chrome(executable_path=chromedriver)
#
#
# def genfm():
# url = ["http://www.987genfm.com/about/chart-ganas/?l=2", "http://www.987genfm.com/about/chart-ganas/2/?l=2",
# "http://www.987genfm.com/about/chart-ganas/3/?l=2", "http://www.987genfm.com/about/chart-ganas/4/?l=2",
# "http://www.987genfm.com/about/chart-ganas/5/?l=2"]
#
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "987genfm_topchart.csv"
# if os.path.exists("987genfm_topchart.csv"):
# os.remove("987genfm_topchart.csv")
# for j in range(len(url)):
# browser.get(url[j])
# time.sleep(20)
# res = browser.page_source
# res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
# song_list = re.findall(r'<span class="song-title">(.*?)</span>', str(res), flags=re.DOTALL)
# artist = re.findall(r'<span class="song-artist">(.*?)</span>', str(res), flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for k in range(len(feat_list)):
# if feat_list[k] in artist[i]:
# artist[i] = artist[i].partition(feat_list[k])[0]
# if artist[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "id-ID"})
# res_dict.update({"Language": "id"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": url[j]})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": ""})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# genfm()


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')


from selenium import webdriver
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import os
import unicodedata
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))

now = datetime.now()
locale = "id-ID"
lang = "id"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url = 'https://www.melon.com/chart/week/index.htm'
url = 'http://www.987genfm.com/about/chart-ganas/?l=2'
# , "http://www.987genfm.com/about/chart-ganas/2/?l=2",
# # "http://www.987genfm.com/about/chart-ganas/3/?l=2", "http://www.987genfm.com/about/chart-ganas/4/?l=2",
# # "http://www.987genfm.com/about/chart-ganas/5/?l=2"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)

# for j in range(len(url)):
 # timeout = 20
browser.get(url)
delay = 1
timeout =20
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/section[3]/div/div/div/div')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.CLASS_NAME,'col-lg-12')
print(len(itembox))
for i in itembox:
 songs = i.find_elements(By.CLASS_NAME,'education-item__title')
 for s in songs:
 # song = s.get_attribute('title')
 data['Title'].append(s.text.strip())
 try:
 WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'education-item__category')))
 author = i.find_elements(By.CLASS_NAME, 'education-item__category')
 except:
 pass
 for a in author:
 # artist = a.get_attribute('title')[:-8]
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('')
 data['Url'].append(urllst)
 links = i.find_elements(By.CLASS_NAME,'video-trigger color-gen')
 x = 0
 for my_href in links:
 link = my_href.get_attribute('href')
 data['Supported Url'].append(link)


file_name = ' GENFM_MTC.csv'
make_csv(file_name, data)
#!/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import re
from datetime import datetime
from datetime import date
import csv
from selenium import webdriver

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# browser = webdriver.Firefox()

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)

url = "https://itopchart.com/it/it/top-songs/christian-gospel/"
browser.get(url)
text = browser.page_source
artist_list = re.findall(r'<div class="artist">(.*?)</div>', text, flags=re.DOTALL) # CHANGE REGEX
song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', text, flags=re.DOTALL) # CHANGE REGEX
url_list = re.findall(r'<a class="item_name" href="(.*?)"', text, flags=re.DOTALL)
res_list = []

for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = {}
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": url_list[i]})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "itopchart_christian.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import unicodedata
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
url = "http://player.gpmusic.co/playlists/62413"
browser.get(url)
time.sleep(20)
res = browser.page_source
res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
song_list, artist_list = [], []
soup_obj = bs(res, "html.parser").findAll("li", {"class": "tile track extended ui-draggable ui-draggable-handle"})
for i in soup_obj:
 song_list.append(i.find("span", {"class": "title"}).text)
 artist_list.append(i.find("span", {"class": "artist"}).text)
res_list = list()
for i in range(len(song_list)):
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": ""})
 res_dict.update({"Locale": "bn-BD"})
 res_dict.update({"Language": "bn"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "gpmusic_topchart.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# return res_list

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import os
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time
import unicodedata


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = ["http://hotcharts.ru/mp3/top/clicks/week/", "http://hotcharts.ru/mp3/top/clicks/week/2",
 "http://hotcharts.ru/mp3/top/clicks/week/3", "http://hotcharts.ru/mp3/top/clicks/week/4"]
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "hotchart_mp3_topchart.csv"
if os.path.exists("hotchart_mp3_topchart.csv"):
 os.remove("hotchart_mp3_topchart.csv")
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
for j in range(len(url)):
 browser.get(url[j])
 time.sleep(20)
 res = browser.page_source
 # res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
 req_song_list = list()
 song_list = re.findall(r'<div class="song_title visible">.*?</a>.*?<span.*?>(.*?)</span>', res,
 flags=re.DOTALL)
 artist = re.findall(r'<div class="song_title visible">.*?<span.*?>(.*?)</span>', res, flags=re.DOTALL)
 url_list = re.findall(r'<div class="song_title visible">.*?</a>.*?<a href="(.*?)"', res,
 flags=re.DOTALL)
 # print(len(song_list))
 # print(len(artist))
 # print(len(url_list))
 # print(url_list)
 # res_list = list()
 res_list = []
 for i in range(len(song_list)):
 url_list[i] = "http://hotcharts.ru" + url_list[i]
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 if not url_list[i]:
 url_list[i] = url[j]
 if artist[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ru-RU"})
 res_dict.update({"Language": "ru"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.hotmusiccharts.com/mx/itunes/100'
response = requests.get(url)
locale = "es-MX"
lang = "es"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('td', {'class': 'details'})
urls= []
for each in acts:
 title = each.find_next('div').text.strip()
 artist = each.find_next('div').find_next('div').text.strip()
 link = each.find_next('a', href=True).find_next('a', href=True)
 urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://www.hotmusiccharts.com'+ urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' itunes_mexico_MTC.csv'
make_csv(file_name, data)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = "https://www.hungama.com/videos/explore/trending-videos-5318/"
res = requests.get(url).text
song_list = re.findall(r'<div class="leftbox">\s*<a.*?>(.*?)</a>', res, flags=re.DOTALL)
res_list = list()
url_list = re.findall(r'<div class="leftbox">\s*<a.*?href="(.*?)"', res, flags=re.DOTALL)
# for i in range(len(url_list)):
# url_regex = url_list[i].partition('<a id="pajax_a" href="')
# url_list[i] = url_regex[2]
for i in range(len(url_list)):
 sub_res = requests.get(url_list[i]).text
 artist = re.search(r'<span>Singers:</span>(.*?)<br>', sub_res, flags=re.DOTALL)
 if not artist:
 artist1 = re.search(r'<span>Artist:</span>(.*?)<br>', sub_res, flags=re.DOTALL)
 if not artist1:
 artist = ""
 else:
 artist_regex = re.findall(r'<a.*?>(.*?)</a>', artist1.group(1), flags=re.DOTALL)
 artist = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 else:
 artist_regex = re.findall(r'<a.*?>(.*?)</a>', artist.group(1), flags=re.DOTALL)
 artist = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
 artist = artist.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist:
 artist = artist.partition(feat_list[j])[0]
 if not url_list[i]:
 url_list[i] = url
 if artist:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-IN"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Tag": "India"})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "hungama_topchart.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# return res_list

#!/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import csv
import bs4
import requests
import re
from datetime import date
from datetime import datetime

from selenium import webdriver

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# browser = webdriver.Firefox()


def los40():
 data = requests.get('https://los40.com/lista40/').text
 soup = bs4.BeautifulSoup(data, "html.parser")
 main_url = "https://los40.com/lista40/"
 element = soup.find_all('div', attrs={'class': re.compile(r'.*info_grupo.*')})
 feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
 song_list = re.findall(r'<div class="info_grupo">\s*<p>(.*?)</p>', str(element))
 res_list = list()
 artist_list = re.findall(r'<h4>(.*?)</h4>', str(element))
 req_artist_list = list()
 supported_url_list = list()
 for i in range(len(artist_list)):
 artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist_list[i])
 detail_page = re.search(r'<a href="(.*?)"', artist_list[i])
 if not artist_regex:
 req_artist_list.append(artist_list[i])
 else:
 req_artist_list.append(artist_regex.group(1))
 if not detail_page:
 supported_url_list.append("")
 else:
 supported_url_list.append("https://los40.com" + detail_page.group(1))
 req_url_list = list()
 url_list = re.findall(r'<li><a title="votar" class="votar login_votar".*?>(.*?)<span class="button_more".*?>', data,
 flags=re.DOTALL)
 for i in range(len(url_list)):
 url_regex = re.search(r"<a href='(.*?)'", url_list[i])
 if not url_regex:
 req_url_list.append("")
 else:
 req_url_list.append(url_regex.group(1))
 for i in range(len(artist_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(";", ", ")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not supported_url_list[i]:
 supported_url_list[i] = main_url
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": req_url_list[i]})
 res_dict.update({"Url": supported_url_list[i]})
 res_list.append(res_dict)
 csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
 csv_file = "los40.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

los40()
# website is down
import re
from datetime import datetime
from datetime import date
from selenium import webdriver
import csv

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = days[wd]
day_date_time = day + "_" + str(date) + "_" + current_time
chromedriver = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(executable_path=chromedriver)
# browser = webdriver.Firefox()
url = "https://www.letssingit.com/charts/japan-singles"
# res = urllib.urlopen(url).read()
browser.get(url)
res = browser.page_source
# res = requests.get(url).text
artist_list = re.findall(r'class="high_profile".*?<a href=.*?>(.*?)</a>', str(res), re.DOTALL)
song_list = re.findall(r'class="high_profile">(.*?)</a>', str(res), re.DOTALL)
url_list = re.findall(r'class="high_profile".*?<a href="(.*?)".*?</a>', str(res), re.DOTALL)

for i in range(len(song_list)):
 song_list[i] = str(song_list[i]).replace(' lyrics', '').replace(', lyrics', '')
# print(artist_list)
# print(song_list)
# print(url_list)
# print(len(artist_list))
# print(len(song_list))
# print(len(url_list))

res_list = list()
for i in range(len(artist_list)):
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url', 'Url']
csv_file = "japan_singles.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()

#website is not opening
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
import re
from datetime import datetime
from datetime import date
from selenium import webdriver
import csv
import urllib.request
import requests

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = days[wd]
day_date_time = day + "_" + str(date) + "_" + current_time
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# browser = webdriver.Firefox()
url = "https://www.letssingit.com/charts/japan-singles"
# res = urllib.request.urlopen(url).read()
browser.get(url)
res = browser.page_source
# res = requests.get(url).text
artist_list = re.findall(r'class="high_profile".*?<a href=.*?>(.*?)</a>', str(res), re.DOTALL)
song_list = re.findall(r'class="high_profile">(.*?)</a>', str(res), re.DOTALL)
url_list = re.findall(r'class="high_profile".*?<a href="(.*?)".*?</a>', str(res), re.DOTALL)

for i in range(len(song_list)):
 song_list[i] = str(song_list[i]).replace(' lyrics', '').replace(', lyrics', '')
# print(artist_list)
# print(song_list)
# print(url_list)
# print(len(artist_list))
# print(len(song_list))
# print(len(url_list))

res_list = list()
for i in range(len(artist_list)):
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url', 'Url']
csv_file = "japan_singles.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import unicodedata
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://lirik.kapanlagi.com/top/100weekly/'
response = requests.get(url)
locale = "id-ID"
lang = "id"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
# soup = bs(response.text, 'html.parser')
#
# acts = soup.find_all('div', {'class': 'list-lt clearfix'})
# urls= []
# for each in acts:
# title = each.find_next('div', {'class': 'li-artist'}).find_next('a').text.strip()
# artist = each.find_next('div', {'class': 'li-artist'}).find_next('div', {'class': 'li-artist'}).find_next('a').text.strip()
# link = each.find_next('a', href=True)
# urls = link['href']
# data['Title'].append(title.strip())
# data['Artist'].append(artist.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# data['Supported Url'].append(urls)
# data['Url'].append(urllst)
# # print(f'{title}\n{artist}\n{urls}\n\n')
timeout =30
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
res = browser.page_source
delay = 10
timeout =20
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'lirik-list')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.XPATH,'//*[@id="lirik-list"]/li ')
print(len(itembox))
# songs = re.findall(r'<div class ="ellip">.*?</div>',str(res), flags = re.DOTALL)
# print(songs)
for i in itembox:
 songs = i.find_elements(By.XPATH,'//*[@id="lirik-list"]/li/div/div[4]')
 author = i.find_elements(By.XPATH, '//*[@id="lirik-list"]/li/div/div[3]')
 links = i.find_elements(By.XPATH, '/html/body/center/div/div[2]/div[11]/div[2]/ul/li/div/div[4]/a')
for my_href in links:
 link = my_href.get_attribute("href")
 data['Supported Url'].append(link)

for s in songs:
 print(s.text)
 data['Title'].append(s.text.strip())
for a in author:
 print(a.text)
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 # data['Supported Url'].append('')
 data['Url'].append(urllst)


file_name = ' kapanLAGI_ID_MTC.csv'
make_csv(file_name, data)

import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.kboing.com.br/musicas/top-musicas/'
response = requests.get(url)
locale = "pt-BR"
lang = "pt"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'top_block'})
urls= []
for each in acts:
 title = each.find_next('a').text.strip()
 artist = each.find_next('a').find_next('a').text.strip()
 link = each.find_next('a', href=True).find_next('a', href=True)
 urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://www.kboing.com.br' +urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' kboing_BR_MTC.csv'
make_csv(file_name, data)


import re
import time
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url = 'https://www.oricon.co.jp/rank/js/w/'
# response = requests.get(url)
# locale = "jp-JP"
# lang = "jp"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# soup = bs(response.text, 'html.parser')
#
# acts = soup.find_all('section', {'class': 'box-rank-entry'})
# urls= []
# for each in acts:
# link = each.find_next('a', href=True)
# urls = link['href']
# title = each.find_next('h2', {'class': 'title'}).text.strip()
# artist = each.find_next('p', {'class': 'name'}).text.strip()
#
# data['Title'].append(title.strip())
# data['Artist'].append(artist.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# data['Supported Url'].append('https://www.oricon.co.jp/rank/js/w/'+ urls)
# data['Url'].append(urllst)
# # print(f'{title}\n{artist}\n{urls}\n\n')
#
# file_name = 'ORICON_MTC.csv'
# make_csv(file_name, data)
data = requests.get('https://los40.com/lista40/').text
soup = BeautifulSoup(data, "html.parser")
main_url = "https://los40.com/lista40/"
element = soup.find_all('div', attrs={'class': re.compile(r'.*info_grupo.*')})
song_list = re.findall(r'<div class="info_grupo">\s*<p>(.*?)</p>', str(element))
res_list = list()
artist_list = re.findall(r'<h4>(.*?)</h4>', str(element))
req_artist_list = list()
supported_url_list = list()
for i in range(len(artist_list)):
 artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist_list[i])
 detail_page = re.search(r'<a href="(.*?)"', artist_list[i])
 if not artist_regex:
 req_artist_list.append(artist_list[i])
 else:
 req_artist_list.append(artist_regex.group(1))
 if not detail_page:
 supported_url_list.append("")
 else:
 supported_url_list.append("https://los40.com" + detail_page.group(1))
req_url_list = list()
url_list = re.findall(r'<li><a title="votar" class="votar login_votar".*?>(.*?)<span class="button_more".*?>', data,
 flags=re.DOTALL)
for i in range(len(url_list)):
 url_regex = re.search(r"<a href='(.*?)'", url_list[i])
 if not url_regex:
 req_url_list.append("")
 else:
 req_url_list.append(url_regex.group(1))
for i in range(len(artist_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(";", ", ")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 if not supported_url_list[i]:
 supported_url_list[i] = main_url
 if req_artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "es-419"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": ""})
 res_dict.update({"Supported Url": req_url_list[i]})
 res_dict.update({"Url": supported_url_list[i]})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "los40.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import unicodedata
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
res = requests.get("https://maistocadas.mus.br/musicas-eletronicas/").text
soup = BeautifulSoup(res, "html.parser")
main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
main_url = re.search(r'content=[\'"]?([^\'" >]+)', str(main_url))
song_list = re.findall(r'<SPAN class="musicas" itemprop="name">(.*?)</SPAN>', res)
artist_list = re.findall(r'<span class="artista" itemprop="byArtist">\s*(.*?)\s*</span>', res)
# for i in range(len(artist_list)):
# if "</a>" in artist_list[i]:
# artist_list[i] = re.findall(r'<a.*?>(.*?)</a>', artist_list[i])
# for i in range(len(artist_list)):
# if not isinstance(artist_list[i], str) and len(artist_list[i]) == 1:
# artist_list[i] = ", ".join(artist_list[i])
# if not isinstance(artist_list[i], str) and len(artist_list[i]) == 2:
# artist_list[i] = artist_list[i][0] + " and " + artist_list[i][1]
# url = re.findall(r'<span class="foto">(.*?)</span>', res)
# url_list = list()
# for i in range(len(url)):
# match = re.search(r'href=[\'"]?([^\'" >]+)', url[i])
# match = match.group(1)
# if main_url.group(1)[0:26] not in match:
# match = main_url.group(1)[0:26] + match
# url_list.append(match)
res_list = list()
for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(',#8211;', '').replace("&#8211;", "").replace("&#8211; ",
 "").strip()
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace(
 str(i + 1), "").replace(". ", "").replace(str(i + 2), "").replace("&#8211;", "-").replace("&#8217;",
 "").strip()
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 # if not url_list[i]:
 # url_list[i] = "https://maistocadas.mus.br/musicas-eletronicas/"
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": "https://maistocadas.mus.br/musicas-eletronicas/"})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "maistocadas.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# return res_list

# ##!/usr/bin/env python
# import csv
# import os
# import re
# from datetime import date
# from datetime import datetime
# from selenium import webdriver
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# # browser = webdriver.Firefox()
# chromedriver = "/usr/local/google/home/pritishc/Downloads/chromedriver"
# browser = webdriver.Chrome(executable_path=chromedriver)
# url = "https://www.melon.com/chart/week/index.htm"
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "../venv/melon_topchart.csv"
#
# if os.path.exists("../venv/melon_topchart.csv"):
# os.remove("../venv/melon_topchart.csv")
#
# browser.get(url)
# song_list = browser.find_elements_by_class_name('ellipsis.rank01 > span > a')
#
# for i in range(len(song_list)):
# song_list[i] = song_list[i].get_attribute('href').split(',')[1].split(')')[0]
# song_list[i] = 'https://www.melon.com/song/detail.htm?songId=' + song_list[i]
#
# res_list = []
#
# for song in song_list:
# browser.get(song)
# title = browser.find_element_by_class_name('song_name').text
# artist = browser.page_source
# artist = re.findall('artistName = .*', artist)[0].split('"')[1]
# res_dict = dict()
# res_dict.update({"Title": title})
# res_dict.update({"Artist": artist})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": song})
# res_list.append(res_dict)
#
# browser.quit()
# csv_file = "melon.csv"
#
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
#
# for data in res_list:
# writer.writerow(data)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')


from selenium import webdriver
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import os
import unicodedata
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))

now = datetime.now()
locale = "ko-KR"
lang = "ko"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Entity Type': [],
}
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.melon.com/chart/week/index.htm'
entity_type = '/music/recording'
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
try:
 # for j in range(len(url)):
 # timeout = 20
 browser.get(url)
 delay = 1
 timeout =20
 try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lst50"]')))
 print("Page is ready!")
 except TimeoutException:
 print("Loading took too much time!")
 itembox = browser.find_elements(By.CLASS_NAME,'lst50')
 # print(len(itembox))
 for i in itembox:
 songs = i.find_elements(By.XPATH,'//*[@id="lst50"]/td[6]/div/div/div[1]/span/a')
 try:
 WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[2]/a')))
 author = i.find_elements(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[2]/a')
 links = ''
 except:
 pass

 for s in songs:
 song = s.get_attribute('title')
 data['Title'].append(song.strip())
 for a in author:
 artist = a.get_attribute('title')[:-8]
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('')
 data['Entity Type'].append(entity_type)

 # link = my_href.get_attribute("href")
 data['Supported Url'].append(links)
except exceptions.StaleElementReferenceException:
 print('stalemateexception bro!!')
 pass
#
file_name = ' MELON_MTC.csv'
make_csv(file_name, data)

# import re
# import csv
# import unicodedata
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from datetime import datetime
# from datetime import date
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# print(day_date_time)
#
# file_csv = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + "mtvde.org.csv"
# csv_file = open(file_csv, 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(
# ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url', 'url'])
# day_date_time
# locale = "de-DE"
# lang = "de"
# tag = ""
# MainUrl = ""
# supp_url = ""
#
# chromedriver = "/usr/local/google/home/pritishc/Downloads/chromedriver"
# browser = webdriver.Chrome(executable_path=chromedriver)
# # browser = webdriver.Firefox()
# url = "http://www.mtv.de/charts/c6mc86/single-top-100?expanded=true"
# browser.get(url)
# while True:
# try:
# time.sleep(5)
# more_buttons = browser.find_element_by_css_selector(".btn-border-dark.float-center.loadMoreBtn")
# more_buttons.click()
# except Exception:
# break
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# soup = BeautifulSoup(res, 'html.parser')
# num = 1
# for items_sk in soup.find_all(class_='chartItemTitle'):
# artist = items_sk.find(class_='videoTitle').text
# print(artist)
# try:
# link = items_sk.find('a')['href']
# print(link)
# except Exception as e:
# link = "http://www.mtv.de/charts/c6mc86/single-top-100?expanded=true"
# print(link)
# try:
# album = items_sk.find(class_='artist').text
# print(album)
# print("_____________________________")
# except Exception as e:
# album = re.sub('<.*>', '', str(album))
# csv_writer.writerow([artist, album, day_date_time, locale, lang, tag, MainUrl, supp_url, link])


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://mtv.marsl.net/demo/showdbcharts.php?c=4'
response = requests.get(url)
locale = "de-DE"
lang = "de"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'charts-marslnet'})
urls= []
for each in acts:
 title = each.find_next('div', {'class': 'cmn-title'}).text.strip()
 artist = each.find_next('div', {'class': 'cmn-artist'}).text.strip()
 link = each.find_next('a', href=True)
 # urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append(link)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' MTV_DE_MTC.csv'
make_csv(file_name, data)

#!/usr/bin/env python
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.common import exceptions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# import csv
# from bs4 import BeautifulSoup
# import requests
# import time
# import re
# from datetime import date
# from datetime import datetime
# from selenium import webdriver
# import itertools
#
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# url = 'https://www.mix1.de/charts/partycharts.htm'
# browser.get(url)
# time.sleep(20)
# res = browser.page_source
# # res = requests.get('https://www.mix1.de/charts/partycharts.htm').text
# song_list = re.findall(r'charts-second-child desktop.*?<a.*?>(.*?)</a>', str(res), re.DOTALL)
# artist_list = re.findall(r'charts-second-child desktop.*?charts-single-interpret">(.*?)</div>', str(res), re.DOTALL)
# url_list = re.findall(r'charts-second-child desktop.*?<a href="(.*?)"', str(res), re.DOTALL)
# supported_url = re.findall(r'charts-second-child desktop.*?</i>\s*<a href="(.*?)"', str(res), re.DOTALL)
# res_list = []
# for i in range(len(artist_list)):
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",") \
# .replace(" And", ",").replace(" &", ",").replace('&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": str(artist_list[i]).strip()})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "de-DE"})
# res_dict.update({"Language": "de"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": supported_url[i]})
# res_dict.update({"Url": url_list[i]})
# res_list.append(res_dict)
# res_list = res_list[0:50]
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "mix_1.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
 # return res_list
# import re
# import csv
# import unicodedata
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from datetime import datetime
# from datetime import date
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# print(day_date_time)
#
# file_csv = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + "mtvde.org.csv"
# csv_file = open(file_csv, 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(
# ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url', 'url'])
# day_date_time
# locale = "de-DE"
# lang = "de"
# tag = ""
# MainUrl = ""
# supp_url = ""
#
# chromedriver = "/usr/local/google/home/pritishc/Downloads/chromedriver"
# browser = webdriver.Chrome(executable_path=chromedriver)
# # browser = webdriver.Firefox()
# url = "http://www.mtv.de/charts/c6mc86/single-top-100?expanded=true"
# browser.get(url)
# while True:
# try:
# time.sleep(5)
# more_buttons = browser.find_element_by_css_selector(".btn-border-dark.float-center.loadMoreBtn")
# more_buttons.click()
# except Exception:
# break
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# soup = BeautifulSoup(res, 'html.parser')
# num = 1
# for items_sk in soup.find_all(class_='chartItemTitle'):
# artist = items_sk.find(class_='videoTitle').text
# print(artist)
# try:
# link = items_sk.find('a')['href']
# print(link)
# except Exception as e:
# link = "http://www.mtv.de/charts/c6mc86/single-top-100?expanded=true"
# print(link)
# try:
# album = items_sk.find(class_='artist').text
# print(album)
# print("_____________________________")
# except Exception as e:
# album = re.sub('<.*>', '', str(album))
# csv_writer.writerow([artist, album, day_date_time, locale, lang, tag, MainUrl, supp_url, link])


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://mtv.marsl.net/demo/showdbcharts.php?c=4'
response = requests.get(url)
locale = "de-DE"
lang = "de"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'charts-marslnet'})
urls= []
for each in acts:
 title = each.find_next('div', {'class': 'cmn-title'}).text.strip()
 artist = each.find_next('div', {'class': 'cmn-artist'}).text.strip()
 link = each.find_next('a', href=True)
 # urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append(link)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' MTV_DE_MTC.csv'
make_csv(file_name, data)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import os
import unicodedata


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url = "https://www.recotop.com/"
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url)
# res = browser.page_source
# res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
# song_list = re.findall(
# r'<mat-card-title _ngcontent-c12="" class="track-title mat-card-title">(.*?)</mat-card-title>', res,
# flags=re.DOTALL)
# artist = re.findall(
# r'<mat-card-subtitle _ngcontent-c12="" class="track-sub mat-card-subtitle">(.*?)</mat-card-subtitle>', res,
# flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# if artist[i]:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "en-US"})
# res_dict.update({"Language": "en"})
# res_dict.update({"Tag": ""})
# res_dict.update({"Main Url": url})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": ""})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "recotop_topchart.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list
 #
 # # def recochokuranking():
url = "https://recochoku.jp/ranking/single/daily/"
browser.get(url)
# time.sleep(30)
res = browser.page_source
res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
album, artist, link = [], [], []
soup_obj = bs(res, "html.parser").find("ul", {"class": "js-viewchange-wrap"})
data_list = bs(str(soup_obj), "html.parser").findAll("div", {"class": "c-product-list__item"})
for i in data_list:
 album.append(i.find("div", {"class": "c-product-list__title c-el"}).text)
 artist.append(i.find("div", {"class": "c-product-list__artist c-el"}).text)

 link.append('https://recochoku.jp' + i.find("a", {"class": "c-product-list__link"})['href'])
# print(len(link))
# print(len(album))
# print(len(artist))
res_list = list()
for i in range(len(album)):
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Title": album[i]})
 res_dict.update({"Artist": artist[i]})
 res_dict.update({"Extraction Time": ""})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": link[i]})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "recochoku_ranking_single_daily_topchart.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# return res_list

#!/usr/bin/env python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import re
import requests
from datetime import datetime
from datetime import date
import csv
from selenium import webdriver
from bs4 import BeautifulSoup as soup

# import HTMLParser

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# browser = webdriver.Firefox()
#
# res = urllib.urlopen("https://maistocadas.mus.br/musicas-sertanejas/").read()
res = requests.get("https://maistocadas.mus.br/musicas-sertanejas/").text
soup = soup(res, "html.parser")
main_url = soup.find('meta', attrs={'property': re.compile(r'.*og:url.*')})
main_url = re.search(r'content=[\'"]?([^\'" >]+)', str(main_url))
song_list = re.findall(r'<SPAN class="musicas" itemprop="name">(.*?)</SPAN>', res, flags=re.DOTALL)
artist_list = re.findall(r'<span class="artista" itemprop="byArtist">(.*?)</span>', res, flags=re.DOTALL)
res_list = list()
for i in range(len(artist_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace(',#8211;', '').replace("&#8211; ", "")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace(str(i + 1),
 "").replace(
 "&#8211;", "-").replace(". ", "")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 # print(len(song_list))
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": "https://maistocadas.mus.br/musicas-sertanejas/"})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']

csv_file = "maistocadas_sartanejas.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
#
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import time
# import itertools
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
#
# # url = "https://www.shazam.com/charts/top-200/japan"
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# # browser.get(url)
# # time.sleep(30)
# # while True:
# # try:
# # more_buttons = browser.find_element(By.CLASS_NAME, "shz-text-btn")
# # more_buttons.click()
# # except Exception:
# # break
# # res = browser.page_source
# # # res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# # item_box = browser.find_elements(By.CLASS_NAME, 'ellip')
# # song_list = list()
# # artist_list = list()
# # url_list = list()
# # item_box = item_box[0:400]
# # for i in range(len(item_box)):
# # if i % 2 == 0:
# # song_list.append(item_box[i].text.encode('utf-8'))
# # else:
# # artist_list.append(item_box[i].text.encode('utf-8'))
# # for i in range(len(song_list)):
# # links = browser.find_elements(By.PARTIAL_LINK_TEXT, song_list[i])
# # for link in links:
# # url_list.append(str(link.get_attribute("href")).replace('u', ''))
# # req_url_list = re.findall(r'<div class="title" data-track-title="">.*?<a href="(.*?)"', str(res), flags=re.DOTALL)
# # res_list = list()
# # for i in range(len(song_list)):
# # for j in range(len(feat_list)):
# # if feat_list[j] in artist_list[i]:
# # artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# # artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# # ",").replace(
# # '&#034;', '"').replace("&#039;", "'")
# # song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# # if not req_url_list[i]:
# # req_url_list[i] = url
# # if artist_list[i]:
# # res_dict = dict()
# # res_dict.update({"Title": song_list[i]})
# # res_dict.update({"Artist": artist_list[i]})
# # res_dict.update({"Extraction Time": day_date_time})
# # res_dict.update({"Locale": "ja-JP"})
# # res_dict.update({"Language": "ja"})
# # res_dict.update({"Tag": ""})
# # res_dict.update({"Main Url": ""})
# # res_dict.update({"Supported Url": ""})
# # res_dict.update({"Url": req_url_list[i]})
# # res_list.ap
# pend(res_dict)
# # csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# # 'Url']
# # csv_file = "shazam_topchart.csv"
# # with open(csv_file, 'w') as csvfile:
# # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# # writer.writeheader()
# # for data in res_list:
# # writer.writerow(data)
# # return res_list
# url = 'https://www.shazam.com/charts/top-200/japan'
# # url= 'http://schema.org/MusicPlaylist'
# response = requests.get(url)
#
# locale = "it-IT"
# lang = "IT"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# timeout =30
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url)
# res = browser.page_source
# delay = 1
# timeout =20
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #
# # try:
# # WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'tracks-container')))
# # print("Page is ready!")
# # except TimeoutException:
# # print("Loading took too much time!")
# # itembox = browser.find_elements(By.CLASS_NAME,'track ')
# # print(len(itembox))
# songs = re.findall(r'<div class ="ellip">.*?</div>',str(res), flags = re.DOTALL)
# print(songs)
# # for i in itembox:
# # songs = i.find_elements(By.XPATH,'//*[@id="/charts/top-200/japan"]/div[3]/div[1]/div[1]/ul/li/article/div[2]/div[1]/div[1]/a')
# # for s in songs:
# # data['Title'].append(s.text.strip())
# # author = i.find_elements(By.XPATH, '//*[@id="/charts/top-200/japan"]/div[3]/div[1]/div[1]/ul/li/article/div[2]/div[1]/div[2]/div')
# # for a in author:
# # data['Artist'].append(a.text.strip())
# # data['Extraction Time'].append(day_date_time.strip())
# # data['Locale'].append(locale.strip())
# # data['Language'].append(lang.strip())
# # data['Tag'].append(tag.strip())
# # data['Main Url'].append(url)
# # data['Supported Url'].append('')
# # data['Url'].append(urllst)
# # links = i.find_elements(By.XPATH,'//*[@id="/charts/top-200/japan"]/div[3]/div[1]/div[1]/ul/li[1]/article/div[2]/div[1]/div[1]/a')
# # for my_href in links:
# # link = my_href.get_attribute("href")
# # data['Supported Url'].append('https://www.shazam.com'+ link)
# #
# #
# # #
# # file_name = ' Shazam_MTC_TOPCHART.csv'
# # make_csv(file_name, data)
#
# # import re
# # import time
# # import requests
# # from bs4 import BeautifulSoup as bs
# # from selenium import webdriver
# # import pandas as pd
# # import unicodedata
# # from datetime import datetime
# # from datetime import date
# # import csv
# # import os
# # import itertools
# #
# # def make_csv(filename, data):
# # with open(filename, 'w+') as file:
# # writer = csv.writer(file)
# # writer.writerow(data.keys())
# # writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
# #
# #
# # now = datetime.now()
# # current_time = now.strftime("%H:%M:%S")
# # date = date.today()
# # wd = date.weekday()
# # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# # day = days[wd]
# # date = str(date)
# # date = date.split("-")
# # month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# # '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# # day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# # feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# # url = 'https://www.shazam.com/charts/top-200/japan'
# # response = requests.get(url)
# # locale = "jp-JP"
# # lang = "jp"
# # tag = ""
# # sup_url =""
# # urllst = ""
# # url_name = []
# # author_name = []
# # song_name = []
# # full_list = []
# # first_half = []
# # urllst = []
# # second_half = []
# # data = {
# # 'Title': [],
# # 'Artist':[] ,
# # 'Extraction Time':[],
# # 'Locale': [],
# # 'Language': [],
# # 'Tag': [],
# # 'Main Url': [],
# # 'Supported Url':[],
# # 'Url': [],
# # }
# # soup = bs(response.text, 'html.parser')
# #
# # acts = soup.find_all('div', {'class': 'titleArtistContainer'})
# # urls= []
# # for each in acts:
# # title = each.find_next('div', {'class': 'title'}).text.strip()
# # link = each.find_next('a', href=True)
# # urls = link['href']
# # artist = each.find_next('div', {'class': 'artist'}).text.strip()
# #
# # data['Title'].append(title.strip())
# # data['Artist'].append(artist.strip())
# # data['Extraction Time'].append(day_date_time.strip())
# # data['Locale'].append(locale.strip())
# # data['Language'].append(lang.strip())
# # data['Tag'].append(tag.strip())
# # data['Main Url'].append(url)
# # data['Supported Url'].append(urls)
# # data['Url'].append(urllst)
# # # print(f'{title}\n{artist}\n{urls}\n\n')
# #
# # file_name = ' SHAZAM_MTC.csv'
# # make_csv(file_name, data)

# You CAN DIRECTLY DOWNLOAD CSV ON SITE ALSO
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import unicodedata
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.shazam.com/charts/top-200/japan'
# url= 'http://schema.org/MusicPlaylist'
# response = requests.get(url)

locale = "ja-JP"
lang = "ja"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
timeout =30
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
res = browser.page_source
delay = 10
timeout =20
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div/div[3]/div[1]/div[1]/ul/li[1]')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.CLASS_NAME,'track ')
print(len(itembox))
# for i in itembox:
# print(i.text)
# songs = re.findall(r'<div class ="ellip">.*?</div>',str(res), flags = re.DOTALL)
# print(songs)
for i in itembox:
 songs = i.find_elements(By.CLASS_NAME,'title')
 for s in songs:
 print(s.text)
 data['Title'].append(s.text.strip())
 author = i.find_elements(By.CLASS_NAME, 'artist')
 for a in author:
 print(a.text)
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 # data['Supported Url'].append('')
 data['Url'].append(urllst)
 links = i.find_elements(By.CLASS_NAME,'open-track-result')
 for my_href in links:
 link = my_href.get_attribute("href")
 data['Supported Url'].append(link)
#
# for s in songs:
# print(s.text)
# for a in author:
# print(a.text)
# data['Artist'].append(a.text.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# # data['Supported Url'].append('')
# data['Url'].append(urllst)

# #
# #
# # #
file_name = ' Shazam_MTC_TOPCHART.csv'
make_csv(file_name, data)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time
import unicodedata

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.soompi.com/article/1383277wpp/red-velvet-maintains-lead-with-psycho-soompis-k-pop-music-chart-2020-february-week-3'
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
res = browser.page_source
# res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
artist_list = re.findall(r'<td class="other"><span>(.*?)</span>', str(res), flags=re.DOTALL)
further_artist = re.findall(r'<span>Artist/Band: </span>\s*(.*?)\s*</div>', str(res))
artist_list.extend(further_artist)
song_list = re.findall(r'<td class="title">\s*<span>(.*?)</span>', str(res), flags=re.DOTALL)
further_songs = re.findall(r'<span class="item-title">\s*(.*?)\s*</span>', str(res))
song_list.extend(further_songs)
res_list = list()
for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 if artist_list[i]:
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ko-KR"})
 res_dict.update({"Language": "ko"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": ""})
 res_list.append(res_dict)
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
 'Url']
csv_file = "soompi_topchart.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://tophit.ru/en/chart/russia/weekly/current/all/all'
response = requests.get(url)
locale = "ru-Ru"
lang = "ru"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'titles_block'})
urls= []
for each in acts:
 link = each.find_next('a', href=True)
 urls = link['href']
 title = each.find_next('a', {'class': 'black'}).text.strip()
 artist = each.find_next('a', {'class': 'track_name black'}).text.strip()

 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://tophit.ru'+ urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' TOPHIT_RUSSIA_MTC.csv'
make_csv(file_name, data)
# url = "https://www.jiosaavn.com/featured/weekly-top-songs/Vzehd0ZQty4_"
# browser.get(url)
# res = browser.page_source
# res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
# artist_list = re.findall(r'<em class="meta">(.*?)</em>', res, flags=re.DOTALL)
# song_list = re.findall(r'<span class="title"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
# url_list = re.findall(r'<meta property="music:song" content="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist_regex = re.findall(r'class="".*?>(.*?)</a>', artist_list[i])
# artist_regex = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
# artist_regex = artist_regex.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# if not url_list[i]:
# url_list[i] = url
# if artist_regex:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist_regex})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ur-Pk"})
# res_dict.update({"Language": "ur"})
# res_dict.update({"Tag": "India"})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": url_list[i]})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "jiosaavn1_topchart.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list
#
# # def jiosaavn():
# url = "https://www.jiosaavn.com/featured/weekly-top-songs"
# browser.get(url)
# res = browser.page_source
# res = str(unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore'))
# artist_list = re.findall(r'<abbr class="spacer">(.*?)</em>', res, flags=re.DOTALL)
# song_list = re.findall(r'<span class="title"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
# url_list = re.findall(r'<meta property="music:song" content="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist_regex = re.findall(r'class="".*?>(.*?)</a>', artist_list[i])
# artist_regex = str(artist_regex).replace("[", "").replace("]", "").replace("'", "")
# artist_regex = artist_regex.replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# if not url_list[i]:
# url_list[i] = url
# if artist_regex:
# res_dict = dict()
# res_dict.update({"Title": song_list[i]})
# res_dict.update({"Artist": artist_regex})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "en-IN"})
# res_dict.update({"Language": "en"})
# res_dict.update({"Tag": "India"})
# res_dict.update({"Main Url": ""})
# res_dict.update({"Supported Url": ""})
# res_dict.update({"Url": url_list[i]})
# res_list.append(res_dict)
# csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url',
# 'Url']
# csv_file = "jiosaavn_topchart.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import unicodedata
import itertools
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from selenium import webdriver
import time


def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_'
# url= 'http://schema.org/MusicPlaylist'
# response = requests.get(url)

locale = "en-IN"
lang = "en"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
timeout =30
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
res = browser.page_source
delay = 1
timeout =20
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/main/section/section/ol/li[1]')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div/main/section/section/ol/li ')
print(len(itembox))
# songs = re.findall(r'<div class ="ellip">.*?</div>',str(res), flags = re.DOTALL)
# print(songs)
for i in itembox:
 songs = i.find_elements(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div/main/section/section/ol/li/div/article/div[2]/figure/figcaption/h4')
 for s in songs:
 print(s.text)
 data['Title'].append(s.text.strip())
 author = i.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/main/section/section/ol/li/div/article/div[2]/figure/figcaption/p[1]')
 for a in author:
 print(a.text)
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 # data['Supported Url'].append('')
 data['Url'].append(urllst)
 links = i.find_elements(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div/main/section/section/ol/li/div/article/div[2]/figure/figcaption/h4/a')
 for my_href in links:
 link = my_href.get_attribute("href")
 data['Supported Url'].append( link)
#
#
# #
file_name = ' JIOSAAVN_MTC_TOPCHART.csv'
make_csv(file_name, data)

#
# import re
# import time
# import requests
# from bs4 import BeautifulSoup as bs
# from selenium import webdriver
# import pandas as pd
# import unicodedata
# from datetime import datetime
# from datetime import date
# import csv
# import os
# import itertools
#
# def make_csv(filename, data):
# with open(filename, 'w+') as file:
# writer = csv.writer(file)
# writer.writerow(data.keys())
# writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))
#
#
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# date = date.today()
# wd = date.weekday()
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
# day = days[wd]
# date = str(date)
# date = date.split("-")
# month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
# '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
# day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
# feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
# url = 'https://www.raaga.com/tamil/top10'
# response = requests.get(url)
# locale = "ta-IN"
# lang = "ta"
# tag = ""
# sup_url =""
# urllst = ""
# url_name = []
# author_name = []
# song_name = []
# full_list = []
# first_half = []
# urllst = []
# second_half = []
# data = {
# 'Title': [],
# 'Artist':[] ,
# 'Extraction Time':[],
# 'Locale': [],
# 'Language': [],
# 'Tag': [],
# 'Main Url': [],
# 'Supported Url':[],
# 'Url': [],
# }
# soup = bs(response.text, 'html.parser')
#
# acts = soup.find_all('li')
# urls= []
# for each in acts:
# link = each.find_next('a', href=True)
# urls = link['href']
# title = each.find_next('p').text.strip()
# artist = each.find_next('p').find_next('p').find_next('p').text.strip()
#
# data['Title'].append(title.strip())
# data['Artist'].append(artist.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)
# data['Supported Url'].append( urls)
# data['Url'].append(urllst)
# # print(f'{title}\n{artist}\n{urls}\n\n')
#
# file_name = 'Raaga_tamil_MTC.csv'
# make_csv(file_name, data)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import itertools
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.raaga.com/tamil/top10'
response = requests.get(url)
locale = "ta-IN"
lang = "ta"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
timeout =30
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
delay = 1
# timeout =20
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Music"]/div/div[2]/section/ul')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.XPATH, '//*[@id="Music"]/div/div[2]/section/ul')
# print(len(itembox))

for i in itembox:
 songs = i.find_elements(By.XPATH,'//*[@id="Music"]/div/div[2]/section/ul/li/p[1]')
 for s in songs:
 data['Title'].append(s.text.strip())
 author = i.find_elements(By.XPATH, '//*[@id="Music"]/div/div[2]/section/ul/li/p[4]/a')
 for a in author:
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('')
 data['Url'].append(urllst)
 links = i.find_elements(By.XPATH,'//*[@id="Music"]/div/div[2]/section/ul/li/a')
 for my_href in links:
 link = my_href.get_attribute("href")
 data['Supported Url'].append(link)

file_name = 'Raaga_tamil_MTC.csv'
make_csv(file_name, data)

import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.oricon.co.jp/rank/js/w/'
response = requests.get(url)
locale = "ja-JP"
lang = "ja"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('section', {'class': 'box-rank-entry'})
urls= []
for each in acts:
 link = each.find_next('a', href=True)
 urls = link['href']
 title = each.find_next('h2', {'class': 'title'}).text.strip()
 artist = each.find_next('p', {'class': 'name'}).text.strip()

 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('https://www.oricon.co.jp/rank/js/w'+ urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = 'ORICON_MTC.csv'
make_csv(file_name, data)


import re
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import unicodedata
from datetime import datetime
from datetime import date
import csv
import os
import itertools

def make_csv(filename, data):
 with open(filename, 'w+') as file:
 writer = csv.writer(file)
 writer.writerow(data.keys())
 writer.writerows(itertools.zip_longest(*data.values(), fillvalue=None))


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug',
 '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = 'https://www.oljo.de/radiochart_d/radio100.shtml'
response = requests.get(url)
locale = "de-DE"
lang = "de"
tag = ""
sup_url =""
urllst = ""
url_name = []
author_name = []
song_name = []
full_list = []
first_half = []
urllst = []
second_half = []
data = {
 'Title': [],
 'Artist':[] ,
 'Extraction Time':[],
 'Locale': [],
 'Language': [],
 'Tag': [],
 'Main Url': [],
 'Supported Url':[],
 'Url': [],
}
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'stplz'})
urls= []
for each in acts:
 title = each.find_next('div', {'class': 'radiopret'}).text.strip()
 artist = each.find_next('div', {'class': 'radiotitel'}).text.strip()
 link = each.find_next('a', href=True)
 urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append(urls)
 data['Url'].append(urllst)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' OLJIO_MTC.csv'
make_csv(file_name, data)


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
import re
from datetime import datetime
from datetime import date
from selenium import webdriver
import csv

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = days[wd]
day_date_time = day + "_" + str(date) + "_" + current_time
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
url = "https://www.letssingit.com/charts/japan-singles"
# res = urllib.urlopen(url).read()
browser.get(url)
res = browser.page_source
# res = requests.get(url).text
artist_list = re.findall(r'class="high_profile".*?<a href=.*?>(.*?)</a>', str(res), re.DOTALL)
song_list = re.findall(r'class="high_profile">(.*?)</a>', str(res), re.DOTALL)
url_list = re.findall(r'class="high_profile".*?<a href="(.*?)".*?</a>', str(res), re.DOTALL)

for i in range(len(song_list)):
 song_list[i] = str(song_list[i]).replace(' lyrics', '').replace(', lyrics', '')
# print(artist_list)
# print(song_list)
# print(url_list)
# print(len(artist_list))
# print(len(song_list))
# print(len(url_list))

res_list = list()
for i in range(len(artist_list)):
 res_dict = dict()
 res_dict.update({"Title": song_list[i]})
 res_dict.update({"Artist": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Tag": ""})
 res_dict.update({"Main Url": url})
 res_dict.update({"Supported Url": ""})
 res_dict.update({"Url": url_list[i]})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Title', 'Artist', 'Extraction Time', 'Locale', 'Language', 'Tag', 'Main Url', 'Supported Url', 'Url']
csv_file = "japan_singles-letssingit.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()


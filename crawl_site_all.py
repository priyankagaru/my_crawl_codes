import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "http://www.billboard-japan.com/charts/detail?a=hot_albums"
res = requests.get(url).text
song_list = re.findall(r'<p class="musuc_title">(.*?)</p>', res)
artist_list = re.findall(r'<p class="artist_name">(.*?)</p>', res)
url_list = re.findall(r'<div class="right_detail">\s*(.*?)\s*</div>', res)
res_list = list()
for i in range(len(song_list)):
 url_regex = re.search(r'<a href="(.*?)"', url_list[i])
 if url_regex:
 url_list[i] = "http://www.billboard-japan.com/" + url_regex.group(1)
 else:
 url_list[i] = ""
 artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist_list[i])
 if artist_regex:
 artist_list[i] = artist_regex.group(1)
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
res_list = res_list[0:199]
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "billboard_japan_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import unicodedata
import time
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = datetime.date(now)
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {
 "01": "Jan",
 "02": "Feb",
 "03": "Mar",
 "04": "Apr",
 "05": "May",
 "06": "June",
 "07": "July",
 "08": "Aug",
 "09": "Sep",
 "10": "Oct",
 "11": "Nov",
 "12": "Dec"
}
day_date_time = day + " " + month[str(
 date[1]
)] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [
 " feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring",
 " (Album"
]
#
# url = "http://www.chartsinfrance.net/charts/itunes-france-albums.php"
# # res = urllib.urlopen(url).read()
# res = requests.get(url).text
# song_list = re.findall( r'<font class="noir11">(.*?)</font>', res, flags=re.DOTALL)
# song_list = song_list[0:50]
# artist = re.findall(r'<font class="noir13b">(.*?)</a>', res, flags=re.DOTALL)
# artist = artist[0:50]
# res_list = list()
# for i in range(len(song_list)):
# if (artist[i] != ''):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(
# " And", ",").replace(" &", ",").replace("&#034;",
# '"').replace("&#039;", "'")
# else:
# artist[i] = ""
# song_list[i] = song_list[i].replace("&amp;",
# "&").replace("&#034;", '"').replace(
# "&#039;", "'")
# print(song_list[i])
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "fr-FR"})
# res_dict.update({"Language": "fr"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = [
# "Album_Name", "Artist_Name", "Extraction Time", "Locale", "Language",
# "Entity_URL", "Detail_URL", "Supported_URL", "Entity Type"
# ]
# csv_file = "chartsinfrance_album.csv"
# with open(csv_file, 'w') as csvfile:
# # subevent_csv_file_path = "/cns/in-d/home/hume-crawl/ketl/workflows/music_albums_crawl/chartsinfrance_album" + day_date_time + ".csv"
# # with gfile.Open(subevent_csv_file_path, "w+") as subevent_csv_file:
# writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

url = "http://www.chartsinfrance.net/charts/albums.php"
# res = urllib.urlopen(url).read()
res = requests.get(url).text
song_list = re.findall(
 r'<font class="noir11"><a.*?>(.*?)</a></font>', res, flags=re.DOTALL)
song_list = song_list[0:50]
artist = re.findall(
 r'<font class="noir13b">(.*?)</font>', res, flags=re.DOTALL)
artist = artist[0:50]
url_list = re.findall(
 r'<font class="noir13b">(.*?)</font>', res, flags=re.DOTALL)
url_list = url_list[0:50]
res_list = list()
for i in range(len(song_list)):
 url_regex = re.search(r'<a href="(.*?)"', url_list[i])
 if url_regex:
 url_list[i] = "http://www.chartsinfrance.net/" + url_regex.group(1)
 else:
 url_list[i] = ""
 artist_regex = re.search(r"<a href.*?>(.*?)</a>", artist[i])
 if artist_regex:
 artist[i] = artist_regex.group(1)
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(
 " And", ",").replace(" &", ",").replace("&#034;",
 '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;",
 "&").replace("&#034;", '"').replace(
 "&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)


df =pd.DataFrame(res_list)
df.to_csv('CHARTSINFRANCE_album.csv',index=False)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "http://www.gaonchart.co.kr/main/section/chart/album.gaon?nationGbn=T"
res = requests.get(url).text
song_list = re.findall(r'<td class="subject">\s*<p.*?>(.*?)</p>', res, flags=re.DOTALL)
print(song_list)
artist = re.findall(r'<p class="singer".*?>(.*?)</p>', res)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ko-KR"})
 res_dict.update({"Language": "ko"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "gaon_album.csv"
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
url = ['https://www.ibs.it/classifica/cd/1week/sold?page=1', 'https://www.ibs.it/classifica/cd/1week/sold?page=2','https://www.ibs.it/classifica/cd/1week/sold?page=3']

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
entity_type = '/music/album'
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
for j in range(len(url)):
 response = requests.get(url[j])
 soup = bs(response.text, 'html.parser')

 acts = soup.find_all('div', {'class': 'cc-product-list-item cc-product-list-item--ranking'})
 urls= []
 for each in acts:
 title = each.find_next('a', {'class': 'cc-title'}).text.strip()
 link = each.find_next('a', href=True)
 artist = each.find_next('a', {'class': 'cc-author-name'}).text.strip()
 urls = link['href']
 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url[j])
 data['Supported Url'].append('https://www.ibs.it'+ urls)
 data['Entity Type'].append(entity_type)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' IBS_IT.csv'
make_csv(file_name, data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://itopchart.com/it/it/music-album-charts/christian-gospel/"
res = requests.get(url).text
song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "itopchart_christian_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests


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
url = "https://itopchart.com/fr/fr/music-album-charts/french-pop/"
res = requests.get(url).text
song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "itopchart_french_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://kworb.net/eua/"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale = re.findall(r'</td><td style.*?>.*?</td><td>(.*?)</td><td>', res)
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_DE.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://kworb.net/eua/index_full.html"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale_list = re.findall(r'<td style=.*?>.*?<td style=.*?>.*?<td>.*?</td><td>.*?</td><td>(.*?)</td>', res)
locale = list()
for i in range(len(locale_list)):
 if i % 2 == 0:
 locale.append(locale_list[i])
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "ES"})
 res_dict.update({"Entity_URL": "https://kworb.net/eua/"})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_ES.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://kworb.net/eua/index_full.html"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale_list = re.findall(r'<td style=.*?>.*?<td style=.*?>.*?<td>.*?</td><td>.*?</td><td>(.*?)</td>', res)
locale = list()
for i in range(len(locale_list)):
 if i % 2 == 0:
 locale.append(locale_list[i])
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-ES"})
 res_dict.update({"Language": "ES"})
 res_dict.update({"Entity_URL": "https://kworb.net/eua/"})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_ES.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://kworb.net/aww/"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale = re.findall(r'</td><td style.*?>.*?<td>.*?</td><td>.*?</td><td>.*?</td><td>(.*?)</td>', res, flags=re.DOTALL)
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_JP.csv"
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
url = ['https://www.lafeltrinelli.it/classifica/cd/1week/sold?defaultPage=1','https://www.lafeltrinelli.it/classifica/cd/1week/sold?defaultPage=2']

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
 'Entity Type': [],
}
entity_type = '/music/album'
for j in range(len(url)):
 response = requests.get(url[j])
 soup = bs(response.text, 'html.parser')

 acts = soup.find_all('div', {'class': 'cc-product-list-item cc-product-list-item--ranking'})
 urls= []
 for each in acts:
 title = each.find_next('div', {'class': 'cc-content-title'}).find_next('a', {'class': 'cc-title'}).text.strip()
 print(title)
 link = each.find_next('a', href=True)
 urls = link['href']
 artist = each.find_next('a', {'class': 'cc-author-name'}).text.strip()
 print(artist)
 # for a in artist:
 # art = a.text
 data['Artist'].append(artist)
 data['Title'].append(title)
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url[j])
 data['Supported Url'].append('https://www.lafeltrinelli.it'+ urls)
 data['Entity Type'].append(entity_type)

 # print(f'{title}\n{artist}\n{urls}\n\n')
 # for i in acts:
 # artst = i.find('div', class_='cc-author').find('a', class_='cc-author-name').text
 # print(artst)

file_name = ' LAFELTRINELLI_IT.csv'
make_csv(file_name, data)

# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# from selenium import webdriver
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import os
# import unicodedata
# import time
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
# url = ["https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=22",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=43",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=64",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=85"]
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# csv_file = "melon1_album.csv"
# if os.path.exists("melon1_album.csv"):
# os.remove("melon1_album.csv")
# browser = webdriver.Chrome(executable_path=chromedriver, options=options)
# for j in range(len(url)):
# print(url[j])
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# res = browser.get(url[j])
# time.sleep(5)
# res = browser.page_source
# make sure you get all the correct urls for scraping till the fifth page

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
lang = "KO"
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
# 1, 22, 43, 64 ,81 : indexes in url
# https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=
# url = 'https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=64'


# https://www.melon.com/genre/album_list.htm?gnrCode=GN0100&dtlGnrCode=#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BmasterpieceYn%5D=N&po=pageObj&startIndex=21
# https://www.melon.com/genre/album_list.htm?gnrCode=GN0100&dtlGnrCode=
# https://www.melon.com/genre/album_list.htm?gnrCode=GN0100&dtlGnrCode=#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BmasterpieceYn%5D=N&po=pageObj&startIndex=41
# https://www.melon.com/genre/album_list.htm?gnrCode=GN0100&dtlGnrCode=#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BmasterpieceYn%5D=N&po=pageObj&startIndex=61
# https://www.melon.com/genre/album_list.htm?gnrCode=GN0100&dtlGnrCode=#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BmasterpieceYn%5D=N&po=pageObj&startIndex=81
url1 = 'https://www.melon.com/genre/album_list.htm?gnrCode=GN0100&dtlGnrCode=#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BmasterpieceYn%5D=N&po=pageObj&startIndex=81'
entity_type = '/music/album'
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
timeout =40
browser = webdriver.Chrome(service=chromedriver, options=op)
try:
 # for j in range(len(url)):
 # timeout = 20
 browser.get(url1)
 delay = 1
 timeout =40
 try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[5]/form/div')))
 print("Page is ready!")
 except TimeoutException:
 print("Loading took too much time!")
 itembox = browser.find_elements(By.CLASS_NAME,'info')
 print(len(itembox))
 for i in itembox:
 songs = i.find_elements(By.XPATH,'//*[@id="frm"]/div/ul/li/div[2]/div[1]/a')
 try:
 WebDriverWait(browser, 120).until(
 EC.presence_of_element_located((By.XPATH, '//*[@id="frm"]/div/ul/li/div[2]/div[1]/span[2]/a')))
 author = i.find_elements(By.XPATH, '//*[@id="frm"]/div/ul/li/div[2]/div[1]/span[2]/a')
 except:
 pass
 for s in songs:
 song = s.get_attribute('title')[:-8]
 data['Title'].append(song.strip())

 for a in author:
 artist = a.get_attribute('title')[:-8]
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url1)
 data['Supported Url'].append('')
 data['Entity Type'].append(entity_type)
 links = ''
 # link = my_href.get_attribute("href")
 data['Supported Url'].append(links)
except exceptions.StaleElementReferenceException:
 print('stalemateexception bro!!')
 pass
# #
file_name = ' MELON_ALBUM.csv'
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
url = 'https://mtv.marsl.net/demo/showdbcharts.php?c=5'
url_main = 'https://www.mtv.de/info/l1eof0/album-top100'
response = requests.get(url)
locale = "de-De"
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
entity_type = '/music/album'

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
soup = bs(response.text, 'html.parser')

acts = soup.find_all('div', {'class': 'cmn-act'})
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
 data['Main Url'].append(url_main)
 data['Supported Url'].append(link)
 data['Entity Type'].append(entity_type)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' MTV_DE.csv'
make_csv(file_name, data)


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = datetime.date(now)
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {
 "01": "Jan",
 "02": "Feb",
 "03": "Mar",
 "04": "Apr",
 "05": "May",
 "06": "June",
 "07": "July",
 "08": "Aug",
 "09": "Sep",
 "10": "Oct",
 "11": "Nov",
 "12": "Dec"
}
day_date_time = day + " " + month[str(
 date[1]
)] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [
 " feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"
]

url = 'http://music-book.jp/music/Ranking/Album/weekly?page=1'
 # ,
 # "http://music-book.jp/music/Ranking/Album/weekly?page=2",
 # "http://music-book.jp/music/Ranking/Album/weekly?page=3",
 # "http://music-book.jp/music/Ranking/Album/weekly?page=4",
 # "http://music-book.jp/music/Ranking/Album/weekly?page=5"]
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']

# url = "http://music-book.jp/music/Ranking/Album/weekly"
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
time.sleep(20)
text = browser.page_source
# browser.close()
title,artist,url_list,res_list,entity_url_list = [],[],[],[],[]
soup = bs(text, "html.parser")
soup = soup.find("ul", class_="list")
# print(soup)
for song in soup:
 # title.append(song.find('a', class_="link_text").get('title'))
 title.append(song.find('span', class_="text text-black -is-ellipsis -line-clamp-2 -bold").text.strip())
 artist.append(song.find('span', class_="text text-black -is-ellipsis -line-clamp-1").text.strip())
 url_list.append("http://music-book.jp/music/Ranking/Album/weekly" + song.find('a', class_="item-link").get('href'))
 entity_url_list.append(url)
for i in range(len(url_list)):
 # print(url_list)
 res_dict = dict()
 res_dict.update({"Album_Name": title[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ja-JP"})
 res_dict.update({"Language": "ja"})
 res_dict.update({"Entity_URL": entity_url_list[i]})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)

csv_file = "music_book.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://music.bugs.co.kr/chart/album/day/total"
res = requests.get(url).text
song_list = re.findall(r'<div class="albumTitle">\s*<a.*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<a.*?class="artistTitle".*?>(.*?)</a>', res, flags=re.DOTALL)
url_list = re.findall(r'<p class="badge">.*?<a href="(.*?)"', res, flags=re.DOTALL)
res_list = list()
for i in range(len(song_list)):
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 if "</span>" in artist[i]:
 artist[i] = artist[i].partition("</span>")[0]
 song_list[i] = song_list[i].replace("&lt;", "(")
 song_list[i] = song_list[i].replace("&gt;", ")")
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &", ",").replace(
 '&#034;', '"').replace("&#039;", "'").replace("&lt;", "(").replace("&gt;", ")").replace("&gt", ")")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace("&lt;", "(").replace("&gt", ")")
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ko-KR"})
 res_dict.update({"Language": "ko"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "music_bugs_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

# changed website structure. page not loading
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = datetime.date(now)
wd = date.weekday()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday"]
day = days[wd]
date = str(date)
date = date.split("-")
month = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June', '07': 'July', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
day_date_time = day + " " + month[str(date[1])] + " " + date[2] + " " + date[0] + " " + current_time + " " + "IST"
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = "https://vibe.naver.com/chart/billboardKpop"
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
time.sleep(20)
text = browser.page_source
browser.close()
title,artist,url_list,res_list,entity_url_list,album = [],[],[],[],[],[]
soup = bs(text, 'html.parser')
soup = soup.find('div', class_='tracklist')
# print(soup)
songs = soup.find_all('tr', class_='')
# print(songs)
songs.pop(0)
for song in songs:
 # title.append(song.find('a', class_="link_text").get('title'))
 artist.append(song.find('div', class_="artist_sub").get('title'))
 album.append(song.find('a', class_="link").text.strip())
 url_list.append("https://vibe.naver.com/" + song.find('a', class_="link_text").get('href'))
 entity_url_list.append(url)
 # print(artist)
 # print(album)
 # print(url_list)
 # print("Songs: ", song.find('a', class_="link_text").get('title'))
 # print("Artist: ", song.find('div', class_="artist_sub").get('title'))
 # print("Album: ", song.find('a', class_="link").text.strip())
 # print("Url: ", "https://vibe.naver.com/" + song.find('a', class_="link_text").get('href'))
 # print(soup)
 # title,artist,url_list,res_list,entity_url_list = [],[],[],[],[]
 # x = soup.find('div', class_='tracklist')
 # print(x)
 # for match in soup.find_all('div', class_='tracklist'):
 # print(match.text.strip())
 # link = match.find('span', class_='inner_cell')
 # print(link)
 # url_list.append('https://vibe.naver.com' + link.get('href'))
 # entity_url_list.append(url)
 #print(entity_url_list)
 # title.append(match.find('div', class_='title_badge_wrap').text.strip())
 # artist.append(match.find('div', class_='artist_sub').text.strip())
 # print(len(url_list))
 print(len(entity_url_list))
for i in range(len(url_list)):
 # print(url_list)
 res_dict = dict()
 res_dict.update({"Album_Name": album[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "ko-KR"})
 res_dict.update({"Language": "ko"})
 res_dict.update({"Entity_URL": entity_url_list[i]})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 # print(res_list)
 # print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "music_naver.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver
import unicodedata

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
url = ["https://www.musicme.com/#/classements-cd/',options=%22/", "https://www.musicme.com/#/classements-cd/2.html",
 "https://www.musicme.com/#/classements-cd/3.html", "https://www.musicme.com/#/classements-cd/4.html",
 "https://www.musicme.com/#/classements-cd/5.html", "https://www.musicme.com/#/classements-cd/6.html",
 "https://www.musicme.com/#/classements-cd/7.html", "https://www.musicme.com/#/classements-cd/8.html",
 "https://www.musicme.com/#/classements-cd/9.html", "https://www.musicme.com/#/classements-cd/10.html",
 "https://www.musicme.com/#/classements-cd/11.html", "https://www.musicme.com/#/classements-cd/12.html",
 "https://www.musicme.com/#/classements-cd/13.html", "https://www.musicme.com/#/classements-cd/14.html",
 "https://www.musicme.com/#/classements-cd/15.html"]
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']

csv_file = "music_me_album.csv"
if os.path.exists("music_me_album.csv"):
 os.remove("music_me_album.csv")
for j in range(len(url)):
 browser.get(url[j])
 time.sleep(20)
 browser.switch_to.frame(browser.find_element(By.ID, 'frmmain'))
 res = browser.page_source
 # res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<span class="itemcoltxt"><a.*?>(.*?)</a>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="itemcolalbline1"><a.*?>(.*?)</a>', str(res), flags=re.DOTALL)
 url_list = re.findall(r'<span class="itemcoltxt"><a href="(.*?)"', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 url_list[i] = "https://www.musicme.com/#" + url_list[i]
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": ""})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Entity_URL": url[j]})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 print(res_list)
 print(len(res_list))
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()

#Moving files
# import shutil
# root = '/home/akhilbhatnagar/Downloads/pycharm-community-2019.3.4/bin/musiccrawl_out/'
# shutil.move('music_me_album.csv' , root + 'music_me_album.csv')

# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
#
# from selenium import webdriver
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import os
# import unicodedata
# import sys
# import codecs
#
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
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
# # browser = webdriver.Chrome(executable_path=chromedriver, options=options)
# browser.get('https://www.oricon.co.jp/rank/ja/w/')
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('ascii', 'ignore')
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "oricon_album.csv"
# if os.path.exists("oricon_album.csv"):
# os.remove("oricon_album.csv")
# url_list_all_page = re.findall(r'<div class="block-rank-pager-bottom mt20">(.*?)</div>', str(res), flags=re.DOTALL)
# url_regex_all_page = re.findall(r'<li><a href="(.*?)"', url_list_all_page[0])
# for i in range(len(url_regex_all_page)):
# url_regex_all_page[i] = "https://www.oricon.co.jp" + url_regex_all_page[i]
# # print(url_regex_all_page)
# for j in range(len(url_regex_all_page)):
# result = browser.get(url_regex_all_page[j])
# result = browser.page_source
# result = unicodedata.normalize('NFKD', result).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', str(result), flags=re.DOTALL)
# # print(song_list)
# # print(len(song_list))
# artist = re.findall(r'<p class="name">(.*?)</p>', str(result), flags=re.DOTALL)
# # print(artist)
# # print(len(artist))
# url_list = re.findall(r'<div class="ribbon">\s*.*?<div class="inner">(.*?)<p class="image">\s*<span>', str(result),
# flags=re.DOTALL)
# # print(url_list)
# # print(len(url_list))
# res_list = list()
# for i in range(len(song_list)):
# url_regex = re.search(r'<a href="(.*?)"', url_list[i])
# if url_regex:
# url_list[i] = "https://www.oricon.co.jp" + url_regex.group(1)
# else:
# url_list[i] = ""
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ja-JP"})
# res_dict.update({"Language": "ja"})
# res_dict.update({"Entity_URL": url_regex_all_page[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# # print(res_list)
# # print(len(res_list))
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# browser.close()

# make sure you get all the correct urls for scraping till the fifth page

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
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
url = 'https://www.oricon.co.jp/rank/ja/w/'

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)

# for j in range(len(url)):
 # timeout = 20
browser.get(url)
delay = 1
timeout =20
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-main"]/div[1]/div[1]')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.CLASS_NAME,'box-rank-entry')
print(len(itembox))
entity_type = '/music/album'

for i in itembox:
 songs = i.find_elements(By.CLASS_NAME,'title')
 author = i.find_elements(By.CLASS_NAME, 'name')
 links = i.find_elements(By.XPATH,'//*[@id="content-main"]/div[1]/div[1]/div/article/section/div[2]/a')

 for s in songs:
 song = s.text
 data['Title'].append(song.strip())
 for a in author:
 # artist = a.get_attribute('href')
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('')
 data['Entity Type'].append(entity_type)
 for my_href in links:
 link = my_href.get_attribute("href")
 data['Supported Url'].append(link)

file_name = ' ORICON_JP_ALBUM.csv'
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
url = 'https://recochoku.jp/ranking/album/weekly/'
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
 'Entity Type': [],
}
entity_type = '/music/album'

current_time = now.strftime("%H:%M:%S")
timeout =30
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
delay = 1
# timeout =20
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rankingContents"]/div[1]')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.CLASS_NAME,'c-product-list__item')
# print(len(itembox))

for i in itembox:
 songs = i.find_elements(By.XPATH,'//*[@id="rankingContents"]/div/a/div[2]/div[1]')
 author = i.find_elements(By.XPATH, '//*[@id="rankingContents"]/div/a/div[2]/div[2]')
 links = i.find_elements(By.CLASS_NAME,'__link')
 for my_href in links:
 link = my_href.get_attribute("href")
 print(link)
 data['Supported Url'].append(link)

for s in songs:
 data['Title'].append(s.text.strip())
for a in author:
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append('')
 data['Entity Type'].append(entity_type)

# soup = bs(response.text, 'html.parser')
# print(soup.prettify())
# acts = soup.find_all('div', {'class': 'c-product-list__item'})
# print(len(acts))
# urls= []
# for each in acts:
# links = each.find_next('a',{'class': 'c-product-list__link'},href =True)
# urls = links['href']
# title = each.find_next('div', {'class': 'c-product-list__title c-el'}).text.strip()
# artist = each.find_next('div', {'class': 'c-product-list__artist c-el'}).text.strip()
# # link = each.find_next('a', href=True)
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
#
file_name = ' RECOCHOKU_ALBUM.csv'
make_csv(file_name, data)
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# options = Options()
# options.add_argument('--headless') # Runs Chrome in headless mode.
# options.add_argument('--no-sandbox') # Bypass OS security model
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import bs4
# import sys
# import codecs
# from html.parser import HTMLParser
# import unicodedata
# from selenium import webdriver
# import time
#
# parser = HTMLParser()
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
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
# url = "https://snkhan.co.uk/stuff/iTunes.php?chart=RUalbums"
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<p>(.*?)</p>', str(res))
# song_list = song_list[3:103]
# artist_list = re.findall(r'<td width.*?>.*?<br>(.*?)<br>', str(res), flags=re.DOTALL)
# supported_url = list()
# supported_url = re.findall(r'<td width.*?>.*?<td width.*?>(.*?)<br>', str(res), flags=re.DOTALL)
# for i in range(len(artist_list)):
# artist_regex = re.search(r'<a.*?>(.*?)</a>', artist_list[i])
# supported_regex = re.search(r'<a href="(.*?)"', supported_url[i])
# if artist_regex:
# artist_list[i] = artist_regex.group(1)
# else:
# artist_list[i] = ""
# if supported_regex:
# supported_url[i] = supported_regex.group(1)
# else:
# supported_url[i] = ""
# res_list = list()
# for i in range(len(song_list)):
# song_list[i] = song_list[i].strip().replace(str(i), "").replace(". ", "")
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ru-RU"})
# res_dict.update({"Language": "ru"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": supported_url[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# print(res_list)
# print(len(res_list))
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
# csv_file = "snkhan_album.csv"
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
url = 'https://snkhan.co.uk/stuff/iTunes.php?chart=RUalbums'
response = requests.get(url)
locale = "ru-RU"
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
 'Entity Type': [],
}
entity_type = '/music/album'
soup = bs(response.text, 'html.parser')

acts = soup.find_all('table', cellspacing=True)
urls= []
for each in acts:
 title = each.find_next('td', width='95%').find_next('a').text.strip()
 link = each.find_next('a', href=True)
 urls = link['href']
 artist = each.find_next('td', width='95%').find_next('a',href=True).find_next('a',href=True).text
 # link = each.find_next('a', href=True)

 data['Title'].append(title.strip())
 data['Artist'].append(artist.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Supported Url'].append(urls)
 data['Entity Type'].append(entity_type)
 # print(f'{title}\n{artist}\n{urls}\n\n')

file_name = ' SNKHAN_Album.csv'
make_csv(file_name, data)


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
#combined_all.py
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import unicodedata
import time
import requests
import os
from selenium import webdriver
import ssl
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
if os.path.exists("out_album.csv"):
 os.remove("out_album.csv")
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring", " (Album"]


def billboardalbum():
 url = "https://www.billboard.com/charts/top-album-sales"
 browser.get(url)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="item-details__title">(.*?)</div>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="item-details__artist">(.*?)</div>', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-US"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "billboard_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # browser.quit()
 return res_list


def billboardlatinalbum():
 url = "https://www.billboard.com/charts/latin-albums?tag=relcharts"
 browser.get(url)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="item-details__title">(.*?)</div>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="item-details__artist">(.*?)</div>', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "billboard_latin_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # browser.quit()
 return res_list


def billboardmexicanalbum():
 url = "https://www.billboard.com/charts/regional-mexican-albums"
 browser.get(url)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="item-details__title">(.*?)</div>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="item-details__artist">(.*?)</div>', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "billboard_mexican_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # browser.quit()
 return res_list

def billboardtropicalalbum():
 url = "https://www.billboard.com/charts/tropical-albums"
 browser.get(url)
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="item-details__title">(.*?)</div>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="item-details__artist">(.*?)</div>', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "billboard_tropical_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # browser.quit()
 return res_list

def chartsalbum():
 url = "https://www.charts.de/musik-charts/alben/"
 res = requests.get(url).text
 song_list = re.findall(r'class="info1-span">(.*?)</span>', str(res), flags=re.DOTALL)
 artist = re.findall(r'class="info1-span">.*?class="info2-span">(.*?)</span><br><div\s*class="td-min-width">', str(res),
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
 if "</span>" in artist[i]:
 artist[i] = artist[i].partition("</span>")[2]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "DE"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "charts_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

# def chartsinfrancealbum():
# url = "http://www.chartsinfrance.net/charts/itunes-france-albums.php"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<font class="noir11">(.*?)</font>', res, flags=re.DOTALL)
# song_list = song_list[0:50]
# artist = re.findall(r'<font class="noir13b">(.*?)</a>', res, flags=re.DOTALL)
# artist = artist[0:50]
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "fr-FR"})
# res_dict.update({"Language": "fr"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "chartsinfrance_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def chartsinfrance1album():
# url = "http://www.chartsinfrance.net/charts/albums.php"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<font class="noir11"><a.*?>(.*?)</a></font>', res, flags=re.DOTALL)
# song_list = song_list[0:50]
# artist = re.findall(r'<font class="noir13b">(.*?)</font>', res, flags=re.DOTALL)
# artist = artist[0:50]
# url_list = re.findall(r'<font class="noir13b">(.*?)</font>', res, flags=re.DOTALL)
# url_list = url_list[0:50]
# res_list = list()
# for i in range(len(song_list)):
# url_regex = re.search(r'<a href="(.*?)"', url_list[i])
# if url_regex:
# url_list[i] = "http://www.chartsinfrance.net/" + url_regex.group(1)
# else:
# url_list[i] = ""
# artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist[i])
# if artist_regex:
# artist[i] = artist_regex.group(1)
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "fr-FR"})
# res_dict.update({"Language": "fr"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "chartsinfrance1_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

def chartsurferalbum():
 url = "https://www.chartsurfer.de/musik/album-charts-deutschland/neueinsteiger"
 res = requests.get(url).text
 song_list = re.findall(r'<div class="ww"><a class="style-1.*?>(.*?)</a>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="ww"><a class="style-2.*?>(.*?)</a>', str(res))
 url_list = re.findall(r'<div class="ww"><a class="style-1 font-weight-bold icon-magnifier" href="(.*?)"', str(res))
 res_list = list()
 for i in range(len(song_list)):
 try:
 url_list[i] = "https://www.chartsurfer.de/" + url_list[i]
 except:
 url_list.append("")
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "DE"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "chartsurfer_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

# def elcorteinglesalbum():
# url = ["https://www.elcorteingles.es/musica/listas/los-mejores-discos-de-la-historia-del-rock/",
# "https://www.elcorteingles.es/musica/listas/los-mejores-discos-de-la-historia-del-rock/2/",
# "https://www.elcorteingles.es/musica/listas/los-mejores-discos-de-la-historia-del-rock/3/"]
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "elcorteingles_album.csv"
# if os.path.exists("elcorteingles_album.csv"):
# os.remove("elcorteingles_album.csv")
# for j in range(len(url)):
# res = urllib.urlopen(url[j]).read()
# song_list = re.findall(r'<h3 class="info-name"><a.*?>\s*(.*?)\s*</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<h4 class="brand c12">\s*(.*?)\s*</h4>', res, flags=re.DOTALL)
# url_list = re.findall(r'<h3 class="info-name"><a href="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# url_list[i] = "https://www.elcorteingles.es/" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for k in range(len(feat_list)):
# if feat_list[k] in artist[i]:
# artist[i] = artist[i].partition(feat_list[k])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "es-ES"})
# res_dict.update({"Language": "es-419"})
# res_dict.update({"Entity_URL": url[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)

# def gaonalbum():
# url = "http://www.gaonchart.co.kr/main/section/chart/album.gaon?nationGbn=T"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<td class="subject">\s*<p.*?>(.*?)</p>', res, flags=re.DOTALL)
# artist = re.findall(r'<p class="singer".*?>(.*?)</p>', res)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "pt-BR"})
# res_dict.update({"Language": "pt"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "gaon_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

def ibsalbum():
 url = ["https://www.ibs.it/classifica/cd/1week/sold", "https://www.ibs.it/classifica/cd/1week/sold?page=2",
 "https://www.ibs.it/classifica/cd/1week/sold?page=3", "https://www.ibs.it/classifica/cd/1week/sold?page=4",
 "https://www.ibs.it/classifica/cd/1week/sold?page=5"]
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "ibs_album.csv"
 if os.path.exists("ibs_album.csv"):
 os.remove("ibs_album.csv")
 for j in range(len(url)):
 res = requests.get(url[j]).text
 song_list = re.findall(r'<h3 class="titleHover">\s*(.*?)\s*</h3>', res, flags=re.DOTALL)
 artist = re.findall(r'<h3 class="caption">\s*(.*?)\s*</h3>', res, flags=re.DOTALL)
 url_list = re.findall(r'<div class="rankProductTitle">\s*<a href="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 url_list[i] = "https://www.ibs.it/" + url_list[i]
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Entity_URL": url[j]})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
# def itopchartchristianalbum():
# url = "https://itopchart.com/it/it/music-album-charts/christian-gospel/"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "it-IT"})
# res_dict.update({"Language": "it"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "itopchart_christian_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def itopchartfrenchalbum():
# url = "https://itopchart.com/fr/fr/music-album-charts/french-pop/"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "fr-FR"})
# res_dict.update({"Language": "fr"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "itopchart_french_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def itopchartmxlatinoalbum():
# url = "https://itopchart.com/mx/en/music-album-charts/latino/"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "es-MX"})
# res_dict.update({"Language": "es"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "itopchart_mx_latino_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def itopchartuslatinoalbum():
# url = "https://itopchart.com/us/en/music-album-charts/latino/"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "es-MX"})
# res_dict.update({"Language": "es"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "itopchart_us_latino_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def itopchartidalbum():
# req_main_url = "https://itopchart.com/id/id/music-album-charts/"
# res = urllib.urlopen("https://itopchart.com/id/id/music-album-charts/").read()
# song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a class="item_name" href="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(artist)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "id-ID"})
# res_dict.update({"Language": "id"})
# res_dict.update({"Entity_URL": req_main_url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "itopchart_id_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

def saavnalbum():
 url = ["https://www.jiosaavn.com/album", "https://www.jiosaavn.com/search/album=-?p=2"]
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "saavn_album.csv"
 if os.path.exists("saavn_album.csv"):
 os.remove("saavn_album.csv")
 for j in range(len(url)):
 browser.get(url[j])
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('ascii', 'ignore')
 song_list = re.findall(r'<span class="title">\s*<a.*?>(.*?)</a>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="search-cell singers">(.*?)</div>', str(res), flags=re.DOTALL)
 url_list = re.findall(r'<span class="title">\s*<a.*?href="(.*?)"', str(res), flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = re.findall(r'<a title.*?>(.*?)</a>', artist[i])
 artist[i] = str(artist[i])
 artist[i] = artist[i].replace("[", "").replace("]", "").replace("'", "").replace('"', '')
 if "(Album" in song_list[i]:
 song_list[i] = (song_list[i]).partition(" (Album")[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "bn-BD"})
 res_dict.update({"Language": "bn"})
 res_dict.update({"Entity_URL": url[j]})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 # browser.quit()

# def kworbbr():
# url = "https://kworb.net/aww/"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale = re.findall(r'</td><td style.*?>.*?<td style.*?>.*?<td style.*?>.*?</td><td>(.*?)</td>', res,
# flags=re.DOTALL)
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "pt-BR"})
# res_dict.update({"Language": "pt"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_BR.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def kworbde():
# url = "https://kworb.net/eua/"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale = re.findall(r'</td><td style.*?>.*?</td><td>(.*?)</td><td>', res)
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "de-DE"})
# res_dict.update({"Language": "de"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_DE.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def kworbes():
# url = "https://kworb.net/eua/index_full.html"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale_list = re.findall(r'<td style=.*?>.*?<td style=.*?>.*?<td>.*?</td><td>.*?</td><td>(.*?)</td>', res)
# locale = list()
# for i in range(len(locale_list)):
# if i % 2 == 0:
# locale.append(locale_list[i])
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "es-ES"})
# res_dict.update({"Language": "ES"})
# res_dict.update({"Entity_URL": "https://kworb.net/eua/"})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_ES.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def kworbgb():
# url = "https://kworb.net/aww/"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale = re.findall(r'</td><td style.*?>.*?</td><td>(.*?)</td><td>', res)
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "en-GB"})
# res_dict.update({"Language": "en"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_GB.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def kworbit():
# url = "https://kworb.net/eua/"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale = re.findall(r'</td><td style.*?>.*?<td>.*?</td><td>.*?</td><td>(.*?)</td>', res, flags=re.DOTALL)
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "it-IT"})
# res_dict.update({"Language": "IT"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_IT.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def kworbjp():
# url = "https://kworb.net/aww/"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale = re.findall(r'</td><td style.*?>.*?<td>.*?</td><td>.*?</td><td>.*?</td><td>(.*?)</td>', res,
# flags=re.DOTALL)
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ja-JP"})
# res_dict.update({"Language": "ja"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_JP.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def kworbus():
# url = "https://kworb.net/aww/"
# res = urllib.urlopen(url).read()
# item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
# song_list = list()
# artist_list = list()
# for i in range(len(item_box)):
# split_song = item_box[i].split("-", 1)
# song_list.append(split_song[1])
# artist_list.append(split_song[0])
# locale = re.findall(r'</td><td style.*?>(.*?)</td><td>', res)
# locale.sort()
# locale.reverse()
# while ("" in locale):
# locale.remove("")
# res_list = list()
# for i in range(len(locale)):
# song_list[i] = song_list[i].strip()
# artist_list[i] = artist_list[i].strip()
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "en-US"})
# res_dict.update({"Language": "en"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "kworb_US.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

def lafeltrinellialbum():
 url = ["https://www.lafeltrinelli.it/fcom/it/home/pages/catalogo/musica/classifica-cd.html",
 "https://www.lafeltrinelli.it/fcom/it/home/pages/catalogo/musica/classifica-cd?page=2",
 "https://www.lafeltrinelli.it/fcom/it/home/pages/catalogo/musica/classifica-cd?page=3",
 "https://www.lafeltrinelli.it/fcom/it/home/pages/catalogo/musica/classifica-cd?page=4",
 "https://www.lafeltrinelli.it/fcom/it/home/pages/catalogo/musica/classifica-cd?page=5"]
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "lafeltrinelli_album.csv"
 if os.path.exists("lafeltrinelli_album.csv"):
 os.remove("lafeltrinelli_album.csv")
 for j in range(len(url)):
 browser.get(url[j])
 res = browser.page_source
 res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="description"><h3><a.*?>(.*?)</a>', str(res), flags=re.DOTALL)
 song_list = song_list[24:44]
 artist = re.findall(r'</span></a></div>.*?<h3><a.*?>(.*?)<div class="add-to-cart">', str(res))
 artist = artist[24:44]
 url_list = re.findall(r'<div class="description"><h3><a href="(.*?)"', str(res))
 url_list = url_list[24:44]
 res_list = list()
 for i in range(len(song_list)):
 artist_regex = re.search(r'<a class.*?>(.*?)</a>', artist[i])
 if artist_regex:
 artist[i] = artist_regex.group(1)
 else:
 artist[i] = ""
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for k in range(len(feat_list)):
 if feat_list[k] in artist[i]:
 artist[i] = artist[i].partition(feat_list[k])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "IT"})
 res_dict.update({"Entity_URL": url[j]})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 with open(csv_file, 'a') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 if j == 0:
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

def letrasalbum():
 url = "https://www.letras.mus.br/top-albuns/"
 res = requests.get(url).text
 soup = BeautifulSoup(res, 'html.parser')
 main_url = soup.find('meta', attrs={'itemprop': re.compile(r'.*item.*')})
 req_main_url = re.search("(?P<url>https?://[^\s]+)", str(main_url)).group("url")
 req_main_url = req_main_url.replace('"', '')
 song_list = re.findall(r'<b title.*?>(.*?)</b>', str(res))
 artist_list = re.findall(r'</b>\s+<span>(.*?)</span>\s+</a>', str(res), flags=re.DOTALL)
 artist_list = artist_list[0:114]
 url_list = re.findall(r'<a href.*?class="cnt cnt--alb g-1-6">\s<em>', str(res), flags=re.DOTALL)
 for each_item in range(len(url_list)):
 if each_item == 0:
 url_list[each_item] = re.search(r'<div class="top-albuns">(.*?)<em>', url_list[each_item]).group(1)
 url_list[each_item] = re.search(r'<a href="(.*?) class', url_list[each_item]).group(1)
 url_list[each_item] = url_list[each_item].replace('"', '')
 url_list[each_item] = req_main_url[0:25] + url_list[each_item]
 res_list = list()
 for i in range(len(song_list)):
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "letras_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

def mix1album():
 url = "https://www.mix1.de/charts/longplaycharts.htm"
 res = requests.get(url).text
 song_list = re.findall(r'<div class="charts-single-title">(.*?)</div>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="charts-single-interpret">\s*(.*?)\s*</div>', str(res), flags=re.DOTALL)
 url_list = re.findall(r'<div class="charts-single-title">(.*?)</div>', str(res), flags=re.DOTALL)
 req_artist_list = list()
 req_url_list = list()
 req_song_list = list()
 for i in range(len(artist)):
 if i % 2 != 0:
 req_artist_list.append(artist[i])
 for i in range(len(song_list)):
 if i % 2 != 0:
 req_song_list.append(song_list[i])
 for i in range(len(url_list)):
 if i % 2 != 0:
 req_url_list.append(url_list[i])
 for i in range(len(req_url_list)):
 url_regex = re.search(r'<a href="(.*?)"', req_url_list[i])
 if url_regex:
 req_url_list[i] = url_regex.group(1)
 else:
 req_url_list[i] = ""
 supported_url = re.findall(r'<div class="charts-links-block hideonprint"><div class="charts-aff-links">(.*?)</a>',
 res, flags=re.DOTALL)
 supported_url_list = list()
 for i in range(len(supported_url)):
 if i % 2 != 0:
 supported_url_list.append(supported_url[i])
 res_list = list()
 for i in range(len(req_song_list)):
 req_artist_list[i] = req_artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And",
 ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 req_song_list[i] = req_song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 song_regex = re.search(r'<a.*?>(.*?)</a>', req_song_list[i])
 if song_regex:
 req_song_list[i] = song_regex.group(1)
 else:
 song_regex1 = re.search(r'<span.*?>(.*?)</span>', req_song_list[i]).group(1)
 req_song_list[i] = song_regex1
 try:
 if "fa fa-apple" in supported_url_list[i]:
 sup_regex = re.search(r'<a HREF="(.*?)"', supported_url_list[i])
 if sup_regex:
 sup_regex = sup_regex.group(1)
 else:
 sup_regex = ""
 supported_url_list[i] = sup_regex
 else:
 supported_url_list[i] = ""
 except:
 supported_url_list.append("")
 for j in range(len(feat_list)):
 if feat_list[j] in req_artist_list[i]:
 req_artist_list[i] = req_artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": req_song_list[i]})
 res_dict.update({"Artist_Name": req_artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": req_url_list[i]})
 res_dict.update({"Supported_URL": supported_url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "mix1_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

# def mtvalbum():
# url = "http://www.mtv.de/charts/70tgrf/album-top-100"
# browser.get(url)
# while True:
# try:
# time.sleep(10)
# more_buttons = browser.find_element_by_css_selector(".btn-border-dark.float-center.loadMoreBtn")
# more_buttons.click()
# except Exception:
# break
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<div class="videoTitle">(.*?)</div>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="artist regular-content">(.*?)</div>', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "de-DE"})
# res_dict.update({"Language": "de"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "mtv_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# #browser.quit()
# return res_list

# def musicbookalbum():
# url = "http://music-book.jp/music/Ranking/Album/weekly"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<p class="title">(.*?)</p>', res, flags=re.DOTALL)
# song_list = song_list[0:100]
# artist = re.findall(r'<p class="name"><a.*?>(.*?)</a></p>', res)
# url_list = re.findall(r'<a class="mod-btn" href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# url_list[i] = "http://music-book.jp/" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ja-JP"})
# res_dict.update({"Language": "ja"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "music_book_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def musicbugsalbum():
# url = "https://music.bugs.co.kr/chart/album/day/total"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<a.*?class="albumTitle".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<a.*?class="artistTitle".*?>(.*?)</a>', res, flags=re.DOTALL)
# url_list = re.findall(r'<p class="badge">.*?<a href="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# if "</span>" in artist[i]:
# artist[i] = artist[i].partition("</span>")[0]
# print(artist[i])
# song_list[i] = song_list[i].replace("&lt;", "(")
# song_list[i] = song_list[i].replace("&gt;", ")")
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'").replace("&lt;", "(").replace("&gt;", ")").replace("&gt", ")")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'").replace("&lt;",
# "(").replace(
# "&gt", ")")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "music_bugs_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def musicmealbum():
# url = ["https://www.musicme.com/#/classements-cd/", "https://www.musicme.com/#/classements-cd/2.html",
# "https://www.musicme.com/#/classements-cd/3.html", "https://www.musicme.com/#/classements-cd/4.html",
# "https://www.musicme.com/#/classements-cd/5.html", "https://www.musicme.com/#/classements-cd/6.html",
# "https://www.musicme.com/#/classements-cd/7.html", "https://www.musicme.com/#/classements-cd/8.html",
# "https://www.musicme.com/#/classements-cd/9.html", "https://www.musicme.com/#/classements-cd/10.html",
# "https://www.musicme.com/#/classements-cd/11.html", "https://www.musicme.com/#/classements-cd/12.html",
# "https://www.musicme.com/#/classements-cd/13.html", "https://www.musicme.com/#/classements-cd/14.html",
# "https://www.musicme.com/#/classements-cd/15.html"]
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "music_me_album.csv"
# if os.path.exists("music_me_album.csv"):
# os.remove("music_me_album.csv")
# for j in range(len(url)):
# browser.get(url[j])
# time.sleep(20)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'</div>\s*<dl>\s*<dt><a href.*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<dd class="artist">\s*(.*?)\s*</dd>', res)
# url_list = re.findall(r'<div class="thumb pht170">\s*<a href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist[i])
# if artist_regex:
# artist[i] = artist_regex.group(1)
# else:
# artist[i] = ""
# url_list[i] = "https://music.naver.com/" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for k in range(len(feat_list)):
# if feat_list[k] in artist[i]:
# artist[i] = artist[i].partition(feat_list[k])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Entity_URL": url[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# #browser.quit()

# def musicnaveralbum():
# url = ["https://music.naver.com/listen/newRelease.nhn?domain=DOMESTIC",
# "https://music.naver.com/listen/newRelease.nhn?domain=DOMESTIC&page=2&display=18",
# "https://music.naver.com/listen/newRelease.nhn?domain=DOMESTIC&page=3&display=18",
# "https://music.naver.com/listen/newRelease.nhn?domain=DOMESTIC&page=4&display=18",
# "https://music.naver.com/listen/newRelease.nhn?domain=DOMESTIC&page=5&display=18"]
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "music_naver_album.csv"
# if os.path.exists("music_naver_album.csv"):
# os.remove("music_naver_album.csv")
# for j in range(len(url)):
# res = urllib.urlopen(url[j]).read()
# time.sleep(10)
# song_list = re.findall(r'</div>\s*<dl>\s*<dt><a href.*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<dd class="artist">\s*(.*?)\s*</dd>', res)
# url_list = re.findall(r'<div class="thumb pht170">\s*<a href="(.*?)"', res)
# res_list = list()
# for i in range(len(song_list)):
# artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist[i])
# if artist_regex:
# artist[i] = artist_regex.group(1)
# else:
# artist[i] = ""
# url_list[i] = "https://music.naver.com/" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for k in range(len(feat_list)):
# if feat_list[k] in artist[i]:
# artist[i] = artist[i].partition(feat_list[k])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Entity_URL": url[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)

def officialchartsalbum():
 url = "https://www.offiziellecharts.de/charts/album"
 res = requests.get(url).text
 song_list = re.findall(r'<span class="info-title">(.*?)</span>', res, flags=re.DOTALL)
 artist = re.findall(r'<span class="info-artist">(.*?)</span>', res, flags=re.DOTALL)
 url_list = re.findall(r'<a class="drill-down"\s*href="(.*?)"', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 url_list[i] = "https://www.offiziellecharts.de/" + url_list[i]
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "official_charts_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

# def oriconalbum():
# url = "https://www.oricon.co.jp/rank/ja/w/"
# browser.get(url)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('ascii', 'ignore')
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "oricon_album.csv"
# if os.path.exists("oricon_album.csv"):
# os.remove("oricon_album.csv")
# url_list_all_page = re.findall(r'<div class="block-rank-pager-bottom mt20">(.*?)</div>', res, flags=re.DOTALL)
# url_regex_all_page = re.findall(r'<li><a href="(.*?)"', url_list_all_page[0])
# for i in range(len(url_regex_all_page)):
# url_regex_all_page[i] = "https://www.oricon.co.jp" + url_regex_all_page[i]
# for j in range(len(url_regex_all_page)):
# result = browser.get(url_regex_all_page[j])
# result = browser.page_source
# result = unicodedata.normalize('NFKD', result).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', result, flags=re.DOTALL)
# artist = re.findall(r'<p class="name">(.*?)</p>', result, flags=re.DOTALL)
# url_list = re.findall(r'<div class="ribbon">\s*.*?<div class="inner">(.*?)<p class="image">\s*<span>', result,
# flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# url_regex = re.search(r'<a href="(.*?)"', url_list[i])
# if url_regex:
# url_list[i] = "https://www.oricon.co.jp" + url_regex.group(1)
# else:
# url_list[i] = ""
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Entity_URL": url_regex_all_page[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# #browser.quit()

# def popvertexlatinalbum():
# url = "http://www.popvortex.com/music/charts/top-latin-albums.php"
# browser.get(url)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<cite class="title">(.*?)</cite>', res, flags=re.DOTALL)
# artist = re.findall(r'<em class="artist">(.*?)</em>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a class="buy-button button" href="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "es-MX"})
# res_dict.update({"Language": "es"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "popvertex_latin_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# #browser.quit()
# return res_list

# def popvertexmexicoalbum():
# url = "http://www.popvortex.com/music/mexico/top-albums.php"
# browser.get(url)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<cite class="title" itemprop="name"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<span itemprop="name">(.*?)</span>', res, flags=re.DOTALL)
# url_list = re.findall(r'<a rel="nofollow" href="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "es-MX"})
# res_dict.update({"Language": "es"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": url_list[i]})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "popvertex_mexico_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# #browser.quit()
# return res_list

# def recochokualbum():
# url = "https://recochoku.jp/ranking/album/weekly/"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<br/>\s*<a.*?class="ttl">(.*?)</a>', res, flags=re.DOTALL)
# song_list = song_list[2:52]
# artist = re.findall(r'class="ttl">.*?<p>(.*?)</p>', res, flags=re.DOTALL)
# artist = artist[1:51]
# url_list = re.findall(r'<br/>\s*<a href="(.*?)" class="ttl">', res)
# url_list = url_list[1:51]
# res_list = list()
# for i in range(len(song_list)):
# url_list[i] = url_list[i].replace('"', '')
# url_list[i] = "https://recochoku.jp" + url_list[i]
# artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist[i])
# if artist_regex:
# artist[i] = artist_regex.group(1)
# else:
# artist[i] = ""
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ja-JP"})
# res_dict.update({"Language": "ja"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "recochoku_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

def rockolalbum():
 url = "https://www.rockol.it/classifiche-musicali/7/Top-of-the-Music?refresh_ce"
 res = requests.get(url).text
 song_list = re.findall(r'<h3 class="font-black heading uppercase text-lg">(.*?)</h3>', res, flags=re.DOTALL)
 artist = re.findall(r'<div class="uppercase text-lg">\s*<a.*?>\s*(.*?)\s*</a>', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "rockol_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

def rollingstonealbum():
 url = "http://www.rollingstone.com/music/lists/10-best-latin-albums-of-the-year-20151230/luzmila-carpio-yuyay-japina-tapes-20151230"
 res = requests.get(url).text
 item_regex = re.findall(r'<h3 class="c-list__title t-bold">\s*(.*?)\s*</h3>', res, flags=re.DOTALL)
 res_list = list()
 for i in range(len(item_regex)):
 item_regex[i] = item_regex[i].split(",")
 item_regex[i][0] = item_regex[i][0].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(
 " &", ",").replace('&#034;', '"').replace("&#039;", "'").strip()
 item_regex[i][1] = item_regex[i][1].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;",
 "'").strip().replace(
 "&#8216;", "'").replace("&#8217;", "'").replace(",#8216;", "'")
 res_dict = dict()
 res_dict.update({"Album_Name": item_regex[i][1]})
 res_dict.update({"Artist_Name": item_regex[i][0]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "rollingstone_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list

# def vagalumealbum():
# url = "https://www.vagalume.com.br/top100/albuns/geral"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<a class="w1 h22".*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<p class=styleBlack>(.*?)</div>', res)
# url_list = re.findall(r'<a class="w1 h22" href=(.*?)>', res)
# res_list = list()
# for i in range(len(song_list)):
# url_list[i] = "https://www.vagalume.com.br" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "pt-BR"})
# res_dict.update({"Language": "pt"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "vagalume_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def billboardjapan():
# url = "http://www.billboard-japan.com/charts/detail?a=hot_albums"
# res = urllib.urlopen(url).read()
# song_list = re.findall(r'<p class="musuc_title">(.*?)</p>', res)
# artist_list = re.findall(r'<p class="artist_name">(.*?)</p>', res)
# url_list = re.findall(r'<div class="right_detail">\s*(.*?)\s*</div>', res)
# res_list = list()
# for i in range(len(song_list)):
# url_regex = re.search(r'<a href="(.*?)"', url_list[i])
# if url_regex:
# url_list[i] = "http://www.billboard-japan.com/" + url_regex.group(1)
# else:
# url_list[i] = ""
# artist_regex = re.search(r'<a href.*?>(.*?)</a>', artist_list[i])
# if artist_regex:
# artist_list[i] = artist_regex.group(1)
# artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist_list[i]:
# artist_list[i] = artist_list[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist_list[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ja-JP"})
# res_dict.update({"Language": "ja"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# res_list = res_list[0:199]
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "billboard_japan_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

# def melonalbum():
# url = ["https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=22",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=43",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=64",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=85"]
# csv_file = "melon_album.csv"
# if os.path.exists("melon_album.csv"):
# os.remove("melon_album.csv")
# for j in range(len(url)):
# res = browser.get(url[j])
# time.sleep(5)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<a.*?class="ellipsis".*?>(.*?)</a>', res, flags=re.DOTALL)
# song_list = song_list[0:21]
# artist = re.findall(r'<div class="ellipsis">\s*(.*?)</div>', res, flags=re.DOTALL)
# artist = artist[0:21]
# url_list = re.findall(r"<a href=\".*?melon\.link\.goAlbumDetail\('(.*?)'\);\".*? class=\"thumb\">", res)
# res_list = list()
# for i in range(len(song_list)):
# artist_regex1 = re.search(r'<a.*?><a.*?>(.*?)</a>', artist[i])
# if artist_regex1:
# artist[i] = artist_regex1.group(1)
# else:
# artist_regex2 = re.search(r'<span.*?>(.*?)</span>', artist[i])
# if artist_regex2:
# artist[i] = artist_regex2.group(1)
# url_list[i] = "https://www.melon.com/album/detail.htm?albumId=" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Entity_URL": url[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)

# def fimialbum():
# url = "https://www.fimi.it/top-of-the-music/classifiche.kl#/charts/1"
# browser.get(url)
# time.sleep(5)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<div class="chart-section-element-title">(.*?)</div>', res, flags=re.DOTALL)
# song_list = song_list[0:100]
# artist = re.findall(r'<div class="chart-section-element-author">(.*?)</div>', res)
# artist = artist[0:100]
# res_list = list()
# for i in range(len(song_list)):
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for j in range(len(feat_list)):
# if feat_list[j] in artist[i]:
# artist[i] = artist[i].partition(feat_list[j])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "it-IT"})
# res_dict.update({"Language": "it"})
# res_dict.update({"Entity_URL": url})
# res_dict.update({"Detail_URL": ""})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "fimi_album.csv"
# with open(csv_file, 'w') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# return res_list

def snepalbum():
 try:
 url = "https://snepmusique.com/les-tops/le-top-de-la-semaine/top-albums/"
 browser.get(url)
 time.sleep(5)
 res = browser.page_source
 # res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
 song_list = re.findall(r'<div class="titre">(.*?)</div>', str(res), flags=re.DOTALL)
 artist = re.findall(r'<div class="artiste">(.*?)</div>', str(res))
 res_list = list()
 for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "fr-FR"})
 res_dict.update({"Language": "fr"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
 csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
 csv_file = "snep_album.csv"
 with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
 return res_list
 except TimeoutException:
 print("Loading took too much time!")


# def musicme():
# url = ["https://www.musicme.com/#/classements-cd/',options=%22/", "https://www.musicme.com/#/classements-cd/2.html",
# "https://www.musicme.com/#/classements-cd/3.html", "https://www.musicme.com/#/classements-cd/4.html",
# "https://www.musicme.com/#/classements-cd/5.html", "https://www.musicme.com/#/classements-cd/6.html",
# "https://www.musicme.com/#/classements-cd/7.html", "https://www.musicme.com/#/classements-cd/8.html",
# "https://www.musicme.com/#/classements-cd/9.html", "https://www.musicme.com/#/classements-cd/10.html",
# "https://www.musicme.com/#/classements-cd/11.html", "https://www.musicme.com/#/classements-cd/12.html",
# "https://www.musicme.com/#/classements-cd/13.html", "https://www.musicme.com/#/classements-cd/14.html",
# "https://www.musicme.com/#/classements-cd/15.html"]
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "music_me_album.csv"
# if os.path.exists("music_me_album.csv"):
# os.remove("music_me_album.csv")
# for j in range(len(url)):
# browser.get(url[j])
# time.sleep(15)
# browser.switch_to.frame(browser.find_element_by_id('frmmain'))
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<span class="itemcoltxt"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
# artist = re.findall(r'<div class="itemcolalbline1"><a.*?>(.*?)</a>', res, flags=re.DOTALL)
# url_list = re.findall(r'<span class="itemcoltxt"><a href="(.*?)"', res, flags=re.DOTALL)
# res_list = list()
# for i in range(len(song_list)):
# url_list[i] = "https://www.musicme.com/#" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# for k in range(len(feat_list)):
# if feat_list[k] in artist[i]:
# artist[i] = artist[i].partition(feat_list[k])[0]
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": ""})
# res_dict.update({"Locale": "fr-FR"})
# res_dict.update({"Language": "fr"})
# res_dict.update({"Entity_URL": url[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)

billboard_album = billboardalbum()
print(billboard_album)
print(len(billboard_album))
# print("**************************************************************")
# billboard_latin_album = billboardlatinalbum()
# print(billboard_latin_album)
# print(len(billboard_latin_album))
# print("**************************************************************")
# billboard_mexican_album = billboardmexicanalbum()
# print(billboard_mexican_album)
# print(len(billboard_mexican_album))
# print("**************************************************************")
# billboard_tropical_album = billboardtropicalalbum()
# print(billboard_tropical_album)
# print(len(billboard_tropical_album))
print("**************************************************************")
charts_album = chartsalbum()
print(charts_album)
print(len(charts_album))
print("**************************************************************")
# charts_in_france_album = chartsinfrancealbum()
# print(charts_in_france_album)
# print(len(charts_in_france_album))
# print("**************************************************************")
# charts_in_france1_album = chartsinfrance1album()
# print(charts_in_france1_album)
# print(len(charts_in_france1_album))
# print("**************************************************************")
chart_surfer_album = chartsurferalbum()
print(chart_surfer_album)
print(len(chart_surfer_album))
print("**************************************************************")
# elcorteinglesalbum()
# print("**************************************************************")
# gaon_album = gaonalbum()
# print(gaon_album)
# print(len(gaon_album))
# print("**************************************************************")
ibsalbum()
print("**************************************************************")
# itopchart_christian_album = itopchartchristianalbum()
# print(itopchart_christian_album)
# print(len(itopchart_christian_album))
# print("**************************************************************")
# itopchart_french_album = itopchartfrenchalbum()
# print(itopchart_french_album)
# print(len(itopchart_french_album))
# print("**************************************************************")
# itopchart_mx_latino_album = itopchartmxlatinoalbum()
# print(itopchart_mx_latino_album)
# print(len(itopchart_mx_latino_album))
# print("**************************************************************")
# itopchart_us_latino_album = itopchartuslatinoalbum()
# print(itopchart_us_latino_album)
# print(len(itopchart_us_latino_album))
# print("**************************************************************")
# itopchart_id_album = itopchartidalbum()
# print(itopchart_id_album)
# print(len(itopchart_id_album))
# print("**************************************************************")
saavnalbum()
print("**************************************************************")
# kworb_br = kworbbr()
# print(kworb_br)
# print(len(kworb_br))
# print("**************************************************************")
# kworb_de = kworbde()
# print(kworb_de)
# print(len(kworb_de))
# print("**************************************************************")
# kworb_es = kworbes()
# print(kworb_es)
# print(len(kworb_es))
# print("**************************************************************")
# kworb_gb = kworbgb()
# print(kworb_gb)
# print(len(kworb_gb))
# print("**************************************************************")
# kworb_it = kworbit()
# print(kworb_it)
# print(len(kworb_it))
# print("**************************************************************")
# kworb_jp = kworbjp()
# print(kworb_jp)
# print(len(kworb_jp))
# print("**************************************************************")
# kworb_us = kworbus()
# print(kworb_us)
# print(len(kworb_us))
# print("**************************************************************")
lafeltrinellialbum()
print("**************************************************************")
letras_album = letrasalbum()
print(letras_album)
print(len(letras_album))
print("**************************************************************")
mix1_album = mix1album()
print(mix1_album)
print(len(mix1_album))
print("**************************************************************")
# mtv_album = mtvalbum()
# print(mtv_album)
# print(len(mtv_album))
# print("**************************************************************")
# music_book_album = musicbookalbum()
# print(music_book_album)
# print(len(music_book_album))
# print("**************************************************************")
# music_bugs_album = musicbugsalbum()
# print(music_bugs_album)
# print(len(music_bugs_album))
# print("**************************************************************")
# musicnaveralbum()
# print("**************************************************************")
official_charts_album = officialchartsalbum()
print(official_charts_album)
print(len(official_charts_album))
# print("**************************************************************")
# oriconalbum()
# print("**************************************************************")
# popvertex_latin_album = popvertexlatinalbum()
# print(popvertex_latin_album)
# print(len(popvertex_latin_album))
# print("**************************************************************")
# popvertex_mexico_album = popvertexmexicoalbum()
# print(popvertex_mexico_album)
# print(len(popvertex_mexico_album))
# print("**************************************************************")
# recochoku_album = recochokualbum()
# print(recochoku_album)
# print(len(recochoku_album))
# print("**************************************************************")
rockol_album = rockolalbum()
print(rockol_album)
print(len(rockol_album))
print("**************************************************************")
# vagalume_album = vagalumealbum()
# print(vagalume_album)
# print(len(vagalume_album))
# print("**************************************************************")
# billboard_japan_album = billboardjapan()
# print(billboard_japan_album)
# print(len(billboard_japan_album))
# print("**************************************************************")
# melonalbum()
# print("**************************************************************")
# fimi_album = fimialbum()
# print(fimi_album)
# print(len(fimi_album))
# print("**************************************************************")
snep_album = snepalbum()
# print(snep_album)
# print(len(snep_album))
# print("**************************************************************")
# # musicme()
# print("**************************************************************")

fout = open("out_album.csv", "a")
for line in open("billboard_album.csv"):
 fout.write(line)
os.remove("billboard_album.csv")
# for line in open("billboard_latin_album.csv"):
# fout.write(line)
# os.remove("billboard_latin_album.csv")
# for line in open("billboard_mexican_album.csv"):
# fout.write(line)
# os.remove("billboard_mexican_album.csv")
# for line in open("billboard_tropical_album.csv"):
# fout.write(line)
# os.remove("billboard_tropical_album.csv")
for line in open("charts_album.csv"):
 fout.write(line)
os.remove("charts_album.csv")
# for line in open("chartsinfrance1_album.csv"):
# fout.write(line)
# os.remove("chartsinfrance1_album.csv")
for line in open("chartsurfer_album.csv"):
 fout.write(line)
os.remove("chartsurfer_album.csv")
# for line in open("elcorteingles_album.csv"):
# fout.write(line)
# os.remove("elcorteingles_album.csv")
# for line in open("gaon_album.csv"):
# fout.write(line)
# os.remove("gaon_album.csv")
for line in open("ibs_album.csv"):
 fout.write(line)
os.remove("ibs_album.csv")
# for line in open("itopchart_christian_album.csv"):
# fout.write(line)
# os.remove("itopchart_christian_album.csv")
# for line in open("itopchart_french_album.csv"):
# fout.write(line)
# os.remove("itopchart_french_album.csv")
# for line in open("itopchart_mx_latino_album.csv"):
# fout.write(line)
# os.remove("itopchart_mx_latino_album.csv")
# for line in open("itopchart_us_latino_album.csv"):
# fout.write(line)
# os.remove("itopchart_us_latino_album.csv")
# for line in open("itopchart_id_album.csv"):
# fout.write(line)
# os.remove("itopchart_id_album.csv")
for line in open("saavn_album.csv"):
 fout.write(line)
os.remove("saavn_album.csv")
# for line in open("kworb_BR.csv"):
# fout.write(line)
# os.remove("kworb_BR.csv")
# for line in open("kworb_DE.csv"):
# fout.write(line)
# os.remove("kworb_DE.csv")
# for line in open("kworb_ES.csv"):
# fout.write(line)
# os.remove("kworb_ES.csv")
# for line in open("kworb_GB.csv"):
# fout.write(line)
# os.remove("kworb_GB.csv")
# for line in open("kworb_IT.csv"):
# fout.write(line)
# os.remove("kworb_IT.csv")
# for line in open("kworb_JP.csv"):
# fout.write(line)
# os.remove("kworb_JP.csv")
# for line in open("kworb_US.csv"):
# fout.write(line)
# os.remove("kworb_US.csv")
for line in open("lafeltrinelli_album.csv"):
 fout.write(line)
os.remove("lafeltrinelli_album.csv")
for line in open("letras_album.csv"):
 fout.write(line)
os.remove("letras_album.csv")
for line in open("mix1_album.csv"):
 fout.write(line)
os.remove("mix1_album.csv")
# for line in open("mtv_album.csv"):
# fout.write(line)
# os.remove("mtv_album.csv")
# for line in open("music_book_album.csv"):
# fout.write(line)
# os.remove("music_book_album.csv")
# for line in open("music_bugs_album.csv"):
# fout.write(line)
# os.remove("music_bugs_album.csv")
# for line in open("music_naver_album.csv"):
# fout.write(line)
# os.remove("music_naver_album.csv")
for line in open("official_charts_album.csv"):
 fout.write(line)
os.remove("official_charts_album.csv")
# for line in open("oricon_album.csv"):
# fout.write(line)
# os.remove("oricon_album.csv")
# for line in open("popvertex_latin_album.csv"):
# fout.write(line)
# os.remove("popvertex_latin_album.csv")
# for line in open("popvertex_mexico_album.csv"):
# fout.write(line)
# os.remove("popvertex_mexico_album.csv")
# for line in open("recochoku_album.csv"):
# fout.write(line)
# os.remove("recochoku_album.csv")
for line in open("rockol_album.csv"):
 fout.write(line)
os.remove("rockol_album.csv")
# for line in open("vagalume_album.csv"):
# fout.write(line)
# os.remove("vagalume_album.csv")
# for line in open("billboard_japan_album.csv"):
# fout.write(line)
# os.remove("billboard_japan_album.csv")
# for line in open("melon_album.csv"):
# fout.write(line)
# os.remove("melon_album.csv")
# for line in open("fimi_album.csv"):
# fout.write(line)
# os.remove("fimi_album.csv")
# for line in open("snep_album.csv"):
# fout.write(line)
# os.remove("snep_album.csv")
# for line in open("music_me_album.csv"):
# fout.write(line)
# os.remove("music_me_album.csv")
fout.close()
browser.quit()
#fimi.py
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import time
import os
from selenium import webdriver
import unicodedata

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
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
url = "https://www.fimi.it/top-of-the-music/classifiche.kl#/charts/1"
browser.get(url)
time.sleep(5)
res = browser.page_source
res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
song_list = re.findall(r'<div class="chart-section-element-title">(.*?)</div>', str(res), flags=re.DOTALL)
song_list = song_list[0:100]
artist = re.findall(r'<div class="chart-section-element-author">(.*?)</div>', str(res))
artist = artist[0:100]
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": ""})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "it"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
csv_file = "fimi_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()
# #melon.py
# from selenium import webdriver
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import os
# import unicodedata
# import time
# # sys.stdout = codecs.getwriter('utf8')(sys.stdout)
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
# url = ["https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=22",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=43",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=64",
# "https://www.melon.com/search/album/index.htm?q=album&section=&searchGnbYn=Y&ipath=srch_form#params%5Bq%5D=album&params%5Bsortorder%5D=&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex=85"]
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# csv_file = "melon1_album.csv"
# if os.path.exists("melon1_album.csv"):
# os.remove("melon1_album.csv")
# for j in range(len(url)):
# print(url[j])
# res = browser.get(url[j])
# time.sleep(5)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<a.*?class="ellipsis".*?>(.*?)</a>', str(res), flags=re.DOTALL)
# song_list = song_list[0:21]
# artist = re.findall(r'<div class="ellipsis">\s*(.*?)</div>', str(res), flags=re.DOTALL)
# artist = artist[0:21]
# url_list = re.findall(r"<a href=\".*?melon\.link\.goAlbumDetail\('(.*?)'\);\".*? class=\"thumb\">", str(res))
# res_list = list()
# for i in range(len(song_list)):
# artist_regex1 = re.search(r'<a.*?><a.*?>(.*?)</a>', artist[i])
# if artist_regex1:
# artist[i] = artist_regex1.group(1)
# else:
# artist_regex2 = re.search(r'<span.*?>(.*?)</span>', artist[i])
# if artist_regex2:
# artist[i] = artist_regex2.group(1)
# url_list[i] = "https://www.melon.com/album/detail.htm?albumId=" + url_list[i]
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ko-KR"})
# res_dict.update({"Language": "ko"})
# res_dict.update({"Entity_URL": url[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# print(res_list)
# print(len(res_list))
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# browser.close()
#mtv_album.py
from selenium import webdriver
import csv
import re
from datetime import date
from datetime import datetime
import unicodedata
import time

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
url = "http://www.mtv.de/charts/70tgrf/album-top-100"
browser.get(url)
while True:
 try:
 time.sleep(10)
 more_buttons = browser.find_element(By.CSS_SELECTOR, ".btn-border-dark.float-center.loadMoreBtn")
 more_buttons.click()
 except Exception:
 break
res = browser.page_source
res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring", " (Album"]
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
song_list = re.findall(r'<div class="videoTitle">(.*?)</div>', str(res), flags=re.DOTALL)
artist = re.findall(r'<div class="artist regular-content">(.*?)</div>', str(res), flags=re.DOTALL)
res_list = list()
for i in range(len(artist)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "de-DE"})
 res_dict.update({"Language": "de"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
csv_file = "mtv_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

browser.quit()
#oricon.py
# from selenium import webdriver
# import re
# import urllib
# from datetime import datetime
# from datetime import date
# import csv
# import os
# import unicodedata
# import sys
# import codecs
#
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
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
# url = "https://www.oricon.co.jp/rank/ja/w/"
# chromedriver = Service("/usr/local/bin/chromedriver")
# op = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=chromedriver, options=op)
# browser.get(url)
# res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('ascii', 'ignore')
# csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
# 'Supported_URL', 'Entity Type']
# csv_file = "oricon_album.csv"
# if os.path.exists("oricon_album.csv"):
# os.remove("oricon_album.csv")
# url_list_all_page = re.findall(r'<div class="block-rank-pager-bottom mt20">(.*?)</div>', str(res), flags=re.DOTALL)
# url_regex_all_page = re.findall(r'<li><a href="(.*?)"', url_list_all_page[0])
# for i in range(len(url_regex_all_page)):
# url_regex_all_page[i] = "https://www.oricon.co.jp" + url_regex_all_page[i]
# # print(url_regex_all_page)
# for j in range(len(url_regex_all_page)):
# result = browser.get(url_regex_all_page[j])
# result = browser.page_source
# result = unicodedata.normalize('NFKD', result).encode('UTF-8', 'ignore')
# song_list = re.findall(r'<h2 class="title" itemprop="name">(.*?)</h2>', str(result), flags=re.DOTALL)
# # print(song_list)
# # print(len(song_list))
# artist = re.findall(r'<p class="name">(.*?)</p>', str(result), flags=re.DOTALL)
# # print(artist)
# # print(len(artist))
# url_list = re.findall(r'<div class="ribbon">\s*.*?<div class="inner">(.*?)<p class="image">\s*<span>', str(result),
# flags=re.DOTALL)
# # print(url_list)
# # print(len(url_list))
# res_list = list()
# for i in range(len(song_list)):
# url_regex = re.search(r'<a href="(.*?)"', url_list[i])
# if url_regex:
# url_list[i] = "https://www.oricon.co.jp" + url_regex.group(1)
# else:
# url_list[i] = ""
# artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
# ",").replace(
# '&#034;', '"').replace("&#039;", "'")
# song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
# res_dict = dict()
# res_dict.update({"Album_Name": song_list[i]})
# res_dict.update({"Artist_Name": artist[i]})
# res_dict.update({"Extraction Time": day_date_time})
# res_dict.update({"Locale": "ja-JP"})
# res_dict.update({"Language": "ja"})
# res_dict.update({"Entity_URL": url_regex_all_page[j]})
# res_dict.update({"Detail_URL": url_list[i]})
# res_dict.update({"Supported_URL": ""})
# res_dict.update({"Entity Type": "/music/album"})
# res_list.append(res_dict)
# # print(res_list)
# # print(len(res_list))
# with open(csv_file, 'a') as csvfile:
# writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# if j == 0:
# writer.writeheader()
# for data in res_list:
# writer.writerow(data)
# browser.close()
#popvertex_latin_album.py
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import unicodedata
import time
from selenium import webdriver

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
url = "http://www.popvortex.com/music/charts/top-latin-albums.php"
browser.get(url)
res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
song_list = re.findall(r'<cite class="title">(.*?)</cite>', str(res), flags=re.DOTALL)
artist = re.findall(r'<em class="artist">(.*?)</em>', str(res), flags=re.DOTALL)
url_list = re.findall(r'<a class="buy-button button" href="(.*?)"', str(res), flags=re.DOTALL)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
csv_file = "popvertex_latin_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()
#popvertex_mexico.py
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import unicodedata
import time
from selenium import webdriver

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
url = "http://www.popvortex.com/music/mexico/top-albums.php"
browser.get(url)
res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
song_list = re.findall(r'<cite class="title" itemprop="name"><a.*?>(.*?)</a>', str(res), flags=re.DOTALL)
artist = re.findall(r'<span itemprop="name">(.*?)</span>', str(res), flags=re.DOTALL)
url_list = re.findall(r'<a rel="nofollow" href="(.*?)"', str(res), flags=re.DOTALL)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
csv_file = "popvertex_mexico_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()

#Moving files
# import shutil
# root = '/home/akhilbhatnagar/Downloads/pycharm-community-2019.3.4/bin/musiccrawl_out/'
# filenames = ['fimi','melon1','mtv','oricon','out','popvertex_latin','popvertex_mexico']
# for file in filenames:
# shutil.move(file + '_album.csv' , root + file + '_album.csv')


import re
import bs4
from datetime import datetime
from datetime import date
import csv
import requests

req_main_url = "https://itopchart.com/id/id/music-album-charts/"
res = requests.get("https://itopchart.com/id/id/music-album-charts/").text
song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
url_list = re.findall(r'<a class="item_name" href="(.*?)"', res, flags=re.DOTALL)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = date.today()
wd = date.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = days[wd]
day_date_time = day + " " + str(date) + " " + current_time
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
res_list = list()
for i in range(len(artist)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "id-ID"})
 res_dict.update({"Language": "id"})
 res_dict.update({"Entity_URL": req_main_url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "itopchart_id_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)


import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://itopchart.com/mx/en/music-album-charts/latino/"
res = requests.get(url).text
song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "itopchart_mx_latino_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://itopchart.com/us/en/music-album-charts/latino/"
res = requests.get(url).text
song_list = re.findall(r'<a class="item_name".*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<div class="artist">(.*?)</div>', res, flags=re.DOTALL)
url_list = re.findall(r'<a class="item_name" href="(.*?)"', res)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "itopchart_us_latino_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import requests
from datetime import datetime
from datetime import date
import csv

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
url = "https://kworb.net/aww/"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale = re.findall(r'</td><td style.*?>.*?<td style.*?>.*?<td style.*?>.*?</td><td>(.*?)</td>', res, flags=re.DOTALL)
locale.sort()
locale.reverse()
print(locale)
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_BR.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import requests
from datetime import datetime
from datetime import date
import csv

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
url = "https://kworb.net/aww/"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale = re.findall(r'</td><td style.*?>.*?</td><td>(.*?)</td><td>', res)
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-GB"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_GB.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import urllib
from datetime import datetime
from datetime import date
import csv
import requests

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
url = "https://kworb.net/eua/"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale = re.findall(r'</td><td style.*?>.*?<td>.*?</td><td>.*?</td><td>(.*?)</td>', res, flags=re.DOTALL)
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "it-IT"})
 res_dict.update({"Language": "IT"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_IT.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import requests
from datetime import datetime
from datetime import date
import csv

import requests

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
url = "https://kworb.net/aww/"
res = requests.get(url).text
item_box = re.findall(r'<td class="mp text"><div>(.*?)</div>', res)
song_list = list()
artist_list = list()
for i in range(len(item_box)):
 split_song = item_box[i].split("-", 1)
 song_list.append(split_song[1])
 artist_list.append(split_song[0])
locale = re.findall(r'</td><td style.*?>(.*?)</td><td>', res)
locale.sort()
locale.reverse()
while("" in locale) :
 locale.remove("")
res_list = list()
for i in range(len(locale)):
 song_list[i] = song_list[i].strip()
 artist_list[i] = artist_list[i].strip()
 artist_list[i] = artist_list[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist_list[i]:
 artist_list[i] = artist_list[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist_list[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "en-US"})
 res_dict.update({"Language": "en"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "kworb_US.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

import re
import requests
from datetime import datetime
from datetime import date
import csv

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
url = "https://www.vagalume.com.br/top100/albuns/geral"
res = requests.get(url).text
song_list = re.findall(r'<a class="w1 h22".*?>(.*?)</a>', res, flags=re.DOTALL)
artist = re.findall(r'<p class=styleBlack>(.*?)</div>', res)
url_list = re.findall(r'<a class="w1 h22" href=(.*?)>', res)
res_list = list()
for i in range(len(song_list)):
 url_list[i] = "https://www.vagalume.com.br" + url_list[i]
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "pt-BR"})
 res_dict.update({"Language": "pt"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": url_list[i]})
 res_dict.update({"Supported_URL": ""})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL', 'Supported_URL', 'Entity Type']
csv_file = "vagalume_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)

#popvertex_latin_album.py
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver
import unicodedata

options = Options()
options.add_argument('--headless') # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
feat_list = [" feat", " ft", " featuring", " FEAT", " Feat", " Ft", " FT", "Featuring"]
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import unicodedata
import time
from selenium import webdriver

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
url = "http://www.popvortex.com/music/charts/top-latin-albums.php"
browser.get(url)
res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
song_list = re.findall(r'<cite class="title">(.*?)</cite>', str(res), flags=re.DOTALL)
artist = re.findall(r'<em class="artist">(.*?)</em>', str(res), flags=re.DOTALL)
url_list = re.findall(r'<a class="buy-button button" href="(.*?)"', str(res), flags=re.DOTALL)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
csv_file = "popvertex_latin_album.csv"
with open(csv_file, 'w') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
 writer.writeheader()
 for data in res_list:
 writer.writerow(data)
browser.close()

#popvertex_mexico.py
import re
import urllib
from datetime import datetime
from datetime import date
import csv
import unicodedata
import time
from selenium import webdriver

chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
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
url = "http://www.popvortex.com/music/mexico/top-albums.php"
browser.get(url)
res = browser.page_source
# res = unicodedata.normalize('NFKD', res).encode('UTF-8', 'ignore')
song_list = re.findall(r'<cite class="title" itemprop="name"><a.*?>(.*?)</a>', str(res), flags=re.DOTALL)
artist = re.findall(r'<span itemprop="name">(.*?)</span>', str(res), flags=re.DOTALL)
url_list = re.findall(r'<a rel="nofollow" href="(.*?)"', str(res), flags=re.DOTALL)
res_list = list()
for i in range(len(song_list)):
 artist[i] = artist[i].replace(" &amp;", ",").replace(" and", ",").replace(" And", ",").replace(" &",
 ",").replace(
 '&#034;', '"').replace("&#039;", "'")
 song_list[i] = song_list[i].replace("&amp;", "&").replace('&#034;', '"').replace("&#039;", "'")
 for j in range(len(feat_list)):
 if feat_list[j] in artist[i]:
 artist[i] = artist[i].partition(feat_list[j])[0]
 res_dict = dict()
 res_dict.update({"Album_Name": song_list[i]})
 res_dict.update({"Artist_Name": artist[i]})
 res_dict.update({"Extraction Time": day_date_time})
 res_dict.update({"Locale": "es-MX"})
 res_dict.update({"Language": "es"})
 res_dict.update({"Entity_URL": url})
 res_dict.update({"Detail_URL": ""})
 res_dict.update({"Supported_URL": url_list[i]})
 res_dict.update({"Entity Type": "/music/album"})
 res_list.append(res_dict)
print(res_list)
print(len(res_list))
csv_columns = ['Album_Name', 'Artist_Name', 'Extraction Time', 'Locale', 'Language', 'Entity_URL', 'Detail_URL',
 'Supported_URL', 'Entity Type']
csv_file = "popvertex_mexico_album.csv"
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
url = 'https://www.billboard.com/charts/billboard-200/'
response = requests.get(url)
locale = "en-US"
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
delay = 1
# timeout =20
try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.CLASS_NAME, 'o-chart-results-list-row-container')
print(len(itembox))
# for x in itembox:
# print(x.text)
rank =1
for i in itembox:
 songs = i.find_elements(By.XPATH,'/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div/ul/li[4]/ul/li[1]/h3')
 author = i.find_elements(By.XPATH,'/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div/ul/li[4]/ul/li[1]/span')
for s in songs:
 print(s.text)
 data['Title'].append(s.text.strip())
for a in author:
 # print(a.text.strip())
 data['Artist'].append(a.text.strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Url'].append('')
 data['Supported Url'].append('https://www.billboard.com/charts/billboard-200/?rank=' + str(rank))
 rank = rank+1
file_name = ' billboard200_albums.csv'
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
url = 'https://www.letras.mus.br/top-albuns/'
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
timeout =30
chromedriver = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver, options=op)
browser.get(url)
delay = 1
timeout =30

try:
 WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/div')))
 print("Page is ready!")
except TimeoutException:
 print("Loading took too much time!")
itembox = browser.find_elements(By.CLASS_NAME, 'g-1-6')
print(len(itembox))
# for x in itembox:
# print(x.text)
counter =1
timeout =20
full_list=[]
song_list = []
author_list = []
for i in itembox:
 songs = i.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/div/a')
 my_str = i.text.strip()
 full_list = ','.join(re.split('(?<!\(.)\n(?!.\))', my_str))
 my_list = full_list.split(',')
 # del my_list[0]
 print(my_list)
 # song_list.extend(my_list[0])
 # print(song_list)
 # author_list.extend(my_list[1])
 links = i.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/div/a')
 data['Title'].append(my_list[0].strip())
 data['Artist'].append(my_list[1].strip())
 data['Extraction Time'].append(day_date_time.strip())
 data['Locale'].append(locale.strip())
 data['Language'].append(lang.strip())
 data['Tag'].append(tag.strip())
 data['Main Url'].append(url)
 data['Url'].append('')
# author = i.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/div/a/span/font/font')
# links = i.find_elements(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/div/a')
# counter= counter+1
# if (counter == 100):
# break
# for s in songs:
# print(s.text)
# data['Title'].append(s.text.strip())
# for a in author:
# # print(a.text.strip())'
# data['Artist'].append(a.text.strip())
# data['Extraction Time'].append(day_date_time.strip())
# data['Locale'].append(locale.strip())
# data['Language'].append(lang.strip())
# data['Tag'].append(tag.strip())
# data['Main Url'].append(url)

for my_href in links:
 link = my_href.get_attribute("href")
 data['Supported Url'].append(link)
#
file_name = ' letras_albums.csv'
make_csv(file_name, data)





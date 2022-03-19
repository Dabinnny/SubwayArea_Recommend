import time, os
import requests, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#서울시 주요역 10개 선정
# data = ['사당역','광화문역','강남역','신촌역','홍대역','왕십리역','여의도역','이태원역','혜화역','건대입구역']

# 카카오맵 크롤링(셀레니움)
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('lang=ko_KR')
chromedriver_path='chromedriver'
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)
driver.get("https://map.kakao.com/")

subway = input("subway_name")

# 겁색 창, 검색어 입력, enter 창, 장소검색
search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')  
search_area.send_keys(subway)  
driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  
time.sleep(2)  
driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER) 

filename = input("file_name")

# 3. 리스트 만들고 크롤링 함수 생성
list = []

def place():
    time.sleep(0.2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    lists = soup.select('.placelist > .PlaceItem')

    count = 1

    for place in lists:
        temp = []

        name = place.select('.head_item > .tit_name > .link_name')[0].text
        category = place.select('.head_item > span')[0].text
        rating = place.select('.rating > .score > .num')[0].text
        review = place.select('.rating > .review > em ')[0].text
        link = place.select('.contact > .moreview')[0]['href']
        add = place.select('.info_item > .addr > p')[0].text
        hour = place.select('.info_item > .openhour > p > a')[0].text
        tel = place.select('.info_item > .contact > span')[0].text

        print(name, category, rating, review, link, add, hour, tel)

        temp.append(name)
        temp.append(category)
        temp.append(rating)
        temp.append(review)
        temp.append(link)
        temp.append(add)
        temp.append(hour)
        temp.append(tel)

        list.append(temp)

    f = open(filename+'.csv', 'w', encoding='utf-8-sig', newline="")
    csvWriter = csv.writer(f)
    header = ['name', 'category', 'rating', 'review', 'link', 'add', 'hour', 'tel']
    csvWriter.writerow(header)

    for i in list:
        csvWriter.writerow(i)
    

#크롤링 시작_1페이지부터 30페이지까지 출력
page = 1
page2 = 0
for i in range(0, 5):
    # 페이지 넘어가며 출력
    try:
        page2+=1
        print("**", page, "**")

        driver.find_element_by_xpath(f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)
        place()

        if (page2) % 5 == 0:
            driver.find_element_by_xpath('//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page2 = 0

        page += 1
    except:
        break

print('finish')

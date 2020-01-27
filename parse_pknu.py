# parser.py
import requests
from bs4 import BeautifulSoup
import os
import json
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcrawl.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
from django_crawl.models import BlogData
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_blog():
    html_url = 'http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005&p_sbsidx=2'
    req = requests.get(html_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # my_titles = soup.find('ul', {'id' : 'board_list'})
    #contents > div.contents-inner > form:nth-child(3) > table > tbody > tr:nth-child(4)
    my_titles = soup.select(
        'div > form > table > tbody > tr'
        )
    print(my_titles)
    #contents > div.contents-inner > form:nth-child(3) > table > tbody > tr:nth-child(4) > td.title > strong > a
    data = {}
    for title in my_titles:
        temp = title.find('td', {'class' : 'title'}).text
        print(temp)
        print(title.find('a').get('href'))
        print(title.find('td', {'class' : 'date'}))
        data[temp] = [title.find('a').get('href'), title.find('td',{'class' : 'date'}).text]
    return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        try:
            BlogData(title=t, link=l[0], tag='pknu', date=l[1]).save()
        except:
            pass
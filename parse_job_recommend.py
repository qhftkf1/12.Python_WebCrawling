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
    html_url = 'http://cms.pknu.ac.kr/pknujob/view.do?no=2343'
    req = requests.get(html_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.find('ul', {'id' : 'board_list'})
    my_titles = my_titles.select(
        'li > a'
        )
    data = {}
    for title in my_titles:
        data[title.find("h4").text] = [title.get('href'), title.find('span',{'class' : 'date'}).text]
    return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l[0], tag='job_general', date=l[1]).save()

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
    req = requests.get('http://cms.pknu.ac.kr/pknujob/view.do?no=2344')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.find('ul', {'id' : 'board_list'})
    print(my_titles)
    my_titles = my_titles.select(
        'li > a'
        )

    print(my_titles)
    #board_list > li:nth-child(1) > a
    #board_list > li:nth-child(1) > a > h4
    #board_list > li:nth-child(10) > a
    # case google
    # req = requests.get('https://www.google.com/search?q=%ED%81%AC%EB%A1%A4%EB%9F%AC&rlz=1C1OKWM_enKR881KR881&oq=%ED%81%AC%EB%A1%A4%EB%9F%AC&aqs=chrome..69i57j0l4j69i61l3.2578j0j7&sourceid=chrome&ie=UTF-8')
    # html = req.text
    # soup = BeautifulSoup(html, 'html.parser')
    # # div
    # my_googles = soup.find_all('div', {'class':'BNeawe vvjwJb AP7Wnd'})
    # case incruit
    # req = requests.get('http://cms.pknu.ac.kr/pknujob/view.do?no=2343')
    # html = req.text
    # soup = BeautifulSoup(html, 'html.parser')
    # my_incruit = soup.find_all('h4')
    # print(my_titles);
    data = {}
    for title in my_titles:
        print(title.find("h4"))
        data[title.find("h4").text] = title.get('href')
    return data

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    data = parse_blog()
    json.dump(data, json_file)

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()


# req = requests.get('https://www.google.com/search?q=%ED%81%AC%EB%A1%A4%EB%9F%AC&rlz=1C1OKWM_enKR881KR881&oq=%ED%81%AC%EB%A1%A4%EB%9F%AC&aqs=chrome..69i57j0l4j69i61l3.2578j0j7&sourceid=chrome&ie=UTF-8')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# my_googles = soup.find_all('div', {'class':'BNeawe vvjwJb AP7Wnd'})

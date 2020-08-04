import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(BASE_URL)

soup = BeautifulSoup(response.text, 'html.parser')

movie_dataset = soup.select('div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li')

for movie_data in movie_dataset:
    title = movie_data.select_one('dl.lst_dsc > dt.tit > a').text
    code = movie_data.select_one('dl.lst_dsc > dt.tit > a')['href'].split('=')[1]

    print(f'title: {title}')
    print(f'code: {code}')
    print()

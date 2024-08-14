import requests
import os
import json
import time
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')

def save_json(data, file_path):
    # 파일 저장 경로 MKDIR
    os.makedirs(os.path.dirname(file_path), exost_ok=True) # file_path =아래에 /data.json뺀 앞 경로까지 만들어줌

    with open(file_path, 'w', encoding='utf-8') ad f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def req(url):
    r = requests.get(url)
    j = r.json()
    return j

def save_movies(year, per_page=10, sleep_time=1):
    file_path = f'data/movies/year={year}/data.json'
    
    # 위 경로가 있으면 API 호출을 멈추고 프로그램 종료
    
    # totCnt 가져오고 total_pages 게산
    url_base = f"https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt={year}&openEndDt={year}"
    req(url_base + f"curPage=1")
    tot_cnt = r['movieListResult']['totCnt']
    total_pages = (tot_cnt // per_page) + 1

    #total_pages 만큼 Loop 돌면서 API호출
    all_data = [] 
    for page in tqdm(range(2, total_pages + 1)):
        time.sleep(sleep_time)
        r = req(url)
        d = r['movieListResult']['movieList']
        all_data.extend(d)

    save_json(all_data, file_path)
    return True

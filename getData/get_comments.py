# step1. 관련 패키지 및 모듈 불러오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import pandas as pd
from tqdm import tqdm


# step2. 네이버 뉴스 댓글정보 수집 함수
def get_naver_news_comments(wait_time=5, delay_time=0.1):
    # 크롬 드라이버로 해당 url에 접속
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # (크롬)드라이버가 요소를 찾는데에 최대 wait_time 초까지 기다림 (함수 사용 시 설정 가능하며 기본값은 5초)
    driver.implicitly_wait(wait_time)

    # 기사 url 다운로드
    df = pd.read_csv('D:\Git\CSE-sentiment\getData\칼부림_20230922.csv', encoding='utf-8')
    company_list = []
    url_list = []
    for i in df['link']:
        url_list.append(i)
    for i in df['company']:
        company_list.append(i)
        # print(url_list)
    symbol = "comment"
    comment_url_list = []
    # 기사의 댓글 url 다운로드
    for i in url_list:
        i = i.replace('article', 'article/comment')
        comment_url_list.append(i)

    nicknames_list_2 = []
    datetimes_list_2 = []
    contents_list = []
    think_list = []
    url_list_2 = []
    company_list_2 = []

    url_i = 0

    for url in tqdm(comment_url_list):
        # url = "https://n.news.naver.com/mnews/article/comment/015/0004638195?sid=102"
        # 인자로 입력받은 url 주소를 가져와서 접속
        driver.get(url)

        nicknames_list = []
        datetimes_list = []
        list_i = 0

        # 더보기가 안뜰 때 까지 계속 클릭 (모든 댓글의 html을 얻기 위함)
        while True:
            # 예외처리 구문 - 더보기 광클하다가 없어서 에러 뜨면 while문을 나감(break)
            try:
                more = driver.find_element(by=By.CSS_SELECTOR, value="a.u_cbox_btn_more")
                more.click()
                time.sleep(delay_time)

            except:
                break

        # 본격적인 크롤링 타임

        # 1)작성자
        # selenium으로 작성자 포함된 태그 모두 수집
        # nicknames = driver.find_elements_by_css_selector('span.u_cbox_nick')
        nicknames = driver.find_elements(by=By.CSS_SELECTOR, value="span.u_cbox_nick")
        # 리스트에 텍스트만 담기 (리스트 컴프리핸션 문법)
        list_nicknames = [nick.text for nick in nicknames]

        print("=======================================================================")

        for i in list_nicknames:
            print(i)
            if i is []:
                continue
            nicknames_list.append(i)
        # nicknames_list.append([nick.text for nick in nicknames])

        # 2)댓글 시간
        # selenium으로 댓글 시간 포bb함된 태그 모두 수집
        # datetimes = driver.find_elements_by_css_selector('span.u_cbox_date')
        datetimes = driver.find_elements(by=By.CSS_SELECTOR, value="span.u_cbox_date")
        # 리스트에 텍스트만 담기 (리스트 컴프리핸션 문법)

        list_datetimes = [datetime.text for datetime in datetimes]
        for i in list_datetimes:
            print(i)
            if i is []:
                continue
            datetimes_list.append(i)
        # datetimes_list.append([datetime.text for datetime in datetimes])

        # 3)댓글 내용
        # selenium으로 댓글내용 포함된 태그 모두 수집
        # contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
        contents = driver.find_elements(by=By.CSS_SELECTOR, value="span.u_cbox_contents")
        # 리스트에 텍스트만 담기 (리스트 컴프리핸션 문법)
        list_contents = [content.text for content in contents]
        for i in list_contents:
            print(i)
            # if i is []:
            # continue
            nicknames_list_2.append(nicknames_list[list_i])
            datetimes_list_2.append(datetimes_list[list_i])
            contents_list.append(i)
            url_list_2.append(comment_url_list[url_i])
            company_list_2.append(company_list[url_i])
            list_i = list_i + 1
        # contents_list.append([content.text for content in contents])
        # print(url_i)
        # print(company_list[url_i])
        url_i = url_i + 1
        print("=======================================================================")

    with open('D:\Git\CSE-sentiment\getData\Test.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        print(company_list_2)
        writer.writerow(['작성자', '작성날짜', '언론사', '실족/살인', 'url', '댓글내용'])
        # writer.writerow(['작성자', '작성날짜', '댓글내용'])
        for i in tqdm(range(len(nicknames_list))):
            writer.writerow(
                [nicknames_list_2[i], datetimes_list_2[i], company_list_2[i], 0, url_list_2[i], contents_list[i]])


# df1 = pd.read_csv('./naver_news_comments_202302.csv', encoding='utf-8')

get_naver_news_comments()

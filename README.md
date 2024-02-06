

# 뉴스 url 크롤링
1.	url 변경
아래의 코드에서 칼부림의 특정 기간을 크롤링하기 위해서는 url을 변경해야합니다. 
url에 ds=2023.08.24&de=2023.08.29가 특정기간동안 올라온 기사들을 필터링하는 것입니다. 위 url과 아래 url을 모두 수정해주시면 됩니다.

```


def makeUrl(search, start_pg, end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
         #https://search.naver.com/search.naver?where=news&query=칼부림&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2023.07.20&de=2023.08.30&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20230720to20230830&is_sug_officeid=0&office_category=0&service_area=0
        # 정렬을 포함한 url로 수정함.
        url = "https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2023.08.24&de=2023.08.29&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20230720to20230830&is_sug_officeid=0&office_category=0&service_area=0&query=" + search + "&start=" + str(start_page)
        print("생성url: ", url)
        return url
    else:
        urls = []
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2023.08.24&de=2023.08.29&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20230720to20230830&is_sug_officeid=0&office_category=0&service_area=0&query=" + search + "&start=" + str(
                page)
            urls.append(url)
        print("생성url: ", urls)
        return urls

    # html에서 원하는 속성 추출하는 함수 만들기 (기사, 추출하려는 속성값)
```

2.	검색어 입력
코드를 실행한후, 시작페이지와 끝 페이지를 입력하고 검색어 “검색하고싶은 키워드”을 입력합니다.  이때 시작페이지와 끝페이지를 입력하는 기준은 실제로 네이버 뉴스에 들어가 해당하는 기간으로 필터링 한뒤에, 끝페이지가 몇 페이지인지 확인한 후 해당 숫자를 끝 페이지 숫자로 입력하면 됩니다.

3.	.csv파일 정리
얻은 .csv파일을 다른 코드에 작성할 적절한 이름으로 변경해주세요. 이후 이 .csv파일은 댓글을 크롤링할 url의 모음으로서 사용됩니다.

# 댓글 크롤링
1.	url List 불러오기
url 크롤링으로부터 얻은 결과물이 있는 경로로 코드를 수정해주세요. 여기에서는 아래와 같은 부분의 수정이 필요합니다.
```
23line의
# 기사 url 다운로드
    df = pd.read_csv(r'D:\Git\CSE-sentiment\getData\url_0720_0725.csv', encoding='utf-8')
```
2.	.csv파일 생성 및 파일명 수정하기
해당 파일은 댓글들의 모음을 저장하는 .csv파일을 생성합니다. 이는 이후 모델학습에 사용되기 때문에 적절한 경로 특정한 이름을 가진 .csv파일을 생성한뒤, 코드를 실행해 주세요. 파일명을 수정하는곳은 다음과 같습니다.
```
112line의

  with open(r'D:\Git\CSE-sentiment\getData\Test.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
```

# 모델 구현 및 테스트
colab에서 코드를 순서대로 진행하면 됩니다. 만약 시간부족이나 오류로 인해 학습된 모델을 바로 사용하고자 한다면, 같이 올린 구글드라이브에 있는 model.pth파일을 이용하시면 됩니다.

# 학습된 모델로 라벨링
이또한 코드를 그대로 진행하면 됩니다. 단, colab에서 한글폰트가 깨지기 때문에 그래프의 한글이 출력이 안되는 오류가 발생합니다. 그부분을 해결하기 위해 아래의 코드를 먼저 실행시키고, 다시시작한뒤에 코드를 순서대로 진행하도록 합니다.
```
해당코드는 코드에 포함되어있습니다.
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```
이후 코드를 순서대로 진행합니다. 진행하다보면 아래와 같은 부분이 나오는데 여기에선 만든 모델을 불러와 사용합니다. 
<img width="783" alt="image" src="https://github.com/bunju20/CSE-sentiment/assets/85238126/a1ac37c3-178a-47a7-8332-70bb44064c32">

이후 그래프를 생성하시면 됩니다.

# LDA 토픽 모델링
코드 그대로 진행하시면 됩니다. 아래와 같은 4개의 결과파일이 나오면 성공입니다.

<img width="366" alt="image" src="https://github.com/bunju20/CSE-sentiment/assets/85238126/58aa948a-d6e8-4a56-bb23-cd314a29c7b8">
    
> ### 연구결과물 및 전체 자료 링크
> 
> https://drive.google.com/drive/folders/10oAtw40IvzotQfpIIpawD8VoOoX-i_e9?usp=sharing

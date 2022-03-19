# #postgresql 연결

import pandas as pd
from sqlalchemy import create_engine
import googlemaps
#df = pd.read_csv("/Users/dabbi/Section3/project3/flask_app/datacsv.csv")

강남 = pd.read_csv('강남역.csv')
강남['sub'] = '강남역'
건대입구 = pd.read_csv('건대입구역.csv')
건대입구['sub'] = '건대입구역'
광화문 = pd.read_csv('광화문역.csv')
광화문['sub'] = '광화문역'
사당 = pd.read_csv('사당역.csv')
사당['sub'] = '사당역'
신촌 = pd.read_csv('신촌역.csv')
신촌['sub'] = '신촌역'
여의도 = pd.read_csv('여의도역.csv')
여의도['sub'] = '여의도역'
왕십리 = pd.read_csv('왕십리역.csv')
왕십리['sub'] = '왕십리역'
이태원 = pd.read_csv('이태원역.csv')
이태원['sub'] = '이태원역'
혜화 = pd.read_csv('혜화역.csv')
혜화['sub'] = '혜화역'
홍대 = pd.read_csv('홍대역.csv')
홍대['sub'] = '홍대역'

df = pd.concat([강남, 건대입구, 광화문, 사당, 신촌, 여의도, 왕십리, 이태원, 혜화, 홍대])

# 평점이 0인 음식점 제거 #
idx = df[df['rating']==0].index
df.drop(idx, inplace=True)

# 중복값 확인 및 제거 -> (3918, 9)
duplicate_rows = df[df.duplicated()]
df = df.drop_duplicates(keep='first')
df = df.reset_index(drop=True)
#print(df['category'].unique())

df_c = {
    "육류,고기":"한식", "베트남음식":"기타","멕시칸,브라질":"기타",
    "초밥,롤":"일식","참치회":"일식","닭요리":"한식", "이탈리안":"양식",
    "일본식주점":"호프,펍","중화요리":"중식","디저트카페":"베이커리,카페",
    "순대":"한식","샤브샤브":"한식","국수":"한식",
    "냉면":"한식","스테이크,립":"양식","돈까스,우동":"일식","곱창,막창":"한식",
    "감자탕":"한식","회":"일식","테마카페":"베이커리,카페","삼겹살":"한식",
    "술집":"호프,펍","호프,요리주점":"호프,펍","커피전문점":"베이커리,카페",
    "양꼬치":"중식","해물,생선":"일식","햄버거":"패스트푸드",
    "떡볶이":"분식","퓨전일식":"일식","다방":"베이커리,카페",
    "일식집":"일식","보드카페":"베이커리,카페","와인바":"호프,펍",
    "도넛":"베이커리,카페","갈비":"한식","치킨":"패스트푸드","찌개,전골":"한식",
    "칵테일바":"호프,펍","도시락":"패스트푸드","샌드위치":"패스트푸드",
    "오리":"한식","족발,보쌈":"한식","아시아음식":"기타",
    "제과,베이커리":"베이커리,카페","고양이카페":"베이커리,카페",
    "인도음식":"기타","퓨전요리":"기타","불고기,두루치기":"한식",
    "삼계탕":"한식","조개":"한식","추어":"한식","퓨전한식":"기타",
    "아이스크림":"베이커리,카페","복어":"한식","국밥":"한식","수제비":"한식",
    "음식점":"기타","동남아음식":"기타","기사식당":"한식","북카페":"베이커리,카페",
    "뷔페":"기타","패밀리레스토랑":"기타","매운탕,해물탕":"한식",
    "실내포장마차":"호프,펍","갤러리카페":"베이커리,카페","만화카페":"베이커리,카페",
    "간식":"패스트푸드","두부전문점":"한식","애견카페":"베이커리,카페",
    "설렁탕":"한식","해장국":"한식","장어":"한식","초콜릿":"베이커리,카페",
    "전통찻집":"베이커리,카페","곰탕":"한식","태국음식":"기타","죽":"패스트푸드",
    "떡,한과":"패스트푸드","게,대게":"한식","쌈밥":"한식","철판요리":"중식",
    "오뎅바":"일식","샐러드":"패스트푸드","아구":"한식","토스트":"패스트푸드",
    "퓨전중식":"중식","키즈카페":"베이커리,카페","굴,전복":"기타","푸드코트":"기타",
    "사철탕,영양탕":"한식","터키음식":"기타","채식뷔페":"기타","사주카페":"베이커리,카페",
    '한식':"한식","분식":"분식","패스트푸드":"패스트푸드","일식":"일식","중식":"중식",'양식':"양식",
    '카페':"베이커리,카페","한정식":"한식","고기뷔페":"한식","해산물":"일식",
    "피자":"패스트푸드","일본식라면":"일식"}
a = [] 
 
for i in range(3918):
    a.append(df_c[df['category'][i]])  

df['category_dic'] = a
df['rating']=df['rating'].astype(int)
df['review']=df['review'].str.replace(',', '').apply(pd.to_numeric)

df.loc[df['review']<=200,'rev']='0 ~ 200 개'
df.loc[(df['review']>200)&(df['review']<=400),'rev']='200 ~ 400 개'
df.loc[(df['review']>400)&(df['review']<=700),'rev']='400 ~ 700 개'
df.loc[(df['review']>700)&(df['review']<=1000),'rev']='700 ~ 1000 개'
df.loc[df['review']>1000,'rev']='1000개 이상'

# 데이터프레임에 위경도 컬럼 추가
API_KEY = "AIzaSyDFwHEgjxdzIn6NNBC2JuRXuvNC0WL2h_A" # 구글맵 키
gmaps = googlemaps.Client(key=API_KEY)

# 위도, 경도
lat = []
lng = []

# 우리나라 위경도 최대 최소값
max_lat = 38.0
min_lat = 33.0
max_lng = 132.0
min_lng = 126.0

addr = []

for name in df['add'][3500:]:
    tmp = gmaps.geocode(name, language='ko')
    addr.append(tmp[0].get("formatted_address"))
    
    tmp_loc = tmp[0].get("geometry")

    lat.append(tmp_loc['location']['lat'])
    lng.append(tmp_loc['location']['lng'])

dfl8 = pd.DataFrame(lat)
dfl8 = dfl8.rename(columns={0: "lat"})
dfn8 = pd.DataFrame(lng)
dfn8 = dfn8.rename(columns={0: "lng"})

# 최종 csv로 저장
df.to_csv("datacsv.csv", encoding="utf-8-sig")

#데이터베이스 연결
engine = create_engine('postgresql://zgyrldjf:ngcUoDi8jpQyKMP8I5QHBTRK16ja6pfy@castor.db.elephantsql.com/zgyrldjf')
df.to_sql("database", engine)

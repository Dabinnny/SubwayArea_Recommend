# SubwayArea_Recommend 

## ✔️ 웹사이트 구현 영상

<img src="https://user-images.githubusercontent.com/90162819/159123970-a43d8ca8-9ef5-4f14-821c-3bea3305736f.gif">

## ✔️ 프로젝트 목적
리뷰와 평점을 기반으로 해당 조건이 많은 식당이 많이 위치한 상권지역을 추천합니다.

## ✔️ Pipeline 

<img src="https://user-images.githubusercontent.com/90162819/159123334-067357d7-1dcc-406f-bf3e-770ae08df0aa.png">

1. 데이터 수집 : 카카오맵 `Crawling` 진행
2. 데이터 적재 : 가게명, 음식종류, 리뷰수, 평점, 인근지하철역, 주소 등의 특성(3918*13), `PostgreSQL` 연동
3. 머신러닝 모델 구축 : `LightGBM`을 활용하여 트리기반 Boosting분류 모델 구축
4. 추천상권에 대한 지도 시각화 : `구글맵 API`, `Folium`, `Geocode` 활용
5. 웹서비스 구현 : `Flask` 활용 웹 서비스 구축 
6. 데이터 시각화 : `Metabase`활용 추천 상권에 대한 insight 도출






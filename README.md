# SubwayArea_Recommend 

## 1. 프로젝트 목적
리뷰와 평점을 기반으로 해당 조건에 부합하는 식당이 많이 위치한 상권지역을 추천합니다.  

</br>

## 2. 웹사이트 구현 영상

<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159124424-9f2df356-0dac-487d-985e-3ba1165be0e4.gif"></div>

</br>

## 3. Pipeline 

<img src="https://user-images.githubusercontent.com/90162819/159123334-067357d7-1dcc-406f-bf3e-770ae08df0aa.png">

</br>

   ### -  **데이터 수집** : 카카오맵 `Crawling` 진행
<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159152948-50aedfe7-615d-401f-93c3-084c4c92a18e.gif"></div>

</br>

   ### -  **데이터 적재** : 가게명, 음식종류, 리뷰수, 평점, 인근지하철역, 주소 등의 특성(3918*13), `PostgreSQL` 연동

   <div align="center"><img src="https://user-images.githubusercontent.com/90162819/159152931-029eafc0-521c-4628-bba2-e92a8fa6f33e.png"></div>

   </br>

   ### -  **머신러닝 모델 구축** : `LightGBM`을 활용하여 트리기반 Boosting분류 모델 구축

   </br>

   ### -  **지도 시각화** : `구글맵 API`, `Folium`, `Geocode` 활용

   </br>

   ### -  **웹서비스 구현** : `Flask` 활용 웹 서비스 구축 

   </br>

   ### -  **데이터 시각화** : `Metabase`활용 추천 상권에 대한 insight 도출

<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159153055-1c56b409-c6c3-449a-a8fb-e41ab9f04ab0.png"></div>

</br>






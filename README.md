# SubwayArea_Recommend 

## ✔️ 프로젝트 목적
리뷰와 평점을 기반으로 해당 조건에 부합하는 식당이 많이 위치한 상권지역을 추천합니다.  

</br>

## ✔️ 웹사이트 구현 영상

<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159124424-9f2df356-0dac-487d-985e-3ba1165be0e4.gif"></div>

</br>

## ✔️ Pipeline 

<div align="center"><img src="https://user-images.githubusercontent.com/90162819/160058274-12bfaba8-7547-4700-854d-2afd49fb09a0.png" width="700"></div>

</br>

   ### 1.  **데이터 수집** 
-  카카오맵 `Crawling` 진행
<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159152948-50aedfe7-615d-401f-93c3-084c4c92a18e.gif"></div>

</br>

   ### 2.  **데이터 적재** 
   -  `PostgreSQL` 연동 (3918*13) 

   <div align="center"><img src="https://user-images.githubusercontent.com/90162819/160058268-7778c0e9-3854-494e-b0b8-9cd54941c918.png" width="700"></div>

   </br>

   ### 3.  **머신러닝 모델 구축** 
   -  `XGBoost`을 활용하여 Ensemble기반 Boosting 분류모델 구축


   ### 4.  **지도 시각화** 
   -  `구글맵 API`, `Folium`, `Geocode` 활용


   ### 5.  **웹서비스 구현** 
   -  `Flask` 활용 웹 서비스 구축 


   ### 6.  **데이터 시각화** 
   -  `Metabase`활용 추천 상권에 대한 insight 도출

<div align="center"><img src="https://user-images.githubusercontent.com/90162819/159153055-1c56b409-c6c3-449a-a8fb-e41ab9f04ab0.png" width="500"></div>

</br>






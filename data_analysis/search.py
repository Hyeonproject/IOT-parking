# 데이터 불러오기
import pandas as pd
cctv_data = pd.read_csv('CCTV_data.csv', encoding='euc-kr')
cctv_data = cctv_data[['소재지지번주소', '촬영방면정보', '위도', '경도']]
cctv_data = cctv_data.dropna(axis=0).reset_index()

# CCTV 명칭 수정
cctv_data['CCTV'] = cctv_data['소재지지번주소'] + ' ' + cctv_data['촬영방면정보']

# 서면지역만 추출
cctv_data = cctv_data[(cctv_data['위도']>=35.153553) & (cctv_data['위도']<=35.158272)]
cctv_data = cctv_data[(cctv_data['경도']>=129.054862) & (cctv_data['경도']<=129.063938)].reset_index()

# 주소, 위도, 경도 크롤링
cctv_name = cctv_data['CCTV']
cctv_lat = cctv_data['위도']
cctv_lng = cctv_data['경도']

# 맵
import folium
map = folium.Map(location=[35.155724, 129.059161], zoom_start=17)

# 마크 표시
for i in range(len(cctv_name)):
    folium.Marker(location=[cctv_lat[i], cctv_lng[i]], popup=cctv_name[i], icon=folium.Icon(color='blue',icon='cloud')).add_to(map)

map.save('CCTV_test.html')
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# 데이터 불러오기
import pandas as pd
cctv_data = pd.read_csv('CCTV_data.csv', encoding='euc-kr')
cctv_data = cctv_data[['소재지지번주소', '촬영방면정보', '위도', '경도']]
cctv_data = cctv_data.dropna(axis=0).reset_index()

# CCTV 명칭 수정
cctv_data['CCTV'] = cctv_data['소재지지번주소'] + ' ' + cctv_data['촬영방면정보']

# 주소, 위도, 경도 크롤링
cctv_name = cctv_data['CCTV']
cctv_lat = cctv_data['위도']
cctv_lng = cctv_data['경도']

# 맵
import folium
map = folium.Map(location=[cctv_lat.mean(), cctv_lng.mean()], zoom_start=8)

# 히트맵1 표시
from folium import plugins
map = map.add_children(plugins.HeatMap(zip(cctv_lat, cctv_lng), radius = 8))
map.save('CCTV_HeatMap1.html')

# 히트맵2 표시
from folium.plugins import HeatMap
map = HeatMap(zip(cctv_lat, cctv_lng)).add_to(map)
map.save('CCTV_HeatMap2.html')
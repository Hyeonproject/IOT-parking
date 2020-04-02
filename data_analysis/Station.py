# 데이터 불러오기
import pandas as pd
station_data = pd.read_csv('Station_data.csv', encoding='euc-kr')
station_data = station_data[['주차장명', '위도', '경도']]
station_data = station_data.dropna(axis=0).reset_index()

# 주소, 위도, 경도 크롤링
station_name = station_data['주차장명']
station_lat = station_data['위도']
station_lng = station_data['경도']

# 맵
import folium
map = folium.Map(location=[station_lat.mean(), station_lng.mean()], tiles='stamentoner', zoom_start=8)

# 히트맵1 표시
from folium import plugins
map = map.add_children(plugins.HeatMap(zip(station_lat, station_lng), radius = 8))
map.save('Station_HeatMap1.html')

# 히트맵2 표시
from folium.plugins import HeatMap
map = HeatMap(zip(station_lat, station_lng)).add_to(map)
map.save('Station_HeatMap2.html')
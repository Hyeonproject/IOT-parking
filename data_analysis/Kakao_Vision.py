import requests

url = "https://kapi.kakao.com/v1/vision/face/detect"
MYAPP_KEY = 'ada3123a03a1e6188150510b7b6518e2'
headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

filename = './data/bk.jpg'
files = { 'file' : open(filename, 'rb')}

response = requests.post(url, headers=headers, files=files)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
# %matplotlib inline

# https://developers.kakao.com/docs/restapi/vision 참조
result = response.json()
print(result)

# 검출된 얼굴의 특징점들을 담은 객체. 총 68개의 특징점이 영역별로 x,y 배열에 담겨있음
faces = result['result']['faces'][0]
facial_points = faces['facial_points']

# 요청 이미지의 가로, 세로 길이
fig_w, fig_h = result['result']['width'], result['result']['height']

# 추정 성별, 나이
sex, age = faces['facial_attributes']['gender'], faces['facial_attributes']['age']

img = mpimg.imread(filename)
fig,ax = plt.subplots(figsize=(10,10))

for each_obj in facial_points.keys():
    for each in facial_points[each_obj]:
        rect_face = patches.Circle((each[0]*fig_w, each[1]*fig_h),
                                   linewidth=3, edgecolor='c')
        ax.add_patch(rect_face)


annotation = 'Male : ' + str(round(sex['male'] * 100, 3)) + ' % \n' + 'Female : ' + str(round(sex['female']  * 100, 3)) + ' % \n' + 'Age : ' + str(round(age, 3))
plt.figtext(0.15, 0.17 , annotation, wrap=True, fontsize=17, color='blue')
    
ax.imshow(img)
plt.show()

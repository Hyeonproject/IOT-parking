import requests
client_id = "X2cpBx6ssnJGwsOwWJKS"
client_secret = "UU8R3UR9j7"
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

filename = './data/bk.jpg'
files = {'image': open(filename, 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)

detect_result = response.json()
print(detect_result)

# 비슷한 연예인, 정확도
celebrity, confidence = detect_result['faces'][0]['celebrity']['value'], detect_result['faces'][0]['celebrity']['confidence']

#==============================================================================
print('======================================================================')

url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지

files = {'image': open(filename, 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url, files=files, headers=headers)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

detect_result = response.json()
print(detect_result)

detect_summary = detect_result['faces'][0]
x, y, w, h = detect_summary['roi'].values()
gender, gen_confidence = detect_summary['gender'].values()
emotion, emotion_confidence = detect_summary['emotion'].values()
age, age_confidence = detect_summary['age'].values()

img = mpimg.imread(filename)
fig,ax = plt.subplots(figsize=(10,10))

rect_face = patches.Rectangle((x,y), w, h, linewidth=5, edgecolor='r', facecolor='none')
ax.add_patch(rect_face)

annotation = 'Sex : ' + gender + ', ' + str(round(gen_confidence * 100, 3)) + ' % \n' + \
            'Emotion : ' + emotion + ', ' + str(round(emotion_confidence * 100, 3)) + ' % \n' + \
            'Age : ' +  age + ', ' + str(round(age_confidence * 100, 3)) + ' % \n'
plt.figtext(0.35, 0.12 , annotation, wrap=True, fontsize=17, color='white')

print('비슷한 연예인 : ' + celebrity + ', ' + str(round(confidence * 100, 3)) + '%')
ax.imshow(img)
plt.show()

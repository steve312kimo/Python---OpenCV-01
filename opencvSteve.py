import cv2
## pip install opencv-python 

#載入分類器  ?????
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# pip show opencv-python 

# Name: opencv-python
# Version: 4.4.0.46
# Summary: Wrapper package for OpenCV python bindings.
# Home-page: https://github.com/skvark/opencv-python
# Author: None
# Author-email: None
# License: MIT
# Location: c:\users\user\anaconda3\lib\site-packages
# Requires: numpy
# Required-by:

# c:/users/user/anaconda3/lib/site-packages
# C:/Users/User/anaconda3/Lib/site-packages/cv2/data

face_cascade.load('C:/Users/User/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    
# face_cascade.load('C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# 讀取圖片 img = cv2.imread('圖片.jpg',顏色參數) 顏色參數=1是彩色圖片 0是黑白圖片
#img = cv2.imread('people.jpg')
#img = cv2.imread('C:/Users/User/Desktop/opencv/people.jpg')
#img = cv2.imread('C:/Users/User/Desktop/opencv/steve.jpg')
img = cv2.imread('C:/Users/User/Desktop/opencv/twice2.jpg')
print(img)

# 轉成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)

# 偵測臉部
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.08,
                                      minNeighbors=5,
                                      minSize=(32, 32))
print(faces)

# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#視窗大小 cv2.WINDOW_NORMAL -> 可改變大小 cv2.WINDOW_AUTOSIZE -> 不可改變大小，自動調整視窗大小以符合圖片大小 cv2.WINDOW_FREERATIO -> 可改變大小可改變比例 cv2.WINDOW_KEEPRATIO -> 可改變大小不可改變比例
cv2.namedWindow('My Image',cv2.WINDOW_KEEPRATIO)

#顯示圖片
cv2.imshow('My Image', img)
#讓視窗暫停直到使用者按下任意鍵
cv2.waitKey(0)
#關閉所有視窗
cv2.destroyAllWindows()

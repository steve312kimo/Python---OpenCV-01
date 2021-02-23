import cv2

#載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade.load('C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
face_cascade.load('C:/Users/User/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# C:/Users/User/anaconda3/Lib/site-packages/cv2/data/
# Out[5]: True

#從視訊鏡頭擷取影片
cap=cv2.VideoCapture(0)
#使用現有影片
#路徑中的 \U 會被視為Unicode-Escape編碼的跳脫字元  解決方法引號前加r 或是將所有\取代成\\ 也能取代成/
#cap=cv2.VideoCapture(r'C:\Users\Milk_Tea0319\.spyder-py3\test.mp4')
#cap=cv2.VideoCapture('C:/Users/User/Desktop/opencv/opencv_video/test.mp4')
# C:/Users/User/Desktop/opencv/opencv_video

# 使用無窮迴圈擷取影像，直到按下Esc鍵結束
while True:
    #抓取，解碼並返回下一個視訊幀。返回值為true表明抓取成功。
    #該函式是組合了grab()和retrieve()，這是最方便的方法。
    #如果沒有幀，該函式返回false，並輸出空影象。
    # 擷取一張影像
    retval,img=cap.read()
    retval
    # Out[10]: True
    img
    # Out[11]:  
    # array([[[123, 136, 141],
    #       [122, 135, 140],
    #       [121, 134, 137],
    #       ...,
    #       [242, 255, 255],
    #       [242, 255, 255],
    #       [242, 255, 255]],
       
    # cap.read() 會讀取一張畫面，其第一個傳回值 ret代表成功與否
    #（True 代表成功，False 代表失敗），
    # 而第二個傳回值 frame 就是攝影機的單張畫面。
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    gray
    '''
    array([[133, 132, 130, ..., 251, 251, 251],
       [133, 132, 131, ..., 251, 251, 251],
       [131, 132, 132, ..., 251, 251, 251],
       ...,
       [137, 130, 124, ...,  90,  89,  89],
       [135, 131, 127, ...,  90,  89,  88],
       [132, 131, 131, ...,  90,  88,  87]], dtype=uint8)'''
    
    faces=face_cascade.detectMultiScale(gray,
                                        scaleFactor=1.8,
                                        # 1.2每次搜尋時減少的倍率1.01X
                                        minNeighbors=3) 
                                        #目標至少被檢測幾次以上
                                        #才認為人臉存在5
    faces
    # Out[8]: array([[319, 111, 237, 237]], dtype=int32)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('人名',img)

    k=cv2.waitKey(1)
    if k==27:  #當按ESC關閉視窗 ASCII 27=esc 
        break

#關閉鏡頭或關閉影片
cap.release()
cv2.destroyAllWindows()



import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade.load('C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

#從視訊鏡頭擷取影片
#cap=cv2.VideoCapture(0)
#使用現有影片
#路徑中的 \U 會被視為Unicode-Escape編碼的跳脫字元  解決方法引號前加r 或是將所有\取代成\\ 也能取代成/
cap=cv2.VideoCapture(r'C:\Users\Milk_Tea0319\.spyder-py3\test.mp4')

# 使用無窮迴圈擷取影像，直到按下Esc鍵結束
while True:
    #抓取，解碼並返回下一個視訊幀。返回值為true表明抓取成功。該函式是組合了grab()和retrieve()，這是最方便的方法。如果沒有幀，該函式返回false，並輸出空影象。
    # 擷取一張影像
    retval,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces=face_cascade.detectMultiScale(gray,
                                        scaleFactor=1.2,#每次搜尋時減少的倍率
                                        minNeighbors=5)#目標至少被檢測幾次以上才認為人臉存在
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('img',img)

    k=cv2.waitKey(1)
    if k==27:#當按ESC關閉視窗 ASCII 27=esc 
        break

#關閉鏡頭或關閉影片
cap.release()
cv2.destroyAllWindows()



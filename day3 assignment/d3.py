import numpy as np
import cv2
img=cv2.imread("index1.jpg");
cap = cv2.VideoCapture('sample.mp4')
while True: 

    flag,frame = cap.read()
    if not flag:
        print("not sucess")
        break
    cap = cv2.resize(frame, (img.shape[1],img.shape[0]))
    result=cv2.addWeighted(frame,0.8,img,0.5,gamma=0.5)
    cv2.imshow('overlay', result)
    video.write(img)
    if(cv2.waitKey(10) & 0xFF == ord('b')): 
            break

cap.release()
cv2.destroyAllWindows()
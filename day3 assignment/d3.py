import cv2
import numpy as np

img = cv2.imread('C:/Users/Hp/Desktop/Untitled Folder/day3 assignment/index2.png')
img1 = cv2.imread('C:/Users/Hp/Desktop/Untitled Folder/day3 assignment/index3.jpg')
img2 = cv2.imread('C:/Users/Hp/Desktop/Untitled Folder/day3 assignment/index4.jpg')
img3 = cv2.imread('C:/Users/Hp/Desktop/Untitled Folder/day3 assignment/index1.png')
img4 = cv2.imread('C:/Users/Hp/Desktop/Untitled Folder/day3 assignment/index.jpg')
img5 = cv2.imread('C:/Users/Hp/Desktop/Untitled Folder/day3 assignment/index5.jpg')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:

    flag, frame = cap.read()
    if not flag:
        print("not success")
        break

    choice = int(input("Enter ur choice: "))
    if choice == 1:
        image = cv2.resize(img, (frame.shape[1], frame.shape[0]))
        result = cv2.addWeighted(frame, 0.8, image, 0.5, gamma=0, )
        cv2.imshow('overlay', result)
        if cv2.waitKey(10) & 0xFF == ord('b'):
            break

    elif choice == 2:
        image = cv2.resize(img1, (frame.shape[1], frame.shape[0]))
        result = cv2.addWeighted(frame, 0.8, image, 0.5, gamma=0, )
        cv2.imshow('overlay', result)
        if cv2.waitKey(10) & 0xFF == ord('b'):
            break

    elif choice == 3:
        image = cv2.resize(img2, (frame.shape[1], frame.shape[0]))
        result = cv2.addWeighted(frame, 0.8, image, 0.5, gamma=0, )
        cv2.imshow('overlay', result)
        if cv2.waitKey(10) & 0xFF == ord('b'):
            break

    elif choice == 3:
        image = cv2.resize(img3, (frame.shape[1], frame.shape[0]))
        result = cv2.addWeighted(frame, 0.8, image, 0.5, gamma=0, )
        cv2.imshow('overlay', result)
        if cv2.waitKey(10) & 0xFF == ord('b'):
            break
    elif choice == 3:
        image = cv2.resize(img4, (frame.shape[1], frame.shape[0]))
        result = cv2.addWeighted(frame, 0.8, image, 0.5, gamma=0, )
        cv2.imshow('overlay', result)
        if cv2.waitKey(10) & 0xFF == ord('b'):
            break
    elif choice == 5:
        image = cv2.resize(img5, (frame.shape[1], frame.shape[0]))
        result = cv2.addWeighted(frame, 0.8, image, 0.5, gamma=0, )
        cv2.imshow('overlay', result)
        if cv2.waitKey(10) & 0xFF == ord('b'):
            break
    elif choice == 0:
        print("out of range")
        break


cap.release()
cv2.destroyAllWindows()

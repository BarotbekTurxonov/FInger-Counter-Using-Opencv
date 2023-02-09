import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(detectionCon=0.8, maxHands=2)
cap = cv.VideoCapture(0)




while True:
    success, img = cap.read()
    hands,img = detector.findHands(img)
    cv.rectangle(img, (0, 480), (300, 425),(50, 50, 255), -2)
    if hands:
        lmList = hands[0]
        fingersUp = detector.fingersUp(lmList)
        print(fingersUp)

        if fingersUp == [0,0,0,0,0]:
            cv.putText(img, 'Finger Count: 0', (20,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)
        

        if fingersUp == [0,0,0,0,1]:
            cv.putText(img, 'Finger Count: 1', (20,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)
            #cv.putText(img, 'Not Jumping', (420,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)


        if fingersUp == [0,0,0,1,1]:
            cv.putText(img, 'Finger Count: 2', (20,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)
            #cv.putText(img, 'Not Jumping', (420,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)

        if fingersUp == [0,0,1,1,1]:
            cv.putText(img, 'Finger Count: 3', (20,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)
            #cv.putText(img, 'Not Jumping', (420,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)

        if fingersUp == [0,1,1,1,1]:
            cv.putText(img, 'Finger Count: 4', (20,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)
            #cv.putText(img, 'Not Jumping', (420,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)

        if fingersUp == [1,1,1,1,1]:
            cv.putText(img, 'Finger Count: 5', (20,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)
            #cv.putText(img, 'Not Jumping', (420,460), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv.LINE_AA)

       

            
    cv.imshow('Img', img)

    key = cv.waitKey(1)
    if key ==ord('q'):
        break
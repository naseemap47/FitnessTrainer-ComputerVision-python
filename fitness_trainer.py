import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('fitness videos/1.mp4')

while True:
    success, img = cap.read()
    img = cv2.resize(img, (740, 480))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
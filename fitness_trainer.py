import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('fitness videos/1.mp4')

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.resize(img, (740, 480))

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)
    print(result.pose_landmarks)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
import cv2
import mediapipe as mp
import time
from find_angle import get_angle
import numpy as np

cap = cv2.VideoCapture('fitness videos/1.mp4')

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

p_time = 0
dir = 0
count = 0
pre_angle = 180

while True:
    success, img = cap.read()
    img = cv2.resize(img, (740, 480))

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)
    # print(result.pose_landmarks)
    if result.pose_landmarks:
        lm_list = []
        for id, lm in enumerate(result.pose_landmarks.landmark):
            # print(id, lm)
            img_height, img_width, channel = img.shape
            x, y = int(lm.x * img_width), int(lm.y * img_height)
            lm_list.append([id, x, y])
            # print(lm_list)
            angle = get_angle(id_list=lm_list, image=img,
                              p1=11, p2=13, p3=15)
            # Fixing Angle Error
            if angle is not None:
                angle = angle
                pre_angle = angle
            else:
                angle = pre_angle
            # print(angle)

            # Percentage
            percent = np.interp(angle, (200, 330), (0, 100))

            # Bar
            bar = np.interp(angle, (200, 330), (400, 150))
            cv2.rectangle(img, (20, 150), (55, 400), (0, 255, 0), 3)
            cv2.rectangle(img, (20, int(bar)), (55, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img, f'{int(percent)} %', (10, 450),
                cv2.FONT_HERSHEY_PLAIN, 1.5,
                (255, 255, 0), 2
            )

            # Count
            if percent == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if percent == 0:
                if dir ==1:
                    count += 0.5
                    dir = 0
            # print(count)

            # Display Count
            cv2.rectangle(
                img, (630, 30), (735, 100),
                (0, 0, 0), cv2.FILLED
            )
            cv2.putText(
                img, str(int(count)), (650, 90),
                cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 255, 255), 3
            )
            cv2.putText(
                img, 'Count:', (650, 48),
                cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 255, 255), 1
            )

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(
        img, f'FPS: {int(fps)}', (10, 70),
        cv2.FONT_HERSHEY_PLAIN, 2,
        (255, 0, 255), 2
    )

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

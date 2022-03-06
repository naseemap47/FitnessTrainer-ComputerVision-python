import cv2
import math


def get_angle(id_list, image, p1, p2, p3, draw=True, draw_angle=True):
    if len(id_list) > 18:
        x1, y1 = id_list[p1][1:]
        x2, y2 = id_list[p2][1:]
        x3, y3 = id_list[p3][1:]

        # Angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2)
                             )
        if angle < 0:
            angle = 360 + angle
        elif angle > 360:
            angle = angle - 360

        if draw:
            # Circle
            cv2.circle(
                image, (x1, y1), 7,
                (0, 0, 255), 1
            )
            cv2.circle(
                image, (x1, y1), 3,
                (0, 0, 255), cv2.FILLED
            )
            cv2.circle(
                image, (x2, y2), 7,
                (0, 0, 255), 1
            )
            cv2.circle(
                image, (x2, y2), 3,
                (0, 0, 255), cv2.FILLED
            )
            cv2.circle(
                image, (x3, y3), 7,
                (0, 0, 255), 1
            )
            cv2.circle(
                image, (x3, y3), 3,
                (0, 0, 255), cv2.FILLED
            )

            # Line
            cv2.line(
                image, (x1, y1), (x2, y2),
                (255, 255, 255), 2
            )
            cv2.line(
                image, (x3, y3), (x2, y2),
                (255, 255, 255), 2
            )
        if draw_angle:
            cv2.putText(
                image, f'Angle: {int(angle)}',
                (x2 - 10, y2 + 10), cv2.FONT_HERSHEY_PLAIN,
                1, (0, 255, 255), 2
            )

        return angle

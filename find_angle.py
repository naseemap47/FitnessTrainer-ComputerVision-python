import cv2

def get_angle(id_list,image, p1, p2, p3, draw=True):
    if len(id_list) > 18:
        x1, y1 = id_list[p1][1:]
        x2, y2 = id_list[p2][1:]
        x3, y3 = id_list[p3][1:]

        if draw:
            cv2.circle(
                image, (x1, y1), 2,
                (0, 0 ,255), 3
            )
            cv2.circle(
                image, (x2, y2), 2,
                (0, 0, 255), 3
            )
            cv2.circle(
                image, (x3, y3), 2,
                (0, 0, 255), 3
            )
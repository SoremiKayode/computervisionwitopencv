import cv2
import numpy as np

video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 440)
video.set(10, 50)

while True:
    _, frame = video.read()
    # frame = img = cv2.flip(frame, 1)
    gray_image= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detectors =  detector.detectMultiScale(gray_image, 1.2, 3)


    for (x, y, w, h) in detectors :
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
    cv2.imshow("image", frame)


    if cv2.waitKey(1) & 0xFF == ord("b"):
            break


# import matplotlib.pyplot as plt
# image = cv2.imread('display_image.jpg')
# width = image.shape[0]
# height = image.shape[1]

# image_resize = cv2.resize(image, (int(width / 3), int(height / 3)), interpolation = cv2.INTER_AREA)
# gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
# # cv2.imshow("real image", image_resize)
# cv2.imshow("gray image", gray)

# detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# detectors =  detector.detectMultiScale(gray, 1.2, 2)


# for (x, y, w, h) in detectors :
#     print(x, y, w, h)
#     cv2.rectangle(image_resize, (x, y), (x+w, y+h), (255, 0, 0), 3)
#     cv2.imshow("image", image_resize)


# cv2.waitKey(0)
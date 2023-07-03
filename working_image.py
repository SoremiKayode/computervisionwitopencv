import cv2 as c
import numpy as np
import dlib

# img = c.imread("car.jpg")
# scale_percent = 60
# width = int(img.shape[1] * scale_percent / 400)
# height = int(img.shape[0] * scale_percent / 400)

# dim = (width, height)
# print(dim)
# images = c.resize(img, dim, interpolation = c.INTER_AREA)
# c.imwrite("car_2.png", images)
# CONVERTING IMAGE TO GRAY
# img_gray = c.cvtColor(images, c.COLOR_BGR2GRAY)

#BLUR IMAGE
# img_blur = c.GaussianBlur(images, (7, 7), 0)

# img_canny = c.Canny(images, 100, 100)
# c.imshow("Image", img_canny)

# USING WEBCAM
# video = c.VideoCapture(0)
# video.set(3, 640)
# video.set(4, 440)
# video.set(10, 50)

#GETTING THE WIDTH AND HEIGHT OF YOUR FRAME RECORDER
# width = int(video.get(c.CAP_PROP_FRAME_WIDTH))
# height = int(video.get(c.CAP_PROP_FRAME_HEIGHT))

# CALLING THE VIDEO WRITER USING CV2 AND PASSING THE NEEDED PARAMETER
# out = c.VideoWriter('output.mp4', c.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

# LOOPING FOR VIDEO DISPLAY
# while True:
#     success, img = video.read()
#     c.imshow("My Video", img)
#     if c.waitKey(1) & 0xFF == ord("b"):
#         break

image = c.imread("my_image.png")
p0 = 10, 10
p1 = 110, 90
p2 = 500, 10

red = (0, 0, 255)
line_image = c.line(image, p0, p1, red, 10)
line_image = c.line(image, p0, p2, (200, 200, 0), 10)

c.waitKey(0)


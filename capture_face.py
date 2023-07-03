import cv2
import numpy as np
import dlib
# import matplotlib.pyplot as plt

image = cv2.imread("20220410_132435.jpg", cv2.COLOR_BGR2RGB)
scale_percent = 10
width = int(image.shape[1] / 4)
height = int(image.shape[0] / 6)

dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
p1 = 100, 100
p2 = 100, 300

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detectors = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detector = detectors.detectMultiScale(gray, 1.2, 3)

for (x, y, w, h) in detector:
    print(x, y, w, h)
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)
    cv2.imshow("My Video", image)
cv2.waitKey(0) 
#Drawing a line in cv2
# cv2.line(image, p1, p2, (0, 0, 255), 5)

#Drawing a Rectangle on the image
# cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 0,), 5)

#Draw a circle 
# cv2.circle(image, (100, 300), 100, (255, 0, 0), 5)

# Drawing an ellipse
# cv2.ellipse(image, (300, 300), (100, 50), 10, 360, 180, (0, 0, 255), 5)

# Drawing a POlygon
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv2.polylines(image, [pts], True, (0, 255, 255))

# cv2.putText(image, "Adeyemi Daniel", (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2, cv2.LINE_8)
# cv2.imshow("Line Image", image)


# video = cv2.VideoCapture(0)
# video.set(3, 640)
# video.set(4, 440)
# video.set(10, 50)

# GETTING THE WIDTH AND HEIGHT OF YOUR FRAME RECORDER
# width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# CALLING THE VIDEO WRITER USING CV2 AND PASSING THE NEEDED PARAMETER
# out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
# LOOPING FOR VIDEO DISPLAY
# while True:
#     success, img = video.read()
#     img = cv2.flip(img, 1)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     detectors = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#     detector = detectors.detectMultiScale(gray, 1.2, 3)

#     for (x, y, x1, y1) in detector:
#         print(x, y, x1, y1)
#         cv2.rectangle(img, (x, y), (x1, y1), (255, 0, 0), 3)
#     cv2.imshow("My Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("b"):
#         break


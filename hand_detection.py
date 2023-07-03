from abc import ABC
from cvzone.HandTrackingModule import HandDetector
import cvzone
import cv2
import math
import numpy as np


video = cv2.VideoCapture(0)

x = [300, 245, 200, 178, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coeff = np.polyfit(x, y, 2) # y = Ax^2 + Bx + C

detector = HandDetector(detectionCon=0.8, maxHands=1)
while True:
    success, frame = video.read()
    hands = detector.findHands(frame, draw=False)

    if hands:
        imlist = hands[0]["lmList"]
        bbox = hands[0]["bbox"]
        x1, y1, z = imlist[5]
        x2, y2, z2 = imlist[17]
        distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
        A, B, C = coeff
        distance_cm = A * distance ** 2 + B * distance + C

        cvzone.cornerRect(frame, bbox)
        cvzone.putTextRect(frame, f"{int(distance_cm)} cm", (bbox[0], bbox[1]-10))
        # print(abs(x2 - x1), distance)
    #     bbox = hands["bbox"]
    #     hand_center = hands["center"]
    #     hand_type = hands["type"]
        
    #     cv2.rectangle(frame, bbox, (2555, 0, 0), 2)

    cv2.imshow("Hand Display", frame)
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break

# from cvzone.FaceDetectionModule import FaceDetector
# import cv2

# cap = cv2.VideoCapture(0)
# detector = FaceDetector()

# while True:
#     success, img = cap.read()
#     img, bboxs = detector.findFaces(img)

#     if bboxs:
#         # bboxInfo - "id","bbox","score","center"
#         center = bboxs[0]["center"]
#         cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# from cvzone.HandTrackingModule import HandDetector
# import cv2

# cap = cv2.VideoCapture(0)
# detector = HandDetector(detectionCon=0.8, maxHands=2)
# while True:
#     # Get image frame
#     success, img = cap.read()
#     # Find the hand and its landmarks
#     hands, img = detector.findHands(img)  # with draw
#     # hands = detector.findHands(img, draw=False)  # without draw

#     if hands:
#         # Hand 1
#         hand1 = hands[0]
#         lmList1 = hand1["lmList"]  # List of 21 Landmark points
#         bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
#         centerPoint1 = hand1['center']  # center of the hand cx,cy
#         handType1 = hand1["type"]  # Handtype Left or Right

#         fingers1 = detector.fingersUp(hand1)

#         if len(hands) == 2:
#             # Hand 2
#             hand2 = hands[1]
#             lmList2 = hand2["lmList"]  # List of 21 Landmark points
#             bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
#             centerPoint2 = hand2['center']  # center of the hand cx,cy
#             handType2 = hand2["type"]  # Hand Type "Left" or "Right"

#             fingers2 = detector.fingersUp(hand2)

#             # Find Distance between two Landmarks. Could be same hand or different hands
#             length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
#             # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
#     # Display
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
# cap.release()
# cv2.destroyAllWindows()
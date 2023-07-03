import cv2
import numpy as np

image = cv2.imread("photo-1488134684157-fea2d81a5ec4.jpeg")
c_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



object_names = []
with open("coco.names.txt") as file:
    object_names = file.read().strip("\n").rsplit("\n")
   
print(object_names)
print(len(object_names))
config_path = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt.txt"
weight_path = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weight_path, config_path)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    c_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    class_ids, confs, bboxes = net.detect(frame, confThreshold=0.6)

    if len(class_ids) != 0:
        for class_id, conf, bbox in zip(class_ids.flatten(), confs.flatten(), bboxes):
            if class_id < 81:
                cv2.rectangle(frame, bbox, (255, 0, 0), 3)
                cv2.putText(frame, str(object_names[class_id - 1]), (bbox[0]+10, bbox[1]+40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
    cv2.imshow("Images", frame)
    if cv2.waitKey(1) & 0xFF == ord("b"):
            break
# print(class_ids)
# print(bbox)
# cv2.waitKey(0)
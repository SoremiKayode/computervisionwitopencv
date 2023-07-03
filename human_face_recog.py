import cv2
import face_recognition
import os

list_of_names = []

path = "faces_library"

name_list = os.listdir(path)
list_of_names = name_list

train_image = face_recognition.load_image_file(f"{path}/Daniel.jpg")
c_train_image = cv2.cvtColor(train_image, cv2.COLOR_RGB2BGR)
train_encoding = face_recognition.face_encodings(train_image)[0]
train_location = face_recognition.face_locations(train_image)[0]

test_image = face_recognition.load_image_file("ab41f12523294f478592830cf31d17f6.jpg")
c_test_image = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)
test_encoding = face_recognition.face_encodings(train_image)[0]
test_location = face_recognition.face_locations(train_image)[0]

result = face_recognition.compare_faces([train_encoding], test_encoding)
print(result)
cv2.rectangle(c_train_image, (train_location[3], train_location[0]), (train_location[1], train_location[2]), (255, 0, 0), 2)

cv2.rectangle(c_test_image, (test_location[3], test_location[0]), (test_location[1], test_location[2]), (255, 0, 0), 2)
cv2.imshow("Train image", c_test_image)
cv2.imshow("Train image", c_train_image)

cv2.waitKey(0)




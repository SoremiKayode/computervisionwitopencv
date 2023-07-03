import face_recognition
import cv2
# train_image = cv2.imread("mypicture.JPG")
train_image = face_recognition.load_image_file("faces_library/kayode_2.JPG")
train_image = cv2.cvtColor(train_image, cv2.COLOR_BGR2RGB)
face_location_train = face_recognition.face_locations(train_image)[0]
train_encodings = face_recognition.face_encodings(train_image)[0]
test_image = face_recognition.load_image_file("faces_library/christian-ferrer-y-tdaKCTOiI-unsplash.jpg")
test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
face_location_test = face_recognition.face_locations(test_image)[0]
test_encodings = face_recognition.face_encodings(test_image)[0]

result = face_recognition.compare_faces([train_encodings], test_encodings)
face_distance = face_recognition.face_distance([train_encodings], test_encodings)

print(result)
print(face_distance)


# cv2.rectangle(train_image, (face_location_train[3], face_location_train[0]), (face_location_train[1], face_location_train[2]), (0, 255, 0), 3)
# cv2.rectangle(test_image, (face_location_test[3], face_location_test[0]), (face_location_test[1], face_location_test[2]), (0, 255, 0), 3)
# cv2.putText(train_image, f"{result[0]} - {face_distance[0]}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 00, 0), 2)
# cv2.imshow("train_image", train_image)
# cv2.imshow("test_image", test_image)
# cv2.waitKey(0)
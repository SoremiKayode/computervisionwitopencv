import os
import face_recognition
import numpy as np
import cv2

# This function is trying to select image in a folder,
# it open the image using openCv
#  it convert each of the image into RGB
# and get the encoding of the image

all_images = os.listdir("faces_library")

def encodings(images):
    encoded_image = []
    for image in images:
        load_image = cv2.imread(f"faces_library/{image}")
        converted_image = cv2.cvtColor(load_image, cv2.COLOR_BGR2RGB)
        image_encode = face_recognition.face_encodings(converted_image)[0]
        encoded_image.append(image_encode)
    return encoded_image

# def face_locations(images):
#     location_of_faces = []
#     for image in images :
#         load_image = cv2.imread(f"faces_library/{image}")
#         converted_image = cv2.cvtColor(load_image, cv2.COLOR_BGR2RGB)
#         image_encode = face_recognition.face_locations(converted_image)[0]
#         location_of_faces.append(image_encode)
#     return location_of_faces

encode_list = encodings(all_images)

# test_image = face_recognition.load_image_file('kayode_2.JPG')
# face_in_encoding = face_recognition.face_encodings(test_image)
# matches = face_recognition.compare_faces(encode_list, face_in_encoding[0])
# face_distance = face_recognition.face_distance(encode_list, face_in_encoding[0])
# print(all_images)
# print(np.argmin(face_distance))
video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    min_frame = cv2.resize(frame, (int(frame.shape[0] / 4), int(frame.shape[1] /4 )))
    converted_frame = cv2.cvtColor(min_frame, cv2.COLOR_BGR2RGB)
    face_in_encoding= face_recognition.face_encodings(converted_frame)
    face_in_location= face_recognition.face_locations(converted_frame)

    for encode_face, located_face in zip(face_in_encoding, face_in_location):
        matches = face_recognition.compare_faces(encode_list, encode_face)
        face_distance = face_recognition.face_distance(encode_list, encode_face)

        match_index = np.argmin([face_distance])
        if matches[match_index]:
            name = all_images[match_index]

    for x, y, w, h in face_in_location:
        cv2.rectangle(frame, (h*4, x*4), (y*4, w*4), (0, 255, 0), 2)
        cv2.rectangle(frame, (h-6, w-35), (y, w), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name[:-4], (h, w-6,), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow("image", frame)
    if cv2.waitKey(1) & 0xFF == ord('b'):
        break

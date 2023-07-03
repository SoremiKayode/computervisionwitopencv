import os
import face_recognition
import numpy as np
import cv2
import datetime
import sqlite3

connection = sqlite3.connect("attendance.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE if not exists attendance_system(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) UNIQUE, encoded_image TEXT UNIQUE)")

your_name = input("")
video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()

    if 0xFF == ord('c'):
        cv2.imwrite(f"faces_library\{your_name}", frame)
        face_encode = face_recognition.face_encodings(frame)[0]
        print(face_encode)

        # cursor.execute("INSERT INTO attendance_system(name, encoded_image) VALUES(?, ?)", (your_name, face_encode))
    cv2.imshow("image", frame)
    if cv2.waitKey(1) & 0xFF == ord('b'):
        converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_encode = face_recognition.face_encodings(converted_frame)
        if face_encode :
            cv2.imwrite(f"faces_library/{your_name}.png", frame)
            cursor.execute("INSERT INTO attendance_system(name, encoded_image) VALUES(?, ?)", (your_name, str(face_encode[0][:])))
            connection.commit()
            connection.close() 
            break


# print(datetime.datetime.now())
# list_of_names = []

# path = "faces_library"

# name_list = os.listdir(path)
# list_of_names = name_list

# def encodings(images):
#     encode_list = []
#     for image in images:
#         my_image = face_recognition.load_image_file(f"{path}/{image}")
#         face_encode = face_recognition.face_encodings(my_image)[0]
#         encode_list.append(face_encode)
#     return encode_list

# encoding_list = encodings(list_of_names)

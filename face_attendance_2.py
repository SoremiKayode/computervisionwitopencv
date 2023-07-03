import os
import face_recognition
import numpy as np
import cv2
import datetime
import sqlite3

connection = sqlite3.connect("attendance.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE if not exists time_resume(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) UNIQUE, time_arrive TEXT UNIQUE)")
# cursor.execute("INSERT INTO time_resume(name) VALUES('kayode')")
connection.commit()
arrive = str(datetime.datetime.now())
list_of_names = []
# name = 0

path = "faces_library"

name_list = os.listdir(path)
list_of_names = name_list

def encodings(images):
    encode_list = []
    for image in images:
        my_image = face_recognition.load_image_file(f"{path}/{image}")
        face_encode = face_recognition.face_encodings(my_image)[0]
        encode_list.append(face_encode)
    return encode_list

encoding_list = encodings(list_of_names)

video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    # min_frame = cv2.resize(frame, (int(frame.shape[0] / 2), int(frame.shape[1] /3 )))
    converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_in_encodings= face_recognition.face_encodings(converted_frame)
    face_in_locations= face_recognition.face_locations(converted_frame)

    for face_encode, face_location in zip(face_in_encodings, face_in_locations):
        matches = face_recognition.compare_faces(encoding_list, face_encode)
        face_distance = face_recognition.face_distance(encoding_list, face_encode)

        match_index = np.argmin(face_distance)
        if matches[match_index] :
            name = list_of_names[match_index]
            name_real = name[:-4]
            query = cursor.execute(f"SELECT * FROM time_resume WHERE name = '{name_real}' ")
            for item in query:
                if item[1] is NULL:
                    cursor.execute(f"UPDATE time_resume SET time_arrive = '{arrive}' WHERE name = '{name_real}' ")
                else:
                    print(f"You have successfully signed in as {item[2]}")
                connection.commit()
                # print(name)




            for x, y, w, h in face_in_locations:
                cv2.rectangle(frame, (h + 10, x), (y + 10, w), (0, 255, 0), 2)
                cv2.rectangle(frame, (h-6, w-35), (y, w), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name[:-4], (h, w-6,), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    

    cv2.imshow("image", frame)

    if cv2.waitKey(1) & 0xFF == ord('b'):
        break
print(encoding_list)
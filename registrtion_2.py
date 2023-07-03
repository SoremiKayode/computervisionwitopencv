import cv2
import numpy as np
import sqlite3
import datetime
import os
import face_recognition
import keyboard

connection = sqlite3.connect("attendance.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE if not exists attendance_system(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT VARCHAR(100))")
name = input("")
video = cv2.VideoCapture(0)
array_search = []
while True :
    success, frame = video.read()
    convert_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    

    if success:
        encoded_image = face_recognition.face_encodings(frame)
        bbox = face_recognition.face_locations(frame)
        if encoded_image  and bbox:
            bbox = face_recognition.face_locations(frame)[0]
            encoded_image = face_recognition.face_encodings(frame)
            print(bbox)
            cv2.rectangle(frame, (bbox[3], bbox[0]), (bbox[1], bbox[2]), (255, 0, 0), 2)
        if cv2.waitKey(1) & 0xFF == ord("b") :
            fetch = cursor.execute("SELECT * FROM attendance_system")
            for data in fetch:
                array_search.append(data[1])
            if name in array_search:
                print("name already exist")
            else :
                cv2.imwrite(f"face_library/{name}.png", convert_frame)
                cursor.execute("INSERT INTO attendance_system(name, encoded_image) VALUES(?, ?)", (name, str(encoded_image[0][:])))
                connection.commit()
                connection.close()
            break
        cv2.imshow("Registration", frame)







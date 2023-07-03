from ast import While
from turtle import speed
from djitellopy import tello
import keyboard
import time
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()
# drone.set_speed(100)
drone.streamon()
class fly_drone():

    def __init__(self, speed, degree):
        self.speed = speed
        self.degree = degree

    def fly(self):
        if keyboard.is_pressed("LEFT") :
            drone.move_left(self.speed)
            time.sleep(0.01)
        elif keyboard.is_pressed("RIGHT"):
            drone.move_right(self.speed)
            time.sleep(0.03)
        elif keyboard.is_pressed("UP"):
            drone.move_forward(self.speed)
            time.sleep(0.03)
        elif keyboard.is_pressed("DOWN"):
            drone.move_back(self.speed)
            time.sleep(0.01)
        elif keyboard.is_pressed("u"):
            drone.move_up(self.speed)
            time.sleep(0.01)
        elif keyboard.is_pressed("d"):
            drone.move_down(self.speed)
            time.sleep(0.01)
        elif keyboard.is_pressed("f"):
            drone.flip_right()
            time.sleep(0.01)
        elif keyboard.is_pressed("l"):
            drone.flip_left()
            time.sleep(0.01)
        elif keyboard.is_pressed("c"):
            drone.rotate_clockwise(self.degree)
            time.sleep(0.03)
        elif keyboard.is_pressed("a"):
            drone.rotate_counter_clockwise(self.degree)
            time.sleep(0.03)


dr = fly_drone(50, 45)

while True:
    dr.fly()
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (200, 200))
    cv2.imshow("Drone", img)
    if keyboard.is_pressed("ENTER") :
        break
    cv2.waitKey(0)




# drone.takeoff()
# time.sleep(1)
# drone.move_forward(100)
# time.sleep(1)
# drone.move_right(100)
# time.sleep(1)
# drone.move_left(50)
# time.sleep(1)
# drone.move_back(50)
# time.sleep()
# drone.move_up(100)
# time.sleep(1)
# drone.flip_left()
# drone.flip_right()
# time.sleep(1)
# drone.rotate_clockwise(90)
# time.sleep(1)
# drone.rotate_counter_clockwise(180)
# time.sleep(1)
drone.send_rc_control(0, 0, 0, 0)
drone.land()



# while True :
#     if keyboard.is_pressed("u"):
#         print("move up")
#         time.sleep(0.3)
#     elif keyboard.is_pressed("s"):
#         break


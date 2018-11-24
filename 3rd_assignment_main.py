#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################
from car import Car
import time
import rear_wheels
import front_wheels

direction = front_wheels.Front_Wheels(db='config')
driving = rear_wheels.Rear_Wheels(db='config')


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()
    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):

        current_angle = 0

        cnt = 0



        while True:

            # sensor #

            dis = self.car.distance_detector.get_distance()

            if dis <= 25:
                direction.turn(30)
                driving.go_forward(50)
                time.sleep(0.85)
                direction.turn(160)
                time.sleep(1.75)


            else:

                # Go

                if current_angle != 90 and self.car.line_detector.is_equal_status([0, 0, 1, 0, 0]):
                    direction.center_alignment()
                    driving.go_forward(40)

                # Left #

                elif current_angle != 65 and self.car.line_detector.is_equal_status([0, 1, 1, 0, 0]):
                    direction.turn(65)
                    driving.go_forward(40)
                    current_angle = 65

                elif current_angle != 55 and self.car.line_detector.is_equal_status([1, 1, 0, 0, 0]):
                    direction.turn(55)
                    driving.go_forward(40)
                    current_angle = 55

                elif current_angle != 40 and self.car.line_detector.is_equal_status([1, 1, 1, 0, 0]):
                    direction.turn(40)
                    driving.go_forward(28)
                    current_angle = 40

                elif current_angle != 35 and self.car.line_detector.is_equal_status([1, 1, 1, 1, 0]):
                    direction.turn(35)
                    driving.go_forward(40)
                    current_angle = 35

                # Right #

                elif current_angle != 125 and self.car.line_detector.is_equal_status([0, 0, 0, 1, 1]):
                    direction.turn(125)
                    driving.go_forward(40)
                    current_angle = 125

                elif current_angle != 120 and self.car.line_detector.is_equal_status([0, 0, 1, 1, 0]):
                    direction.turn(120)
                    driving.go_forward(40)
                    current_angle = 120

                elif current_angle != 140 and self.car.line_detector.is_equal_status([0, 0, 1, 1, 1]):
                    direction.turn(140)
                    driving.go_forward(40)
                    current_angle = 140

                elif current_angle != 145 and self.car.line_detector.is_equal_status([0, 1, 1, 1, 1]):
                    direction.turn(145)
                    driving.go_forward(40)
                    current_angle = 145

                # back #

                elif self.car.line_detector.is_equal_status([0,0,0,0,0]) and current_angle != 90:
                    direction.center_alignment()
                    driving.go_backward(40)
                    time.sleep(0.3)

                # count #
                elif self.car.line_detector.is_equal_status([1,1,1,1,1]):
                    driving.go_forward(40)
                    cnt = cnt + 1

                elif cnt > 2:
                    driving.stop()







if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()

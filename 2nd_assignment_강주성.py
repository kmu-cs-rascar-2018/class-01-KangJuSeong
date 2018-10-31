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

        driving.go_forward(25)

        current_angle = 0

        while True:

            if current_angle != 90 and self.car.line_detector.is_equal_status([0, 0, 1, 0, 0]):
                direction.center_alignment()
                current_angle = 90

            # Very Little step turn left and right #
            if current_angle != 100 and self.car.line_detector.is_equal_status([0, 0, 1, 1, 0]):
                direction.turn(100)
                current_angle = 100
            elif current_angle != 85 and self.car.line_detector.is_equal_status([0, 1, 1, 0, 0]):
                direction.turn(80)
                current_angle = 80

            # Little step turn left and right #
            elif current_angle != 105 and self.car.line_detector.is_equal_status([0, 0, 0, 1, 1]):
                direction.turn(105)
                current_angle = 105
            elif current_angle != 75 and self.car.line_detector.is_equal_status([1, 1, 0, 0, 0]):
                direction.turn(75)
                current_angle = 75

            # Large step turn left and right #
            elif current_angle != 60 and self.car.line_detector.is_equal_status([1, 1, 1, 0, 0]):
                direction.turn(60)
                current_angle = 60
            elif current_angle != 120 and self.car.line_detector.is_equal_status([0, 0, 1, 1, 1]):
                direction.turn(120)
                current_angle = 120

            # Very Large step turn left and right #
            elif current_angle != 55 and self.car.line_detector.is_equal_status([1, 1, 1, 1, 0]):
                direction.turn(55)
                current_angle = 55
            elif current_angle != 125 and self.car.line_detector.is_equal_status([0, 1, 1, 1, 1]):
                direction.turn(125)
                current_angle = 125

            print(self.car.line_detector.read_digital)


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
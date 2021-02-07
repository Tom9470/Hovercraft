import RPi.GPIO as GPIO
import time


class Hovercraft():

    def __init__(lift, lthrust, rthrust, rudder):

        super().__init__()

        GPIO.setmode(GPIO.BOARD)
        global lift_pin
        lift_pin = lift
        GPIO.setup(lift_pin, GPIO.OUT)
        
        if lthrust != lift:
            global left_thrust
            left_thrust = lthrust
            GPIO.setup(left_thrust, GPIO.OUT)
        else:
            return("left thrust is the same as one of the other pins")

        if rthrust != lthrust and rthrust != lift:
            global right_thrust
            right_thrust = rthrust
            GPIO.setup(lift_pin, GPIO.OUT)
        else:
            return("right thrust is the same as one of the other pins")

        if rudder != rthrust and rudder != lthrust and rudder != lift:
            if isinstance(rudder, int):
                global rudder_pin
                rudder_pin = rudder
                GPIO.setup(lift_pin, GPIO.OUT)
        else:
            return("rudder pin is the same as one of the other pins")


    #def 

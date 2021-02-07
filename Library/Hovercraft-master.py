import RPI.GPIO as GPIO
import time


class Hovercraft():

    def __init__(lift, lthrust, rthrust, rudder):

        super().__init__()


        global lift_pin
        lift_pin = lift
        
        if lthrust != lift:
            global left_thrust
            left_thrust = lthrust
        else:
            return("left thrust is the same as one of the other pins")

        if rthrust != lthrust and rthrust != lift:
            global right_thrust
            right_thrust = rthrust
        else:
            return("right thrust is the same as one of the other pins")

        if rudder != rthrust and rudder != lthrust and rudder != lift:
            if isinstance(rudder, int):
                global rudder_pin
                rudder_pin = rudder
        else:
            return("rudder pin is the same as one of the other pins")


    #def 

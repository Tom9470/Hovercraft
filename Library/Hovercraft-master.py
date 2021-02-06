import RPI.GPIO as GPIO
import time

class Hovercraft():

    def __init__(lift_pin, left_thrust, right_thrust, rudder_pin):
        global lift_pin
        if left_thrust != lift_pin:
            global left_thrust
        else:
            return("left thrust is the same as one of the other pins")
        if right_thrust != left_thrust and right_thrust != lift_pin
            global right_thrust
        else:
            return("right thrust is the same as one of the other pins")
        if isinstance(rudder_pin, int) and rudder_pin != right_thrust and rudder_pin != left_thrust and rudder_pin != lift_pin:
            global rudder_pin
        else:
            return("rudder pin is the same as one of the other pins")
    
    def

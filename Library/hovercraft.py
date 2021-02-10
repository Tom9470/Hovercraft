import RPi.GPIO as GPIO
import time
print("The UPHCL. (Universal Pi Hovercraft Control Library)\nSyntax for setup is Hovercraft(lift pin, left thrust pin, right thrust pin, rudder pin.).\n If you do not have a rudder, then put \"None\".\n for usage, refer to https://github.com/Tom9470/Hovercraft")

def __init__(lift, lthrust, rthrust, rudder):

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
        GPIO.cleanup()

    if rthrust != lthrust and rthrust != lift:
        global right_thrust
        right_thrust = rthrust
        GPIO.setup(right_thrust, GPIO.OUT)
    else:
        return("right thrust is the same as one of the other pins")
        GPIO.cleanup()

    if rudder != rthrust and rudder != lthrust and rudder != lift:
        if isinstance(rudder, int):
            global is_rudder_pin
            is_rudder_pin = 1
            global rudder_pin
            rudder_pin = rudder
            GPIO.setup(rudder_pin, GPIO.OUT)
    else:
        return("rudder pin is the same as one of the other pins")
        GPIO.cleanup()
    
    def startup():
        
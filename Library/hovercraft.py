import RPi.GPIO as GPIO
import time
print("The UPHCL. (Universal Pi Hovercraft Control Library)\nSyntax for setup is Hovercraft(lift pin, maximum lift power in percent, left thrust pin, right thrust pin, rudder pin.).\n If you do not have a rudder, then put \"None\".\n for usage, refer to https://github.com/Tom9470/Hovercraft")
global current_lift
current_lift = 0
def setup(lift, maxlift, lthrust, rthrust, rudder):

    GPIO.setmode(GPIO.BOARD)
    global lift_pin
    global maxlift
    lift_pin = GPIO.setup(lift, GPIO.OUT)
    GPIO.output(lift_pin, GPIO.LOW)
    liftpwm = GPIO.PWM(lift_pin, 100)
    liftpwm.start(0)
       
    if lthrust != lift:
        global left_thrust
        left_thrust = GPIO.setup(lthrust, GPIO.OUT)
        GPIO.output(left_thrust, GPIO.LOW)
        ltpwm = GPIO.PWM(left_thrust, 100)
        ltpwm.start(0)

    else:
        return("left thrust is the same as one of the other pins")
        GPIO.cleanup()

    if rthrust != lthrust and rthrust != lift:
        global right_thrust
        right_thrust = GPIO.setup(rthrust, GPIO.OUT)
        GPIO.output(right_thrust, GPIO.LOW)
        rtpwm = GPIO.PWM(right_thrust, 100)
        rtpwm.start(0)

    else:
        return("right thrust is the same as one of the other pins")
        GPIO.cleanup()

    if rudder != rthrust and rudder != lthrust and rudder != lift:
        global is_rudder_pin
        if isinstance(rudder, int):
            is_rudder_pin = 1
            global rudder_pin
            rudder_pin = GPIO.setup(rudder, GPIO.OUT)
            yawpwm = GPIO.PWM(rudder_pin, 100)
            yawpwm.start(0)
        
        else:
            is_rudder_pin = 0

    else:
        return("rudder pin is the same as one of the other pins")
        GPIO.cleanup()
    
    def change_lift(magnitude):
        try:
            if current_lift < magnitude:
                for PW in range(current_lift, magnitude, 1):
                    pwm.ChangeDutyCycle(PW)
                    time.sleep(0.05)

            elif current_lift > magnitude:
                for PW in range(current_lift, magnitude, -1):
                    pwm.ChangeDutyCycle(PW)
                    time.sleep(0.05)

        except:
            print("That didn't work. change_lift() requires and only accepts an integer parameter")
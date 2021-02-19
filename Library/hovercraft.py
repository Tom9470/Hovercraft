import RPi.GPIO as GPIO
import time
print("The UPHCL. (Universal Pi Hovercraft Control Library)\nSyntax for setup is:\nHovercraft(lift pin, maximum lift power in percent, forward left thrust pin, backward left thrust pin, forward right thrust pin, backward right thrust pin, rudder pin.).\n If you do not have a rudder, then put \"None\".\n for usage, refer to https://github.com/Tom9470/Hovercraft")
global current_lift
current_lift = 0
usedpins = list()
global thrust
thrust = int(0)

def setup(lift, maxlift, lthrustfwd, lthrustbkwd, rthrustfwd, rthrustbkwd, rudder):

    GPIO.setmode(GPIO.BOARD)
    global lift_pin
    global maxlift
    lift_pin = GPIO.setup(lift, GPIO.OUT)
    GPIO.output(lift_pin, GPIO.LOW)
    liftpwm = GPIO.PWM(lift_pin, 100)
    liftpwm.start(0)
    usedpins.add(lift)
       
    if lthrustfwd not in usedpins:
        global left_thrustfwd
        left_thrustfwd = GPIO.setup(lthrustfwd, GPIO.OUT)
        GPIO.output(left_thrust, GPIO.LOW)
        ltfwdpwm = GPIO.PWM(left_thrustfwd, 100)
        ltfwdpwm.start(0)
        usedpins.add(lthrustfwd)

    else:
        return("left thrust forward is the same as one of the other pins")
        GPIO.cleanup()

    if lthrustbkwd not in usedpins:
        global left_thrustbkwd
        left_thrustbkwd = GPIO.setup(lthrustbkwd, GPIO.OUT)
        GPIO.output(left_thrustbkwd, GPIO.LOW)
        ltbkwdpwm = GPIO.PWM(left_thrustbkwd, 100)
        ltbkwdpwm.start(0)
        usedpins.add(lthrustbkwd)

    else:
        return("left thrust backward is the same as one of the other pins")
        GPIO.cleanup()

    if rthrustfwd not in usedpins:
        global right_thrustfwd
        right_thrustfwd = GPIO.setup(rthrustfwd, GPIO.OUT)
        GPIO.output(right_thrust, GPIO.LOW)
        rtfwdpwm = GPIO.PWM(right_thrustfwd, 100)
        rtfwdpwm.start(0)
        usedpins.add(rthrustfwd)

    else:
        return("right thrust forward is the same as one of the other pins")
        GPIO.cleanup()

    if rthrustbkwd not in usedpins:
        global right_thrustbkwd
        right_thrustbkwd = GPIO.setup(rthrustbkwd, GPIO.OUT)
        GPIO.output(right_thrustbkwd, GPIO.LOW)
        rtbkwdpwm = GPIO.PWM(right_thrustbkwd, 100)
        rtbkwdpwm.start(0)
        usedpins.add(rthrustbkwd)

    else:
        return("right thrust backward is the same as one of the other pins")
        GPIO.cleanup()


    if rudder not in usedpins:
        global is_rudder_pin
        if isinstance(rudder, int):
            is_rudder_pin = 1
            global rudder_pin
            rudder_pin = GPIO.setup(rudder, GPIO.OUT)
            yawpwm = GPIO.PWM(rudder_pin, 100)
            yawpwm.start(0)
            usedpins.add(rudder)
        
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
    
def change_thrust(magnitude):
    try:
        if magnitude > 0:
            left_thrustfwd.ChangeDutyCycle(magnitude)
            right_thrustfwd.ChangeDutyCycle(magnitude)
            left_thrustbkwd.ChangeDutyCycle(0)
            right_thrustbkwd.ChangeDutyCycle(0)
            thrust = magnitude
    
        elif magnitude < 0:
            left_thrustbkwd.ChangeDutyCycle(magnitude)
            right_thrustbkwd.ChangeDutyCycle(magnitude)
            left_thrustfwd.ChangeDutyCycle(0)
            right_thrustfwd.ChangeDutyCycle(0)
            thrust = magnitude
        
        elif magnitude == 0:
            left_thrustbkwd.ChangeDutyCycle(0)
            right_thrustbkwd.ChangeDutyCycle(0)
            left_thrustfwd.ChangeDutyCycle(0)
            right_thrustfwd.ChangeDutyCycle(0)
            thrust = 0

    except:
        print("change_thrust(needs to be an integer between -100 and 100)")

def turn(Direction):
    if Direction == "left":
        if thrust > 0: 
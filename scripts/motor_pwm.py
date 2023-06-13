import RPi.GPIO as GPIO
import time 

right_motor_b    =  24
right_motor_a    =  23
right_motor_en   =  25

left_motor_b    =   14
left_motor_a    =   15
left_motor_en   =   4


GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_a, GPIO.OUT)
GPIO.setup(right_motor_b, GPIO.OUT)
GPIO.setup(right_motor_en, GPIO.OUT)

GPIO.setup(left_motor_a, GPIO.OUT)
GPIO.setup(left_motor_b, GPIO.OUT)
GPIO.setup(left_motor_en, GPIO.OUT)

pwm_r = GPIO.PWM(right_motor_en , 1000)
pwm_l = GPIO.PWM(left_motor_en , 1000)

pwm_r.start(25)
pwm_l.start(25)

def forward(second):
    print("forward")
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)
    
def reverse(second):
    print("reverse")
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(second)
    
def left(second):
    print("left")
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)
    
def right(second):
    print("right")
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(second)

def stop():
    print("stopping")
    pwm_l.ChangeDutyCycle(0)
    pwm_r.ChangeDutyCycle(0)
    
def exit():
    GPIO.cleanup()

    
def main():
    forward(8)
    reverse(8)
    left(8)
    right(8)
    stop()
    exit()
    
    
    
if __name__ == "__main__":
    main()
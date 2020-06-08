import RPi.GPIO as GPIO
import time

channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin,GPIO.HIGH)
    print('on')

def motor_off(pin):
    GPIO.output(pin,GPIO.LOW)
    print('offp')

if __name__ =='__main__':
    try:
        motor_on(channel)
        time.sleep(2)
        motor_off(channel)
        time.sleep(2)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass



print('pere')

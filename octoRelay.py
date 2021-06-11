import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(27, GPIO.OUT) 
GPIO.setup(22, GPIO.OUT) 
GPIO.setup(23, GPIO.OUT) 
GPIO.output(17, True) 
sleep(2) 
GPIO.output(17, False)
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)

def symbole(delai1, delai0):
    GPIO.output(22, GPIO.HIGH)  # antenne sur broche 22
    time.sleep(delai0)
    GPIO.output(22, GPIO.LOW)
    time.sleep(delai1)


def transmission_data(data):
    start=time.time()
    for i in range(len(data)):
        if data[i] == '0':
            symbole(0.000999, 0.000333)  # T1_T3
            symbole(0.000333, 0.000999)  # T3_T1

        if data[i] == '1':
            symbole(0.000999, 0.000333)  # T1_T3
            symbole(0.000999, 0.000333)  # T1_T3
            
        if data[i] == '2':
            symbole(0.000333, 0.000999)
            symbole(0.000333, 0.000999)

        if data[i] == "S":
            symbole(0.010656, 0.000333) #T1_T32
    end=time.time()
    print('time transmission_data=',end-start)

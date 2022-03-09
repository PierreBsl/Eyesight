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
    for i in range(len(data)):
        if data[i] == '0':
            symbole(0.0009, 0.000175)  # T1_T3
            symbole(0.000175, 0.0009)  # T3_T1

        if data[i] == '1':
            symbole(0.0009, 0.000175)  # T1_T3
            symbole(0.0009, 0.000175)  # T1_T3
            
        if data[i] == '2':
            symbole(0.000175, 0.0009)
            symbole(0.000175, 0.0009)

        if data[i] == "S":
            symbole(0.010656, 0.000175) #T1_T32
            
def trans_2(data):
        if data == '0':
                symbole(0.0009, 0.000175)  # T1_T3
                symbole(0.000175, 0.0009)  # T3_T1
                print('0')

        if data == '1':
                symbole(0.0009, 0.000175)  # T1_T3
                symbole(0.0009, 0.000175)  # T1_T3
                print('1')

        if data == '2':
                symbole(0.000175, 0.0009)
                symbole(0.000175, 0.0009)

        if data == "S":
                symbole(0.010656, 0.000175)  # T1_T32
                print('S\n')
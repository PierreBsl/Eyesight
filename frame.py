#!/usr/bin/python3
import cv2
import time
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
from flask import flash

ip1 = '10.30.50.174'  # Modifier ici l'adresse ip de la camera IP
ip2 = '10.30.50.180'  # Modifier ici l'adresse ip de la camera IP

def grab_frame(text): #fonction prise de photo camera IP
    cap = cv2.VideoCapture(text)
    re, frame = cap.read()
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def grab_frame2(): #fonctio prise de photo camera_usb
    os.system('./cam.sh')
    ff = cv2.imread('/home/pi/oui.png')
    return ff


def photo():
    start=time.time()
    add_photo1 = 'http://' + ip1 + '/axis-cgi/jpg/image.cgi'
    add_photo2 = 'http://' + ip2 + '/axis-cgi/jpg/image.cgi'
    yeux = []
    yeux_ip = []
    yeux_ip2 = []
    countTimeout = 0
    liste = list()
    FiltreY = cv2.CascadeClassifier("haarcascade_eye.xml")

    # ---- Prise des photos ff=camera_usb ff_ip=camera ip
    while len(yeux) != 2 and len(yeux_ip) != 2 and countTimeout != 5 and len(yeux_ip2)!=2:
        countTimeout += 1
        ff = grab_frame2()
        yeux = FiltreY.detectMultiScale(ff, scaleFactor=1.3, minNeighbors=4, minSize=(50, 25))
        print(len(yeux))
        if ip1 != '':
            ff_ip1 = grab_frame(add_photo1)
            yeux_ip = FiltreY.detectMultiScale(ff_ip1, scaleFactor=1.3, minNeighbors=4, minSize=(50, 25))
            print(len(yeux_ip))
        if ip2 != '':
            ff_ip2 = grab_frame(add_photo2)
            yeux_ip2 = FiltreY.detectMultiScale(ff_ip2, scaleFactor=1.3, minNeighbors=4, minSize=(50, 25))
            print(len(yeux_ip2))
    print(countTimeout)
    # ---- Traitement de la photo de la caméra_usb
    if len(yeux) == 2:
        flash('Caméra USB', 'success')
        fichier = open("data.txt", "w")
        for (x, y, h, w) in yeux:
            print('x=', x, 'y=', y, 'h=', h, 'w=', w)
            cv2.rectangle(ff, (x, y), (x + h, y + w), (0, 255, 0), 5)
            message = str(x) + ' ' + str(y) + ' ' + str(h) + ' ' + str(w) + '\n'
            print(message)
            liste.append(message)
        fichier.write(liste[0])
        fichier.write(liste[1])
        fichier.close()
        cv2.imwrite("bonnePhoto.png", ff)

    # ---- Traitement de la photo de la caméra_IP1
    if len(yeux_ip) == 2:
        flash('Caméra IP 1', 'success')
        fichier = open("data.txt", "w")
        for (x, y, h, w) in yeux_ip:
            print('x=', x, 'y=', y, 'h=', h, 'w=', w)
            cv2.rectangle(ff_ip1, (x, y), (x + h, y + w), (0, 255, 0), 5)
            message = str(x) + ' ' + str(y) + ' ' + str(h) + ' ' + str(w) + '\n'
            print(message)
            liste.append(message)
        fichier.write(liste[0])
        fichier.write(liste[1])
        fichier.close()
        cv2.imwrite("bonnePhoto.png", ff_ip1)

    # ---- Traitement de la photo de la caméra_IP2
    if len(yeux_ip2) == 2:
        flash('Caméra IP 2', 'success')
        fichier = open("data.txt", "w")
        for (x, y, h, w) in yeux_ip2:
            print('x=', x, 'y=', y, 'h=', h, 'w=', w)
            cv2.rectangle(ff_ip2, (x, y), (x + h, y + w), (0, 255, 0), 5)
            message = str(x) + ' ' + str(y) + ' ' + str(h) + ' ' + str(w) + '\n'
            print(message)
            liste.append(message)
        fichier.write(liste[0])
        fichier.write(liste[1])
        fichier.close()
        cv2.imwrite("bonnePhoto.png", ff_ip2)

    # ---- Création du fichier pour autoriser la fonction On_off
    on = open('on_off.txt', 'w')
    if len(yeux) == 2 or len(yeux_ip) == 2 or len(yeux_ip2)==2:
        on.write('1')
    else:
        on.write('0')
    # ---- Création du fichier pour le choix de la caméra
    cam = open('choix.txt', 'w')
    if len(yeux) == 2:
        cam.write('0')
    elif len(yeux_ip) == 2:
        cam.write('1')
    elif len(yeux_ip2)==2:
    		cam.write('2')
    cam.close()
    # ---- Copie et redimension de la photo pour l'affichge sur l'interface web
    os.system('cp /home/pi/Downloads/bonnePhoto.png /home/pi/Downloads/eyesight/static/bonnePhoto.png')
    img=cv2.imread('/home/pi/Downloads/eyesight/static/bonnePhoto.png')
    res=cv2.resize(img,dsize=(384,288),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('/home/pi/Downloads/eyesight/static/bonnePhoto.png',res)
    end=time.time()
    print('time photo =',end-start)
    

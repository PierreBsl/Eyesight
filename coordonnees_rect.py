#!/usr/bin/python3
import sys
import cv2
from matplotlib import pyplot as plt
import image
import numpy as np
import RPi.GPIO as GPIO
import time

def coordonne():
    start=time.time()
#----Extraction des coordonnées des yeux 
    t = image.Extract("data.txt", 0)
    x1, y1, h1, w1 = t[0]
    x2, y2, h2, w2 = t[1]
#----Recherche emplacement des pupilles
    im = cv2.imread("bonnePhoto.png")
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    imageDroite = im[int(y1) + int(round(0.2 * int(h1))):int(y1) + int(round(0.8 * int(h1))),
                  int(x1) + int(round(0.2 * int(w1))):int(x1) + int(round(0.8 * int(w1)))]
    imageGauche = im[int(y2) + int(round(0.2 * int(h2))):int(y2) + int(round(0.8 * int(h2))),
                  int(x2) + int(round(0.2 * int(w2))):int(x2) + int(round(0.8 * int(w2)))]
    (ret, thresh2) = cv2.threshold(cv2.equalizeHist(cv2.cvtColor(imageGauche, cv2.COLOR_BGR2GRAY)), 6, 255,
                                   cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    thresh_erode = cv2.dilate(thresh2, kernel, iterations=1)
    (ret, thresh2_2) = cv2.threshold(cv2.equalizeHist(cv2.cvtColor(imageDroite, cv2.COLOR_BGR2GRAY)), 6, 255,
                                     cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    thresh_erode_2 = cv2.dilate(thresh2_2, kernel, iterations=1)
#---- Resultat de l'emplacement des pupilles gauche=0 droite=1
    result = image.position(image.taille(thresh_erode), thresh_erode) + image.position(image.taille(thresh_erode_2), thresh_erode_2)
    print('position yeux = ',result)
    if result==1 or result==0 :
      fichier = open("position_yeux.txt", 'w')
      fichier.write(str(result))
      fichier.close()
    else:
      fichier=open("position_yeux.txt", 'w')
      fichier.write('')
      fichier.close()
    print('result =' ,result)
    end=time.time()
    print('time coordonnees rect=',end-start)

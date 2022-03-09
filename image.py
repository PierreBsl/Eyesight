import symbole
import numpy as np
import time

def taille(image):
    count = 0
    for b in image[0]:
        count += 1
    return count

def position(taille, image):
    countGauche = 0
    countDroite = 0
    result = ""
    for i in image:
        count = 0
        for b in i:
            if count < (taille / 2):
                if b == 255:
                    countGauche += 1
            else:
                if b == 255:
                    countDroite += 1
            count += 1
    if countGauche > countDroite:
        result = 1
        # droite
    else:
        result = 0
        # gauche
    return result

def Extract(File, position):
    fichier = open(File, 'r')
    fichier.seek(position)
    r = fichier.readline()
    x1, y1, h1, w1 = r.split()
    r = fichier.readline()
    x2, y2, h2, w2 = r.split()
    number = fichier.readline()
    taille = fichier.tell()
    fichier.close()
    return ([x1, y1, h1, w1], [x2, y2, h2, w2])

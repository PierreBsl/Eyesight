import symbole
import time
import ouverture
from flask import flash

def On_off():
    start=time.time()
    # ---- Vérification de la detection des yeux
    autorisation=open("on_off.txt",'r')
    data=''
    autor=autorisation.read()
    print('authorisation=',autor)
    if autor=='1':
    # ---- Choix de la prise selon la caméra qui detecte les yeux
        fichier=open("position_yeux.txt",'r')
        pos=fichier.read()
        fichier.close()
        print('author ok')
        choix=open('choix.txt','r')
        cam=choix.read()
        if cam=='0':
            if pos=='0':
                gauche=open('objet_1.txt','r')
                data=gauche.read()
                gauche.close()
            else:
                droite=open('objet_2.txt','r')
                data=droite.read()
                droite.close()
        if cam=='1':
            if pos=='0':
                gauche=open('objet_3.txt','r')
                data=gauche.read()
                gauche.close()
            else:
                droite=open('objet_4.txt','r')
                data=droite.read()
                droite.close()
        if cam=='2':
            print('cam 2 ok')
            if pos=='0':
                gauche=open('objet_5.txt','r')
                data=gauche.read()
                gauche.close()
            else:
                droite=open('objet_6.txt','r')
                data=droite.read()
                droite.close()
        choix.close()
        fichier2=open("etat.txt",'r')
        etat=fichier2.read()
        L=list(etat)
        fichier2.close()
        count=0
    # ---- Envoie de la trame
        if data=='A1' and L[0]=='0' :
            while count<50:
                symbole.transmission_data(['1','0','0','0','1','0','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='A1' and L[0]=='1' :
            while count<50:
                symbole.transmission_data(['1','0','0','0','1','0','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='A2' and L[1]=='0':
            while count < 50:
                symbole.transmission_data(['1','0','0','0','0','1','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='A2' and etat[1]=='1':
            while count < 50:
                symbole.transmission_data(['1','0','0','0','0','1','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='A3' and L[2]=='0' :
            while count < 50:
                symbole.transmission_data(['1','0','0','0','0','0','1','0','1','1','1','0','S']) #on
                count+=1
        elif data=='A3' and L[2]=='1' :
            while count < 50:
                symbole.transmission_data(['1','0','0','0','0','0','1','0','1','1','1','1','S']) #off
                count+=1
        if data=='B1' and L[3]=='0':
            while count<50:
                symbole.transmission_data(['0','1','0','0','1','0','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='B1' and L[3]=='1' :
            while count<50:
                symbole.transmission_data(['0','1','0','0','1','0','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='B2' and L[4]=='0' :
            while count < 50:
                symbole.transmission_data(['0','1','0','0','0','1','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='B2' and L[4]=='1':
            while count < 50:
                symbole.transmission_data(['0','1','0','0','0','1','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='B3' and L[5]=='0':
            while count < 50:
                symbole.transmission_data(['0','1','0','0','0','0','1','0','1','1','1','0','S']) #on
                count+=1
        elif data=='B3' and L[5]=='1' :
            while count < 50:
                symbole.transmission_data(['0','1','0','0','0','0','1','0','1','1','1','1','S']) #off
                count+=1
        if data=='C1' and L[6]=='0' :
            while count < 50:
                symbole.transmission_data(['0','0','1','0','1','0','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='C1' and L[6]=='1' :
            while count < 50:
                symbole.transmission_data(['0','0','1','0','1','0','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='C2' and L[7]=='0' :
            while count < 50:
                symbole.transmission_data(['0','0','1','0','0','1','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='C2' and L[7]=='1' :
            while count < 50:
                symbole.transmission_data(['0','0','1','0','0','1','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='C3' and L[8]=='0' :
            while count < 50:
                symbole.transmission_data(['0','0','1','0','0','0','1','0','1','1','1','0','S']) #on
                count+=1
        elif data=='C3' and L[8]=='1' :
            while count < 50:
                symbole.transmission_data(['0','0','1','0','0','0','1','0','1','1','1','1','S']) #off
                count+=1
        if data=='D1' and L[9]=='0':
            while count < 50:
                symbole.transmission_data(['0','0','0','1','1','0','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='D1' and L[9]=='1' :
            while count < 50:
                symbole.transmission_data(['0','0','0','1','1','0','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='D2' and L[10]=='0' :
            while count < 50:
                symbole.transmission_data(['0','0','0','1','0','1','0','0','1','1','1','0','S']) #on
                count+=1
        elif data=='D2' and L[10]=='1' :
            while count < 50:
                symbole.transmission_data(['0','0','0','1','0','1','0','0','1','1','1','1','S']) #off
                count+=1
        if data=='D3' and L[11]=='0':
            while count < 50:
                symbole.transmission_data(['0','0','0','1','0','0','1','0','1','1','1','0','S']) #on
                count+=1
        elif data=='D3' and L[11]=='1':
            while count < 50:
                symbole.transmission_data(['0','0','0','1','0','0','1','0','1','1','1','1','S']) #off
                count+=1
        if data=='Aucun':
            print('Aucun objet séléctionné\n')
        # ---- Appelle de la fonction changement_etat afin de sauvegarder l'état actuelle des prises
        ouverture.changement_etat(data)
        flash(data, 'success')
        fichier.close()
    autorisation.close()
    end=time.time()
    print('time On_off=',end-start)
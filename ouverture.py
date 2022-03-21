def changement_etat(text):
    file=open('etat.txt','r')
    etat=file.read()
    file.close()
    file = open('etat.txt', 'w')
    L = list(etat)
    if text=='A1' and L[0]=='0':
        L[0]='1'
    elif text=='A1' and L[0]=='1':
        L[0]='0'
    if text == 'A2' and L[1] == '0':
        L[1] = '1'
    elif text == 'A2' and L[1] == '1':
        L[1] = '0'
    if text == 'A3' and L[2] == '0':
        L[2] = '1'
    elif text == 'A3' and L[2] == '1':
        L[2] = '0'
    if text == 'B1' and L[3] == '0':
        L[3] = '1'
    elif text == 'B1' and L[3] == '1':
        L[3] = '0'
    if text == 'B2' and L[4] == '0':
        L[4] = '1'
    elif text == 'B2' and L[4] == '1':
        L[4] = '0'
    if text == 'B3' and L[5] == '0':
        L[5] = '1'
    elif text == 'B3' and L[5] == '1':
        L[5] = '0'
    if text == 'C1' and L[6] == '0':
        L[6] = '1'
    elif text == 'C1' and L[6] == '1':
        L[6] = '0'
    if text == 'C2' and L[7] == '0':
        L[7] = '1'
    elif text == 'C2' and L[7] == '1':
        L[7] = '0'
    if text == 'C3' and L[8] == '0':
        L[8] = '1'
    elif text == 'C3' and L[8] == '1':
        L[8] = '0'
    if text == 'D1' and L[9] == '0':
        L[9] = '1'
    elif text == 'D1' and L[9] == '1':
        L[9] = '0'
    if text == 'D2' and L[10] == '0':
        L[10] = '1'
    elif text == 'D2' and L[10] == '1':
        L[10] = '0'
    if text == 'D3' and L[11] == '0':
        L[11] = '1'
    elif text == 'D3' and L[11] == '1':
        L[11] = '0'

    etat="".join(L)
    print(etat)
    file.write(etat)
    file.close()

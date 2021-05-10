#Function to Assign Cipher

def encryp(message):
    enc=[]
    for i in message:
        enc.append(ord(i)+5)
    d=[]
    for j in enc:
        d.append(chr(j))
    print(''.join(d))

encryp('Hi, Vyshak !!') # Testing the Function

def descryp(message):
    dec=[]
    for i in message:
        dec.append(ord(i)-5)
    e=[]
    for j in dec:
        e.append(chr(j))
    print(''.join(e))

descryp('Mn1%[~xmfp%&&')
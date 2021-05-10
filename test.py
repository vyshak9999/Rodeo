#Function to Assign Cipher

def encryp(message):
    enc=[]
    for i in message:
        enc.append(ord(i)+5)
    d=[]
    for j in enc:
        d.append(chr(j))
    print(''.join(d))

#encryp('Hi, Vyshak !!') # Testing the Function
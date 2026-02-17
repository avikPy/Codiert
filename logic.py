from cryptography.fernet import Fernet
import image
import os
import GPK

p = input()

if p=="ineedpass":
    GPK.create()
    exit()
else:
    a = Fernet( image.decode_image(p) )

com = None
while com != ["000",]:
    com = input("->> ").split()
    match com[0]:
        case "enc" :
            print(str(a.encrypt(com[1].encode()))[2:-1])
        case "dec" :
            print( str(a.decrypt(com[1]))[2:-1] )
            
os.system("cls")
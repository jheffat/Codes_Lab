#you can even use the fisrt method or the second one; if you want encryption more secure, enable the haslib
import hashlib    #calling the hashlib module to execute the hash
#my first encryption method from 2006; as optional you can enable hash  to get stronger the key and hard to guess
def cipher(msg,key,o):
    #key=hashlib.sha256(key.encode("utf-8")).hexdigest()
    klen=len(key);e="";c=0
    for x  in msg: 
        if o==True:
            e+=chr(ord(x)+ord(key[c%klen]) & 255)
        else:
            e+=chr(ord(x)-ord(key[c%klen]) & 255)
        c+=1    
    return e 
#is the second method to encrypt too, learned by UCATECI university DR, La vega; you can enable the hash too
def cipher2(msg,key):
    #key=hashlib.sha256(key.encode("utf-8")).hexdigest()
    klen=len(key);e="";c=0
    for x  in msg: 
        e+=chr(ord(x) ^ ord(key[c%klen]))    
        c+=1    
    return e 
    
#the msg target to be encrypted
msg="""Alzheimer's Law of Programming: If you read a code you wrote
more than two weeks ago it's like you're seeing it for the first time"""

#first method using +/- operators
msg_x=cipher(msg,"mariajose",True)   #encrypt
msg_y=cipher(msg_x,"mariajose",False)   #decrypt

print("Cifrado1:",f"[{msg_x}]")
print("Descifrado1:",f"[{msg_y}]")

print("\n---------------------------------------------------------------------\n")
#second method using XOR operator "^"
msg_x=cipher2(msg,"mariajose")
msg_y=cipher2(msg_x,"mariajose")

print("Cifrado2:",f"[{msg_x}]")
print("Descifrado2:",f"[{msg_y}]")

#By Jheff Mat 12/17/2022

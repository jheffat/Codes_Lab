#encrypt files(pictures,video, mp3,programs,text etc..); 2 methods to get the job done
def cipher(filename,key,o):
    klen=len(key);e=bytearray();c=0
    b=open(filename,"rb+")
    f=b.read()
    for x  in f: 
        if o==True:
            e+=bytes([x+ord(key[c%klen]) & 255])
        else:
            e+=bytes([x-ord(key[c%klen]) & 255])
        c+=1    
    b.seek(0)
    b.write(e)
    
def cipher2(filename,key):
    klen=len(key);e=bytearray();c=0
    b=open(filename,"rb+")
    f=b.read()
    for x  in f:       
        e+=bytes([x^ord(key[c%klen])])
        c+=1    
    b.seek(0)
    b.write(e)
    
    
#first method of file's encryption -------------------------------------

#cipher("filename","jose",True) #encrypt the file
#cipher("filename","jose",False) #decrypt the file

    
#second method of file's encryption -------------------------------------

#cipher2("filename","jose") #encrypt the file
#cipher2("filename","jose") #decrypt the file



#Jheff Mat 12/17/2022
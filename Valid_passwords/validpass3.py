
import re

def ValidPass(Passwd):
    errx=[]
    if 8<=len(Passwd)<=16:
        if not re.search("[0-9]",Passwd):errx+=["At least one Number"]
        if not re.search("[A-Z]",Passwd):errx+=["At least one Upper case"]
        if not re.search("[a-z]",Passwd):errx+=["At least one Lower case"]
        if not re.search("[@#$!]",Passwd):errx+=["At least one Special char: @#$!"]     
    else: errx+=["Must be at least 8 or more Characters, max 16"]
    return errx

state=["0"]
while state!=[]:
    state=ValidPass(input("enter password :"))      
    if len(state)> 0:
        for x in range(len(state)):
            print("**** "+state[x])


print("Password accepted")
     
import re

def ValidPass(Passwd):
    if 8<=len(Passwd)<=16:
        if  re.search("[A-Z]",Passwd):
            if  re.search("[a-z]",Passwd): 
                if  re.search("[0-9]",Passwd): 
                    if  re.search("[@#$!]",Passwd):
                        return True  
    else: return False
    return False

state=bool
while state!=True:
    state=ValidPass(input("Enter Password :"))
    print(state)

 
 
  
print("Password accepted")
     
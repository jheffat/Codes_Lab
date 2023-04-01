import random
import os
result=""
youico=""
limits=15
pc=""
you_p=0
pc_p=0
r_u=open("Rock-u.asc","r").readlines()
p_u=open("Paper-u.asc","r").readlines()
s_u=open("Scissor-u.asc","r").readlines()
r_pc=open("Rock-PC.asc","r").readlines()
p_pc=open("Paper-PC.asc","r").readlines()
s_pc=open("Scissor-PC.asc","r").readlines()
while True:
    os.system("cls")
    print("\nROCK,PAPER & SCISSOR---------------------------------------------------------------------------------")
    print("😈PC=",pc_p,"                                      🙂You=",you_p)
    
    if len(result)>0:
        for x in range(19):
           print("".join(pc[x]).strip("\n")," | ","".join(youico[x]).strip("\n"))
       
 
        print("█Result:"+result)
    result=""
   
    you=input("CHOOSE r p s:").lower()
    if you=="q":break
    if you not in "rps":continue
   
    pc=random.choice([s_pc,p_pc,r_pc])
    
    if you=="s": youico=s_u
    if you=="p": youico=p_u
    if you=="r": youico=r_u
    
    if pc==s_pc:
        if you=="s":
            result="DRAW!!!"         
        if you=="p":
            result="PC won"
            pc_p+=1
        if you=="r":
            result="You won"
            you_p+=1
    
    if pc==r_pc:
        if you=="s":
            result="PC won"
            pc_p+=1
        if you=="p":
            result="You won"
            you_p+=1
        if you=="r":
            result="DRAW!!!"
            
    if pc==p_pc:
        if you=="s":
            result="You won"
            you_p+=1
        if you=="p":
            result="DRAW!!!"
        if you=="r":
            result="PC won"  
            pc_p+=1 
    
    if pc_p >=limits or you_p>=limits:break
print("SCORES=============================================")
print("PC:",pc_p)
print("you:",you_p)

if pc_p>you_p:
    print("PC kicked your ass!!!")
    print("noob")
else:
    print("You are a warrior!")       





#Jheff Mat 12/18/2022
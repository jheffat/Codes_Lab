from random import choice,shuffle
pwd=[];repeated_pwd=0
numbers=['0','1','2','3','4','5','6','7','8','9']
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special=['!','@','#','$','%','^','&','*','?']
print("**Password generator by customized**\n")
l=int(input("How many Letters?"))
n=int(input("How many Numbers?"))
s=int(input("How many Special char?"))
np=int(input("How many Password want to generate?"))
 
for x in range(0,np):
    n_let=[choice(letters) for _ in range(l)]
    n_num=[choice(numbers) for _ in range(n)]
    n_spe=[choice(special) for _ in range(s)]
         
    chars=n_let+n_num+n_spe
    shuffle(chars)
    password_generated="".join(chars)
    
    if pwd.count(password_generated)==0:
        print(x+1, "| "+password_generated+" |")
        pwd.append(password_generated)      
    else:
        repeated_pwd+=1

print(f"\n{len(pwd)} Passwords generated of {np}")

      
print(f"{repeated_pwd} Passwords repeated & Eleminated.")
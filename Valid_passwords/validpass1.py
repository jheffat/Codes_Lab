def validpass(Passwd):
    C_spc=0;C_nmb=0;C_upp=0  
    if 8<=len(Passwd)  <= 16:
        for C in Passwd:      
            CC=ord(C)
            if CC>=35 and CC<=38 or C=="!" or C=="@":C_spc+=1
            if CC>=48 and CC<=57:C_nmb+=1
            if CC>=65 and CC<=98:C_upp+=1
            if CC>=91 and CC<=96 or CC>=123 and CC<=126 or CC>=39 and CC<= 47 or CC>=57 and CC<=63 or CC>=128 and CC<=254:return "Error: Only Special character (!, @, #, $, "+chr(38)+ " and "+ chr(37)+")"
        if C_nmb==0 or C_upp==0 or C_spc==0:return "Error: At least 1 uppercase, 1 number and 1 special character"
    else: return "Error:Must have at least 8 characters, max 16"
    return "Valid!"

state=""

while state!="Valid!":
    state= validpass(input("Enter password: "))
    print(state)

print("Password accepted!***", )
 


       





 



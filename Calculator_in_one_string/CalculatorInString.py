import string
def mid(s,pos,amount):
    return s[pos:pos+amount]
def calc(expx):
    group_num=""; express=[];
    #Here will convert from string to List but a group of numbers will be separated by operators 
    for i in expx:
        if i in string.ascii_letters+"=$#@!&~_)([]{}|?><":return "ASCII not support"  
        if i in ".0123456789":
            group_num+=i
        elif i in "+-*/^":
            if len(group_num)>0:
                express+=[group_num]
                group_num=""
            express+=[i]   
    express+=[group_num]
    
    #will just return  a single value if exist, otherwise return an error
    if len(express)<=2: 
        try:
            return float(expx)
        except:
            return "Invalid expression"
  
    #The math operation start from here--------------------------------------------------------
    
    #if the first item from the list express equal '-' then we'll add new item '0' before,
    # in that way my algorithm will be easy to do the calculation....ex: -5+2 to 0-5+2 
    if express[0] in "+-":express=["0"]+express
          
    #if exist Exponential notation ^ then execute this operation......
    #Note: this part still in development
    while "^" in express:
        for y in range(0,len(express),2):
            try:              
                catchx=express[y:y+3]
                if "^" in catchx:
                    express.pop(y)
                    express.pop(y)
                    express.pop(y)
                    p=float(catchx[0])**float(catchx[2])
                    express.insert(y,str(p))           
            except:
                return "Invalid expression"

    #if exist  items like '*' or '/' then execute the multiplication and division...
    while "*" in express or "/" in express:
        for y in range(0,len(express),2):
            try:         
                catchx=express[y:y+3]
                if "*" in catchx:
                    express.pop(y)
                    express.pop(y)
                    express.pop(y)
                    p=float(catchx[0])*float(catchx[2])
                    express.insert(y,str(p))           
                if "/" in catchx:
                    express.pop(y)
                    express.pop(y)
                    express.pop(y)
                    p=float(catchx[0])/float(catchx[2])
                    express.insert(y,str(p))             
            except:
                return "Invalid expression"
    
    #if exist items like '+' and '-' then proceed with the addition and subtraction
    while "+" in express or "-" in express:
            for y in range(0,len(express),2):
                try:         
                    catchx=express[y:y+3]
                    if "+" in catchx:
                        express.pop(y)
                        express.pop(y)
                        express.pop(y)
                        p=float(catchx[0])+float(catchx[2])
                        express.insert(y,str(p))           
                    if "-" in catchx:
                        express.pop(y)
                        express.pop(y)
                        express.pop(y)
                        p=float(catchx[0])-float(catchx[2])
                        express.insert(y,str(p))             
                except:
                    return "Invalid expression"    
  
    return "".join(express)
    

result=0.0
print("\nBy Jheff Alberty 12/15/2022\n")
print("Calculator in one input string with /*-+^")
while  result!=0.1:
    result=calc(input("Enter Expression: ")) 
    print("=",result)


#By Jheff Alberty /icodexys

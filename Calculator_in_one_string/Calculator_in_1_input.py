import string

oper={"^":lambda a,b:a**b,
      "*":lambda a,b:a*b,
      "/":lambda a,b:a/b,
      "+":lambda a,b:a+b,
      "-":lambda a,b:a-b}

def calc(expx):
    group_num=""; express=[];
   
    for i in expx:
        if i not in string.digits+"+-*/^":return "Expression not support"  
        if i in ".0123456789":
            group_num+=i
        elif i in "+-*/^":
            if len(group_num)>0:
                express+=[float(group_num)]
                group_num=""
            express+=[i]   
    express+=[float(group_num)]
    
    
    if len(express)<=2: 
        try:
            return float(expx)
        except:
            return "Invalid expression"
  
    #***
 
    if str(express[0]) in "+-":express=[0]+express
          

    for o in "^*/+-":
        

        while o in express:
            try:
                print(express)
                pos=express.index(o)
                p=oper[o](express[pos-1],express[pos+1])
                express.pop(pos-1)
                express.pop(pos-1)
                express.pop(pos-1)
                express.insert(pos-1,p)
               
            except:
                return "Invalid Expression"
                
      
   
 
  
    return express
    



result=0.0
print("\nBy Jheff Alberty 12/15/2022\n")
print("Calculator in one input string with /*-+^")
while  result!=0.1:
    result=calc(input("Enter Expression: ")) 
    print("=",result)


#By Jheff Alberty /icodexys

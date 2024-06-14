def calc(exps):
    #get the string into list. ex: "22+45-23" --> [22,'+',45,'-',23]
    express=[];gn=""
    if exps[0] in "+-":exps="0"+exps
    for l in exps:
        if l in ".0123456789":gn=gn+l      
        if l in "^*/+-": 
           express=express+[float(gn)]+[l]
           gn=""
    express=express+[float(gn)]  
   #Here where it start the calculation; 
    for o in "^*/+-": #-->every cycle it will use one operator to do the operation using the dictionary {oper}.
        while o in express: #-->while an operator exist in the list [express] it will continue                     
            try:            #   executing the process til there is no operators but the result.
                pos=express.index(o)
                result=oper[o](express[pos-1],express[pos+1])
                _=[express.pop(pos-1) for _ in range(3)]
                express.insert(pos-1,result)              
            except:
                return "Invalid Expression" 
    return express

#By creating a Dictionary {oper} it will help to do the operation. ex: print(oper['+'](5,4)) --> 9
oper={"^":lambda a,b:a**b,
      "*":lambda a,b:a*b,
      "/":lambda a,b:a/b,
      "+":lambda a,b:a+b,
      "-":lambda a,b:a-b}
    
#EXAMPLE-----------------------------------------------------

result=0.0
print("\nBy Jheff Alberty 12/15/2022\n")
print("Calculator in one input string with /*-+^")
while  results!=[0.1]:
    try:
        results=calc(input("Enter Expression: ")) 
        print("=",results)
    except:
        print("Invalid Expression")

#By Jheff Alberty /icodexys

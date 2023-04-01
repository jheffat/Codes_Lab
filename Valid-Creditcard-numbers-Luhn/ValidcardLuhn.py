def isvalid(n):
    # this function will determine if the numbers are valid for a credit card
    t=0
    for x,y in enumerate(reversed(n)):
        y=int(y)
        if x%2==1:
            y=y*2
            if y>=10:
                t+=y//10+y%10
            else:
                t+=y
        else:
            t+=y
    return t%10==0

def cardtype(n):
    # thids one will show what type of credit card number is. ex VISA, MASTERCARD, DISCOVER or AMERICA EXPRESS
    a=int(n[0]);b=int(n[0:2])
    if b>49 and b<56:return '**MASTERCARD'
    if b==34 or b==37:return '**AMERICA EXPRESS'
    if b in [60,62,64,65]: return '**DISCOVER'
    if a==4: return '**VISA'
    return 'NONE--'

   
#this is just a loop until NC=0
while NC!='0':
    NC=input("Enter credit card#:")
    
    if isvalid(NC)==True:    #if the credit card number is valid then will print the brand...VISA, MASTERCARD etc..
        print("Is Valid!, type:",cardtype(NC))
    else:
        print("Invalid...")




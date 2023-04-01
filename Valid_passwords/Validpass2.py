def validpass(Passwd):
    Charz=""
    specialchars="@#$!"
    specialchars_denied="~`^*()_+|}{[]\=-':;/>.<,?"
    if 8<=len(Passwd) <= 16:
        if not any(Charz.isdigit() for Charz in Passwd): return "Error: At least one number 0 - 9"
        if not any(Charz.isupper() for Charz in Passwd): return "Error: At least 1 uppercase"
        if not any(Charz.islower() for Charz in Passwd): return "Error: At least 1 lowercase"
        if not any(Charz in specialchars for Charz in Passwd): return "Error: At least 1 Special character:@#$!" 
        if  any(Charz in specialchars_denied for Charz in Passwd): return "Error: Only special characters is allowed: @#$!"  
    else: return "Error: No less than 8 characters or more than 16 characters"
    return "valid!"

state=""
while state!="valid!":
    state= validpass(input("Enter password: "))
    print(state)
    
print("Valid Password!!!!!***")
 


       





 



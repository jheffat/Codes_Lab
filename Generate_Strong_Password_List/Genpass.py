from string import digits,ascii_lowercase,ascii_uppercase,punctuation
#from random import random,sample,choice,randint
from secrets import choice
import bcrypt
chars=ascii_uppercase+digits+ascii_lowercase+punctuation
passgen="";l=10;c=1000;passhash=""

for n in range(c):
    
    
    passgen+="".join(choice(chars) for _ in range(l))
    
 #-->Lines 14 - 16 is optional for random module, you can use one of those line to generate passwords, but secrect module is recommended for security / Cryptography purpose
    #passgen+="".join(chr(randint(33,126)) for _ in range(l))
    #passgen+="".join(choice(chars) for _ in range(l))
    #passgen="".join(sample(chars,l))

    passhash=bcrypt.hashpw(passgen.encode("utf-8"), salt=bcrypt.gensalt(rounds=10))
    print(n, " Password generated: ", passgen, "==>Hashed: ",passhash)
    passgen=""

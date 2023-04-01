def encrypt(msg):
    Chars_x="abcdefghijklmnñopqsrtuvwyxzABCDEFGHIJKLMNÑOPQSRTUVWYXZ0123456789,.;()? "
    Chars_y="plmoknijbuhvñygctfxrdzeswaqQAZWSXEDCRFVTGBYÑHNUJMIKOLP7531902468(,;.?) "
    msg_cifrado=""
    #here is where the substitution starts by chars....it will check if the msg exist a char that is in chars_x, then will catch the position number and 
    #will be used for chars_y to locate the same position that rely in one of those characters, after that will be add that character from chars_y to msg_cifrado and so on...
    for x in msg:
        for n  in range(len(Chars_x)):
            if x==Chars_x[n]:
                msg_cifrado+=Chars_y[n]
    return msg_cifrado

def decrypt(msg):
    Chars_y="abcdefghijklmnñopqsrtuvwyxzABCDEFGHIJKLMNÑOPQSRTUVWYXZ0123456789,.;()? "
    Chars_x="plmoknijbuhvñygctfxrdzeswaqQAZWSXEDCRFVTGBYÑHNUJMIKOLP7531902468(,;.?) "
    msg_cifrado=""
    for x in msg:
        for n  in range(len(Chars_x)):
            if x==Chars_x[n]:
                msg_cifrado+=Chars_y[n]
    return msg_cifrado


#example----------------------------------------------

msg="Cryptography may also refer to the art of cryptanalysis, by which cryptographic codes are broken"
msgx=encrypt(msg)
print(msgx)
print(decrypt(msgx))
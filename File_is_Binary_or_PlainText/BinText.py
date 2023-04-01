#You can either use one of this functions and it will tell you if the 
#file is Binary or Plain-text

def is_binary(f):
    fcontent=open(f, 'rb').read()
    chars=bytearray({7,8,9,10,12,13,27}| set(range(32, 256)) - {127})
    return bool(fcontent.translate(None, chars))

def is_binary2(f):
    fcontent=open(f, 'rb').read()
    return (b'\x00' in fcontent)
     
    
def is_binary3(f):
    fcontent=open(f, 'rb').read()
    return (0 in list(fcontent))
    
#Example

print(is_binary("file.txt"))

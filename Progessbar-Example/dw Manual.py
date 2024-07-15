import requests
x=0
url="https://cdnm.meln.top/mr/Aventura%20-%20Cuando%20volverus.mp3?session_key=e9d097de1af1de63ca33368675f57da1&hash=f224dd320e707ef27097863a359a7250"
file=requests.get(url,stream=True)


size=int(file.headers['Content-Length'])
filename="aventura.mp3"
Sizebar=100

fw=open(filename,"wb")

for bs in file:
    x+=len(bs)
    print('\r' + 'Downloading...: %s [%s%s]%.2f%% ' % (filename,'█' * int(x*Sizebar/size), '░'*(Sizebar-int(x*Sizebar/size)), float(x/size*100)), str(x)+' Bytes',end='')
    fw.write(bs)

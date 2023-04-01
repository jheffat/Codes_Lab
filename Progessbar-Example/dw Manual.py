import requests
x=0
url="https://cdnm.meln.top/mr/Aventura%20-%20Cuando%20Volveras.mp3?session_key=69e46c3bf738ecc46eb521c7547462f2&hash=04042964424a6d1682b5f315d3188253"
file=requests.get(url,stream=True)


size=int(file.headers['Content-Length'])
filename="aventura.mp3"
Sizebar=100

fw=open(filename,"wb")

for bs in file:
    x+=len(bs)
    print('\r' + 'Downloading...: %s [%s%s]%.2f%% ' % (filename,'█' * int(x*Sizebar/size), '░'*(Sizebar-int(x*Sizebar/size)), float(x/size*100)), str(x)+' Bytes',end='')
    fw.write(bs)

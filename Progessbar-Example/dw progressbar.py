 


import progressbar,time,requests
data=0
url="https://cdnm.meln.top/mr/Aventura%20-%20Cuando%20Volveras.mp3?session_key=69e46c3bf738ecc46eb521c7547462f2&hash=04042964424a6d1682b5f315d3188253"
file=requests.get(url,stream=True)
size=int(filez.headers['Content-Length'])
 

bar=progressbar.ProgressBar(maxval=size, widgets=["Descarcando... ",progressbar.Percentage(),progressbar.Bar('█', '[',']'), progressbar.DataSize(), progressbar.FileTransferSpeed()])

fw=open("file.mp3","wb")

bar.start()

for bs in file.iter_content(chunk_size=1024):
    bar.update(data)
    data+=len(bs)
    fw.write(bs)


bar.finish()
 

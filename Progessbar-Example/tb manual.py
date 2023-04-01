from pytube import YouTube 

def iteracion(stream = None, chunk = None, file_handle = None, remaining = None):
    global OriSize,size,Filename,barsize
    size += len(chunk)
    print('\r' + 'Downloading...: %s [%s%s]%.2f%% ' % (Filename,
    '█' * int(size*barsize/OriSize), '░'*(barsize-int(size*barsize/OriSize)), 
    float(size/OriSize*100)), str(size)+' Bytes',end='')

url="https://www.youtube.com/watch?v=dumscH7Qt_I"

yt = YouTube(url, on_progress_callback=iteracion)

gotb=yt.streams.filter(progressive=True,file_extension='mp4').first()

size=0
Filename=gotb.default_filename
OriSize = gotb.filesize
barsize=50

gotb.download()

print("\nCompleted...")

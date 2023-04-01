from pytube import YouTube 
import progressbar
def iteracion(stream = None, chunk = None, file_handle = None, remaining = None):
    global bar,Chunks
    Chunks+=len(chunk)
    bar.update(Chunks)

Chunks=0

url="https://www.youtube.com/watch?v=dumscH7Qt_I"

yt = YouTube(url, on_progress_callback=iteracion)

gotb=yt.streams.filter(progressive=True,file_extension='mp4').first()

bar=progressbar.ProgressBar(maxval=gotb.filesize, widgets=["Downloading...: ",gotb.default_filename," ",progressbar.Percentage(), progressbar.Bar('█','[',']'),progressbar.DataSize(), progressbar.FileTransferSpeed()])

bar.start()

gotb.download()

bar.finish()

print("Completed...")
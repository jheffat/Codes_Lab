from pytube import YouTube 
from tqdm import tqdm

def iteracion(stream = None, chunk = None, file_handle = None, remaining = None):
    global bar
    bar.update(len(chunk))

url="https://www.youtube.com/watch?v=dumscH7Qt_I"

yt = YouTube(url, on_progress_callback=iteracion)

gotb=yt.streams.filter(progressive=True,file_extension='mp4').first()

bar=tqdm(range(gotb.filesize),desc="Downloading..."+gotb.default_filename)

gotb.download()

bar.close()
print("Completed...")
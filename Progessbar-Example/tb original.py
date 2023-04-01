from pytube import YouTube 
from pytube.cli import on_progress

url="https://www.youtube.com/watch?v=dumscH7Qt_I"

yt = YouTube(url, on_progress_callback=on_progress)

gotb=yt.streams.filter(progressive=True,file_extension='mp4').first()


print('Downloading...: %s' % gotb.default_filename)
gotb.download()
print("\nComplete...")


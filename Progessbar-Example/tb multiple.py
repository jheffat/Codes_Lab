from pytube import YouTube, Playlist
def byteme(n):
    p=len(n)
    if p<7:
        return n+" Bytes"
    if p>6 and p<10:
        i=n[:len(n)-6]
        d=n[len(i):len(i)-6]
        return i+"."+d +" MB"
    if p>9 and p<13:
        i=n[:len(n)-9]
        d=n[len(i):len(i)-9]
        return i+"."+d +" GB"
    if p>12 and p<16:
        i=n[:len(n)-12]
        d=n[len(i):len(i)-12]
        return i+"."+d +" TB"  

def iteracion(stream=None,chunk=None,file_handle=None,remaining=None):
    global OriSize,size,Filename,barsize
    size+=len(chunk)
    print('\r Downloading: [%s%s]%.2f%% ' % ('█' * int(size*barsize/OriSize), '░'*(barsize-int(size*barsize/OriSize)), float(size/OriSize*100)),byteme(str(size)),' Video: '+Filename+"    " ,end='')
count_dwld=0
count_failed=0

playlist = Playlist('https://www.youtube.com/playlist?list=PLCD0445C57F2B7F41') 
print(len(playlist)," Videos to Download....")

for url in playlist:
    try: 
        yt= YouTube(url,on_progress_callback=iteracion)
        gotb=yt.streams.filter(progressive=True).get_highest_resolution()
        size=0
        Filename= gotb.default_filename
        OriSize=gotb.filesize
        barsize=100
        gotb.download("d:/")
        print("\nCompleted.....")
        count_dwld+=1
    except:
        print("Error on: "+url )
        count_failed+=1
        continue

    
    

print(count_dwld, "Videos Downloaded....")
print(count_failed, "Videos failed to Download....")

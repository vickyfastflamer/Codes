import youtube_dl

def download_ytvid_as_mp3():
    video_url = input("https://youtu.be/Upsm3E2NUI8?si=TJwGLIrIeLTEet-d")
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print(f"Download complete: {filename}")

download_ytvid_as_mp3()

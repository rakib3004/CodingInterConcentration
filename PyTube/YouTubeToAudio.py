from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})

try:

    print('Audio Downloader'.center(40, '_'))
    URL = "https://www.youtube.com/watch?v=j5Sl8LyI7k8&ab_channel=TED-Ed"
    audio_downloader.extract_info(URL)

except:
    print("Error")
from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist


url = input("Set playList : ")
playlist = Playlist(url)
print( len(playlist))

for i in playlist:
    youtube=YouTube(i,on_progress_callback=on_progress)
    video=youtube.streams.filter(file_extension="mp4").get_highest_resolution()
    video.download()
    print(f"video {i} downloaded")
print("all videos downloaded")
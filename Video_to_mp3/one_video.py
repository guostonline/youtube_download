from pytube import YouTube
from pytube.cli import on_progress

url = input("set url ")

youtube = YouTube(url, on_progress_callback=on_progress)

video = youtube.streams.get_highest_resolution()
video.download()

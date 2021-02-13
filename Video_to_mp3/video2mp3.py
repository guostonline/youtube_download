from moviepy.editor import *
from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored
from my_function import *

url = input(colored('Entree Youtube link : ', "yellow"))
print("please wait..Download video must begin")
youtube = YouTube(url, on_progress_callback=on_progress)
video = youtube.streams.get_lowest_resolution()
videoTilte = video.title

video.download(filename="myVideo")

print(colored(f"{videoTilte} is downloaded!", "green"))


mp3_file = input(colored("Set name of mp3 file : ", "yellow"))
position = input(colored("Set Position of sound  B/M/E : "))
if position.upper() == "B":
    Cfunction(mp3_file, 5, 15)
if position.upper() == "M":
    Cfunction(mp3_file, 120, 130)
if position.upper() == "E":
    Cfunction(mp3_file, 300, 310)

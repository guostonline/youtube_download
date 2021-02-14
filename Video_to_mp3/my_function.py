
from moviepy.editor import *
from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored
from pytube import Playlist
import os


class Cfunction:



    def move_this_file(self, source, destination):
        os.replace(self.mp3_file, destination)

    def donwload_one_video():
        print(colored("##################### Download one Youtube video ######################", "blue"))
        url = input(colored("Paste your url video.. ", "yellow"))
        youtube = YouTube(url, on_progress_callback=on_progress)
        video = youtube.streams.filter(adaptive=True, file_extension="mp4")
        index = 0
        for i in video:
            index += 1
            print(index, i)
        downloadVideo=int(input(colored("Select wich video you want to download. ","yellow")))-1
        video[downloadVideo].download()
        print(colored("Finally is done","blue"))

    def download_list():
        print(colored("##################### Download Playlist Youtube ######################", "blue"))
        url = input(colored("Paste url playList : ","yellow"))
        playlist = Playlist(url)
        print(colored(f"Waiting for download {len(playlist)} videos","magenta" ))

        for i in playlist:
            youtube=YouTube(i,on_progress_callback=on_progress)
            video=youtube.streams.filter(file_extension="mp4").get_highest_resolution()
            video.download(output_path="videos output")
            print(f"video {video.title} downloaded  ")
        print(colored("all videos downloaded","magenta"))
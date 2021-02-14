
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
        print(colored(
            "##################### Download one Youtube video ######################", "blue"))
        url = input(colored("Paste your url video.. ", "yellow"))
        youtube = YouTube(url, on_progress_callback=on_progress)
        video = youtube.streams.filter(adaptive=True, file_extension="mp4")
        index = 0
        for i in video:
            index += 1
            print(index, i)
        downloadVideo = int(
            input(colored("Select wich video you want to download. ", "yellow")))-1
        video[downloadVideo].download()
        print(colored("Finally is done", "blue"))

    def download_list():
        print(colored(
            "##################### Download Playlist Youtube ######################", "blue"))
        url = input(colored("Paste url playList : ", "yellow"))
        playlist = Playlist(url)
        print(
            colored(f"Waiting for download {len(playlist)} videos", "magenta"))

        for i in playlist:
            youtube = YouTube(i, on_progress_callback=on_progress)
            video = youtube.streams.filter(
                file_extension="mp4").get_highest_resolution()
            video.download(output_path="videos output")
            print(f"video {video.title} downloaded  ")
        print(colored("all videos downloaded", "magenta"))

    def download_sound():
        print(colored(
            "##################### Download Sound only ######################", "blue"))
        url = input(colored("Paste url Youtube : ", "yellow"))
        youtube = YouTube(url, on_progress_callback=on_progress)
        video = youtube.streams.get_lowest_resolution()
        file_name = input(colored("Set a file name : ", "yellow"))
        video.download(filename="myVideo")
        print(
            colored(f"Audio of '{video.title}'' has been download ", "magenta"))

        print(colored("Select an option.", "magenta"))
        print("""
        1. Trim from begin 
        2. Trim from middle 
        3. Trim from end
        4. Download all audio
        """)
        choice = int(input(colored("Select an option please : ", "yellow")))

        if choice == 1:
            Cfunction.convert_video(file_name, 5, 15)
        if choice == 2:
            Cfunction.convert_video(file_name, 120, 125)
        if choice == 3:
            Cfunction.convert_video(file_name, 200, 210)
        if choice == 4:
            Cfunction.convert_video(file_name, "all audio")

    def convert_video(*args):
        
        videoClip = VideoFileClip("myVideo.mp4")
        if args[1] == "all audio":
            audioClip = videoClip.audio
            audioClip.write_audiofile(args[0]+".mp3", bitrate="96k")
        else :
            audioClip = videoClip.subclip(t_start=args[1], t_end=args[2]).audio
            audioClip.write_audiofile(args[0]+".mp3", bitrate="96k")
        audioClip.close()
        videoClip.close()

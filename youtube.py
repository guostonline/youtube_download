import bcolors
from pytube import YouTube
from termcolor import colored


#url=input("Set youtube URL please : ")
i=0
url=input(colored('Entree Youtube link : ',"yellow"))
youtube=YouTube(url)
a=bcolors
video=youtube.streams
video.filter(progressive=True)

video.order_by("resolution")
#print('\033[93m'+ video.get_highest_resolution())c

for stream in video:
    i+=1
    print(str(i)+colored(stream,"green") )
choise=input(colored('Select wich video want to download : ',"yellow"))
if choise.isdigit:
    choise=int(choise)
    print(colored(video[choise-1],"blue"))




validation=input(colored("Entre yes : ","blue"))
if validation=="yes":
    video[choise-1].download(output_path="C://Users//guost//Videos")
    print (colored("is done","yellow"))

       

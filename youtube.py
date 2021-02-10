import bcolors
from pytube import YouTube
from termcolor import colored

print(dir(bcolors)
#url=input("Set youtube URL please : ")
url=input(colored('Entree Youtube link : ',"yellow"))
youtube=YouTube(url)
a=bcolors
video=youtube.streams
video.filter(progressive=True)

video.order_by("resolution")
#print('\033[93m'+ video.get_highest_resolution())c
i=0
for stream in video:
    i+=1
    print(str(i)+colored(stream,"green") )
choise=int(input(colored('Select wich video want to download : ',"yellow")))


print(colored(video[choise-1],"blue"))


validation=input(colored("Entre yes : ","blue"))
if validation=="yes":
    video[choise-1].download(output_path="C://Users//guost//Videos")
    print ("is done")

       

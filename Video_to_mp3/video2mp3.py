from moviepy.editor import *
from termcolor import colored
from my_function import Cfunction





print(colored("Select an option.","yellow"))
print("""
1. Download one video
2. Download Playlist
3. Download audio only
""")


choice = int(input(colored('Choice your option : ', "yellow")))-1

operation=[Cfunction.donwload_one_video,Cfunction.download_list]
operation[choice]()

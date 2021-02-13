
from moviepy.editor import *


class Cfunction:
    def __init__(self, mp3_file_name, begin, end):

        self.mp3_file = mp3_file_name+".mp3"
        self.begin = begin
        self.end = end

        videoClip = VideoFileClip("myVideo.mp4")
        audioClip = videoClip.subclip(self.begin, self.end).audio
        audioClip.write_audiofile(self.mp3_file, bitrate="96k")
        audioClip.close()
        videoClip.close()


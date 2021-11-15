from speech_recognition import AudioFile
from moviepy.editor import *
my_audio = AudioFileClip("Lab.wav")

clip_1 = my_audio.subclip(180, 294)
clip_1.write_audiofile(f"Parte 2.wav")
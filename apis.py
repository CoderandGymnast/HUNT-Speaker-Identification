import wave as w
import constants as c
from os import path
from pyaudio import PyAudio

def createOrAppend(fileName,frames):
    p = PyAudio()
    if path.isfile(fileName):
        f= w.open(fileName,"rb")
        preFrames=f.readframes(c.AUDIO_MAX_NUM_FRAMES)
        f.close()
        
        f=w.open(fileName, "wb")
        f.setnchannels(c.NUM_CHANNEL)
        f.setsampwidth(p.get_sample_size(c.FORMAT))
        f.setframerate(c.SAMPLE_RATE) 
        allFrames=preFrames+b''.join(frames) 
        f.writeframes(allFrames[:c.AUDIO_MAX_NUM_FRAMES])
        f.close()
    else:
        f=w.open(fileName, "wb")
        f.setnchannels(c.NUM_CHANNEL)
        f.setsampwidth(p.get_sample_size(c.FORMAT))
        f.setframerate(c.SAMPLE_RATE) 
        f.writeframes(b''.join(frames))
        f.close()
    
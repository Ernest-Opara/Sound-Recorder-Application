import sounddevice as sound
import soundfile as sf
from scipy.io.wavfile import write
#from tktest import fileName, formatselection
#import tktest

freq = 44100

#format = ['mp3','wav','flac']

#formatselection = random.choice(format)
#formatselection = 'flac'
#print(format(tktest))

#Duration in seconds
duration = 10

def recButton(fileName,formatselection):
    recording = sound.rec(int(duration * freq), samplerate=freq, channels = 2)
    print('Recording has started!')
    print(recording)
    sound.wait()
    fullFileName = fileName + "." + formatselection
    write(fullFileName,freq,recording)
    print('Recording has finished!')
    #exit()
#recButton("Test9","flac")

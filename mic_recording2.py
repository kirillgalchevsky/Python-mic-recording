import os
import pyaudio 
import wave
import sounddevice as sd 
import soundfile as sf
import winshell

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5 
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream  = p.open(format = FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer =CHUNK)

recycle_bin = winshell.recycle_bin()

print("* recording")

frames = []


for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
                                                                                                                                                            
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

filename = "output.wav"
data, fs = sf.read(filename, dtype="float32")
sd.play(data, fs)
status = sd.wait()

def delet():
  os.remove("output.wav")

def emptyrecbin():
  recycle_bin.empty(confirm=False, sound=False, show_progress=False)

delet()
emptyrecbin()
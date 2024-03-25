import pyaudio
import numpy as np
import threading

class MicrophoneInput(threading.Thread):
    def __init__(self):
        super().__init__()
        self.audio_level = 0
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.stream = None  # Initialize stream without opening
        self.running = False

    def open_stream(self):
        global AudioDevice
        try:
            self.stream = self.p.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      input=True,
                                      input_device_index=AudioDevice,
                                      frames_per_buffer=self.CHUNK)
            self.running = True
        except Exception as e:
            print("Error opening audio stream:", e)

    def run(self):
        try:
            while self.running:
                data = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.int16)
                self.audio_level = np.max(data)
                print("Current audio level:", self.audio_level, "                   ", end="\r")
        except Exception as e:
            print("Error in audio stream:", e)

    def stop(self):
        self.running = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

    def curVal(self):
        return self.audio_level

    
def getAudioDevice():
    global AudioDevice
    print(AudioDevice)
    return AudioDevice
    
def setAudioDevice(deviceID):
    global AudioDevice
    AudioDevice = deviceID


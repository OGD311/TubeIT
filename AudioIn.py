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
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)
        self.running = False

    def run(self):
        self.running = True
        try:
            while self.running:
                data = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.int16)
                self.audio_level = np.max(data)
                #print(f"Microphone input level: {self.audio_level}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

    def stop(self):
        self.running = False

    def curVal(self):
        return self.audio_level
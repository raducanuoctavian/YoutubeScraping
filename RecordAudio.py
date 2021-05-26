import pyaudio
import wave


class RecordAudio:
    # the file name output you want to record into
    filename = "recorded.wav"
    record_seconds = 120

    def __init__(self, filename=filename, record_seconds=record_seconds):
        self.filename = filename
        self.record_seconds = record_seconds

    def record_audio(self):
        # initialize PyAudio object
        p = pyaudio.PyAudio()
        # open stream object as input & output
        # set the chunk size of 1024 samples
        chunk = 1024
        # sample format
        format = pyaudio.paInt16
        # mono
        channels = 1
        # 44100 samples per second
        sample_rate = 44100
        stream = p.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)
        frames = []
        print("Audio record on")
        for i in range(int(44100 / chunk * self.record_seconds)):
            data = stream.read(chunk)
            frames.append(data)
        print("Audio record off")
        stream.stop_stream()
        wf = wave.open(self.filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()
        p.terminate()


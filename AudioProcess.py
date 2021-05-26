import numpy as np
import soundfile
import matplotlib.pyplot as plt
import csv


class AudioProcess:

    filename = 'recorded.wav'

    def __init__(self, filename=filename):
        self.filename = filename

    def convert_to_decibel(self, arr):
        ref = 1
        if arr != 0:
            return 20 * np.log10(abs(arr) / ref)
        else:
            return -60

    def plot_dB(self):

        signal, sr = soundfile.read(self.filename)
        samples_sf = signal
        data = [self.convert_to_decibel(i) for i in samples_sf]
        percentile = np.percentile(data, [25, 50, 75])
        f = open("fisier.csv", "w")
        writer = csv.writer(f)
        for i in range(len(data)):
            print(f"[{i} : {data[i]}]", file=f)
        f.close()
        plt.figure()
        plt.plot(data)
        plt.xlabel('Samples')
        plt.ylabel('dB Full Scale (dB)')
        plt.tight_layout()
        plt.show()

import threading
import YoutubeConnect
import VideoRecording
import RecordAudio
import AudioProcess

connecter = YoutubeConnect.YoutubeConnect()
vrecorder = VideoRecording.VideoRecording()
arecorder = RecordAudio.RecordAudio()
aprocesser = AudioProcess.AudioProcess()

p0 = connecter.connect_to_youtube
p1 = vrecorder.record_screen
p2 = arecorder.record_audio
p3 = aprocesser.plot_dB

t0 = threading.Thread(target=p0)
t1 = threading.Thread(target=p1)
t2 = threading.Thread(target=p2)


t0.start()
t1.start()
t2.start()
t0.join()
t1.join()
t2.join()

aprocesser.plot_dB()




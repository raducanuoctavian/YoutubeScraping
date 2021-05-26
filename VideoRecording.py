import cv2
import numpy as np
import pyautogui


class VideoRecording:
    screen_size = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "Recording.avi"
    fps = 20
    duration = 120

    def __init__(self, screen_size=screen_size, filename=filename, fps=fps, duration=duration):
        self.screen_size = screen_size
        self.filename = filename
        self.fps = fps
        self.duration = duration

    def record_screen(self):
        out = cv2.VideoWriter(self.filename, self.codec, self.fps, self.screen_size)
        print("Video recording on")
        for i in range(self.fps * self.duration):
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        out.release()
        cv2.destroyAllWindows()
        print("Video recording off")

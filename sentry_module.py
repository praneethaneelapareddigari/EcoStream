import cv2

class SentryDetector:
    def __init__(self):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    def detect(self, frame):
        fg_mask = self.bg_subtractor.apply(frame)
        motion_score = fg_mask.sum()
        return motion_score
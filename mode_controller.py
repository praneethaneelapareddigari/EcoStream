import time

class ModeController:
    def __init__(self):
        self.current_mode = "SENTRY"
        self.motion_threshold = 5000
        self.cooldown_time = 3
        self.last_motion_time = time.time()

    def update(self, motion_score):
        current_time = time.time()

        if motion_score > self.motion_threshold:
            if self.current_mode != "ACTIVE":
                print("[EVENT DETECTED] Switching to ACTIVE MODE (30 FPS)")
            self.current_mode = "ACTIVE"
            self.last_motion_time = current_time

        if self.current_mode == "ACTIVE":
            if current_time - self.last_motion_time > self.cooldown_time:
                print("[IDLE] Returning to SENTRY MODE (2 FPS)")
                self.current_mode = "SENTRY"

    def get_target_fps(self):
        return 30 if self.current_mode == "ACTIVE" else 2
import cv2
import time
from mode_controller import ModeController
from sentry_module import SentryDetector
from active_module import ActiveDetector
from metrics import ComputeMeter

VIDEO_SOURCE = 0  # webcam

def main():
    cap = cv2.VideoCapture(VIDEO_SOURCE)

    controller = ModeController()
    sentry = SentryDetector()
    active = ActiveDetector()
    meter = ComputeMeter()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        mode = controller.current_mode

        if mode == "SENTRY":
            motion_score = sentry.detect(frame)
            controller.update(motion_score)
            meter.update_sentry()
        else:
            active.detect(frame)
            controller.update(0)
            meter.update_active()

        cv2.putText(frame, f"Mode: {controller.current_mode}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.putText(frame, f"FPS Target: {controller.get_target_fps()}",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

        cv2.imshow("EcoStream", frame)

        key = cv2.waitKey(int(1000/controller.get_target_fps()))
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
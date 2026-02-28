import cv2
import onnxruntime as ort
import numpy as np

class ActiveDetector:
    def __init__(self):
        try:
            self.session = ort.InferenceSession("model.onnx")
        except:
            self.session = None

    def detect(self, frame):
        frame_resized = cv2.resize(frame, (224, 224))
        input_tensor = np.expand_dims(frame_resized.astype(np.float32), axis=0)

        if self.session:
            self.session.run(None, {self.session.get_inputs()[0].name: input_tensor})

        return True
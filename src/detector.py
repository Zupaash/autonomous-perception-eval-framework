# src/detector.py
import numpy as np
from ultralytics import YOLO

class SafetyCriticalDetector:
    def __init__(self, model_weight="yolov8n.pt"):
        """Loads the official pre-optimized model architecture."""
        self.model = YOLO(model_weight)

    def run_inference(self, frame: np.ndarray):
        """Runs an inference pass silently to protect hardware timing loops."""
        return self.model(frame, verbose=False)

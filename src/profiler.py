# src/profiler.py
import time
import psutil
import numpy as np
from src.detector import SafetyCriticalDetector

class PerformanceProfiler:
    def __init__(self, model_weight="yolov8n.pt", frames=100):
        self.detector = SafetyCriticalDetector(model_weight)
        self.frames = frames
        # Use a deterministic mock array to eliminate disk reading lag
        self.mock_frame = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)

    def measure_pipeline(self):
        """Warms up hardware cache, then actively profiles latency and system strain."""
        # 1. Warm up hardware to clear cold-start spikes
        for _ in range(15):
            self.detector.run_inference(self.mock_frame)

        latencies = []
        cpu_metrics = []

        # 2. Core evaluation cycle
        for _ in range(self.frames):
            start = time.perf_counter_ns()
            self.detector.run_inference(self.mock_frame)
            end = time.perf_counter_ns()

            # Convert nanoseconds to milliseconds
            latencies.append((end - start) / 1_000_000)
            cpu_metrics.append(psutil.cpu_percent())

        # 3. Compile statistics
        latencies = np.array(latencies)
        return {
            "mean": np.mean(latencies),
            "median": np.median(latencies),
            "p95": np.percentile(latencies, 95),
            "p99": np.percentile(latencies, 99),
            "fps": 1000 / np.mean(latencies),
            "cpu": np.mean(cpu_metrics)
        }

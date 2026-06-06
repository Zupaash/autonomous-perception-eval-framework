import time


class BenchmarkRunner:
    def __init__(self, detector):
        self.detector = detector

    def run(self, image_path: str, num_runs: int = 10):
        results = []

        for run_id in range(1, num_runs + 1):
            start_time = time.perf_counter()

            detections = self.detector.detect(image_path)

            end_time = time.perf_counter()
            latency_ms = (end_time - start_time) * 1000

            results.append({
                "run_id": run_id,
                "latency_ms": latency_ms,
                "num_detections": len(detections),
            })

        return results

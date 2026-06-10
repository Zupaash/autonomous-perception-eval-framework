import csv
from datetime import datetime
from pathlib import Path


class ExperimentLogger:
    def __init__(self, output_dir="results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def save_results(self, benchmark_results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_file = (
            self.output_dir /
            f"benchmark_{timestamp}.csv"
        )

        with open(output_file, "w", newline="") as csvfile:
            fieldnames = [
                "run_id",
                "latency_ms",
                "num_detections"
            ]

            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for result in benchmark_results:
                writer.writerow(result)

        return output_file

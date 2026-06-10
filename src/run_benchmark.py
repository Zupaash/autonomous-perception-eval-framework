from logging.experiment_logger import ExperimentLogger

from inference.yolo_detector import YOLODetector
from benchmarking.benchmark_runner import BenchmarkRunner


def main():
    image_path = "https://ultralytics.com/images/bus.jpg"

    detector = YOLODetector("yolov8n.pt")
    benchmark = BenchmarkRunner(detector)

    results = benchmark.run(image_path, num_runs=10)

    logger = ExperimentLogger()
    output_file = logger.save_results(results)

    print()
    print(f"Results saved to: {output_file}")
    print()

    for result in results:
        print(
            f"Run {result['run_id']}: "
            f"{result['latency_ms']:.2f} ms, "
            f"{result['num_detections']} detections"
        )


if __name__ == "__main__":
    main()

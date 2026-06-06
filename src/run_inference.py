from inference.yolo_detector import YOLODetector


def main():
    detector = YOLODetector("yolov8n.pt")
    detections = detector.detect("https://ultralytics.com/images/bus.jpg")

    for detection in detections:
        print("Detected object:")
        print(f"  Class: {detection['class_name']}")
        print(f"  Confidence: {detection['confidence']:.2%}")
        print(f"  Box: {detection['box']}")
        print()

if __name__ == "__main__":
    main()

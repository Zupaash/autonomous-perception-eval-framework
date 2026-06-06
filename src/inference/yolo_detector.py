from ultralytics import YOLO


class YOLODetector:
    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image_path: str):
        results = self.model(image_path)
        detections = []

        for result in results:
            names = result.names

            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0]

                detections.append({
                    "class_id": class_id,
                    "class_name": names[class_id],
                    "confidence": confidence,
                    "box": {
                        "x1": float(x1),
                        "y1": float(y1),
                        "x2": float(x2),
                        "y2": float(y2),
                    },
                })

        return detections

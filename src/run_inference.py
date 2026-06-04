from ultralytics import YOLO


def main():
    # Load the pretrained YOLOv8 nano model
    model = YOLO("yolov8n.pt")

    # Run inference on a test image
    results = model("https://ultralytics.com/images/bus.jpg")

    # ============================================================
    # ORIGINAL VERSION
    #
    # This prints the raw YOLO Boxes object.
    # Useful for exploring the data structure and understanding
    # what information YOLO returns internally.
    #
    # Example outputs:
    #   - cls (class IDs)
    #   - conf (confidence scores)
    #   - xyxy (bounding box coordinates)
    #   - xywh (center, width, height format)
    # ============================================================

    # for result in results:
    #     print(result.boxes)

    # ============================================================
    # HUMAN-READABLE VERSION
    #
    # Converts raw tensors into meaningful information.
    # Prints:
    #   - Object class name
    #   - Confidence score
    #   - Bounding box coordinates
    # ============================================================

    # YOLO returns a list of results, one per image
    for result in results:
        names = result.names  # class ID -> class name mapping

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            x1, y1, x2, y2 = box.xyxy[0]

            print("Detected object:")
            print(f"  Class: {names[class_id]}")
            print(f"  Confidence: {confidence:.2%}")
            print(f"  Box: ({x1:.1f}, {y1:.1f}) to ({x2:.1f}, {y2:.1f})")
            print()


if __name__ == "__main__":
    main()

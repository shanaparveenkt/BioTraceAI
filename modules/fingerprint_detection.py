import cv2
import numpy as np


def detect_fingerprint(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return {"error": "Image not found"}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width, _ = image.shape

    # Risk calculation
    resolution_score = min((width * height) / 100000, 40)

    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness_score = min(sharpness / 50, 30)

    brightness = gray.mean()
    exposure_score = min(brightness / 4, 30)

    risk_score = resolution_score + sharpness_score + exposure_score
    risk_score = min(risk_score, 100)

    finger_detected = brightness > 40

    save_path = "extracted/fingerprints/fingerprint_region.jpg"
    cv2.imwrite(save_path, image)

    return {
        "finger_detected": finger_detected,
        "risk_score": round(risk_score, 2),
        "saved_path": save_path
    }
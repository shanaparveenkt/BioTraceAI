import cv2
import os

def detect_face(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return {"error": "Image not found"}

    image = cv2.resize(image, (600, 600))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
        )

    if len(faces) == 0:
        return {
            "face_detected": False,
            "risk_score": 0
        }

    x, y, w, h = faces[0]

    # Extract face
    face_crop = image[y:y+h, x:x+w]

    save_path = "extracted/faces/face.jpg"
    cv2.imwrite(save_path, face_crop)

    # Risk score calculation
    resolution_score = min((w * h) / 1000, 40)

    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness_score = min(sharpness / 50, 30)

    visibility_score = 30

    risk_score = resolution_score + sharpness_score + visibility_score
    risk_score = min(risk_score, 100)

    return {
        "face_detected": True,
        "risk_score": round(risk_score, 2),
        "saved_path": save_path
    }
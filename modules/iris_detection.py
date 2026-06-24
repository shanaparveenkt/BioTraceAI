import cv2

def detect_iris(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return {"error": "Image not found"}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
    )

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    if len(eyes) == 0:
        return {
            "iris_detected": False,
            "risk_score": 0
        }

    x, y, w, h = eyes[0]

    # Extract eye region
    eye_crop = image[y:y+h, x:x+w]

    save_path = "extracted/iris/iris.jpg"
    cv2.imwrite(save_path, eye_crop)

    resolution_score = min((w * h) / 500, 40)

    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness_score = min(sharpness / 50, 30)

    exposure_score = 30

    risk_score = resolution_score + sharpness_score + exposure_score
    risk_score = min(risk_score, 100)

    return {
        "iris_detected": True,
        "risk_score": round(risk_score, 2),
        "saved_path": save_path
    }
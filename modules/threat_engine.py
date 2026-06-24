def analyze_threat(face_score, fingerprint_score, iris_score):

    overall_score = (
        0.4 * face_score +
        0.35 * fingerprint_score +
        0.25 * iris_score
    )

    if overall_score <= 40:
        threat_level = "LOW"
    elif overall_score <= 70:
        threat_level = "MEDIUM"
    else:
        threat_level = "HIGH"

    threats = []
    recommendations = []

    # Face Analysis
    if face_score > 70:
        threats.append("High deepfake risk from facial exposure")
    elif face_score > 40:
        threats.append("Moderate facial exposure detected")

    # Fingerprint Analysis
    if fingerprint_score > 70:
        threats.append("High biometric spoofing risk from fingerprint exposure")
    elif fingerprint_score > 40:
        threats.append("Moderate fingerprint exposure detected")

    # Iris Analysis
    if iris_score > 70:
        threats.append("High identity misuse risk from iris exposure")
    elif iris_score > 40:
        threats.append("Moderate iris exposure detected")

    # Recommendations
    recommendations.append("Review social media privacy settings")
    recommendations.append("Avoid posting ultra-HD selfies publicly")

    if face_score > 40:
        recommendations.append("Reduce public exposure of facial close-up images")

    if fingerprint_score > 40:
        recommendations.append("Avoid visible finger close-ups in selfies")

    if iris_score > 40:
        recommendations.append("Avoid posting high-resolution eye images")

    return {
        "overall_score": round(overall_score, 2),
        "threat_level": threat_level,
        "threats": threats,
        "recommendations": recommendations
    }
import streamlit as st
import os

from modules.face_detection import detect_face
from modules.fingerprint_detection import detect_fingerprint
from modules.iris_detection import detect_iris
from modules.threat_engine import analyze_threat

st.title("BioTrace AI")
st.markdown("### Biometric Privacy Risk Intelligence System")
st.markdown("Analyze selfie images to detect biometric exposure risks from face, iris, and fingerprint visibility.")

uploaded_file = st.file_uploader("Upload a selfie", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    file_path = os.path.join("samples", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded Selfie", width="stretch")

    st.write("Analyzing biometrics...")

    face_result = detect_face(file_path)
    fingerprint_result = detect_fingerprint(file_path)
    iris_result = detect_iris(file_path)

    face_score = face_result["risk_score"]
    fingerprint_score = fingerprint_result["risk_score"]
    iris_score = iris_result["risk_score"]

    final_result = analyze_threat(
        face_score,
        fingerprint_score,
        iris_score
    )

    st.markdown("---")

    st.write("## BioTrace Intelligence Report")

    st.write(f"Face Risk Score: {face_score}")
    st.write(f"Fingerprint Risk Score: {fingerprint_score}")
    st.write(f"Iris Risk Score: {iris_score}")

    st.markdown("---")
    
    st.subheader("Risk Visualization")

    st.write("Face Risk")
    st.progress(int(face_result["risk_score"]))

    st.write("Fingerprint Risk")
    st.progress(int(fingerprint_result["risk_score"]))

    st.write("Iris Risk")
    st.progress(int(iris_result["risk_score"]))

    st.markdown("---")

    st.subheader("Extracted Biometrics")

    if face_result.get("saved_path"):
        st.image(face_result["saved_path"], caption="Extracted Face", width="stretch")

    if fingerprint_result.get("saved_path"):
        st.image(fingerprint_result["saved_path"], caption="Fingerprint Region", width="stretch")

    if iris_result.get("saved_path"):
        st.image(iris_result["saved_path"], caption="Extracted Iris", width="stretch")

    st.markdown("---")

    st.write("## Final Threat Analysis")
    st.write(f"Overall Threat Score: {final_result['overall_score']}")
    if final_result["threat_level"] == "LOW":
        st.success("Threat Level: LOW")
    elif final_result["threat_level"] == "MEDIUM":
        st.warning("Threat Level: MEDIUM")
    else:
        st.error("Threat Level: HIGH")

    st.write("## Threats")
    for threat in final_result["threats"]:
        st.write("- ", threat)

    st.markdown("---")

    st.write("## Recommendations")

    for rec in final_result["recommendations"]:
        st.info(rec)


    st.progress(face_score / 100)
    st.progress(fingerprint_score / 100)
    st.progress(iris_score / 100)



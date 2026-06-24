# BioTrace AI  
### Biometric Privacy Risk Intelligence System

BioTrace AI is an intelligent biometric privacy risk analysis system designed to assess whether social media selfies expose sensitive biometric information that could be misused for identity theft, spoofing, cybercrime, or digital fraud.

This project analyzes uploaded selfie images to estimate the exposure risk of three major biometric identifiers:

- Face
- Fingerprint
- Iris

Using computer vision and intelligent threat scoring, BioTrace AI evaluates how much sensitive biometric data may be exposed through publicly shared images and generates a complete privacy risk report with threat analysis and recommendations.

---

# Project Motivation

In today’s digital world, millions of people share high-resolution selfies and personal images on social media platforms every day.

However, many users are unaware that these images may unintentionally expose sensitive biometric data such as:

- Facial features usable for deepfake generation
- Fingerprint visibility from hand gestures
- Iris details from close-up facial photos

Such biometric exposure can potentially lead to:

- Identity theft
- Deepfake misuse
- Biometric spoofing
- Privacy breaches
- Cyber fraud

BioTrace AI was developed to create awareness and provide intelligent risk assessment for biometric privacy exposure.

---

# Problem Statement

Can publicly shared selfie images reveal enough biometric information to pose privacy and security risks?

BioTrace AI addresses this problem by detecting and analyzing biometric exposure from selfie images and converting the findings into actionable risk intelligence.

---

# Objectives

- Detect biometric regions from uploaded selfie images
- Analyze face exposure risk
- Analyze fingerprint exposure risk
- Analyze iris exposure risk
- Generate an overall biometric threat score
- Classify threat levels into Low, Medium, or High
- Provide security recommendations to users

---

# Key Features

- Selfie Image Upload
- Face Detection and Risk Analysis
- Fingerprint Exposure Detection
- Iris Risk Analysis
- Threat Intelligence Report
- Risk Visualization
- Privacy Recommendations

---

# System Workflow

```text
User Uploads Selfie
        ↓
Face Detection
Fingerprint Exposure Detection
Iris Detection
        ↓
Risk Score Calculation
        ↓
Threat Intelligence Engine
        ↓
Final Privacy Risk Report
```

---

# Tech Stack

- Python
- OpenCV
- Streamlit
- NumPy
- Pandas

---

# Project Architecture

```text
BioTraceAI/
│
├── modules/
│   ├── face_detection.py
│   ├── fingerprint_detection.py
│   ├── iris_detection.py
│   └── threat_engine.py
│
├── samples/
├── extracted/
├── app.py
├── requirements.txt
└── README.md
```

---

# Module Description

## Face Detection Module

This module detects facial regions from uploaded images using OpenCV.

The system evaluates:
- Face visibility
- Image resolution
- Image sharpness

Based on these metrics, a Face Risk Score is generated.

Potential risks include:
- Deepfake generation
- Facial recognition misuse
- Identity theft

---

## Fingerprint Exposure Detection Module

This module estimates whether visible finger regions in selfies could expose fingerprint-related biometric information.

Since normal social media images rarely provide full fingerprint ridge details, the system focuses on exposure risk estimation rather than full fingerprint extraction.

The system analyzes:
- Finger visibility
- Image clarity
- Resolution
- Sharpness

Potential risks include:
- Biometric spoofing
- Unauthorized identity verification
- Security breaches

---

## Iris Detection Module

This module estimates iris exposure risk from facial images.

The system analyzes:
- Eye visibility
- Iris clarity
- Sharpness
- Image quality

Potential risks include:
- Iris recognition misuse
- Identity impersonation
- Biometric fraud

---

## Threat Engine Module

This is the intelligence core of BioTrace AI.

It combines:
- Face Risk Score
- Fingerprint Risk Score
- Iris Risk Score

Weighted scoring formula:

Overall Threat Score =  
0.40 × Face Score + 0.35 × Fingerprint Score + 0.25 × Iris Score

Threat classification:
- LOW
- MEDIUM
- HIGH

---

# Risk Scoring Parameters

Risk analysis is based on:

- Image Resolution
- Image Sharpness
- Biometric Visibility
- Exposure Quality

Higher quality biometric visibility results in higher risk scores.

---

# Sample Output

## BioTrace Intelligence Report

- Face Risk Score: 78
- Fingerprint Risk Score: 64
- Iris Risk Score: 70

## Final Threat Analysis

- Overall Threat Score: 71.3
- Threat Level: HIGH

## Threats

- High deepfake risk from facial exposure
- High biometric spoofing risk from fingerprint exposure
- High identity misuse risk from iris exposure

## Recommendations

- Avoid posting ultra-HD selfies publicly
- Limit public profile visibility
- Avoid close-up eye photos
- Avoid visible finger close-ups in social media posts

---

# Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/BioTraceAI.git
```

Go to project folder:

```bash
cd BioTraceAI
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Project

Start Streamlit app:

```bash
streamlit run app.py
```

The application will open in browser automatically.

Upload a selfie and analyze biometric exposure risks.

---

# Future Enhancements

- YOLO-based biometric detection
- Deep Learning based threat classification
- Real-time webcam analysis
- PDF report generation
- Advanced biometric visualization
- Cloud deployment

---

# Applications

BioTrace AI can be used in:

- Digital Forensics
- Cybersecurity
- Privacy Intelligence
- Identity Theft Prevention
- Social Media Risk Assessment

---

# Limitations

- Fingerprint detection is exposure-based, not full ridge extraction
- Iris analysis depends on image quality
- Risk scores are estimation-based

---

# Conclusion

BioTrace AI is an innovative biometric privacy intelligence system that demonstrates how seemingly harmless social media selfies can unintentionally expose sensitive biometric information.

By combining computer vision and intelligent threat scoring, the system helps users understand biometric privacy risks and encourages safer digital behavior.

This project highlights the growing importance of biometric security, digital privacy, and cyber awareness in modern society.

---

# Author

Shana Parveen KT

---

# License

This project is for educational and research purposes.

# A Resilient Vision-Based Lane Detection System for All-Weather Autonomous Driving

## 📌 Project Overview

Lane detection is a critical component in Advanced Driver Assistance Systems (ADAS) and Autonomous Driving. Reliable lane detection enables safe navigation and supports features like Lane Keep Assistance and Adaptive Cruise Control.

Real-world challenges such as rain, fog, night driving, glare, shadows, and faded lane markings make traditional lane detection unreliable.

This project proposes a robust, adaptive, and real-time lane detection system capable of performing consistently across diverse weather and lighting conditions.

---

## 🎯 Problem Statement

Human error is a leading cause of road accidents. Autonomous systems require highly reliable lane detection, but existing approaches:

- Fail in poor weather and low-light conditions  
- Use static thresholds  
- Use fixed ROI (Region of Interest)  
- Lack temporal continuity across frames  

This project introduces an adaptive and resilient lane detection framework to overcome these limitations.

---

## 🚀 Proposed Solution

The system integrates multiple computer vision techniques with adaptive tuning:

- Bilateral Filtering – Noise reduction while preserving edges  
- Canny Edge Detection – Extract lane edges  
- Fuzzy Logic Controller – Dynamically adjusts Canny thresholds  
- Adaptive ROI Selection – Focuses only on road region  
- Hough Transform – Detects lane line geometry  
- Temporal Tracking – Maintains continuity across video frames  

---

## 🏗 System Architecture

### Processing Pipeline

1. Video Frame Acquisition  
2. Preprocessing using Bilateral Filter  
3. Adaptive Edge Detection (Canny + Fuzzy Logic)  
4. ROI Selection  
5. Lane Detection using Hough Transform  
6. Temporal Tracking  
7. Lane Overlay Visualization  

---

## 🧠 Methodology

### 1️⃣ Preprocessing
Removes noise using Bilateral Filtering while preserving lane edge details.

### 2️⃣ Adaptive Edge Detection
Uses Canny Edge Detection.  
A Fuzzy Logic Controller dynamically tunes threshold values based on lighting and weather conditions.

### 3️⃣ Region of Interest (ROI)
Dynamically selects only the road area.  
Reduces false detections and improves computational efficiency.

### 4️⃣ Lane Line Detection
Uses Hough Transform to detect lane boundaries.  
Supports mild curves using curve fitting techniques.

### 5️⃣ Temporal Tracking
Uses previous frame information to maintain lane continuity.  
Handles:
- Temporary occlusion  
- Faded lanes  
- Shadows  
- Glare  

---

## 📊 Results

The system was tested under multiple real-world conditions:

- Daytime lane detection  
- Rainy conditions  
- Foggy conditions  
- Night driving  
- Mild curves  
- Solid white roads  
- Yellow lane detection  

The system demonstrated robustness and consistent performance across all scenarios.

---

## ✅ Advantages

- All-weather adaptability  
- Dynamic threshold adjustment  
- Noise reduction with edge clarity  
- Higher accuracy  
- Frame-to-frame continuity  
- Real-time performance  
- Suitable for ADAS integration  

---

## 🆚 Comparison with Existing Systems

| Feature | Existing Systems | Proposed System |
|----------|-----------------|----------------|
| Static Threshold | Yes | No |
| Adaptive ROI | No | Yes |
| Temporal Tracking | No | Yes |
| Weather Robustness | Low | High |
| Real-Time Capability | Limited | Yes |

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- NumPy  
- Computer Vision Techniques  
- Fuzzy Logic  
- Hough Transform  

---

## 📂 Project Structure

Lane-Detection/
│── input_videos/
│── output_results/
│── src/
│    ├── preprocessing.py
│    ├── fuzzy_controller.py
│    ├── lane_detection.py
│    ├── temporal_tracking.py
│── main.py
│── requirements.txt
│── README.md

---

## ⚙ Installation

```bash
git clone https://github.com/your-username/lane-detection.git
cd lane-detection
pip install -r requirements.txt
```

---

## ▶ How to Run

```bash
python main.py --video input_videos/test_video.mp4
```

The processed output video will be saved in:

```
output_results/
```

---

## 🔮 Future Scope

- CNN-based Deep Learning integration  
- 3D Lane Detection using Stereo Vision or LiDAR  
- Handling complex intersections and multi-lane highways  
- Real-time embedded deployment on NVIDIA Jetson  
- Hybrid classical + deep learning model  

---

## 🏁 Conclusion

The proposed system enhances traditional lane detection by integrating adaptive thresholding, bilateral filtering, dynamic ROI selection, Hough Transform, and temporal tracking.

It provides a scalable, real-time, and robust solution suitable for ADAS and autonomous vehicle systems.

---

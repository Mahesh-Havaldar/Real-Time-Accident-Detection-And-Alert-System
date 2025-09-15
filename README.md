# Real-Time-Accident-Detection-And-Alert-System
🚗 Accident Detection and Alert System is a real-time intelligent solution that uses YOLOv8, image processing, and machine learning to detect road accidents and fire incidents from video feeds. The system automatically sends alerts to emergency services (police, hospital, fire brigade) to ensure faster response and save lives.
# 🚗 Real Time Accident Detection and Alert System Using Image Processing and Machine Learning

## 📌 Introduction
The **Accident Detection and Alert System** is a real-time intelligent system that uses **image processing** and **machine learning** to automatically detect road accidents from video feeds. Once an accident is detected, the system immediately sends alerts to the relevant authorities such as **police, hospital, or fire brigade** depending on the type of incident.  

The main goal of this project is to **reduce response time** after accidents, potentially saving lives by ensuring that medical and emergency services are informed as quickly as possible.  

---

## ✨ Features
- 🔍 Real-time accident detection using **YOLOv8 object detection model**  
- 🚨 Automated alert generation (SMS/Email)  
- 🚗 Detects multiple types of incidents:  
  - Car-to-car accidents (alerts police + hospital)  
  - Single-car accidents (alerts hospital)  
  - Car fire (alerts fire brigade)  
- 📹 Works with **CCTV/video surveillance systems**  
- 📊 High accuracy with large accident and fire datasets  
- ⚡ Fast inference for real-time processing  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Deep Learning Framework:** PyTorch  
- **Model:** YOLOv8 (You Only Look Once v8)  
- **Libraries Used:**  
  - OpenCV (image/video processing)  
  - Ultralytics
  - PIL (Image, Image Tk)  
  - smtplib (for alerts)  
  - Tkinter for GUI
---

## 📂 Dataset
Two custom datasets were prepared for model training:  
- **Accident Detection Dataset:** 7,512 images (Download Dataset from Kaggle)
- **Fire Detection Dataset:** 10,446 images (Download Dataset from Kaggle)

The datasets were labeled with bounding boxes for training the YOLOv8 model.  

---

## 📁 Project Structure
```
Accident-Detection-System/
├── Training.py
├── Testing.py
└── requirments.txt
├── README.md

```

---

## ⚙️ How It Works
1. **Input Video** → The system takes live CCTV/video input.  
2. **Detection** → YOLOv8 model detects cars, collisions, or fire.  
3. **Classification** → Identifies type of incident (car-to-car, single-car, or fire).  
4. **Alert Mechanism** → Automatically sends alert:  
   - 🚔 Police + 🚑 Hospital for multi-car accidents  
   - 🚑 Hospital for single-car accidents  
   - 🚒 Fire brigade for fire incidents  
5. **Output** → Annotated video with detection boxes + alerts sent.  

---

## 📊 Results
- Achieved **high accuracy** in detecting accident and fire scenarios.  
- Real-time processing speed suitable for **CCTV and traffic monitoring systems**.  
- Effective alerting mechanism tested via SMS and Email.  

---

## ✅ Advantages
- ⏱️ **Reduced response time** for emergency services  
- 💡 **Automated monitoring** without human intervention  
- 🌐 Can be integrated with **smart cities & intelligent traffic systems**  
- 🛡️ Helps in **saving lives** by quick emergency response  

---

## 🔮 Future Scope
- 🚦 Integration with **IoT-enabled vehicles and smart traffic lights**  
- 📱 Development of a **mobile application** for instant user notifications  
- 🛰️ Integration with **GPS for exact accident location tracking**  
- 🌍 Deployment on **edge devices** for faster real-time detection  

---

## 🚀 Installation & Setup
1. Clone the repository  
   ```bash
   git clone https://github.com/Mahesh-Havaldar/Real-Time-Accident-Detection-And-Alert-System.git
   cd accident-detection-system
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model (if required)  
   ```bash
   python src/Training.py
   ```
4. Run accident detection on a video  
   ```bash
   python Testing.py 
   ```
5. Alerts will be triggered automatically upon detection.  

---
## 👨‍💻 Author
**Mahesh Havaldar**  
- B.Tech in Computer Science and Engineering (Data Science)  
- Interests: Machine Learning, Image Processing, Networking  

---
 

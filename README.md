
# 🚗 Deploying Real-Time Object Detection and Obstacle Avoidance for Smart Mobility Using Edge-AI

[![License: CC BY](https://img.shields.io/badge/license-CC%20BY-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Platform: Raspberry Pi](https://img.shields.io/badge/platform-Raspberry%20Pi-red)](https://www.raspberrypi.com/)
[![Edge-AI](https://img.shields.io/badge/edge--ai-SSD--MobileNetV2-green)](#)

This repository presents a complete implementation of a low-cost autonomous rover capable of:
- Performing **real-time object detection** using `SSD-MobileNetV2`
- Executing **obstacle avoidance** via `HC-SR04` ultrasonic sensors
- Running entirely on a **Raspberry Pi 3 Model B** without cloud/GPU reliance

Designed for **smart mobility**, **traffic monitoring**, and **autonomous navigation**, this system demonstrates efficient embedded AI using affordable hardware.

---

## 🛠️ Installation & Environment Setup

### 1. Update Raspberry Pi OS
```bash
sudo apt-get update
sudo apt-get dist-upgrade
```

### 2. Install TensorFlow and Dependencies
```bash
pip3 install tensorflow pillow lxml jupyter matplotlib cython
sudo apt-get install libatlas-base-dev python3-tk protobuf-compiler
```

### 3. Install OpenCV
```bash
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev qt4-dev-tools
sudo pip3 install opencv-python
```

### 4. Clone TensorFlow Models Repo
```bash
mkdir TensorFlow && cd TensorFlow
git clone --depth 1 https://github.com/tensorflow/models.git
```

### 5. Set PYTHONPATH
Append the following to `~/.bashrc`:
```bash
export PYTHONPATH=$PYTHONPATH:/home/pi/TensorFlow/models/research:/home/pi/TensorFlow/models/research/slim
```

### 6. Compile Protobuf Files
```bash
cd ~/TensorFlow/models/research
protoc object_detection/protos/*.proto --python_out=.
```

---

## 🧠 Model Selection and Deployment

Download the SSDLite-MobileNetV2 model:
```bash
wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
```

This model offers the best trade-off between inference speed and accuracy on the Raspberry Pi platform.

---

## ▶️ Running the Detection

Ensure PiCamera is enabled:
```bash
sudo raspi-config
```

Run detection:
```bash
python3 Object_detection_picamera.py        # For PiCamera
python3 Object_detection_picamera.py --usbcam  # For USB camera
```

Detection should initialize within 30 seconds and display real-time bounding boxes on a live camera feed.

---

## 📦 Project Structure

```
├── object_avoiding.py
├── obstacle_avoiding.py
├── keyboard.py
├── README.md
├── object_detection/
│   ├── frozen_inference_graph.pb
│   ├── label_map.pbtxt
│   └── graph.pbtxt
```

---

## 📈 Performance Overview

| Model             | mAP@0.5 | Inference FPS | Total Loss |
|------------------|---------|----------------|-------------|
| SSD-MobileNetV2  | 0.851   | **1.5 FPS**    | 1.816       |
| SSD-Inception V2 | 0.862   | 1.0 FPS        | 2.379       |
| SSD-ResNet-50    | 0.923   | 0.6 FPS        | —           |

---

## 📸 Final Project Images

![Final Project Images](https://github.com/AbhishekTyagi404/Object-Detection-on-Raspberry-Pi-with-obstacle-avoiding-rover/blob/main/Images/Final%20Project%20Images.png)

---

## 📬 Contact

For collaboration or questions:  
📧 mechatronics.abhishek@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/-abhishek-tyagi/)
🔗 [Portfolio](https://kritrimintelligence.com/abhishek-tyagi/)

---

## 📜 License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

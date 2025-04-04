# 🛰️ Future Extensions for Smart Rover System

## 📸 Project Architecture

![Modular Edge-AI System Architecture: Object detection is performed on-device using Coral Edge TPU, with GPS tagging and MQTT-based real-time data transmission to a centralized monitoring server for surveillance, mobility analysis, and incident logging.](https://github.com/AbhishekTyagi404/Object-Detection-on-Raspberry-Pi-with-obstacle-avoiding-rover/blob/main/Images/Final%20Project%20Images.png)

## 1. TPU Integration (Coral USB Accelerator)
- Use PyCoral API
- Convert SSD-MobileNetV2 to .tflite and compile with EdgeTPU Compiler
- Achieve 15+ FPS inference on Pi with Coral TPU

## 2. Centralized Logging with MQTT
- Each rover pushes detection logs to a cloud broker (e.g., HiveMQ)
- Backend server logs and visualizes aggregated data

## 3. GPS Tagging
- Use GPS module to attach location to each detection
- Enable geo-aware surveillance and mobility analysis

## 4. Future: Red Light Surveillance Deployment
- Mount rover at junctions
- Log traffic violations
- Alert over GSM or Wi-Fi to a dashboard


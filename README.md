
# 🤖 Hand Gesture Controlled Wi-Fi Robot using ESP32

Control a mobile robot in real-time using hand gestures captured by a webcam. This project combines computer vision (MediaPipe), Wi-Fi communication, and embedded systems (ESP32) to create a low-cost, gesture-based robot interface.

---

## 📌 Features

- Real-time hand gesture recognition using webcam
- Wireless robot control over Wi-Fi (HTTP requests)
- Supports gestures: Forward, Left, Right, Stop
- PWM-based motor speed control
- Modular and extensible design

---

## 🧰 Tech Stack

| Component        | Technology             |
|------------------|------------------------|
| Gesture Tracking | Python, OpenCV, MediaPipe |
| Communication    | HTTP over Wi-Fi        |
| Microcontroller  | ESP32 DevKit           |
| Motor Control    | L298N Dual H-Bridge     |
| Motors           | DC Gear Motors         |

---

## 🔧 Hardware Requirements

- ESP32 DevKit v1
- L298N Motor Driver Module
- 2× DC Motors (6–12V)
- Power supply (e.g., 9V battery or Li-ion)
- PC/Laptop with webcam
- Wi-Fi network

---

## ⚙️ Software Setup

### 1. ESP32 Code

Upload the provided Arduino code to ESP32 via Arduino IDE.

- Required libraries: `WiFi.h`, `WebServer.h`
- Set your Wi-Fi credentials in the code
- Connect:
  - Motor1: GPIO 27, 26, ENA → 14
  - Motor2: GPIO 33, 25, ENB → 32

### 2. PC Gesture Controller

Install required Python packages:
```bash
pip install opencv-python mediapipe requests
```

Run the gesture controller:
```bash
python gesture_control.py
```

Edit the script to match your ESP32's IP address.

---

## 🧠 System Architecture

```
[ User Hand ]
     ↓
[ PC Webcam ] → [ Python + MediaPipe ]
     ↓              ↓
[ HTTP Commands ] → [ ESP32 WebServer ]
     ↓
[ L298N Motor Driver ]
     ↓
[ Robot Movement ]
```

---

## 🖐️ Supported Gestures

| Gesture       | Action           |
|---------------|------------------|
| Index finger up | Move Forward   |
| Thumb left of pinky | Turn Left  |
| Thumb right of pinky | Turn Right |
| All fingers down | Stop          |

---

## 📷 Screenshots

![Gesture UI](assets/gesture_ui.png)
![Robot Setup](assets/robot_setup.jpg)

---

## ✅ To-Do / Future Work

- Add reverse gesture
- Improve gesture classification using ML
- Implement phone camera support
- Add voice + gesture hybrid control

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

- [MediaPipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [ESP32](https://www.espressif.com/)

import cv2
import mediapipe as mp
import requests

# Replace with your actual ESP32 IP address
ESP32_IP = "http://172.20.10.12"

# Gesture-to-URL mapping
def send_command(cmd):
    try:
        requests.get(f"{ESP32_IP}/{cmd}")
        print(f"Sent: {cmd}")
    except:
        print("Failed to connect to ESP32")

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

previous_cmd = None

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Flip image for mirror view
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)

    h, w, _ = image.shape
    if result.multi_hand_landmarks:
        lm = result.multi_hand_landmarks[0].landmark

        # Get tip of index and middle finger
        index_y = lm[8].y
        middle_y = lm[12].y
        thumb_tip_x = lm[4].x
        pinky_tip_x = lm[20].x

        # Gesture conditions (very basic for demo)
        if index_y < middle_y:  # Fingers up
            cmd = "forward"
        elif thumb_tip_x > pinky_tip_x:  # Hand turned
            cmd = "left"
        elif thumb_tip_x < pinky_tip_x:
            cmd = "right"
        else:
            cmd = "stop"

        if cmd != previous_cmd:
            send_command(cmd)
            previous_cmd = cmd

    cv2.imshow("Hand Control", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
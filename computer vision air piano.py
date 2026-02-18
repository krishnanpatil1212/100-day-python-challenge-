import cv2
import mediapipe as mp
from pygame import mixer

# Initialize sound and hand tracking
mixer.init()
note_c = mixer.Sound('c4.wav') 

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # 1. Convert to RGB for MediaPipe
    # 2. Process frame to get landmarks
    # 3. If landmarks exist, get Landmark 8 (Index Tip)
    # 4. Check if Landmark 8 is inside your rectangle coordinates
    # 5. Play sound!
    
    cv2.imshow('Air Piano', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

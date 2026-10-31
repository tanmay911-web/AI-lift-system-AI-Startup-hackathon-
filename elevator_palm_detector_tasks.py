"""
Elevator Palm Detection (OpenCV + MediaPipe Tasks API)

Shows "palm is open" and "lift+stop" when an open hand with the PALM
facing the camera is held steadily for a few frames.

Install:  python -m pip install opencv-python mediapipe
Run:      python elevator_palm_detector_tasks.py
Quit:     press 'q'

The hand model (hand_landmarker.task, ~8 MB) is downloaded automatically
next to this script the first time you run it.
"""

import math
import os
import time
import urllib.request

import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

# ---------------- Settings ----------------
HOLD_FRAMES = 5            # frames the gesture must persist (reduces flicker)
CAMERA_INDEX = 0
FLIP_HANDEDNESS = True     # set False if palm/back of hand are detected swapped

MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
             "hand_landmarker/float16/latest/hand_landmarker.task")
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "hand_landmarker.task")

# Hand skeleton connections (landmark index pairs) for drawing
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17),
]


def ensure_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading hand model (one time)...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Done.")


def dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def all_fingers_extended(lm):
    """True if index, middle, ring, pinky and thumb are all extended.
    Uses distance from the wrist, so it works at any hand tilt/rotation."""
    wrist = lm[0]

    # Four fingers: tip farther from wrist than the PIP joint
    for tip, pip in ((8, 6), (12, 10), (16, 14), (20, 18)):
        if dist(lm[tip], wrist) < dist(lm[pip], wrist) * 1.1:
            return False

    # Thumb: tip farther from the pinky base than the thumb's IP joint
    if dist(lm[4], lm[17]) < dist(lm[3], lm[17]) * 1.05:
        return False

    return True


def palm_faces_camera(lm, label):
    """True if the palm (not the back of the hand) faces the camera."""
    v1 = (lm[5].x - lm[0].x, lm[5].y - lm[0].y)     # wrist -> index base
    v2 = (lm[17].x - lm[0].x, lm[17].y - lm[0].y)   # wrist -> pinky base
    cross = v1[0] * v2[1] - v1[1] * v2[0]
    is_right = (label == "Right")
    if FLIP_HANDEDNESS:
        is_right = not is_right
    return cross > 0 if is_right else cross < 0


def draw_hand(img, lm):
    h, w = img.shape[:2]
    pts = [(int(p.x * w), int(p.y * h)) for p in lm]
    for a, b in HAND_CONNECTIONS:
        cv2.line(img, pts[a], pts[b], (255, 255, 255), 2)
    for p in pts:
        cv2.circle(img, p, 4, (0, 0, 255), -1)


def main():
    ensure_model()

    options = vision.HandLandmarkerOptions(
        base_options=mp_python.BaseOptions(model_asset_path=MODEL_PATH),
        running_mode=vision.RunningMode.VIDEO,
        num_hands=1,
        min_hand_detection_confidence=0.7,
        min_hand_presence_confidence=0.7,
        min_tracking_confidence=0.7,
    )
    landmarker = vision.HandLandmarker.create_from_options(options)

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("Could not open webcam.")
        return

    print("Starting camera... Press 'q' to quit.")
    streak = 0
    start = time.monotonic()
    last_ts = -1

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab frame.")
            break

        img = cv2.flip(img, 1)                       # mirror view
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)

        ts = int((time.monotonic() - start) * 1000)
        if ts <= last_ts:
            ts = last_ts + 1
        last_ts = ts

        result = landmarker.detect_for_video(mp_image, ts)

        palm_open = False
        if result.hand_landmarks:
            lm = result.hand_landmarks[0]
            label = result.handedness[0][0].category_name
            draw_hand(img, lm)

            if all_fingers_extended(lm) and palm_faces_camera(lm, label):
                palm_open = True

        # Require the gesture to hold for a few frames before showing it
        streak = streak + 1 if palm_open else 0

        if streak >= HOLD_FRAMES:
            cv2.putText(img, "palm is open", (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)
            cv2.putText(img, "lift+stop", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)

        cv2.imshow("Elevator Palm Detection", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    landmarker.close()


if __name__ == "__main__":
    main()
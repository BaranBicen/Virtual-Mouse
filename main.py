import cv2
import mediapipe as mp
import pyautogui

# To capture video as the name suggests
cap = cv2.VideoCapture(0)
# To define hands
hands_detector = mp.solutions.hands.Hands()
# To draw landmarks of the hands
drawing_utils = mp.solutions.drawing_utils
# To get the screen size
screen_width, screen_height = pyautogui.size()
# To be able to click
index_y = 0

# Starting an infinite while loop to get the video all the time
while True:
    # Reading, converting its color and detecting hands then streaming the video in a cv2 window
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detector = hands_detector.process(converted_frame)
    hands = detector.multi_hand_landmarks

    if hands:
        # Checking hands then in hands we draw landmarks
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            # Giving each node an id to separate each finger and node from each other
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                print(x, y)
                # Checking if the id is 8 then drawing a circle around the fingertip
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=20, color=(255, 255, 0))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)

                # Checking if the id is 8 then drawing a circle around the fingertip
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=20, color=(255, 255, 0))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print("Differance : ", abs(index_y - thumb_y))

                    # If the distance differance between index finger and thumb is less than 30 we click
                    if abs(index_y - thumb_y) < 35:
                        print("Clicked")
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow("Mouse", frame)
    cv2.waitKey(1)

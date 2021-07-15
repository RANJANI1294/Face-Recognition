import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
with mp_hand.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        sucess, frame = cap.read()


        if sucess:
            print("Yay!!! We got the video.")
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False

            results = hands.process(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame.flags.writeable = True
            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS)

            cv2.imshow('Frame', frame)

            k = cv2.waitKey(50)
            if k & 0xff == ord('r'):
                break
        else:
            print("Sed Lyf :( :(")
            break

cap.release()
cv2.destroyAllWindows()

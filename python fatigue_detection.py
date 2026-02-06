
import cv2
import time
import winsound

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

closed_start = None
CLOSE_TIME = 2  # seconds


def alarm():
    winsound.Beep(2000, 800)


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    status = "AWAKE"

    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_gray)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        if len(eyes) == 0:  
            if closed_start is None:
                closed_start = time.time()

            if time.time() - closed_start > CLOSE_TIME:
                status = "DROWSY!"
                alarm()
        else:
            closed_start = None

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.putText(frame, status, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                (0, 255, 0) if status == "AWAKE" else (0, 0, 255), 3)

    cv2.imshow("Fatigue Detection (OpenCV)", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

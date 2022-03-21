import cv2
import time

def detection(img):
    start=time.time()
    casc='haarcascade_frontalface_default.xml'

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(casc)

    # Read the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces)==1:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imwrite("Visage.png",img)
        end=time.time()
        print('time visage detecte=',end-start)
        return True
    else:
        end=time.time()
        print('time visage non detecte=',end-start)
        return False

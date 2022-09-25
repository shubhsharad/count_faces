import cv2
import numpy as np
import dlib

capture = cv2.VideoCapture(0) # connecting your face camera/ webcam
detector = dlib.get_frontal_face_detector() # Coordinates detector
while True: # Loop to capture continous frames

    ret, frames = capture.read() # Instructions to capture faces frame by frame
    frames = cv2.flip(frames, 1)
    gray_scale = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) # Converting the colors to grayscale for easy processing
    faces_detected = detector(gray_scale)
    count_faces = 0 # count of faces

    for face_detected in faces_detected:
 
        x, y = face_detected.left(), face_detected.top() # Coordinates of the faces
        x1, y1 = face_detected.right(), face_detected.bottom() # Coordinates of the faces
        cv2.rectangle(frames, (x, y), (x1, y1), (255, 255, 0), 2) # create a rectangle around the face
 
        count_faces = count_faces+1 # Increment counter for each face detected
        cv2.putText(frames, 'Face number '+str(count_faces), (x-10, y-10),# Display box and number
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 2)
        print(face_detected, count_faces)
        
    cv2.imshow('frame', frames)
    if cv2.waitKey(1) & 0xFF == ord('e'):# press "e" to exit
        break

capture.release()
cv2.destroyAllWindows()
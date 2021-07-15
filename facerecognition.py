import cv2
import face_recognition
import numpy as np

harry = face_recognition.load_image_file('C:/Users/MY HP/Desktop/Untitled Folder/harry.jpg')
h_encoding = face_recognition.face_encodings(harry)[0]

vijay = face_recognition.load_image_file('C:/Users/MY HP/Desktop/Untitled Folder/vj.jpg')
v_encoding = face_recognition.face_encodings(vijay)[0]

known_face_encoding = [
    h_encoding,
    v_encoding
]

known_face_names = [
    harry,
    vijay
]

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while cap.isOpened():
    flag,frame = cap.read()
    if not flag:
        print("Sorry not succeed")
        break
    sf = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rsf = cv2.cvtcolor(sf,cv2.COLOR_BGR2RGB)
    fl = face_recognition.face_locations(rsf)
    fe = face_recognition.face_encodings(rsf,fl)
    face_names = []
    for fes in fe:
       m = face_recognition.compare_faces(known_face_encodings,fe)
       name = "Unknown"
       fd = face_recognition.face_distance(known_face_encodings,fe)
       best_match_index = np.argmin(fd)
       if m[best_match_index]:
           name = known_face_names[best_match_index]
       face_names.append(name)
       print(face_names)
    cv2.imshow("FRAME",rsf)
    if cv2.waitKey(1) & 0xff == ord('r'):
        break
cap.release()
cv2.destroyAllWindows()

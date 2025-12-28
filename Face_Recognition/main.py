import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Open webcam
video_capture = cv2.VideoCapture(1)

# Load known faces
ravi_image = face_recognition.load_image_file("Faces/ravi.jpg")
ravi_face_encoding = face_recognition.face_encodings(ravi_image)[0]

reena_image = face_recognition.load_image_file("Faces/reena.jpg")
reena_face_encoding = face_recognition.face_encodings(reena_image)[0]

aman_image = face_recognition.load_image_file("Faces/aman.jpg")
aman_face_encoding = face_recognition.face_encodings(aman_image)[0]

known_face_encodings = [ravi_face_encoding, reena_face_encoding,aman_face_encoding]
known_face_names = ["ravi","reena","aman"]

students = known_face_names.copy()

# Get current date
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open CSV file
f = open(f"{current_date}.csv", "w", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Time"])

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Mark attendance once
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])

        # Draw rectangle
        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
f.close()

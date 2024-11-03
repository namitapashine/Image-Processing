import cv2

# Load the Haar Cascade classifier for pedestrian detection
pedestrian_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Capture video from the specified source
cap = cv2.VideoCapture("walking.avi")

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for better detection performance
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect pedestrians
    pedestrians = pedestrian_cascade.detectMultiScale(gray_frame, 1.1, 5)

    # Draw rectangles around detected pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Pedestrian Detection', frame)

    # Break the loop 
    if cv2.waitKey(0)==32:
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
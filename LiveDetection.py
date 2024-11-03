import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start the webcam
vid = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = vid.read()
    
    # Convert the frame to grayscale for better face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Draw rectangles around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the frame with detected faces
    cv2.imshow("Webcam", frame)
    
    # Break the loop when the spacebar (ASCII 32) is pressed
    if cv2.waitKey(25) == 32:  # Spacebar key
        break

# Release the webcam and close all OpenCV windows
vid.release()
cv2.destroyAllWindows()

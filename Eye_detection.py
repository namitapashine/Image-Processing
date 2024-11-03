import cv2

# Load the pre-trained Haar Cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start the webcam
vid = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = vid.read()
    if not ret:
        break
    
    # Convert the frame to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Draw rectangles around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Define the face region of interest (ROI) in grayscale and color
        face_roi_gray = gray[y:y + h, x:x + w]
        face_roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(face_roi_gray, 1.1, 5)
        
        # Draw rectangles around each detected eye
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    # Display the frame with detected faces and eyes
    cv2.imshow("Webcam", frame)
    
    # Break the loop when the spacebar (ASCII 32) is pressed
    if cv2.waitKey(25) == 32:  # Spacebar key
        break

# Release the webcam and close all OpenCV windows
vid.release()
cv2.destroyAllWindows()


import cv2

# Open the webcam
vid_rec = cv2.VideoCapture(0)  # Use "0" to access the primary webcam

# Check if the webcam opened successfully
if not vid_rec.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture video properties
height = int(vid_rec.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid_rec.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(vid_rec.get(cv2.CAP_PROP_FPS)) or 20  # Default to 20 if fps is not available

# Video writer initialization
content = cv2.VideoWriter(r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Desktop\namita\VisualStudio\ImageProcessing\videos_recorded\webcam_record_1.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

# Record video
while True:
    ret, frame = vid_rec.read()
    
    if not ret:
        print("Error: Frame capture failed.")
        break

    # Display the frame
    cv2.imshow("Recording", frame)
    
    # Write the frame to the video file
    content.write(frame)
    
    # Press spacebar (ASCII 32) to exit the loop
    if cv2.waitKey(1) == 32:  # Spacebar key
        break

# Release resources
vid_rec.release()
content.release()
cv2.destroyAllWindows()

import cv2
import os

# Path to the directory containing the images
image_folder = (r'C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Desktop\namita\VisualStudio\Images\Sequence' )

# Get a list of images
images = []

for img in os.listdir(image_folder):
    images.append(img)
images.sort()  

# Check if there are images
if not images:
    print("No images found in the folder.")
    exit()

# Read the first image to get the dimensions
first_image_path = os.path.join(image_folder, images[0])
print(first_image_path)
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# Define the codec and create a VideoWriter object
output_video_file = (r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Desktop\namita\VisualStudio\Images\Img_vid\Sunrise.mp4")
video = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'mp4v'), 15, (width, height))  

# Loop through the images and write them to the video
for image in images:
   
    img_path = os.path.join(image_folder, image)
  #  print(img_path)
    frame = cv2.imread(img_path)
    
    # Optional: Resize or apply shape properties
    # frame = cv2.resize(frame, (width, height))  # Resize if necessary
    
    video.write(frame)  # Write the frame to the video
    


# Release the video writer
video.release()
cv2.destroyAllWindows()

print(f"Video saved as {output_video_file}")

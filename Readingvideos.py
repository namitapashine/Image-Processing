# Video: FPS:measure of how fast the images are transitioning (40 fps: 40 images displayed in a second)

import cv2

#vid=cv2.VideoCapture(0)  # 

#vid=cv2.VideoCapture(r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Desktop\namita\VisualStudio\Images\Img_vid\Sunrise.mp4")

vid=cv2.VideoCapture("video_sample.mp4")


if(vid.isOpened()==False):
    print("unable to read the Video ")
while(True):
    ret,frame=vid.read()
    if not ret:
      print("Failed to grab frame.")
      break

    cv2.imshow("video display", frame)
  
    if cv2.waitKey(20)==32:  # 32 is ASCII code of space key
     break
vid.release()
cv2.destroyAllWindows()



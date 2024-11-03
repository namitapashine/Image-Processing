# image classification
# classifier:trained to identify faces by running them onto several thousands of images,then when it sees an image with a face , it can detect the face


# OpenCV library has a face detection classifier data stored in XML file format called as Haar Cascade Classifier

# Haar Cascade: Object detection Algorithm used to identify objects in an image or video


import cv2

img = cv2.imread('Nam1.jpg')
if img is None:
    print("Error: Image not found or cannot be read.") 
else:
    
    scale_percent = 20
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    #cv2.imshow('Resized Image', resized_image)  # Display resized image
    gray=cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)


    #face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
    
    faces=face_cascade.detectMultiScale(gray)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(resized_image,(x,y),(x+w,y+w),(255,0,0),2)
        cv2.imshow("img",resized_image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
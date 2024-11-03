#CV:help the computer to identify and understand the digital content

#pixels:digital image stored a set of numbers// tiny dots on computer display arranged in rows and columns

# Binary images:black and white images(0:balck, 1:white), 
# Gray-scale images:monochrome/one colored(0-255)
# colored image: 3 bands/channels -red band(0-255),green band(0-255),blue(0-255)


# openCV
#pip install opencv-python

#cv2


import cv2

img=cv2.imread("playerimg.png")

cv2.imshow("Original image",img)
cv2.waitKey(0)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2LUV)
cv2.imshow("Gray image",gray_img)
#print(img)
cv2.waitKey(0)

# in open cv colored images are represented as BGR band

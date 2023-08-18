# Importing the cv2 module
import cv2

# Storing the solar system image into img
img = cv2.imread("solar-system.jpg")

# Text for the Sun
cv2.putText(img, "Sun", (100, 100), cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color=(0,0,255))
# Text for Mercury
cv2.putText(img, "Mercury", (120, 190), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Venus
cv2.putText(img, "Venus", (195, 170), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Earth
cv2.putText(img, "Earth", (290, 170), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Mars
cv2.putText(img, "Mars", (385, 180), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Jupiter
cv2.putText(img, "Jupiter", (580, 50), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Saturn
cv2.putText(img, "Saturn", (790, 120), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Uranus
cv2.putText(img, "Uranus", (975, 140), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))
# Text for Neptune
cv2.putText(img, "Neptune", (1115, 140), cv2.FONT_HERSHEY_COMPLEX, fontScale=0.4, color=(255,255,255))

# Displaying the image for infinite time
cv2.imshow("Output", img)
cv2.waitKey(0)

# Saving the image as solar-system-with-name.jpg
cv2.imwrite("solar-system-with-name.jpg", img)
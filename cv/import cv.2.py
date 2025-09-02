import cv2

# Read the image (OpenCV loads images in BGR format by default)
img = cv2.imread("C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\food photo.jpg")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert BGR to Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow('BGR Image', img)
cv2.imshow('RGB Image', img_rgb)
cv2.imshow('Grayscale Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
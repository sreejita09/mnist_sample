import cv2

# Read the image
img = cv2.imread("C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\food photo.jpg")  # Replace with your image path

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()
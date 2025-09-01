import cv2
import time

# List of image paths
image_paths = [
    r"C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\p1.png",
    r"C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\p2.png",
    r"C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\p3.png",
    r"C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\p4.png",
    r"C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\p5.png",
    r"C:\Users\DELL\OneDrive\Desktop\SELF STUDY\main quest\samples in cv\photos and other materials\p6.png",
    # Add more image paths as needed
]
for path in image_paths:
    frame = cv2.imread(path)
    if frame is not None:
        cv2.imshow('Frame', frame)
        cv2.waitKey(1000)  # Display each frame for 1000 ms (1 second)
    else:
        print(f"Could not load image: {path}")

cv2.destroyAllWindows()
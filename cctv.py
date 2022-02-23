import cv2

cap = cv2.VideoCapture(0)


while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    if ret:
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

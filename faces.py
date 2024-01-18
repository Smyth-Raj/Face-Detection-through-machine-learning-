import cv2

# Load an image with faces
image_path = "D:/Desk.jpg"
image = cv2.imread(image_path)

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convert the image to grayscale for better performance
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.01, minNeighbors=10, minSize=(30, 30))

# Print the number of faces found
face_count = len(faces)
print(f"Found {face_count} face(s) in the image.")

# Print face locations
for i, (x, y, w, h) in enumerate(faces, 1):
    print(f"Face {i} found at pixel location X: {x}, Y: {y}, Width: {w}, Height: {h}")

# Display the image with rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Face Detection & Face Counts", image )
# cv2.imcount("Face COunts",face_count)
print("faceCount : ",face_count)
cv2.waitKey(0)
cv2.destroyAllWindows()

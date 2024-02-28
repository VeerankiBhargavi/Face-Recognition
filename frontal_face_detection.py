#Detection of frontal faces 
import cv2

class FaceDetector:
    def __init__(self, cascade_path):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_faces(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        return faces

    def draw_faces(self, image, faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    def detect_and_draw_faces(self, image):
        faces = self.detect_faces(image)
        self.draw_faces(image, faces)
        return image

if __name__ == "__main__":
    # Path to the cascade classifier for face detection
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

    # Path to the input image
    image_path = 'source_image.jpg'

    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load the image.")
    else:
        # Initialize the FaceDetector object
        face_detector = FaceDetector(cascade_path)

        # Detect and draw faces on the image
        image_with_faces = face_detector.detect_and_draw_faces(image)

        # Display the image with detected faces
        cv2.imshow("Detected Faces", image_with_faces)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

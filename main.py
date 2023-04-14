import cv2

# Uploading makeup images
makeup_images = [
    cv2.imread('img.png', -1),
    cv2.imread('img_1.png', -1),
    cv2.imread('img_2.png', -1)
]

# Uploading Haar cascades for face and eye recognition
face_cascade = cv2.CascadeClassifier('faces.xml')
eye_cascade = cv2.CascadeClassifier('eyes.xml')

# Starting the video stream from the camera
cap = cv2.VideoCapture(0)
makeup_image = makeup_images[0]

while True:
    # Getting a frame from a video camera
    ret, frame = cap.read()

    # Converting the frame to black and white format to improve face and eye recognition
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Finding the faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 19)

    # Displaying the found faces in the image
    for (x, y, w, h) in faces:
        # Finding the eyes in the image of the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 19)

        # Displaying images of makeup on the eyes
        for (ex, ey, ew, eh) in eyes:
            if x + ex < x + w and y + ey < y + h: # Проверяем, что глаз находится внутри области лица
                # Choosing a makeup image from the set
                makeup_choice = cv2.waitKey(1) & 0xFF
                if makeup_choice == ord('1'):
                    makeup_image = makeup_images[0]
                elif makeup_choice == ord('2'):
                    makeup_image = makeup_images[1]
                elif makeup_choice == ord('3'):
                    makeup_image = makeup_images[2]
                else:
                    makeup_image = makeup_image

                    # Check the dimension of the makeup image
                if makeup_image.shape[2] != 4:
                        # If the image does not have an Alpha channel, adding it
                    makeup_image = cv2.cvtColor(makeup_image, cv2.COLOR_BGR2BGRA)
                # Scaling the makeup image according to the size of the eye
                resized_makeup = cv2.resize(makeup_image, (ew, eh))

                # Applying an image of makeup to the eyes
                if ex < w // 2: # Mirroring makeup for the left eye
                    resized_makeup = cv2.flip(resized_makeup, 1)
                for i in range(resized_makeup.shape[0]):
                    for j in range(resized_makeup.shape[1]):
                        if resized_makeup[i][j][3] != 0:
                            roi_color[ey + i, ex + j, :] = resized_makeup[i, j, :-1]

    # Displaying a frame from a video camera
    cv2.imshow('Makeup', frame)

    # If the 'q' key is pressed, ending the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Freeing up resources
cap.release()
cv2.destroyAllWindows()
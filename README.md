# interactive-makeup-selection
A Python program using OpenCV, which provides the ability to interactively select makeup from a given set and overlay in a video stream from a video camera in real time.

The work was implemented using the PyCharm Community Edition 2023.1 development environment. To implement the program, the OpenCV Python library (pip install opencv-python) was used to process images and videos in real time. Haar cascades for face and eye recognition were also uploaded.

The algorithm of the program:
1. Loading makeup images into computer memory.
2. Loading Haar cascades for face and eye recognition into computer memory.
3. Starting the video stream from the camera.
4. Getting a frame from a video camera.
5. Converting the frame to black and white format to improve face and eye recognition.
6. Finding faces in the image using the Haar cascade for face recognition.
7. Displaying of the found faces in the image.
8. Finding the eyes on the face image using the Haar cascade for eye recognition.
9. Displaying of makeup images on the eyes.
10. If the "1", "2" or "3" key is pressed, selecting the appropriate makeup image.
11. Scaling the makeup image according to the size of the eye.
12. Applying an image of makeup to the eyes.
13. Displaying a frame from a video camera with makeup applied on the eyes.
14. If the "q" key is pressed, the program ends.
15. Releasing of resources.
The program uses a loop to perform steps 4-14 on each frame of the video stream until the "q" key is pressed.

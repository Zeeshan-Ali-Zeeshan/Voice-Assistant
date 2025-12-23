# import cv2
# import mediapipe as mp
# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

# # Path to the downloaded model
# model_path = 'path/to/gesture_recognizer.task'

# # Set up base options
# base_options = vision.GestureRecognizerOptions.BaseOptions(model_asset_path=model_path)

# # Create the gesture recognizer
# options = vision.GestureRecognizerOptions(base_options=base_options)
# recognizer = vision.GestureRecognizer.create_from_options(options)

# # Start video capture
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     success, frame = cap.read()
#     if not success:
#         break

#     # Convert the frame to RGB
#     image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Create an Image object
#     mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

#     # Recognize gestures
#     result = recognizer.recognize(mp_image)

#     # Process the result
#     if result.gestures:
#         print("Detected gesture:", result.gestures[0].category_name)

#     # Display the frame
#     cv2.imshow('Hand Gesture Recognition', frame)

#     if cv2.waitKey(5) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


import os

def open_this_pc():
    os.system("explorer shell:MyComputerFolder")

open_this_pc()
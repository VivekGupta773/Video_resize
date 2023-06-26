import cv2

# Open the video file
video_path = "butterfly_flower_insect_nature_515.mp4"
cap = cv2.VideoCapture(video_path)

# Create a VideoWriter object to save the resized video
output_path = "output_video"
output = cv2.VideoWriter(output_path, 0, 1, (0, 0))

# Process each frame of the video
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Resize the frame to 50% of its original size
        resized_frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

        # Write the resized frame to the output video
        output.write(resized_frame)

        # Display the resized frame
        cv2.imshow("Resized Video", resized_frame)

        # Check for 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the resources
cap.release()
output.release()
cv2.destroyAllWindows()

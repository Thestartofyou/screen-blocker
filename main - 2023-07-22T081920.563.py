import cv2

def block_camera():
    camera = cv2.VideoCapture(0)  # Open the default camera (0)

    while True:
        ret, frame = camera.read()  # Read a frame from the camera

        # Create a blue screen image (blue color: BGR format)
        blue_screen = frame.copy()
        blue_screen[:, :, :] = (255, 0, 0)

        cv2.imshow("Blocked Camera", blue_screen)

        # Wait for a key press; press any key to exit
        if cv2.waitKey(1) != -1:
            break

    camera.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    block_camera()



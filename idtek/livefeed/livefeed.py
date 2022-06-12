import cv2 as cv


def open_camera():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        # Display the resulting frame
        cv.imshow("IdTek", frame)
        if cv.waitKey(1) == ord("q"):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


def main():

    open_camera()


if __name__ == "__main__":
    main()

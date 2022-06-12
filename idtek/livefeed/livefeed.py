import cv2

face_cascade = cv2.CascadeClassifier(
    "./idtek/livefeed/haarscascades/haarcascade_frontalface_default.xml"
)


def detect_face(img):

    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (0, 255, 0), 5)

    return face_img


def open_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        frame = detect_face(frame)
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        # Display the resulting frame
        cv2.imshow("IdTek", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def main():

    open_camera()


if __name__ == "__main__":
    main()

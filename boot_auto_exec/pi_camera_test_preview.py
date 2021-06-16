import cv2
import time
from threading import Thread

def VideoTest():
    time.sleep(5)
    
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, img = cap.read()
        if ret:
            cv2.imshow("preview!!!", img)
        if cv2.waitKey(1) & 0xFF == 27: # ESC 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    thread = Thread(target=VideoTest)
    thread.start()
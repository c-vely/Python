import cv2

# 영상스트리밍 서비스인 MJPG-streamer를 쓰고 있기 때문에 URL로 접속한다.
cap = cv2.VideoCapture('http://127.0.0.1:8090/?action=stream')

# MJPG-streamer에서 비디오 디바이스인 /dev/video0를 쓰고 있기 때문에 아래 코드로는
# 동작하지 않으나 별도 서비스가 동작중이지 않을때는 cv2.VideoCapture(0) 를 쓴다.
# cap = cv2.VideoCapture(0)

while cap.isOpened:
    ret, frame = cap.read()
    cv2.imshow("example Video. (press 'q' to Quit)", frame)
    # 30프레임 만들기 위해 한 프레임 처리 후 33ms 대기한다.
    # 대기하는 동안 읽은 key는 key 변수에 저장한다.
    key = cv2.waitKey(33)  # <--  시간조절 가능
    # key 값이 q가 들어오면 종료한다.
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# v1.5.4_fix1
import cv2
import math
import threading
import queue
import os
import time
import numpy as np
import datetime
import glob
import traceback
import platform
import urllib.request

# 전처리 FLAG
class Augmentation_Option:
    PADDING = 1
    HORIZONTAL_FLIP = 2
    VERTICAL_FLIP = 3
    GAUSSIAN_BLUR = 4
    GRAY_SCALE = 5

# 카메라 interface 클래스
class PyCamera:
    camera = None
    
    # 전처리 사용 여부
    USE_PADDING = False
    USE_HORIZONTAL_FLIP = False
    USE_VERTICAL_FLIP = False
    USE_GAUSSIAN_BLUR = False
    USE_GRAY_SCALE = False
    USE_DSHOW_OPTION = False

    def __init__(self):
        raise Exception("PyCamera 클래스는 interface 클래스이므로 인스턴트 생성을 지원하지 않습니다.")

    # 카메라로부터 영상을 1 프레임 읽어들임
    def get_frame(self):
        ret, frame = self.camera.read()
        if(ret == False or frame is None):
            print("카메라와 연결이 종료되었습니다. None 값 반환됨.")
            return frame

        # 만약 option으로 PADDING 지정 시, 이미지를 1:1 비율에 맞게 Padding을 넣고 리턴함
        if(self.USE_PADDING == True):
            frame = addPadding(frame, color=(0, 0, 0))
        if(self.USE_HORIZONTAL_FLIP == True):
            frame = cv2.flip(frame, 1)
        if(self.USE_VERTICAL_FLIP == True):
            frame = cv2.flip(frame, 0)
        if(self.USE_GAUSSIAN_BLUR == True):
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
        if(self.USE_GRAY_SCALE == True):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        return frame

    # 카메라 옵션 설정
    def set_option(self, option=None, status=True):
        if(option == Augmentation_Option.PADDING):
            self.USE_PADDING = status
        elif(option == Augmentation_Option.HORIZONTAL_FLIP):
            self.USE_HORIZONTAL_FLIP = status
        elif(option == Augmentation_Option.VERTICAL_FLIP):
            self.USE_VERTICAL_FLIP = status
        elif(option == Augmentation_Option.GAUSSIAN_BLUR):
            self.USE_GAUSSIAN_BLUR = status
        elif(option == Augmentation_Option.GRAY_SCALE):
            self.USE_GRAY_SCALE = status

        return
    
    # 카메라가 열려있는 지 여부
    def isOpened(self):
        return self.camera.isOpened()

    # 카메라 자원 할당 해제
    def dispose(self):
        self.camera.release()

# USB 카메라로부터 프레임을 가져오는 클래스 (GStreamer 미테스트)
class USBCamera(PyCamera):
    # camera_index : 카메라 포트 번호
    # width : 카메라 영상 너비 설정
    # height : 카메라 영상 높이 설정
    # DSHOW_OPTION : 카메라로부터 캡처 시 사용할 백엔드를 지정
    def __init__(self, camera_index=None, camera_width=None, camera_height=None, DSHOW_OPTION=False):
        if(camera_index == None):
            raise Exception("Camera 번호가 지정되지 않았습니다.")

        self.camera_index = camera_index
        self.USE_DSHOW_OPTION = DSHOW_OPTION

        # OpenCV 버전 확인
        cv2_version_info = (cv2.__version__).split('.')
        (major_ver, minor_ver, subminor_ver) = [int(i) for i in cv2_version_info]

        # cv2.CAP_DSHOW 옵션 사용 여부
        cv2_index = int(camera_index) + cv2.CAP_DSHOW if DSHOW_OPTION else int(camera_index)
        
        # OpenCV 3.4.3 이하는 VideoCapture에서 두 개 이상의 인자를 지정하지 못함 (apipreference를 지원하지 않음)
        # Jetson에서 apt-get으로 opencv를 설치하면 3.2.0 버전이 설치된다.
        if(major_ver <= 3 and minor_ver <= 4 and subminor_ver <= 3):
            self.camera = cv2.VideoCapture(cv2_index + (cv2.CAP_ANY if platform.system() != "Linux" else cv2.CAP_V4L2))
        else:
            self.camera = cv2.VideoCapture(cv2_index, cv2.CAP_ANY if platform.system() != "Linux" else cv2.CAP_V4L2)

        # 명시적으로 너비 혹은 높이를 지정했을 때 아래와 같이 수동으로 카메라 설정을 조작
        if(camera_width is not None):
            self.camera.set(3, camera_width)
        if(camera_height is not None):
            self.camera.set(4, camera_height)

        self.camera_width = self.camera.get(3)
        self.camera_height = self.camera.get(4)
        
        # 카메라의 정보 출력
        self.printCameraInformation()

    def printCameraInformation(self):
        # 카메라 유효값 체크
        if(not self.camera.isOpened()):
            print("Camera 연결이 종료되어 정보를 가져올 수 없습니다.")
            return
        
        # 카메라 정보 출력
        print("카메라 정보  : ")
        if(self.USE_DSHOW_OPTION):
            print("Camera Index : {0}".format(int(self.camera_index) + cv2.CAP_DSHOW))
        else:
            print("Camera Index : {0}".format(int(self.camera_index)))

        print("Camera Width : {0}".format(self.camera.get(3)))
        print("Camera Height : {0}".format(self.camera.get(4)))
        print("DSHOW_OPTION : {0}".format(self.USE_DSHOW_OPTION))

# 영상 파일로부터 프레임을 가져오는 클래스
class VideoCamera(PyCamera):
    # video_file : 영상 파일 이름
    def __init__(self, video_file=None, loop=False):
        if(video_file == None):
            raise Exception("영상 파일이 지정되지 않았습니다.")

        self.video_file = video_file
        self.camera = cv2.VideoCapture(self.video_file)

        self.camera_width = self.camera.get(3)
        self.camera_height = self.camera.get(4)

        # 카메라의 정보 출력
        self.printCameraInformation()

        self.loop = loop

    # 카메라로부터 영상을 1 프레임 읽어들임
    def get_frame(self):
        ret, frame = self.camera.read()
        if(ret == False or frame is None):
            if(self.loop):
                print("비디오 영상이 종료되었으므로 다시 재생합니다.")
                self.camera.release()
                self.camera = cv2.VideoCapture(self.video_file)
                ret, frame = self.camera.read()
            else:
                print("비디오 영상이 종료되었습니다.")
                return frame

        # 만약 option으로 PADDING 지정 시, 이미지를 1:1 비율에 맞게 Padding을 넣고 리턴함
        if(self.USE_PADDING == True):
            frame = addPadding(frame, color=(0, 0, 0))
        if(self.USE_HORIZONTAL_FLIP == True):
            frame = cv2.flip(frame, 1)
        if(self.USE_VERTICAL_FLIP == True):
            frame = cv2.flip(frame, 0)
        if(self.USE_GAUSSIAN_BLUR == True):
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
        if(self.USE_GRAY_SCALE == True):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        return frame
        
    def printCameraInformation(self):
        # 카메라 유효값 체크
        if(not self.camera.isOpened()):
            print("영상이 종료되어 정보를 가져올 수 없습니다.")
            return
        
        # 카메라 정보 출력
        print("영상 파일 정보 : ")
        print("Video File Name : {0}".format(self.video_file))
        print("Video Width : {0}".format(self.camera.get(3)))
        print("Video Height : {0}".format(self.camera.get(4)))

# 주소 형식(tcp, http 등)으로부터 프레임을 가져오는 클래스
class URLCamera(PyCamera):
    # camera_url : 카메라 주소
    def __init__(self, camera_url=None, live_thread=True):
        if(camera_url == None):
            raise Exception("Camera 주소가 지정되지 않았습니다.")

        self.camera_url = camera_url
        self.live_thread = live_thread

        # # 읽어들인 이미지를 저장할 Queue
        # self.frame_queue = queue.Queue()

        self.camera = cv2.VideoCapture(camera_url)
        self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.camera_width = self.camera.get(3)
        self.camera_height = self.camera.get(4)
        self.frame = self.camera.read()[1]

        # URL로부터 이미지를 읽어들일 경우 (영상 지연 문제로 쓰레드를 별도로 만들어 아래와 같이 비동기로 읽어들임)
        if(self.live_thread):
            self.is_run = True
            self.read_thread = threading.Thread(target=self._reader)
            self.read_thread.daemon = True
            self.read_thread.start()

        # 카메라의 정보 출력
        self.printCameraInformation()
    
    # while문 안에서 이미지를 계속 읽어들임
    def _reader(self):
        while(self.is_run):
            ret, self.frame = self.camera.read()
            if(self.frame is None):
                break
            # if not self.frame_queue.empty():
            #     try:
            #         self.frame_queue.get_nowait()
            #     except queue.Empty:
            #         pass
            # self.frame_queue.put(frame) 
            time.sleep(0.001)
        self.is_run = False

    # 카메라로부터 영상을 1 프레임 읽어들임 (_reader 함수로 인하여 아래와 같이 함수 재정의)
    def get_frame(self):
        if(self.live_thread):
            if(self.is_run == True and self.read_thread.is_alive()):
                # frame = self.frame_queue.get()
                frame = self.frame
            else:
                print("카메라와 연결이 종료되었습니다. None 값 반환됨.")
                frame = None
                return frame
        else:
            ret, frame = self.camera.read()
            if(ret == False or frame is None):
                print("카메라와 연결이 종료되었습니다. None 값 반환됨.")
                return frame
        
        # 만약 option으로 PADDING 지정 시, 이미지를 1:1 비율에 맞게 Padding을 넣고 리턴함
        if(self.USE_PADDING == True):
            frame = addPadding(frame, color=(0, 0, 0))
        if(self.USE_HORIZONTAL_FLIP == True):
            frame = cv2.flip(frame, 1)
        if(self.USE_VERTICAL_FLIP == True):
            frame = cv2.flip(frame, 0)
        if(self.USE_GAUSSIAN_BLUR == True):
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
        if(self.USE_GRAY_SCALE == True):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        return frame

    def printCameraInformation(self):
        # 카메라 유효값 체크
        if(not self.camera.isOpened()):
            print("Camera 연결이 종료되어 정보를 가져올 수 없습니다.")
            return
        
        # 카메라 정보 출력
        print("카메라 정보  : ")
        print("Camera Address : {0}".format(self.camera_url))
        print("Camera Width : {0}".format(self.camera.get(3)))
        print("Camera Height : {0}".format(self.camera.get(4)))
    
        # 카메라 자원 할당 해제
    def dispose(self):
        self.is_run = False
        while(self.read_thread is not None and self.read_thread.is_alive()):
            time.sleep(1)
            
        self.camera.release()
        self.read_thread = None
    
# CSI 카메라 (GStreamer 미테스트)
class CSICamera(PyCamera):
    # camera_index : 카메라 포트 번호
    # width : 카메라 영상 너비 설정
    # height : 카메라 영상 높이 설정
    # DSHOW_OPTION : 카메라로부터 캡처 시 사용할 백엔드를 지정
    def __init__(self, camera_index=None, camera_width=None, height=None, DSHOW_OPTION=False):
        if(camera_index == None):
            raise Exception("Camera 번호가 지정되지 않았습니다.")
            
        self.camera_index = camera_index
        self.DSHOW_OPTION = DSHOW_OPTION

        # cv2.CAP_DSHOW 옵션 사용 여부
        if(DSHOW_OPTION):
            self.camera = cv2.VideoCapture(int(camera_index) + cv2.CAP_DSHOW, cv2.CAP_ANY if platform.system() != "Linux" else cv2.CAP_V4L2)
        else:
            self.camera = cv2.VideoCapture(int(camera_index), cv2.CAP_ANY if platform.system() != "Linux" else cv2.CAP_V4L2)

        # 명시적으로 너비 혹은 높이를 지정했을 때 아래와 같이 수동으로 카메라 설정을 조작
        if(camera_width is not None):
            self.camera.set(3, camera_width)
        if(camera_height is not None):
            self.camera.set(4, camera_height)

        self.camera_width = self.camera.get(3)
        self.camera_height = self.camera.get(4)
        
        # 카메라의 정보 출력
        self.printCameraInformation()

    def printCameraInformation(self):
        # 카메라 유효값 체크
        if(not self.camera.isOpened()):
            print("Camera 연결이 종료되어 정보를 가져올 수 없습니다.")
            return
        
        # 카메라 정보 출력
        print("카메라 정보  : ")
        if(self.USE_DSHOW_OPTION):
            print("Camera Index : {0}".format(int(self.camera_index) + cv2.CAP_DSHOW))
        else:
            print("Camera Index : {0}".format(int(self.camera_index)))

        print("Camera Width : {0}".format(self.camera.get(3)))
        print("Camera Height : {0}".format(self.camera.get(4)))
        print("DSHOW_OPTION : {0}".format(self.USE_DSHOW_OPTION))

# def _gst_str(self):
#     return 'v4l2src device=/dev/video{} ! video/x-raw, width=(int){}, height=(int){}, framerate=(fraction){}/1 ! videoconvert !  video/x-raw, format=(string)BGR ! appsink'.format(self.capture_device, self.capture_width, self.capture_height, self.capture_fps)

# def _gst_str(self, camera_index, width, height, fps):
#     return 'nvarguscamerasrc sensor-id=%d ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (
#             self.capture_device, self.capture_width, self.capture_height, self.capture_fps, self.width, self.height)


# 폴더 내 이미지를 읽어오는 클래스
class ImagesReader(PyCamera):
    # camera_url : 카메라 주소
    def __init__(self, image_dir=None, ext=["png", "jpg", "gif"]):
        if(image_dir == None):
            raise Exception("이미지가 저장된 폴더가 지정되지 않았습니다.")
        if(not os.path.isdir(image_dir)):
            raise Exception("해당 폴더는 존재하지 않는 경로입니다.")

        self.image_dir = image_dir
        self.image_ext = ext
        self.image_list = []
        self.image_index = 0

        # 이미지 파일 목록을 가져온다.
        for e in ext:
            self.image_list += glob.glob(self.image_dir + '/*.' + e)
        
        # 이미지의 총 개수
        self.image_count = len(self.image_list)

        # 폴더의 정보 출력
        self.printCameraInformation()

    # 이미지 1개를 가져옴 (파일명도 같이 반환)
    def get_frame(self):
        while(True):
            # 더 이상 검색할 이미지가 없을 때 None 값 반환
            if(self.image_count == 0 or self.image_index >= self.image_count):
                print("검색할 이미지가 더 이상 없습니다.")
                return (None, None)

            # 검색할 이미지의 경로
            image_file_path = self.image_list[self.image_index]

            # 해당 이미지가 존재하지 않는 경우 무시하고 다음 이미지를 검색함
            if(not os.path.isfile(image_file_path)):
                self.image_index += 1
                continue

            frame = imread(image_file_path)
            
            # 만약 option으로 PADDING 지정 시, 이미지를 1:1 비율에 맞게 Padding을 넣고 리턴함
            if(self.USE_PADDING == True):
                frame = addPadding(frame, color=(0, 0, 0))
            if(self.USE_HORIZONTAL_FLIP == True):
                frame = cv2.flip(frame, 1)
            if(self.USE_VERTICAL_FLIP == True):
                frame = cv2.flip(frame, 0)
            if(self.USE_GAUSSIAN_BLUR == True):
                frame = cv2.GaussianBlur(frame, (5, 5), 0)
            if(self.USE_GRAY_SCALE == True):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            
            self.image_index += 1

            return ([image_file_path, frame.shape[1], frame.shape[0]], frame)
    
    # 폴더 내 이미지를 재검색합니다. (index는 0으로 초기화됩니다.)
    def refreshSearch(self):
        self.image_list = []
        self.image_index = 0

        # 이미지 파일 목록을 가져온다.
        for e in self.image_ext:
            self.image_list += glob.glob(self.image_dir + '/*.' + e)
        
        # 이미지의 총 개수
        self.image_count = len(self.image_list)

        # 폴더의 정보 출력
        self.printCameraInformation()

    def printCameraInformation(self):
        # 폴더 정보 출력
        print("폴더 정보  : ")
        print("Directory Path : {0}".format(self.image_dir))
        print("Image Count : {0}".format(self.image_count))
    
    # 폴더 정보 초기화
    def dispose(self):
        self.image_list = []
        self.image_count = 0


class Camera_Recorder():
    recordStarted = False
    frame_rate = 30
    saveVideoDir = None

    # camera : 카메라 클래스
    # fps : 카메라 영상으로부터 프레임을 추출할 때 지정
    # save_path : 추출한 프레임을 저장할 위치
    def __init__(self, camera, frame_rate=30, save_dir=None):
        self.current_class = camera.__class__
        self.base_class = camera.__class__.__base__
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.camera = camera
        self.frame_rate = frame_rate

        # 해당 Camera 클래스가 PyCamera 클래스를 상속 받는 지 확인
        if(self.base_class == None or self.base_class.__name__ != "PyCamera"):
            raise Exception("잘못된 PyCamera 형식입니다.")
        if(self.current_class.__name__ == "ImagesReader"):
            raise Exception("ImagesReader 클래스는 Camera_Recorder 인스턴스를 생성할 수 없습니다.")

        if(save_dir == None):
            save_dir = "./record"
        self.save_dir = save_dir

        if(not os.path.isdir(save_dir)):
            os.mkdir(save_dir)
        
    def setFrameRate(self, frame_rate):
        self.frame_rate = frame_rate
    
    def start(self):
        if(self.recordStarted):
            return
        file_name =  str(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S_video.avi"))
        save_file_name = os.path.join(self.save_dir, file_name)
        videoWriter = cv2.VideoWriter(save_file_name, self.fourcc, self.frame_rate, (int(self.camera.camera_width), int(self.camera.camera_height)))
        self.recordStarted = True

        while(self.recordStarted):
            frame = self.camera.get_frame()
            if(frame is None):
                break
            videoWriter.write(frame)

            cv2.imshow("Video Recorder", frame)
            waitKey = cv2.waitKey(1)
            if waitKey == ord('q'):
                break
        
        videoWriter.release()
        cv2.destroyAllWindows()
        self.recordStarted = False

    def start_async(self):
        if(self.recordStarted):
            print("이미 프레임을 추출하고 있습니다.")

        self.extract_thread = threading.Thread(target=self.start)
        self.extract_thread.daemon = True
        self.extract_thread.start()
    
    def stop_async(self):
        self.recordStarted = False
        self.extract_thread = None



# 카메라 영상으로부터 프레임 추출하기
class Camera_Frame_Extractor():
    frame_unit_sec = None
    save_index = 0
    save_path = None
    is_run_extract = False
    extract_thread = None

    # camera : 카메라 클래스
    # fps : 카메라 영상으로부터 프레임을 추출할 때 지정
    # save_path : 추출한 프레임을 저장할 위치
    def __init__(self, camera, frame_unit_sec=0.2, save_path=None):
        self.current_class = camera.__class__
        self.base_class = camera.__class__.__base__

        # 해당 Camera 클래스가 PyCamera 클래스를 상속 받는 지 확인
        if(self.base_class == None or self.base_class.__name__ != "PyCamera"):
            raise Exception("잘못된 PyCamera 형식입니다.")
        if(self.current_class.__name__ == "ImagesReader"):
            raise Exception("ImagesReader 클래스는 Camera_Recorder 인스턴스를 생성할 수 없습니다.")

        self.camera = camera
        self.frame_unit_sec = frame_unit_sec
        self.save_path = save_path
        self.current_time = datetime.datetime.now()
    
    # 몇 초(second)마다 Frame을 가져올 지 설정합니다.
    def setUnitsSecond(self, frame_unit_sec):
        self.frame_unit_sec = frame_unit_sec
    
    # Frame을 저장할 경로를 지정합니다.
    def setSavePath(self, save_path):
        self.save_path = save_path
    
    # Frame 저장 (클래스 내부에서 처리)
    def save_frame(self, frame):
        file_name = str(self.current_time.strftime("%Y-%m-%d_%H%M%S_{0:08d}.jpg".format(self.save_index)))
        
        imwrite(os.path.join(self.save_path, file_name), frame)
        self.save_index += 1

    # 프레임 추출 시작
    # max_save : 추출할 최대 프레임 개수 (0일 경우 무한 반복)
    def start(self, max_save=100, display=False):
        self.is_run_extract = True

        if(self.save_path == None):
            print("추출된 프레임을 저장할 경로가 지정되지 않았습니다.")
            return
        if(not os.path.isdir(self.save_path)):
            os.makedirs(self.save_path)
            print("추출된 프레임을 저장할 경로가 지정되지 않아 폴더를 새로 생성하였습니다.")
        
        self.save_index = 0
        self.current_time = datetime.datetime.now()

        if(self.camera.__class__.__name__ == "VideoCamera"):
            # 초당 프레임 가져오기
            fps = self.camera.camera.get(cv2.CAP_PROP_FPS) # Gets the frames per second
            multiplier = fps * self.frame_unit_sec
            # 동영상이 끝날 때까지 프레임 추출을 반복
            while((self.save_index < max_save or max_save == 0) and self.is_run_extract):
                frameId = int(round(self.camera.camera.get(1))) #current frame number
                frame = self.camera.get_frame()
                if frame is None:
                    break
                if frameId % multiplier < 1:
                    # 프레임 저장
                    frame = self.camera.get_frame()
                    self.save_frame(frame)
                if(display):
                    cv2.imshow("test", frame)
                    cv2.waitKey(1)
        else:
            check_time = 0
            while((self.save_index < max_save or max_save == 0) and self.is_run_extract):
                if(time.time() - check_time > self.frame_unit_sec):
                    check_time = time.time()
                    frame = self.camera.get_frame()
                    # 프레임 저장
                    self.save_frame(frame)
                if(display):
                    cv2.imshow("test", frame)
                    cv2.waitKey(1)
        
        print("프레임 추출이 종료되었습니다.")
        print("총 프레임 수 : {0}장".format(self.save_index))
        
        cv2.destroyAllWindows()
        self.is_run_extract = False
    
    # 비동기로 프레임 추출 시작
    # max_save : 추출할 최대 프레임 개수 (0일 경우 무한 반복)
    def start_async(self, max_save=100):
        if(self.is_run_extract):
            print("이미 프레임을 추출하고 있습니다.")
        # 지연 문제 방지를 위해 이미지 읽기는 별도의 쓰레드에서 돌아가도록 설정함
        self.extract_thread = threading.Thread(target=self.start, args=(max_save,))
        self.extract_thread.daemon = True
        self.extract_thread.start()
    
    # 프레임 추출 종료 (비동기일 경우 사용)
    # max_save : 추출할 최대 프레임 개수 (0일 경우 무한 반복)
    def stop_async(self, max_save=100):
        self.is_run_extract = False
        self.extract_thread = None


# 이미지를 1:1 비율에 맞게 Padding을 넣음
def addPadding(frame, color=(0, 0, 0)):
    original_height, original_width, channel = frame.shape
    borderType = cv2.BORDER_CONSTANT
    background_color = color

    if(original_height > original_width):
        left = math.ceil((original_height - original_width) / 2)
        right = math.floor((original_height - original_width) / 2)
        top, bottom = (0, 0)
    elif(original_height < original_width):
        top = math.ceil((original_width - original_height) / 2)
        bottom = math.floor((original_width - original_height) / 2)
        left, right = (0, 0)

    frame = cv2.copyMakeBorder(frame, top, bottom, left, right, borderType, None, background_color)
    return frame

# OpenCV2 이미지 읽기(Read)/쓰기(Write) - 한글 경로에 있는 것도 읽어들일 수 있음
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        traceback.print_exc()
        print("imread {0} : ".format(e))
        return None

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        traceback.print_exc()
        print("imwrite {0} : ".format(e))
        return False

def imread_url(url, dtype=np.uint8):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=dtype)
    img = cv2.imdecode(arr, -1)
    # 뒤의 Alpha는 지원하지 않도록 함 (다른 API간 호환성 대비)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img
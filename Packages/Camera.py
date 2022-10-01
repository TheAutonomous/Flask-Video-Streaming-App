from threading import Thread
import cv2, time, base64

class WebCamAPI():
    CurrentFrame = ""
    
    def BackgroundProcess(self):
        CurCamera = cv2.VideoCapture(0)
        while (CurCamera.isOpened()):
            _, Arr = cv2.imencode(".png", CurCamera.read())
            self.CurrentFrame = base64.b64encode(Arr.tobytes())
            print(self.CurrentFrame)
        CurCamera.release()
        cv2.destroyAllWindows()
        
    def RunLoop(self):
        Thread(target=self.BackgroundProcess).start()

WebCamAPI = WebCamAPI()
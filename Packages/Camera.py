from threading import Thread
from PIL import Image
from io import BytesIO
import cv2, time, base64

class WebCamAPI():
    CurrentFrame = ""
    
    def BackgroundProcess(self):
        CurCamera = cv2.VideoCapture(0)
        while (CurCamera.isOpened()):
            Start = time.perf_counter()
            NImg = Image.fromarray(CurCamera.read()[1])
            Buffer = BytesIO()
            NImg.save(Buffer, format="JPEG")
            self.CurrentFrame = base64.b64encode(Buffer)
            print("Finished Frame In " + str(time.perf_counter()-Start) + "ms")
            time.sleep(0.03)
        CurCamera.release()
        cv2.destroyAllWindows()
        
    def RunLoop(self):
        Thread(target=self.BackgroundProcess).start()

WebCamAPI = WebCamAPI()

if __name__ == '__main__':
    WebCamAPI.RunLoop()
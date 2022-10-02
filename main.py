from Packages.FlaskBase import FlaskInitialize
import os, socket

########### Requirements ###########
#         pip install flask        #
#  pip install "uvicorn[standard]" #
#     pip install opencv-python    #
####################################

if __name__ == '__main__':
    FlaskAPP = FlaskInitialize().Setup()
    FlaskAPP.run(host=str(socket.gethostbyname(socket.gethostname())), port="8080")
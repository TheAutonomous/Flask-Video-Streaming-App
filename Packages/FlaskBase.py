from flask import Flask, request, jsonify, render_template, send_from_directory
from .Camera import WebCamAPI

class FlaskInitialize():
    def Setup(self):
        FlaskAPP = Flask(__name__, static_url_path="/", static_folder="../WebFiles")
        
        @FlaskAPP.route("/", methods=["GET"])
        def index():
            return FlaskAPP.send_static_file('index.html')
        
        @FlaskAPP.route("/camera", methods=["GET"])
        def cam():
            return WebCamAPI.CurrentFrame
        
        WebCamAPI.RunLoop()
        return FlaskAPP
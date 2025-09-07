from flask import Flask, render_template, jsonify, Response
import json
import time
import cv2
app = Flask(__name__)
compartido = None  # Será asignado desde main.py
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos')
def data():
    try:
        with open("resources/datos_para_reporte.json") as f:
            stats = json.load(f)
    except FileNotFoundError:
        stats = {"cuadrante1":0,"cuadrante2":0,"cuadrante3":0,"cuadrante4":0}
    return jsonify(stats)

def gen_frames():
    while True:
        frame = cv2.imread("web_app/resources/frame.jpg")
        if frame is not None:
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        time.sleep(5)  # Leer un nuevo frame cada 5 segundos

@app.route('/fuente_video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == "__main__":
    app.run(debug=True)

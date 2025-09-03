from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detectar_vehiculos(frame):
    resultados = model(frame)
    return resultados

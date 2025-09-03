import cv2
from deteccion import detectar_vehiculos
from analisis import analizar_cuadrantes
from visualizacion import dibujar_gui, imprimir_alertas, guardar_reporte

video_path = "assets/video_facebook.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    resultados = detectar_vehiculos(frame)
    cant_por_cuadrantes = analizar_cuadrantes(resultados,503,370)

    total_vehiculos = sum(cant_por_cuadrantes.values())
    print(f"Vehículos detectados: {total_vehiculos} | {cant_por_cuadrantes}")
    imprimir_alertas(cant_por_cuadrantes)
    guardar_reporte(cant_por_cuadrantes)
    gui = dibujar_gui(frame, resultados,503,370)
    cv2.imshow("Vehiculos detectados por cuadrante", gui)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

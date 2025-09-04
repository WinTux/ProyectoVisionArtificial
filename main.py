import cv2
import time
from deteccion import detectar_vehiculos
from analisis import analizar_cuadrantes
from visualizacion import dibujar_gui, imprimir_alertas, guardar_reporte

video_path = "assets/video_facebook.mp4"
cap = cv2.VideoCapture(video_path)
lista_fps = []  # Lista para guardar los FPS (métrica)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    tiempo_inicio = time.time()
    frame = cv2.resize(frame, (640, 480))
    resultados = detectar_vehiculos(frame)
    cant_por_cuadrantes = analizar_cuadrantes(resultados,503,370)
    tiempo_final = time.time()
    fps = 1 / (tiempo_final - tiempo_inicio + 1e-6)  # Cálculo de FPS
    lista_fps.append(fps)
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
# FPS promedio
if lista_fps:
    fps_promedio = sum(lista_fps) / len(lista_fps)
    print(f"\nPS Promedio: {fps_promedio:.2f}")
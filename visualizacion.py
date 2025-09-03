import cv2

def dibujar_gui(frame, resultados, ancho_usable=540, alto_usable=380):
    media_ancho = ancho_usable // 2
    media_alto = alto_usable // 2

    resultado_f = resultados[0].plot()
    cv2.line(resultado_f, (media_ancho, 0), (media_ancho, alto_usable), (0, 255, 255), 2)
    cv2.line(resultado_f, (0, media_alto), (ancho_usable, media_alto), (0, 255, 255), 2)
    cv2.rectangle(resultado_f, (0, 0), (ancho_usable, alto_usable), (0, 255, 0), 2)
    return resultado_f

def imprimir_alertas(cant_por_cuadrantes):
    for q, contador in cant_por_cuadrantes.items():
        if contador > 6:
            print(f"[ALERTA] Alto tráfico en cuadrante {q} con {contador} vehículos")

def guardar_reporte(cant_por_cuadrantes, filename="reportes/log.txt"):
    with open(filename, "a") as f:
        for q, c in cant_por_cuadrantes.items():
            f.write(f"{q}: {c} vehículos\n")
        f.write("-" * 30 + "\n")

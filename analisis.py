def analizar_cuadrantes(resultados, ancho_usable=540, alto_usable=380):
    media_ancho = ancho_usable // 2
    media_alto = alto_usable // 2

    cant_por_cuadrantes = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

    for r in resultados:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls not in [2, 3, 5, 7]:
                continue
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            centro_x = (x1 + x2) // 2
            centro_y = (y1 + y2) // 2

            if centro_x >= ancho_usable or centro_y >= alto_usable:
                continue

            if centro_x < media_ancho and centro_y < media_alto:
                cant_por_cuadrantes["Q1"] += 1
            elif centro_x >= media_ancho and centro_y < media_alto:
                cant_por_cuadrantes["Q2"] += 1
            elif centro_x < media_ancho and centro_y >= media_alto:
                cant_por_cuadrantes["Q3"] += 1
            else:
                cant_por_cuadrantes["Q4"] += 1

    return cant_por_cuadrantes

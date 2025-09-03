# Detección de Vehículos por Cuadrante con YOLOv8 + OpenCV

Este proyecto realiza detección y conteo de vehículos en un video, dividiendo el área útil en cuatro cuadrantes y mostrando alertas en caso de alto tráfico. La visualización es en tiempo real mediante OpenCV, y los reportes se pueden integrar con una interfaz web Flask (opcional).

---

## Requisitos de sistema (características con las que se ejecutó)

- Python 3.12.3
- pip (gestor de paquetes de Python)
- Virtualenv

---

## Estructura del Proyecto

```bash
ProyectoVisionArtificial/
│
├── main.py                    # Script principal: procesa video y muestra GUI
├── deteccion.py               # Lógica de detección con YOLOv8
├── analisis.py                # Lógica de análisis por cuadrantes
├── visualizacion.py           # Visualización de resultados y alertas
├── requirements.txt           # Lista de dependencias
├── assets/
│   └── video_facebook.mp4     # Video de entrada
├── reportes/
│   └── log.txt                # Reportes generados en texto
├── shared_data.json           # Reportes en formato JSON
├── web_app/                   # Interfaz HTML con Flask
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── script.js
└── README.md                  # Este archivo

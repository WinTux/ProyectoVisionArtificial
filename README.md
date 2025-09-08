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
│   └── resources/
│       └── datos_para_reporte.json # Se genera durante la ejecución
│       └── frame.jpg               # Se genera durante la ejecución
└── README.md                  # Este archivo
```

## Clonar el repositorio

```bash
cd /home/rusok/Documentos
git clone https://github.com/WinTux/ProyectoVisionArtificial.git
cd ProyectoVisionArtificial
```
### Crear y activar el entornno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```
### Instalar las dependencias necesarias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### Abrir el proyecto con Visual Studio Code
```bash
code .
```
### Seleccionar el intérprete del entorno virtual
```bash
Ctrl+Shift+P → Python: Select Interpreter → venv/bin/python
```
### Ejecutar el proyecto
En una primera consola:
```bash
python main.py
```
En una segunda consola:
```bash
python app.py
```
En un navegador nos dirigimos a http://localhost:5000
### Finalizar el entorno virtual
```bash
deactivate
```
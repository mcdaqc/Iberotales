# Iberotales

Proyecto de análisis y procesamiento de datos.

## Estructura del Proyecto

```
Iberotales/
├── data/                  # Directorio para todos los datos
│   ├── raw/              # Datos en bruto originales
│   ├── processed/        # Datos procesados/limpios
│   └── external/         # Datos externos de referencia
│
├── notebooks/            # Jupyter notebooks para análisis exploratorio
│
├── src/                  # Código fuente
│   ├── data/            # Scripts para procesamiento de datos
│   ├── features/        # Scripts para creación de features
│   ├── visualization/   # Scripts para visualizaciones
│   └── utils/           # Funciones de utilidad
│
├── tests/               # Tests unitarios
```

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/Iberotales.git
cd Iberotales
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Coloca tus datos en bruto en el directorio `data/raw/`
2. Utiliza los scripts en `src/data/` para procesar los datos
3. Los notebooks en `notebooks/` contienen análisis exploratorio
4. Los datos procesados se guardarán en `data/processed/`

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

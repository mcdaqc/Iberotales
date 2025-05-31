import json
import os
from pathlib import Path

def create_raw_image_structure(data_dir: str, raw_images_dir: str):
    """Create simple directory structure for raw images."""
    # Crear directorio de imágenes raw
    os.makedirs(raw_images_dir, exist_ok=True)
    
    # Procesar cada archivo JSON
    for file in os.listdir(data_dir):
        if file.endswith('.json'):
            country = file.replace('.json', '')
            print(f"✅ Preparado para imágenes de {country}")
            print(f"   Coloca las imágenes en: {raw_images_dir}")
            print(f"   Nombra las imágenes como: {country}_0_0.jpg, {country}_0_1.jpg, etc.")

def main():
    # Definir directorios
    raw_data_dir = 'data/raw'
    raw_images_dir = 'data/raw/images'
    
    print(f"\n{'='*50}")
    print("CREANDO ESTRUCTURA PARA IMÁGENES RAW")
    print(f"{'='*50}")
    
    # Crear estructura
    create_raw_image_structure(raw_data_dir, raw_images_dir)
    
    print(f"\n{'='*50}")
    print("PROCESO COMPLETADO")
    print(f"{'='*50}")
    print("\nEstructura de carpetas creada:")
    print("data/raw/images/")
    print("└── [aquí van todas las imágenes]")
    print("\nPara agregar imágenes:")
    print("1. Coloca todas las imágenes en data/raw/images/")
    print("2. Nombra las imágenes como [país]_[número]_[número].jpg")
    print("   Ejemplo: españa_0_0.jpg, españa_0_1.jpg, etc.")
    print("\nNota: Más adelante, cuando estés listo para procesar el dataset,")
    print("      las imágenes se organizarán en la estructura de Hugging Face")

if __name__ == "__main__":
    main() 
"""
Funciones de utilidad para el proyecto.
"""
import pandas as pd
import numpy as np
from typing import List, Union
from pathlib import Path

def create_directory(path: Union[str, Path]) -> None:
    """
    Crea un directorio si no existe.
    
    Args:
        path (Union[str, Path]): Ruta del directorio a crear
    """
    Path(path).mkdir(parents=True, exist_ok=True)

def save_dataframe(df: pd.DataFrame, 
                  filepath: Union[str, Path], 
                  file_format: str = 'csv') -> None:
    """
    Guarda un DataFrame en el formato especificado.
    
    Args:
        df (pd.DataFrame): DataFrame a guardar
        filepath (Union[str, Path]): Ruta donde guardar el archivo
        file_format (str): Formato del archivo ('csv' o 'excel')
    """
    if file_format == 'csv':
        df.to_csv(filepath, index=False)
    elif file_format == 'excel':
        df.to_excel(filepath, index=False)
    else:
        raise ValueError(f"Formato no soportado: {file_format}")

def load_dataframe(filepath: Union[str, Path], 
                  file_format: str = 'csv') -> pd.DataFrame:
    """
    Carga un DataFrame desde un archivo.
    
    Args:
        filepath (Union[str, Path]): Ruta del archivo a cargar
        file_format (str): Formato del archivo ('csv' o 'excel')
        
    Returns:
        pd.DataFrame: DataFrame cargado
    """
    if file_format == 'csv':
        return pd.read_csv(filepath)
    elif file_format == 'excel':
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Formato no soportado: {file_format}") 
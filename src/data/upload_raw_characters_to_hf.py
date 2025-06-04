import os
import json
import shutil
from pathlib import Path
from datasets import load_dataset

def main():
    raw_dir = Path("data/raw")
    image_dir = raw_dir / "images"
    characters_dir = Path("data/characters")
    train_dir = characters_dir / "train"
    train_dir.mkdir(parents=True, exist_ok=True)
    
    # Listas para almacenar las entradas
    metadata_entries = []  # Solo personajes con imágenes
    all_characters = []    # Todos los personajes
    
    # Copiar la imagen null.webp al directorio de train
    null_image = image_dir / "null.webp"
    if null_image.exists():
        shutil.copy2(str(null_image), str(train_dir / "null.webp"))
    else:
        print("⚠️ Advertencia: No se encontró null.webp en el directorio de imágenes")
    
    # Procesar cada archivo JSON
    json_files = [f for f in raw_dir.glob("*.json") if "images" not in str(f)]
    print(f"Procesando {len(json_files)} archivos JSON...")

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            characters = json.load(f)
            for character in characters:
                # Crear entrada base
                character_entry = {
                    "image": "null.webp",  # Imagen por defecto
                    "nombre": character['nombre'],
                    "pais": character['pais'],
                    "descripcion": character['descripcion'],
                    "historia": character['historia'],
                    "id": character['id'],
                    "url_fuentes": character['url_fuentes']
                }
                
                # Buscar imagen para este personaje
                for ext in ["jpg", "jpeg", "png", "webp"]:
                    pattern = f"{character['id']}_*.{ext}"
                    matches = list(image_dir.glob(pattern))
                    if matches:
                        image_path = matches[0]
                        # Copiar la imagen a data/characters/train/
                        new_image_path = train_dir / image_path.name
                        shutil.copy2(str(image_path), str(new_image_path))
                        
                        # Añadir a metadata solo si tiene imagen
                        metadata_entry = character_entry.copy()
                        metadata_entry["file_name"] = image_path.name
                        metadata_entries.append(metadata_entry)
                        break
                else:
                    # Si no se encontró imagen, añadir con null.webp
                    metadata_entry = character_entry.copy()
                    metadata_entry["file_name"] = "null.webp"
                    metadata_entries.append(metadata_entry)
                
                # Añadir a la lista de todos los personajes
                all_characters.append(character_entry)

    # Guardar metadata.jsonl (solo personajes con imágenes)
    with open(train_dir / "metadata.jsonl", "w", encoding="utf-8") as f:
        for entry in metadata_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    # Guardar todos los personajes en un JSON
    with open(characters_dir / "all_characters.json", "w", encoding="utf-8") as f:
        json.dump(all_characters, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Procesados {len(all_characters)} personajes en total")
    print(f"✅ {len(metadata_entries)} personajes en metadata")
    print(f"✅ Imágenes copiadas a {train_dir}")
    print(f"✅ Metadata guardada en {train_dir}/metadata.jsonl")
    print(f"✅ Todos los personajes guardados en {characters_dir}/all_characters.json")

    # Subir a HuggingFace
    print("\nSubiendo dataset a HuggingFace...")
    dataset = load_dataset("imagefolder", data_dir=str(characters_dir), split="train")
    dataset.push_to_hub("daqc/ibero-characters-es")
    print("✅ Dataset subido exitosamente!")

if __name__ == "__main__":
    main() 
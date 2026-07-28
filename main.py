from pathlib import Path
import time

downloads = Path.home() / "Downloads"

pastas = {
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    ".tiff": "Imagens",
    ".tif": "Imagens",
    ".webp": "Imagens",
    ".svg": "Imagens",
    ".ico": "Imagens",
    ".heic": "Imagens",
    ".heif": "Imagens",
    ".raw": "Imagens",
    ".cr2": "Imagens",
    ".nef": "Imagens",
    ".arw": "Imagens",
    ".dng": "Imagens",
    ".pdf": "Documentos",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".odt": "Documentos",
    ".rtf": "Documentos",
    ".txt": "Documentos",
    ".xls": "Documentos",
    ".xlsx": "Documentos",
    ".ods": "Documentos",
    ".csv": "Documentos",
    ".ppt": "Documentos",
    ".pptx": "Documentos",
    ".odp": "Documentos",
    ".epub": "Documentos",
    ".md": "Documentos",
    ".mp4": "Vídeos",
    ".mkv": "Vídeos",
    ".avi": "Vídeos",
    ".mov": "Vídeos",
    ".wmv": "Vídeos",
    ".flv": "Vídeos",
    ".webm": "Vídeos",
    ".mpeg": "Vídeos",
    ".mpg": "Vídeos",
    ".m4v": "Vídeos",
    ".3gp": "Vídeos",
    ".ts": "Vídeos",
    ".mp3": "Áudios",
    ".wav": "Áudios",
    ".flac": "Áudios",
    ".aac": "Áudios",
    ".ogg": "Áudios",
    ".wma": "Áudios",
    ".m4a": "Áudios",
    ".opus": "Áudios",
    ".aiff": "Áudios",
    ".mid": "Áudios",
    ".midi": "Áudios",
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",
    ".tar": "Compactados",
    ".gz": "Compactados",
    ".bz2": "Compactados",
    ".xz": "Compactados",
    ".tgz": "Compactados",
    ".exe": "Executáveis",
    ".msi": "Executáveis",
    ".bat": "Executáveis",
    ".cmd": "Executáveis",
    ".com": "Executáveis",
    ".ps1": "Executáveis",
    ".iso": "Imagem de Disco",
    ".img": "Imagem de Disco",
    ".bin": "Imagem de Disco",
    ".cue": "Imagem de Disco",
}

print("Organizando Arquivos...")
time.sleep(1)

for item in downloads.iterdir(): 

  if item.is_file():
    categoria = pastas.get(item.suffix, 'Outros')
    caminho_categoria = downloads / categoria

    print(f"✔ {item.name} → {categoria}")
    time.sleep(0.3)

    if not caminho_categoria.is_dir():
      caminho_categoria.mkdir()

    caminho_final = caminho_categoria / item.name

    item.rename(caminho_final)
from pathlib import Path
import time

downloads = Path.home() / "Downloads"

def identificar_categoria(extensao):
  return pastas.get(extensao, 'Outros')

def criar_pastas(caminho_categoria):
  if not caminho_categoria.is_dir():
        caminho_categoria.mkdir()

def encontrar_nome_novo(caminho_final):
  contador = 1

  while True:
    nome_novo = (f"{caminho_final.stem}({contador}){caminho_final.suffix}")
    caminho_novo = caminho_final.parent / nome_novo

    if caminho_novo.exists():
      contador += 1
    else:
       return caminho_novo

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
    categoria = identificar_categoria(item.suffix)
    caminho_categoria = downloads / categoria

    print(f"✔ {item.name} → {categoria}")
    time.sleep(0.3)

    criar_pastas(caminho_categoria)

    caminho_final = caminho_categoria / item.name

    if caminho_final.exists():
       caminho_final = encontrar_nome_novo(caminho_final)
    item.rename(caminho_final)
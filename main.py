from pathlib import Path
from funcoes.funcoes import (
  identificar_categoria,
  criar_pastas,
  encontrar_nome_novo
)
import time

downloads = Path.home() / "Downloads"

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
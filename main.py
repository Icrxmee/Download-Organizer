import time
from pathlib import Path
from funcoes.funcoes import (
  organiza_arquivo
)

print("Organizando Arquivos...")
time.sleep(1)

downloads = Path.home() / "Downloads"

for item in downloads.iterdir(): 

  if item.is_file():
    organiza_arquivo(item, downloads)
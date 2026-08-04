import time
from pathlib import Path
from funcoes.funcoes import (
  organizar_downloads
)

print("Organizando Arquivos...")
time.sleep(1)

downloads = Path.home() / "Downloads"

organizar_downloads(downloads)
from categorias import pastas
import time

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

def organiza_arquivo(item, downloads):
  categoria = identificar_categoria(item.suffix)
  caminho_categoria = downloads / categoria
   
  print(f"✔ {item.name} → {categoria}")
  time.sleep(0.3)
   
  criar_pastas(caminho_categoria)
   
  caminho_final = caminho_categoria / item.name
   
  if caminho_final.exists():
    caminho_final = encontrar_nome_novo(caminho_final)

  item.rename(caminho_final)
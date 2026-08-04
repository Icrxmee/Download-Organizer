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

def organizar_downloads(downloads):
  arquivos_organizados = 0
  arquivos_com_erro = 0

  for item in downloads.iterdir(): 

    if item.is_file():

      if organiza_arquivo(item, downloads):
        arquivos_organizados += 1
      else:
        arquivos_com_erro += 1

  print()
  print("-" * 20)
  print("Organização Concluída!")
  print(f"Arquivos Organizados: {arquivos_organizados}")
  print(f"Arquivos com Erros: {arquivos_com_erro}")
  print("-" * 20)
  time.sleep(60)

def organiza_arquivo(item, downloads):
  try:

    categoria = identificar_categoria(item.suffix.lower())
    caminho_categoria = downloads / categoria
    
    print(f"✔ {item.name} → {categoria}")
    time.sleep(0.3)
    
    criar_pastas(caminho_categoria)
    
    caminho_final = caminho_categoria / item.name
    
    if caminho_final.exists():
      caminho_final = encontrar_nome_novo(caminho_final)

    item.rename(caminho_final)
    return True

  except Exception as erro:
    print()
    print(f'Houve um erro no arquivo "{item.name}"')
    print(f"Motivo: {erro}")
    return False
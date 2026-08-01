from categorias import pastas

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
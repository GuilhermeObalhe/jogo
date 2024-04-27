class Player:
  def __init__(self, mov):
    self.mov = mov
    self.perc = "Nada por perto"
    self.orient = "^"
    self.linha = 0
    self.coluna = 0
    self.pontos = 0
    self.flecha = 1
    self.vivo = True
    self.pegou = False
    self.Ouro = Ouro #Instância de ouro associada ao jogador
    self.Wumpus = Wumpus #Instância de Wumpus associada ao jogador
    self.Poco = Poco #Instância de poco associada ao jogador
  
  def Mover(self):
    # Adicionar validação para o jogador não sair do mapa
    
    if self.orient == "^":
      self.linha -= 1
      
    elif self.orient == ">":
      self.coluna += 1

    elif self.orient == "v":
      self.linha += 1

    else:
      self.coluna -= 1
      
    self.Percepcao()

  def GirarEsquerda(self):
    if self.orient == "^":
      self.orient = "<"

    elif self.orient == "<":
      self.orient = "v"
    
    elif self.orient == "v":
      self.orient = ">"
    
    else:
      self.orient = "^"
  
  def GirarDireita(self):
    if self.orient == "^":
      self.orient = ">"

    elif self.orient == ">":
      self.orient = "v"
    
    elif self.orient == "v":
      self.orient = "<"
    
    else:
      self.orient = "^"
  
  def Atirar(self):
    if self.flecha == 0:
      print("Você não tem flechas!")
    
    else:
      # Posição da flecha
      proxima_linha, proxima_coluna = self.linha, self.coluna
      
      if self.orient == "^":
        proxima_linha -= 1
      
      elif self.orient == ">":
        proxima_coluna += 1

      elif self.orient == "v":
        proxima_linha += 1
      
      else:
        proxima_coluna -= 1
      
      # Conferindo se acertou o Wumpus
      if (proxima_linha, proxima_coluna) == (self.Wumpus.linha, self.Wumpus.coluna):
        print("Ouvi um urro agonizante!")
        self.Wumpus.vivo = False
        self.pontos += 10000
      
      else:
        print("Você não acertou o tiro!")

      # Decremento do número de flechas
      self.flecha -= 1

  def Pegar(self):
    if (self.linha, self.coluna) == (self.Ouro.linha, self.Ouro.coluna) and self.Ouro.existe:
      self.pontos += 1000
      self.pegou = True
      self.Ouro.existe = False
      print("Você pegou o ouro!")
    
    else:
      print("Não há ouro nesta sala!")

  def Sair(self):
    if (self.linha, self.coluna) == (0, 0):
      print("-----------")
      print("FIM DE JOGO")
      print("-----------")
      print(f"Pontos: {self.pontos}")
    
    else:
      print("Vá para a saída da caverna")

  def Percepcao(self):
    # Para o ouro
    if self.Ouro.existe and (self.linha, self.coluna) == (self.Ouro.linha, self.Ouro.coluna):
      self.perc = "R"
      print("Algo está brilhando")
    
    # Para o Wumpus
    if (self.linha - 1, self.coluna) == (self.Wumpus.linha, self.Wumpus.coluna) or \
      (self.linha + 1, self.coluna) == (self.Wumpus.linha, self.Wumpus.coluna) or \
      (self.linha, self.coluna - 1) == (self.Wumpus.linha, self.Wumpus.coluna) or \
      (self.linha, self.coluna + 1) == (self.Wumpus.linha, self.Wumpus.coluna):
      self.perc = "F"
      print("Estou sentindo um fedor horrível!")

    #Para o poço
    if (self.linha - 1, self.coluna) == (self.Poco.linha, self.Poco.coluna) or \
      (self.linha + 1, self.coluna) == (self.Poco.linha, self.Poco.coluna) or \
      (self.linha, self.coluna - 1) == (self.Poco.linha, self.Poco.coluna) or \
      (self.linha, self.coluna + 1) == (self.Poco.linha, self.Poco.coluna):
      self.perc = "B"
      print("Estou sentindo uma brisa!")

    # Caso o personagem caia no poço ou se encontre com o wumpus
    if ((self.linha, self.coluna) == (self.Poco.linha, self.Poco.coluna)) or \
    ((self.linha, self.coluna) == (self.Wumpus.linha, self.Wumpus.coluna)):
      self.vivo = False


class Ouro:
  def __init__(self, linha, coluna):
    self.linha = linha
    self.coluna = coluna
    self.existe = True

class Wumpus:
  def __init__(self, linha, coluna):
    self.linha = linha
    self.coluna = coluna
    self.vivo = True

class Poco:
  def __init__(self, linha, coluna):
    self.linha = linha
    self.coluna = coluna

class Mundo:
  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.celulas = [['?' for i in range(tamanho)] for i in range(tamanho)]

  def adicionar_ouro(self, linha, coluna):
    self.celulas[linha][coluna] = 'O'
  
  def adicionar_wumpus(self, linha, coluna):
    self.celulas[linha][coluna] = 'W'
  
  def adicionar_poco(self, linha, coluna):
    self.celulas[linha][coluna] = 'P'
  
  def adicionar_jogador(self, linha, coluna):
    self.celulas[linha][coluna] = "^"
  
  def limpar_celula(self, linha, coluna):
    self.celulas[linha][coluna] = '?'
  
  def imprimir_mapa(self):
    print("Percepção após a última ação:")
    print("[]")
    print("Mundo do Wumpus conhecido pelo agente:")
    print("---------------------------------")
    
    for linha in range(self.tamanho):
      for coluna in range(self.tamanho):
        print(f"| {self.celulas[linha][coluna]} ", end="")
      print("|\n---------------------------------")
    print()
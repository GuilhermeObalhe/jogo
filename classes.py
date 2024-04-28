class Player:
  def __init__(self, Mundo):
    self.perc = " "
    self.orient = "^"
    self.linha = Mundo.tamanho-1
    self.coluna = 0
    self.pontos = 0
    self.flecha = 1
    self.vivo = True
    self.pegou = False
    self.Mundo = Mundo #Instância de mundo associada ao jogador
    self.Wumpus = Wumpus(3, 2) #Preciso deixar isso genérico
    self.Ouro = Ouro(1, 2) #Preciso deixar isso genérico
    self.Poco = Poco(3, 4) #Preciso deixar isso genérico
    self.linha_anterior = self.linha
    self.coluna_anterior = self.coluna

  def Mover(self):
    self.linha_anterior, self.coluna_anterior = self.linha, self.coluna
    nova_linha, nova_coluna = self.linha, self.coluna
    
    if self.orient == "^":
      nova_linha -= 1
      
    elif self.orient == ">":
      nova_coluna += 1

    elif self.orient == "v":
      nova_linha += 1

    else:
      nova_coluna -= 1
      
    # Verificando se não sai do mapa
    if 0 <= nova_linha < self.Mundo.tamanho and 0 <= nova_coluna < self.Mundo.tamanho:
      self.linha = nova_linha
      self.coluna = nova_coluna
      self.Mundo.imprimeMundo(self.linha_anterior, self.coluna_anterior)
      self.Percepcao()
    else:
      print("Choque contra a parede da caverna!")

  def GirarEsquerda(self):
    if self.orient == "^":
      self.orient = "<"

    elif self.orient == "<":
      self.orient = "v"
    
    elif self.orient == "v":
      self.orient = ">"
    
    else:
      self.orient = "^"

    self.Mundo.imprimeMundo(self.linha, self.coluna)

  def GirarDireita(self):
    if self.orient == "^":
      self.orient = ">"

    elif self.orient == ">":
      self.orient = "v"
    
    elif self.orient == "v":
      self.orient = "<"
    
    else:
      self.orient = "^"

    self.Mundo.imprimeMundo(self.linha, self.coluna)

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
      self.Mundo.imprimeMundo(self.linha, self.coluna)

  def Pegar(self):
    if (self.linha, self.coluna) == (self.Ouro.linha, self.Ouro.coluna) and self.Ouro.existe:
      self.pontos += 1000
      self.pegou = True
      self.Ouro.existe = False
      print("Você pegou o ouro!")
    
    else:
      print("Não há ouro nesta sala!")

    self.Mundo.imprimeMundo(self.linha, self.coluna)

  def Sair(self):
    if (self.linha, self.coluna) == (self.Mundo.tamanho-1, 0):
      print("-----------")
      print("FIM DE JOGO")
      print("-----------")
      print(f"Pontos: {self.pontos}")
    
    else:
      print("Vá para a saída da caverna")
    self.Mundo.imprimeMundo(self.linha, self.coluna)

  def Percepcao(self):
    self.perc = " "
    # Para o ouro
    if self.Ouro.existe and (self.linha, self.coluna) == (self.Ouro.linha, self.Ouro.coluna):
      self.perc = "R"
      print("Algo está brilhando")
    
    # Para o Wumpus
    if ((self.linha - 1, self.coluna) == (self.Wumpus.linha, self.Wumpus.coluna) or \
      (self.linha + 1, self.coluna) == (self.Wumpus.linha, self.Wumpus.coluna) or \
      (self.linha, self.coluna - 1) == (self.Wumpus.linha, self.Wumpus.coluna) or \
      (self.linha, self.coluna + 1) == (self.Wumpus.linha, self.Wumpus.coluna)) \
      and self.Wumpus.vivo:
      self.perc = "F"
      print("Estou sentindo um fedor terrível!")

    #Para o poço
    if (self.linha - 1, self.coluna) == (self.Poco.linha, self.Poco.coluna) or \
      (self.linha + 1, self.coluna) == (self.Poco.linha, self.Poco.coluna) or \
      (self.linha, self.coluna - 1) == (self.Poco.linha, self.Poco.coluna) or \
      (self.linha, self.coluna + 1) == (self.Poco.linha, self.Poco.coluna):
      self.perc = "B"
      print("Estou sentindo uma brisa!")

    # Caso o personagem caia no poço ou se encontre com o wumpus
    if ((self.linha, self.coluna) == (self.Poco.linha, self.Poco.coluna)) or \
    ((self.linha, self.coluna) == (self.Wumpus.linha, self.Wumpus.coluna)and self.Wumpus.vivo):
      print("Você morreu!")
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
    self.Player = Player(self)
    self.mapa = [["?"for i in range(self.tamanho)]for i in range(self.tamanho)]
  
  def imprimeMundo(self, linha_anterior, coluna_anterior):
    self.mapa[linha_anterior][coluna_anterior] = self.Player.perc
    self.mapa[self.Player.linha][self.Player.coluna] = self.Player.orient

    # Imprimir linha superior do mapa
    print("-" * (4 * self.tamanho + 1))

    for i in range(self.tamanho):
      # Imprimir o início de cada linha
      print("|", end="")
      for j in range(self.tamanho):
        print(f" {self.mapa[i][j]} |", end = "")
      # Imprimir linha divisória entre cada linha do mapa
      print()
      print("-" * (4*self.tamanho+1))
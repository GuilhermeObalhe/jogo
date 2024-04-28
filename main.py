# AMBIENTE DE TESTES
from classes import *

def main():
  tamanho = 5
  mundo = Mundo(tamanho)

  # Instanciando o jogador
  jogador = Player(mundo)

  mundo.imprimeMundo(mundo.Player.linha, mundo.Player.coluna)
  
  while (jogador.vivo):
    
    comando = input()

    # Comandos de movimentos básicos
    if comando == 'M':
      mundo.Player.Mover()
    
    elif comando == 'D':
      mundo.Player.GirarDireita()
    
    elif comando == 'E':
      mundo.Player.GirarEsquerda()

    elif comando == 'S':
      mundo.Player.Sair()
      if (mundo.Player.linha, mundo.Player.coluna) == (mundo.tamanho-1, 0):
        mundo.Player.Sair()
        break
      

if __name__ == '__main__':
  main()
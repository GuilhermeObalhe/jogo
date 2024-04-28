# AMBIENTE DE TESTES
from classes import *

def main():
  # Criando o Mundo
  tamanho = 5
  mundo = Mundo(tamanho)

  mundo.imprimeMundo(mundo.Player.linha, mundo.Player.coluna)

  while (mundo.Player.vivo):
    print()
    comando = input("Insira seu movimento: (M/D/E/T/G/S)")
    comando = comando.upper()

    # Comandos de movimentos básicos
    if comando == 'M':
      mundo.Player.Mover()
    
    elif comando == 'D':
      mundo.Player.GirarDireita()
    
    elif comando == 'E':
      mundo.Player.GirarEsquerda()

    elif comando == 'T':
      mundo.Player.Atirar()

    elif comando == 'S':
      mundo.Player.Sair()
      if (mundo.Player.linha, mundo.Player.coluna) == (mundo.tamanho-1, 0):
        mundo.Player.Sair()
        break

    elif comando == 'G':
      mundo.Player.Pegar()

    else:
      print("Comando inválido!")

    # print(mundo.Player.perc)

if __name__ == '__main__':
  main()
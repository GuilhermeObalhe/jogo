# AMBIENTE DE TESTES
from classes import *
tam = 5
mundo = Mundo(tam)
mundo.imprimeMundo(tam)

# Movimentando
jogador = Player(mundo)
jogador.Mover()
mundo.imprimeMundo(tam)
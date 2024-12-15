# -- coding: utf-8 --
from random import randint
from random import choice

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def _init_(self, tabuleiro : Tabuleiro, tipo : int):
        super()._init_(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        # Prioriza vencer (r1 e r1b combinados)
        for i in range(0, 3):
            cont = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            for j in range(0, 3):
                if self.matriz[i][j] == Tabuleiro.JOGADOR_0:
                    cont += 1
                elif self.matriz[i][j] == Tabuleiro.JOGADOR_X:
                    cont += 4
                if self.matriz[j][i] == Tabuleiro.JOGADOR_0:
                    cont2 += 1
                elif self.matriz[j][i] == Tabuleiro.JOGADOR_X:
                    cont2 += 4
                if self.matriz[j][j] == Tabuleiro.JOGADOR_0:
                    cont3 += 1
                elif self.matriz[j][j] == Tabuleiro.JOGADOR_X:
                    cont3 += 4
                if self.matriz[j][2-j] == Tabuleiro.JOGADOR_0:
                    cont4 += 1
                elif self.matriz[j][2-j] == Tabuleiro.JOGADOR_X:
                    cont4 += 4

            # Verifica vitória da IA
            if cont == 2:  # Vitória em linha
                for c in range(0, 3):
                    if self.matriz[i][c] == Tabuleiro.DESCONHECIDO:
                        return (i, c)
            if cont2 == 2:  # Vitória em coluna
                for c in range(0, 3):
                    if self.matriz[c][i] == Tabuleiro.DESCONHECIDO:
                        return (c, i)
            if cont3 == 2:  # Vitória na diagonal principal
                for c in range(0, 3):
                    if self.matriz[c][c] == Tabuleiro.DESCONHECIDO:
                        return (c, c)
            if cont4 == 2:  # Vitória na diagonal secundária
                for c in range(0, 3):
                    if self.matriz[c][2-c] == Tabuleiro.DESCONHECIDO:
                        return (c, 2-c)

        # Caso não possa vencer, tenta bloquear (r1b adaptado)
        for i in range(0, 3):
            cont = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            for j in range(0, 3):
                if self.matriz[i][j] == Tabuleiro.JOGADOR_X:
                    cont += 4
                elif self.matriz[i][j] == Tabuleiro.JOGADOR_0:
                    cont += 1
                if self.matriz[j][i] == Tabuleiro.JOGADOR_X:
                    cont2 += 4
                elif self.matriz[j][i] == Tabuleiro.JOGADOR_0:
                    cont2 += 1
                if self.matriz[j][j] == Tabuleiro.JOGADOR_X:
                    cont3 += 4
                elif self.matriz[j][j] == Tabuleiro.JOGADOR_0:
                    cont3 += 1
                if self.matriz[j][2-j] == Tabuleiro.JOGADOR_X:
                    cont4 += 4
                elif self.matriz[j][2-j] == Tabuleiro.JOGADOR_0:
                    cont4 += 1

            # Bloqueio do jogador
            if cont == 8:  # Bloqueio em linha
                for c in range(0, 3):
                    if self.matriz[i][c] == Tabuleiro.DESCONHECIDO:
                        return (i, c)
            if cont2 == 8:  # Bloqueio em coluna
                for c in range(0, 3):
                    if self.matriz[c][i] == Tabuleiro.DESCONHECIDO:
                        return (c, i)
            if cont3 == 8:  # Bloqueio na diagonal principal
                for c in range(0, 3):
                    if self.matriz[c][c] == Tabuleiro.DESCONHECIDO:
                        return (c, c)
            if cont4 == 8:  # Bloqueio na diagonal secundária
                for c in range(0, 3):
                    if self.matriz[c][2-c] == Tabuleiro.DESCONHECIDO:
                        return (c, 2-c)

        # r3: Joga no centro se estiver vazio
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        #r4 
        if self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return(2,2)
        if self.matriz[0][2] == Tabuleiro.JOGADOR_X and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return(2,0)
        if self.matriz[2][0] == Tabuleiro.JOGADOR_X and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return(0,2)
        if self.matriz[2][2] == Tabuleiro.JOGADOR_X and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return(0,0)


        # r5: Jogadas de cantos
        cantos = []
        if self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            cantos.append((0, 0))
        if self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            cantos.append((0, 2))
        if self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            cantos.append((2, 0))
        if self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            cantos.append((2, 2))

        if len(cantos) > 0:
            return choice(cantos)

        # r6: Escolha aleatória caso nenhuma regra anterior seja válida
        lista = []
        for l in range(0, 3):
            for c in range(0, 3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if len(lista) > 0:
            p = randint(0, len(lista) - 1)
            return lista[p]
        else:
            return None
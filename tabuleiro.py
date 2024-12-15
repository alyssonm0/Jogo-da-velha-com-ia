# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        # Verifica se tem um campeão nas linhas, colunas e diagonais(principal e secundária, para ambos os jogadores)
        for i in range(0,3):
            cont = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            for j in range(0,3):
                if(self.matriz[i][j] == Tabuleiro.JOGADOR_X):
                    cont += 4
                elif(self.matriz[i][j] == Tabuleiro.JOGADOR_0):
                    cont += 1
                if(self.matriz[j][i] == Tabuleiro.JOGADOR_X):
                    cont2 += 4
                elif(self.matriz[j][i] == Tabuleiro.JOGADOR_0):
                    cont2 += 1
                if(self.matriz[j][j] == Tabuleiro.JOGADOR_0):
                    cont3 += 1

                elif(self.matriz[j][j] == Tabuleiro.JOGADOR_X):
                    cont3 += 4
                if(self.matriz[j][2-j] == Tabuleiro.JOGADOR_0):
                    cont4 += 1
                elif(self.matriz[j][2-j] == Tabuleiro.JOGADOR_X):
                    cont4 += 4
            if(cont == 3 or cont2 == 3 or cont3 == 3 or cont4 == 3):
                return Tabuleiro.JOGADOR_0
            elif(cont == 12 or cont2 == 12 or cont3 == 12 or cont4 == 12):
                return Tabuleiro.JOGADOR_X
            
        
        return Tabuleiro.DESCONHECIDO
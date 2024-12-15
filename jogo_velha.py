# -*- coding: utf-8 -*-
from tabuleiro_screen import TabuleiroScreen
from tabuleiro import Tabuleiro
from jogador import Jogador
from jogador_ia import JogadorIA
from jogador_humano import JogadorHumano
from random import randint

class JogoVelha:
    def __init__(self):
        self.screen = TabuleiroScreen()
        self.tabuleiro = Tabuleiro()
        
        #Jogadores
        self.jogadores = [
                JogadorIA(self.tabuleiro, Tabuleiro.JOGADOR_0),
                JogadorHumano(self.tabuleiro, self.screen.buttons, Tabuleiro.JOGADOR_X)
            ]
        self.id_jogador_corrente = randint(0,1)
        self.jogador_corrente : Jogador = self.jogadores[self.id_jogador_corrente]
        
        
    def troca_jogador(self):
        self.id_jogador_corrente = (self.id_jogador_corrente + 1) % 2
        self.jogador_corrente = self.jogadores[self.id_jogador_corrente]
        
        
    def wait_quit_event(self):
        self.screen.wait_quit_event()
    
    
    def acabou_jogo(self):    
        if(self.tabuleiro.tem_campeao() == Tabuleiro.JOGADOR_X):
            self.screen.resultado_txt = "X vencedor!"
            return True
            
        if(self.tabuleiro.tem_campeao() == Tabuleiro.JOGADOR_0):
            self.screen.resultado_txt = "0 vencedor!"
            return True
        
        return False
                              

    def start(self):
        acabou_jogo = False
        contador = 0
        
        while True:
            x, y = self.jogador_corrente.getJogada()
            self.screen.update_text_button(x, y, self.jogador_corrente.tipo)
            self.tabuleiro.matriz[x][y] = self.jogador_corrente.tipo
                                
            contador = contador + 1
            
            acabou_jogo = self.acabou_jogo()
                                
            if (acabou_jogo == False) and (contador == 9):
                self.screen.resultado_txt = "Deu velha!"
                acabou_jogo = True
            
            self.screen.desenha_tabuleiro()
            
            
            if(acabou_jogo == True):
                break
            
            self.troca_jogador()
            
           
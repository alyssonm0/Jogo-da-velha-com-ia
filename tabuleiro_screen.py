# -*- coding: utf-8 -*-
import buttons as bt
import pygame

class TabuleiroScreen:
    def __init__(self):
        self.resultado_txt = ""
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        screen.fill((255, 255, 255))                
        self.screen = screen
        self.buttons = [[], [], []]
         
        for l in range(0,3):
            y = 50 + l*200
            for c in range(0,3):
                x = 50 + c*200
                self.buttons[l].append( bt.Button(self.screen, (x, y), (200, 200)))
        
        self.desenha_tabuleiro()
         
    def wait_quit_event(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
         
    def desenha_tabuleiro(self):
        bt.buttons_v.update()
        bt.buttons_v.draw(self.screen)
        
        pygame.draw.line(self.screen,(0, 0, 0),(250,50),(250,650), 5)
        pygame.draw.line(self.screen,(0, 0, 0),(450,50),(450,650), 5)
        pygame.draw.line(self.screen,(0, 0, 0),(50,250),(650,250), 5)
        pygame.draw.line(self.screen,(0, 0, 0),(50,450),(650,450), 5)
        
        colors = "black on white"
        fg, _ = colors.split(" on ")
        font = pygame.font.SysFont("Arial", 40)
        text_render = font.render(self.resultado_txt, 1, fg)
        self.screen.blit(text_render, (270, 5))
        
        pygame.display.update()
        
    def update_text_button(self, x : int, y : int, player : int):
        b = self.buttons[x][y]
        b.change_text(player)
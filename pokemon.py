from window_class import Window
import pygame
pygame.init()

branco = (255, 255, 255)
preto = (0, 0, 0)

windowJogoMenu = Window(800, 600, branco) #objeto janeta (dimensões e características da janela a ser criada e montada)
pykemonSurface = pygame.display.set_mode((windowJogoMenu.get_height, windowJogoMenu.get_width)) #surface (é) onde vai ocorrer o nosso jogo
pygame.display.set_caption("Pykémon")
pykemonSurface.fill(windowJogoMenu.get_wcolor)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
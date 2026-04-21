import random
import os
import pygame
from PIL import Image

def build(screen):
    bottom_bun = pygame.image.load("Burger_Game_Assets/burger_build/Build_Bottom_Bun.png").convert_alpha()
    #Make hitbox
    b_bun_rect = bottom_bun.get_rect(topleft = (632, 815))
    bun_hitbox = b_bun_rect.inflate(-20, -20)

# to see my hitbox for changing
    screen.blit(bottom_bun, (632, 815))
    pygame.draw.rect(screen, (255, 0, 0), bun_hitbox, 2)

def main():
    pygame.init()
    pygame.display.set_caption("Build Burger")
    screen = pygame.display.set_mode((1920, 1080))
    bg = pygame.image.load("Burger_Game_Assets/Burger_BG.png").convert()
    clock = pygame.time.Clock()
    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(bg, (0, 0))
        build(screen)

        pygame.display.flip()
        dt = clock.tick(24)

    pygame.quit()


















if __name__ == "__main__":
    main()

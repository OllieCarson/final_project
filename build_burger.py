import random
import pygame
from PIL import Image

def main():
    pygame.init()
    pygame.display.set_caption("Build Burger")
    screen = pygame.display.set_mode((1920, 1080))
    bg = pygame.image.load("Burger_BG.png")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(bg, (0, 0))
        pygame.display.flip()

    pygame.quit()


















if __name__ == "__main__":
    main()

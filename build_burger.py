import random
import os
import pygame
from PIL import Image



class Asset:
    def __init__(self, folder_path):
        self.image = self.get_random_image(folder_path)
        self.rect = self.image.get_rect(center = (0, 100))
        self.hitbox = self.rect.inflate(-20, -90)
        self.moving = True
        self.dropping = False
        self.speed_x = 5
        self.speed_y = 0

    def get_random_image(folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.startswith('Build_') and f.endswith('.png')]
        if not image_files:
            return None
        random_image = random.choice(image_files)
        return pygame.image.load(os.path.join(folder_path, random_image)).convert_alpha()

    def display_random_ing(screen, folder_path):
        random_ing = get_random_image(folder_path)
        if random_ing:
            ing_rect = random_ing.get_rect(center = (960, 100))
            ing_hitbox = ing_rect.inflate(-20, -90)

            screen.blit(random_ing, ing_rect)
            pygame.draw.rect(screen, (0, 255, 0), ing_hitbox, 2)


def build(screen):
    bottom_bun = pygame.image.load("Burger_Game_Assets/Build_Bottom_Bun.png").convert_alpha()
    #Make hitbox
    b_bun_rect = bottom_bun.get_rect(topleft = (632, 815))
    bun_hitbox = b_bun_rect.inflate(-20, -90)

    screen.blit(bottom_bun, (632, 815))
    pygame.draw.rect(screen, (255, 0, 0), bun_hitbox, 2)








def main():
    pygame.init()
    pygame.display.set_caption("Build Burger")
    screen = pygame.display.set_mode((1920, 1080))
    bg = pygame.image.load("Burger_Game_Assets/Burger_BG.png").convert()
    clock = pygame.time.Clock()
    folder_path = os.path.join("Burger_Game_Assets", "burger_build")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(bg, (0, 0))
        build(screen)
        display_random_ing(screen, folder_path)

        pygame.display.flip()
        clock.tick(24)

    pygame.quit()


















if __name__ == "__main__":
    main()

import random
import os
import pygame
from PIL import Image



class Asset:
    def __init__(self, folder_path):
        self.image = self.get_random_image(folder_path)
        self.rect = self.image.get_rect(center = (random.randint(self.image.get_width()//2, 1920 - self.image.get_width()//2), 100))
        self.hitbox = self.rect.inflate(-20, -90)
        self.moving = True
        self.dropping = False
        self.speed_x = random.choice([-5, 5])
        self.speed_y = 0
        
    @staticmethod
    def get_random_image(folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.startswith('Build_') and f.endswith('.png')]
        if not image_files:
            return None
        random_image = random.choice(image_files)
        return pygame.image.load(os.path.join(folder_path, random_image)).convert_alpha()
    
    def update(self, burger_hitbox):
        if self.moving:
            self.rect.x += self.speed_x
            self.hitbox.x += self.speed_x
            if self.rect.left < 0 or self.rect.right > 1920:
                self.speed_x *= -1
        if self.dropping:
            self.rect.y += self.speed_y
            self.hitbox.y += self.speed_y
            self.speed_y += 1
            if self.hitbox.colliderect(burger_hitbox):
                self.dropping = False
                self.rect.bottom = burger_hitbox.top


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)


def build(screen):
    bottom_bun = pygame.image.load("Burger_Game_Assets/Build_Bottom_Bun.png").convert_alpha()
    #Make hitbox
    b_bun_rect = bottom_bun.get_rect(topleft = (632, 815))
    bun_hitbox = b_bun_rect.inflate(-20, -90)

    screen.blit(bottom_bun, (632, 815))
    pygame.draw.rect(screen, (255, 0, 0), bun_hitbox, 2)
    return bun_hitbox





def main():
    pygame.init()
    pygame.display.set_caption("Build Burger")
    screen = pygame.display.set_mode((1920, 1080))
    bg = pygame.image.load("Burger_Game_Assets/Burger_BG.png").convert()
    clock = pygame.time.Clock()
    folder_path = os.path.join("Burger_Game_Assets", "burger_build")

    asset = Asset(folder_path)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and asset.moving:
                    asset.moving = False
                    asset.dropping = True
                    asset.speed_y = 0
                
        screen.blit(bg, (0, 0))
        burger_hitbox = build(screen)
        if not asset.dropping and not asset.moving:
            asset = Asset(folder_path)

        asset.update(burger_hitbox)
        asset.draw(screen)
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


















if __name__ == "__main__":
    main()

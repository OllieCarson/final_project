import random
import os
import pygame
from PIL import Image
# Realized that trying to cap it at 10 and then adding the top bun wasnt working, and just spawning the top bun once it reaches 9 was easier.
# took me an embarasingly long time to figure that out.
class Asset:
    def __init__(self, folder_path, force_top_bun=False):
        if force_top_bun:
            self.image = pygame.image.load(os.path.join(folder_path, 'Build_Top_Bun.png'))
        else: 
            self.image = Asset.get_random_image(folder_path)
        self.rect = self.image.get_rect(center = (random.randint(self.image.get_width()//2, 1920 - self.image.get_width()//2), 100))
        self.hitbox = self.rect.inflate(-20, -150)
        self.moving = True
        self.dropping = False
        self.speed_x = random.choice([-5, 5])
        self.speed_y = 0
        
    @staticmethod
    def get_random_image(folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.startswith('Build_') and f.endswith('.png') and f != 'Build_Top_Bun.png']
        if not image_files:
            return None
        random_image = random.choice(image_files)
        return pygame.image.load(os.path.join(folder_path, random_image)).convert_alpha()
    
    def update(self, burger_hitbox, dropped_assets):
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
                dropped_assets.append(self)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)


    def is_top_bun(self, folder_path):
        image_path = os.path.join(folder_path, 'Build_Top_Bun.png')
        return self.image.get_size() == pygame.image.load(image_path).convert_alpha().get_size()


def build(screen, dropped_assets):
    bottom_bun = pygame.image.load("Burger_Game_Assets/Build_Bottom_Bun.png").convert_alpha()
    #Make hitbox
    b_bun_rect = bottom_bun.get_rect(topleft = (632, 815))
    bun_hitbox = b_bun_rect.inflate(-20, -90)

    screen.blit(bottom_bun, (632, 815))
    pygame.draw.rect(screen, (255, 0, 0), bun_hitbox, 2)

    for asset in dropped_assets:
        screen.blit(asset.image, asset.rect)
        pygame.draw.rect(screen, (0, 255, 0), asset.hitbox, 2)

        if dropped_assets:
            bun_hitbox = dropped_assets[-1].hitbox
        
    return bun_hitbox


def main():
    pygame.init()
    pygame.display.set_caption("Build Burger")
    screen = pygame.display.set_mode((1920, 1080))
    bg = pygame.image.load("Burger_Game_Assets/Burger_BG.png").convert()
    clock = pygame.time.Clock()
    folder_path = os.path.join("Burger_Game_Assets", "burger_build")

    jar_folder_path = os.path.join("Burger_Game_Assets", "jar")
    jar_images = [f for f in os.listdir(jar_folder_path) if f.startswith('Burger_Stage') and f.endswith('.png')]
    jar_images = sorted(jar_images)
    jar_stage_images = [pygame.image.load(os.path.join(jar_folder_path, image)).convert_alpha() for image in jar_images]
    jar_image = jar_stage_images[0]

    dropped_assets = []
    game_over = False
    stage = 0

    asset = Asset(folder_path)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and asset.moving and not game_over:
                    asset.moving = False
                    asset.dropping = True
                    asset.speed_y = 0
                
        screen.blit(bg, (0, 0))
        screen.blit(jar_image, (133, 510))
        burger_hitbox = build(screen, dropped_assets)
        asset.update(burger_hitbox, dropped_assets)
        asset.draw(screen)


        if not asset.dropping and not asset.moving and not game_over:
            dropped_assets.append(asset)
            if asset.is_top_bun(folder_path):
                game_over = True
                pygame.display.flip()
                pygame.time.wait(1000)
                if stage < len(jar_stage_images) - 1:
                    stage += 1
                    jar_image = jar_stage_images[stage]
                    asset = Asset(folder_path)
                    dropped_assets = []
                    game_over = False
                else:
                    running = False
            elif len(dropped_assets) >= 10:
                asset = Asset(folder_path, asset.is_top_bun)
            else:
                asset = Asset(folder_path)


 
    
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


















if __name__ == "__main__":
    main()

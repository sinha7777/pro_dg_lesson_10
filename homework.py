import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Treasure Hunt")

screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# plain white background
def change_background():
    screen.fill((255, 255, 255))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Skull(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("skull.webp")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

class Treasure(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()


treasure_list = pygame.sprite.Group()
skull_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

bin = Bin()
allsprites.add(bin)

for i in range(20):
    skull = Skull()
    skull.rect.x = random.randrange(screen_width)
    skull.rect.y = random.randrange(screen_height)
    skull_list.add(skull)
    allsprites.add(skull)

images = ["trusure.webp", "coin.webp", "skull.webp"]

for i in range(50):
    treasure = Treasure(random.choice(images))
    treasure.rect.x = random.randrange(screen_width)
    treasure.rect.y = random.randrange(screen_height)
    treasure_list.add(treasure)
    allsprites.add(treasure)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman", 22)
text = myFont.render("Score = " + str(0), True, BLACK)

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False

    timeElapsed = time.time() - start_time
    if timeElapsed >= 60:
        if score >= 20:
            screen.fill(GREEN)
            text1 = myFont.render("Good job!", True, BLACK)
        else:
            screen.fill(RED)
            text1 = myFont.render("You lost.", True, BLACK)
        screen.blit(text1, (250, 40))
    else:
        change_background()
        countDown = myFont.render("Time Left: " + str(60 - int(timeElapsed)), True, BLACK)
        screen.blit(countDown, (20, 10))

import pygame
import math

def createPolygonSurface():
    r = 150
    x = 150
    y = 150
    surface = pygame.Surface((300,300),pygame.SRCALPHA)
    points = []

    for i in range(12):

        angle = (i * 30) * math.pi / 180
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        points.append((px, py))
    
    pygame.draw.polygon(surface,ZIELONY,points)
    pygame.draw.rect(surface,(0,0,0),(100,125,100,50))
    return surface


pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

image = createPolygonSurface()
original_image = image
image_rect = image.get_rect(center=(300,300))

run = True
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_1:
                image = original_image
                image_rect = image.get_rect(center=(300,300))

            elif event.key == pygame.K_2:
                image = original_image
                image = pygame.transform.rotate(image,-45)
                image_rect = image.get_rect(center=(300,300))

            elif event.key == pygame.K_3:
                image = original_image
                image = pygame.transform.rotate(image,180)
                image = pygame.transform.scale(image,(200,500))
                image_rect = image.get_rect(center=(300,300))

            elif event.key == pygame.K_4:
                image = original_image
                image = pygame.transform.smoothscale(image,(350,300))
                image = pygame.transform.rotate(image,10)
                image_rect = image.get_rect(center=(300,300))

            elif event.key == pygame.K_5:
                image = original_image
                image = pygame.transform.scale(image,(300,100))
                image_rect = image.get_rect(center=(300,50))

            elif event.key == pygame.K_6:
                image = original_image
                image = pygame.transform.smoothscale(image,(350,300))
                image = pygame.transform.rotate(image,-70)
                image_rect = image.get_rect(center=(300,300))

            elif event.key == pygame.K_7:
                image = original_image
                image = pygame.transform.flip(image,True,False)
                image = pygame.transform.scale(image,(150,300))
                image = pygame.transform.rotate(image,180)
                image_rect = image.get_rect(center=(300,300))

            elif event.key == pygame.K_8:
                image = original_image
                image = pygame.transform.scale(image, (450,250))
                image = pygame.transform.rotate(image,145)
                image_rect = image.get_rect(center=(200,400))

            elif event.key == pygame.K_9:
                image = original_image
                image = pygame.transform.smoothscale(image,(350,300))
                image = pygame.transform.rotate(image,140)
                image_rect = image.get_rect(center=(430,400))
    
    win.blit(image, image_rect.topleft)
    pygame.display.update()
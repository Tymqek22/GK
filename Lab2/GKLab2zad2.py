import pygame

pygame.init()
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Figure")

CZERWONY = (255, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.rect(win,CZERWONY,(200,200,200,20))
    middle_part = pygame.Surface((280,20),pygame.SRCALPHA)
    middle_part.fill(CZERWONY)
    middle_part = pygame.transform.rotate(middle_part,50)
    middle_part_rect = middle_part.get_rect(center=(300,320))
    pygame.draw.rect(win,CZERWONY,(200,420,200,20))

    win.blit(middle_part,middle_part_rect.topleft)
    pygame.display.update()
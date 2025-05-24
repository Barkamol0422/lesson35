import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
done=False
while not done:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            pygame.quit()
        pygame.draw.rect(screen,(0,155,215),pygame.Rect(30,30,120,60))
    pygame.display.flip()

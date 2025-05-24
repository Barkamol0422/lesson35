import pygame
pygame.init()
a,b=800, 600
c,d,e=(255, 255, 255),(0, 0, 255),(0, 0, 0)
f=pygame.display.set_mode((a, b))
pygame.display.set_caption("Hello World")
g=pygame.font.SysFont(None,48)
h=g.render("Hello, Pygame!",True,e)
i=True
while i:
    f.fill(c)
    pygame.draw.rect(f,d,pygame.Rect(300,200,200,100))
    f.blit(h,(280,100))
    for j in pygame.event.get():
        if j.type==pygame.QUIT:
            i=False
    pygame.display.flip()
pygame.quit()

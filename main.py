import pygame
import random
# push test

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((1200,700))
screen_w = pygame.display.Info().current_w
screen_h = pygame.display.Info().current_h
pygame.display.set_caption("2D Shooter")

# define fonts
font = pygame.font.SysFont("CASTELLAR", 30)
for x in pygame.font.get_fonts():
    print(x)

# define colors
text_color = (255, 255, 255)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x,y))

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

run = True
while run:
    draw_text("cool game", font, text_color, 0, 0)
    draw_text("cool game", font, text_color, 0, 15)
    draw_text("cool game", font, text_color, 120, 0)
    draw_text(str(random.randint(0,255)), font, text_color, random.randint(0,screen_w), random.randint(0,screen_h))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
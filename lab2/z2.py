import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_GRAY = (220, 220, 220)      
SNOW_WHITE = (255, 255, 255)    
COAT_BROWN = (90, 70, 50)       
STRIP_BROWN = (60, 40, 30)      
HOOD_COLOR = (245, 245, 245)    
SKIN_COLOR = (230, 215, 200)   
CAT_GRAY = (150, 150, 150)      
FISH_BLUE = (80, 100, 180)
FISH_RED = (200, 50, 50)

PI = 3.14

def draw_igloo(surface, x, y):
    radius = 160
    
    pygame.draw.circle(surface, WHITE, (x, y), radius)
    pygame.draw.rect(surface, SNOW_WHITE, (x - radius, y, radius * 2, radius))

    rect = (x - radius, y - radius, radius * 2, radius * 2)
    pygame.draw.arc(surface, BLACK, rect, 0, PI, 2)
    
    
    pygame.draw.arc(surface, BLACK, (x - radius + 20, y - radius + 40, (radius - 20)*2, (radius - 40)*2), 0, PI, 1)
    pygame.draw.arc(surface, BLACK, (x - radius + 5, y - radius + 90, (radius - 5)*2, (radius - 90)*2), 0, PI, 1)
    
    pygame.draw.line(surface, BLACK, (x, y - radius), (x, y), 1)
    
    pygame.draw.arc(surface, BLACK, (x - 80, y - radius, 80, radius*2), PI/2, PI, 1)
    
    pygame.draw.arc(surface, BLACK, (x, y - radius, 80, radius*2), 0, PI/2, 1)


def draw_chukcha(surface, x, y):
    
    pygame.draw.line(surface, BLACK, (x - 70, y - 10), (x - 70, y - 150), 2)

    pygame.draw.ellipse(surface, STRIP_BROWN, (x - 25, y, 20, 35)) # Левая
    pygame.draw.ellipse(surface, STRIP_BROWN, (x + 5, y, 20, 35))  # Правая

    body_height = 70
    body_points = [
        (x - 30, y - body_height), 
        (x + 30, y - body_height), 
        (x + 55, y),              
        (x - 55, y)                
    ]
    pygame.draw.polygon(surface, COAT_BROWN, body_points)
   
    pygame.draw.rect(surface, STRIP_BROWN, (x - 55, y - 10, 110, 10)) # Низ
    pygame.draw.rect(surface, STRIP_BROWN, (x - 5, y - body_height, 10, body_height)) # Центр

   
    pygame.draw.ellipse(surface, COAT_BROWN, (x - 75, y - 50, 40, 20)) # Левая
    pygame.draw.ellipse(surface, COAT_BROWN, (x + 35, y - 50, 40, 20)) # Правая

    head_y = y - body_height - 15
    
    pygame.draw.circle(surface, HOOD_COLOR, (x, head_y), 38)
    
    pygame.draw.circle(surface, SKIN_COLOR, (x, head_y), 26)
    
    
    eye_y = head_y - 5 
    pygame.draw.line(surface, BLACK, (x - 12, eye_y - 3), (x - 4, eye_y + 3), 2)
    pygame.draw.line(surface, BLACK, (x + 4, eye_y + 3), (x + 12, eye_y - 3), 2)
    
    
    mouth_y = head_y + 8
    pygame.draw.arc(surface, BLACK, (x - 8, mouth_y, 16, 10), 0, PI, 2)

def draw_cat(surface, x, y):
    
    
   
    pygame.draw.ellipse(surface, CAT_GRAY, (x + 40, y - 5, 60, 20))
    

    pygame.draw.ellipse(surface, CAT_GRAY, (x + 20, y + 10, 12, 52))
    pygame.draw.ellipse(surface, CAT_GRAY, (x + 35, y + 10, 12, 52))
    pygame.draw.ellipse(surface, CAT_GRAY, (x - 10, y + 10, 12, 52))
    pygame.draw.ellipse(surface, CAT_GRAY, (x - 25, y + 10, 12, 52))

    pygame.draw.ellipse(surface, CAT_GRAY, (x - 30, y - 10, 90, 40))

    pygame.draw.circle(surface, CAT_GRAY, (x - 35, y + 5), 22)
    
    pygame.draw.polygon(surface, CAT_GRAY, [(x - 45, y - 10), (x - 50, y - 20), (x - 35, y - 15)])
    pygame.draw.polygon(surface, CAT_GRAY, [(x - 25, y - 15), (x - 20, y - 20), (x - 15, y - 10)])
    
    pygame.draw.circle(surface, WHITE, (x - 42, y + 2), 5)
    pygame.draw.circle(surface, BLACK, (x - 42, y + 2), 2)
    
    pygame.draw.circle(surface, WHITE, (x - 28, y + 2), 5)
    pygame.draw.circle(surface, BLACK, (x - 28, y + 2), 2)
    
    fx, fy = x - 55, y + 15
    pygame.draw.ellipse(surface, FISH_BLUE, (fx, fy, 30, 12))
    pygame.draw.polygon(surface, FISH_RED, [(fx, fy + 6), (fx - 8, fy), (fx - 8, fy + 12)])


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    horizon = 220 
    pygame.draw.rect(screen, SKY_GRAY, (0, 0, WIDTH, horizon))
    pygame.draw.rect(screen, SNOW_WHITE, (0, horizon, WIDTH, HEIGHT - horizon))

    
    draw_igloo(screen, 320, horizon)

    
    draw_chukcha(screen, 650, 350)

    
    draw_cat(screen, 180, 400)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
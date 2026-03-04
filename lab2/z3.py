import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_GRAY = (225, 225, 225)     
SNOW_WHITE = (253, 253, 253)   
COAT_BROWN = (100, 80, 60)      
STRIP_BROWN = (70, 50, 40)     
HOOD_COLOR = (240, 240, 240)    
SKIN_COLOR = (230, 215, 200)    
CAT_GRAY = (170, 170, 170)      
FISH_BLUE = (80, 110, 190)
FISH_RED = (200, 60, 60)

PI = 3.14


def draw_igloo(surface, x, y, scale=1.0):
    s = scale
    radius = int(150 * s)
    

    pygame.draw.circle(surface, WHITE, (x, y), radius)

    pygame.draw.rect(surface, SNOW_WHITE, (x - radius, y, radius * 2, radius))


    rect = (x - radius, y - radius, radius * 2, radius * 2)
    width = max(1, int(2 * s)) # Толщина линии зависит от масштаба
    pygame.draw.arc(surface, BLACK, rect, 0, PI, width)
    
  
    pygame.draw.arc(surface, BLACK, (x - radius + 20*s, y - radius + 40*s, (radius - 20*s)*2, (radius - 40*s)*2), 0, PI, 1)
    pygame.draw.arc(surface, BLACK, (x - radius + 5*s, y - radius + 90*s, (radius - 5*s)*2, (radius - 90*s)*2), 0, PI, 1)
    

    pygame.draw.line(surface, BLACK, (x, y - radius), (x, y), 1)
    pygame.draw.arc(surface, BLACK, (x - 70*s, y - radius, 70*s, radius*2), PI/2, PI, 1)
    pygame.draw.arc(surface, BLACK, (x, y - radius, 70*s, radius*2), 0, PI/2, 1)


def draw_chukcha(surface, x, y, scale=1.0):
    s = scale


    pygame.draw.line(surface, BLACK, (x - 65*s, y - 10*s), (x - 65*s, y - 140*s), max(1, int(2*s)))

    pygame.draw.ellipse(surface, STRIP_BROWN, (x - 25*s, y, 20*s, 30*s)) 
    pygame.draw.ellipse(surface, STRIP_BROWN, (x + 5*s, y, 20*s, 30*s))

    body_h = 65 * s
    body_points = [
        (x - 30*s, y - body_h), 
        (x + 30*s, y - body_h), 
        (x + 55*s, y),               
        (x - 55*s, y)                
    ]
    pygame.draw.polygon(surface, COAT_BROWN, body_points)
    

    pygame.draw.rect(surface, STRIP_BROWN, (x - 55*s, y - 8*s, 110*s, 8*s))
    pygame.draw.rect(surface, STRIP_BROWN, (x - 5*s, y - body_h, 10*s, body_h))

    pygame.draw.ellipse(surface, COAT_BROWN, (x - 70*s, y - 45*s, 40*s, 18*s))
    pygame.draw.ellipse(surface, COAT_BROWN, (x + 30*s, y - 45*s, 40*s, 18*s))

    head_y = y - body_h - 15*s
    pygame.draw.circle(surface, HOOD_COLOR, (x, head_y), 35*s)
    pygame.draw.circle(surface, SKIN_COLOR, (x, head_y), 24*s)
    
    eye_y = head_y - 4*s
    pygame.draw.line(surface, BLACK, (x - 10*s, eye_y - 2*s), (x - 4*s, eye_y + 2*s), max(1, int(2*s)))
    pygame.draw.line(surface, BLACK, (x + 4*s, eye_y + 2*s), (x + 10*s, eye_y - 2*s), max(1, int(2*s)))
    
    mouth_y = head_y + 6*s
    pygame.draw.arc(surface, BLACK, (x - 7*s, mouth_y, 14*s, 8*s), 0, PI, max(1, int(2*s)))

def draw_cat(surface, x, y):
    
    s = 1.0 
    
    pygame.draw.ellipse(surface, CAT_GRAY, (x + 40*s, y - 5*s, 90*s, 18*s))
    
    pygame.draw.ellipse(surface, CAT_GRAY, (x + 20*s, y + 8*s, 14*s, 35*s))
    pygame.draw.ellipse(surface, CAT_GRAY, (x + 40*s, y + 8*s, 14*s, 35*s))
    pygame.draw.ellipse(surface, CAT_GRAY, (x - 15*s, y + 8*s, 14*s, 35*s))
    pygame.draw.ellipse(surface, CAT_GRAY, (x - 35*s, y + 8*s, 14*s, 35*s))

    pygame.draw.ellipse(surface, CAT_GRAY, (x - 40*s, y - 12*s, 110*s, 35*s))

    pygame.draw.circle(surface, CAT_GRAY, (x - 45*s, y + 2*s), 22*s)
    
    pygame.draw.polygon(surface, CAT_GRAY, [(x - 55*s, y - 12*s), (x - 60*s, y - 25*s), (x - 45*s, y - 18*s)])
    pygame.draw.polygon(surface, CAT_GRAY, [(x - 35*s, y - 18*s), (x - 30*s, y - 25*s), (x - 25*s, y - 12*s)])
    
    pygame.draw.circle(surface, WHITE, (x - 52*s, y), 5*s)
    pygame.draw.circle(surface, BLACK, (x - 52*s, y), 2*s)
    
    pygame.draw.circle(surface, WHITE, (x - 38*s, y), 5*s)
    pygame.draw.circle(surface, BLACK, (x - 38*s, y), 2*s)
    
    fx, fy = x - 65*s, y + 12*s
    pygame.draw.ellipse(surface, FISH_BLUE, (fx, fy, 30*s, 12*s))
    pygame.draw.polygon(surface, FISH_RED, [(fx, fy + 6*s), (fx - 8*s, fy), (fx - 8*s, fy + 12*s)])


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    horizon = 230
    pygame.draw.rect(screen, SKY_GRAY, (0, 0, WIDTH, horizon))
    pygame.draw.rect(screen, SNOW_WHITE, (0, horizon, WIDTH, HEIGHT - horizon))

    
    draw_igloo(screen, 150, 290, scale=0.5) 
    draw_igloo(screen, 500, 290, scale=0.5) 

    draw_chukcha(screen, 600, 280, 0.35)
    draw_chukcha(screen, 660, 270, 0.35)
    draw_chukcha(screen, 720, 280, 0.35)
    draw_chukcha(screen, 580, 330, 0.4)
    draw_chukcha(screen, 640, 340, 0.4)
    draw_chukcha(screen, 700, 330, 0.4)

    draw_igloo(screen, 320, 330, scale=1.1)

    draw_igloo(screen, 180, 380, scale=0.6) 
    draw_igloo(screen, 420, 380, scale=0.6) 

    draw_chukcha(screen, 720, 480, scale=1.2)

    draw_cat(screen, 320, 430)
    
    draw_cat(screen, 180, 520)
    
    draw_cat(screen, 50, 460)
    
    draw_cat(screen, 550, 550)
   
    draw_cat(screen, 750, 560)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
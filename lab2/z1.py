import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill(WHITE)
    
    pygame.draw.circle(screen, YELLOW, (WIDTH//2, HEIGHT//2), 200)
    
    pygame.draw.circle(screen, RED, (WIDTH//2 - 80, HEIGHT//2 - 50), 30)
    pygame.draw.circle(screen, BLACK, (WIDTH//2 - 80, HEIGHT//2 - 50), 15)
    
    pygame.draw.circle(screen, RED, (WIDTH//2 + 80, HEIGHT//2 - 50), 30)
    pygame.draw.circle(screen, BLACK, (WIDTH//2 + 80, HEIGHT//2 - 50), 15)
    
    mouth_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 70, 200, 30)
    pygame.draw.rect(screen, BLACK, mouth_rect)
    
    brow_left_points = [
        (WIDTH//2 - 180, HEIGHT//2 - 160),  
        (WIDTH//2 - 30, HEIGHT//2 - 120),  
        (WIDTH//2 - 50, HEIGHT//2 - 90),    
        (WIDTH//2 - 200, HEIGHT//2 - 130)  
    ]
    pygame.draw.polygon(screen, BLACK, brow_left_points)
    
    brow_right_points = [
        (WIDTH//2 + 30, HEIGHT//2 - 120),   
        (WIDTH//2 + 180, HEIGHT//2 - 160),  
        (WIDTH//2 + 200, HEIGHT//2 - 130),  
        (WIDTH//2 + 50, HEIGHT//2 - 90)     
    ]
    pygame.draw.polygon(screen, BLACK, brow_right_points)
    
    pygame.display.flip()

pygame.quit()
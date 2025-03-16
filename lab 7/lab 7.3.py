#Third exercise: Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
# When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 
# 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to 
# leave of the screen should be ignored

import pygame  
pygame.init()

# Height and Width of display. 
WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Third exercises lab 7")

# Түстер
color1 = (255, 255, 255)  # White background
color2 = (255, 0, 0)      # Red circle

ball_x, ball_y = WIDTH // 2, HEIGHT // 2  
radius = 25  # Radius of circle 

# Pixel
step = 20  

running = True  
while running:  
    screen.fill(color1)  # White background
    pygame.draw.circle(screen, color2, (ball_x, ball_y), radius)  # Drawing the circle
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # Closing the display.
            running = False  
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP and ball_y - radius - step >= 0:
                ball_y -= step  # Up
            if event.key == pygame.K_DOWN and ball_y + radius + step <= HEIGHT:
                ball_y += step  # Down
            if event.key == pygame.K_LEFT and ball_x - radius - step >= 0:
                ball_x -= step  # Left
            if event.key == pygame.K_RIGHT and ball_x + radius + step <= WIDTH:
                ball_x += step  # Right

    pygame.display.update() 

pygame.quit()  
#first exercises: Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. 
# Use Mickey's right hand as minutes arrow and left - as seconds. 
# For moving Mickey's hands you can use: pygame.transform.rotate more explanation:


import pygame
import datetime 

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's clock")

clock_img = pygame.image.load("clock.png")
clock_face = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))
hand_right = pygame.image.load("rightarm.png")
hand_left = pygame.image.load("leftarm.png")

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
running = True 

while running: 
    screen.fill(WHITE)
    screen.blit(clock_face, (0, 0))
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    minute_angle = - (minutes * 6)  
    second_angle = - (seconds * 6)   
    
    rotated_right_hand = pygame.transform.rotate(hand_right, minute_angle)
    rotated_left_hand = pygame.transform.rotate(hand_left, second_angle)
    
    rh_rect = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    lh_rect = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    screen.blit(rotated_right_hand, rh_rect.topleft)
    screen.blit(rotated_left_hand, lh_rect.topleft)
    
    pygame.display.update()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            
    clock.tick(60)

pygame.quit()
import pygame
import random

# Pygame-ді инициализациялау. 
pygame.init()

# Экран, дисплей жасау және дисплейдің атауын енгізу. 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Машина және жол суреттері
car_img = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab 8\car.png")  # Машинаның суреті
road_img = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab 8\coin.png")  # Жолдың суреті
coin_img = pygame.image.load(r"C:\Users\user\Desktop\PP2\Lab 8\road.jpg")  # Монетаның суреті

# Машинаның бастапқы орны
car_x, car_y = WIDTH // 2 - 25, HEIGHT - 100
car_speed = 5

# Монетаның параметрлерін енгізу. 
coin_x = random.randint(50, WIDTH - 50)
coin_y = -50
coin_speed = 3
coins_collected = 0

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)  # Фонды ақ түске келтірдік.
    screen.blit(road_img, (0, 0))  # Жолдың суретін экранға шығардық. 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Егер қолданушы экрандағы Х батырмасын басса, ойын тоқтайды. 
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 50:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 100:
        car_x += car_speed
    
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_x = random.randint(50, WIDTH - 50)
        coin_y = -50
    
    car_rect = pygame.Rect(car_x, car_y, 50, 100)
    coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)
    if car_rect.colliderect(coin_rect):
        coins_collected += 1
        coin_x = random.randint(50, WIDTH - 50)
        coin_y = -50
    
    # Графиканы салу
    screen.blit(car_img, (car_x, car_y))  # Машинаны салу
    screen.blit(coin_img, (coin_x, coin_y))  # Монетаны салу
    
    # Жинаған монеталарды көрсету
    font = pygame.font.Font(None, 30)
    text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(text, (WIDTH - 100, 10))
    
    pygame.display.update() # Экранды жаңалау. 
    clock.tick(30)

pygame.quit() # Экранды жабу. 

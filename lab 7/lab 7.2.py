#Second exercise: Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys.
#Player has to react to the given command appropriately.

import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

music_files = [
    "music1.mp3", 
    "music2.mp3",  
    "music3.mp3"   
]
current_track = 0 

def play_music():
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill(WHITE)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT: 
                current_track = (current_track + 1) % len(music_files)
                play_music()
            elif event.key == pygame.K_LEFT: 
                current_track = (current_track - 1) % len(music_files)
                play_music()
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
    
    pygame.display.update()
    
pygame.quit()

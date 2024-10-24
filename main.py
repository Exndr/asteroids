import pygame
from constants import *
from player import Player



def main():
    pygame.init() #Initialize pygame

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Player object instantiation

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

    #Game Clock -> 60 FPS
    clock = pygame.time.Clock()
    dt = 0
        
    running = True
    while running:

        for event in pygame.event.get(): #Lets us close the window with "X"
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0)) #fill the screen with black, double parentheses just for colour
        player.draw(screen)
        pygame.display.flip() #refresh the screen

        dt = clock.tick(60) / 1000 # Limit to 60 frames per second


        


if __name__ == "__main__":
    main()




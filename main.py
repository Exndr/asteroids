import pygame
from constants import *



def main():
    pygame.init() #Initialize pygame

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game Clock -> 60 FPS
    clock = pygame.time.Clock()
    dt = 0
        
    running = True
    while running:

        for event in pygame.event.get(): #Lets us close the window with "X"
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0)) #fill the screen with black, double parentheses just for colour
        pygame.display.flip() #refresh the screen

        dt = clock.tick(60) / 1000 # Limit to 60 frames per second


        


if __name__ == "__main__":
    main()




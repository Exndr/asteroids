import pygame
from constants import *



def main():
    pygame.init() #Initialize pygame

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) #fill the screen with black, double parentheses just for colour
        pygame.display.flip() #refresh the screen


        

        





if __name__ == "__main__":
    main()



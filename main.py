import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock=pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()# Group object
    drawable = pygame.sprite.Group()# Group object
    Player.containers = (updatable, drawable) # Containers for Player
    PLAYER = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        updatable.update(dt)
        screen.fill("black")        
        for object in drawable:
            object.draw(screen)                
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.get_time() / 1000
        # print(dt)
        
if __name__ == "__main__":
    
    main()


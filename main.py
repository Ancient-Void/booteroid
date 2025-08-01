import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initializing pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0 # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups and Containment
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)
    
    # Initializing Player
    player = Player(
        SCREEN_WIDTH / 2, 
        SCREEN_HEIGHT / 2,
        PLAYER_RADIUS)

    # Initializing Asteroid Field
    asteroidfield = AsteroidField()

    # ======== Game Loop ========
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        for element in drawable:
            element.draw(screen)

        # Checking for collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                return

        pygame.display.flip() # refresh display
        dt = clock.tick(60)/1000
    # ========= End Loop =========

if __name__ == "__main__":
    main()

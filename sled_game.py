import pygame
import random
import game_objects as go

def sky_change(red, green, blue):
    """changes the color of the sky from black to sky blue (0, 128, 255"""
    if green < 128:
        green += 1
    if blue < 255:
        blue += 3

    return red, green, blue

pygame.init()

#setting constant variables
BLACK = (0, 0, 0)
SADDLE_BROWN = (139, 69, 19)
SPRING_GREEN = (0, 255, 127)
GREEN = (85, 107, 47)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
FPS = 30

#creating screen and clock objects
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#objects to be drawn to scene stars, 2 mountains, sun, sled
stars = [go.star(WIDTH, HEIGHT, screen)for x in range(50)]

upper_range = HEIGHT*.5
lower_range = HEIGHT*.6
trees = [go.tree(random.randint(0, WIDTH), random.randint(upper_range, lower_range),
             WIDTH, HEIGHT, GREEN, SADDLE_BROWN, screen)for x in range(100)]

mountain1 = go.mountain(0, HEIGHT//2, WIDTH, HEIGHT,
                     SPRING_GREEN, SADDLE_BROWN, screen )
mountain2 = go.mountain(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT,
                     SPRING_GREEN, SADDLE_BROWN, screen )

sun = go.sun(screen, WIDTH//10, HEIGHT//2, WIDTH//40, WIDTH, HEIGHT)

sled = go.sled(screen, 50, 400, WIDTH)

#variables for sky color change
sky_red, sky_green, sky_blue = 0, 0, 0

running = True
x_coord = 10
y_coord = HEIGHT - .25*HEIGHT
ySpeed = 0

while running:

    sled_y = sled.get_y()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ySpeed = -3
            elif event.key == pygame.K_DOWN and sled_y < HEIGHT-100:
                ySpeed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ySpeed = 0
            elif event.key == pygame.K_DOWN and sled_y >= HEIGHT-100:
                ySpeed = 0

    #Changing sky color from night to day
    sky_red, sky_green, sky_blue = sky_change(sky_red, sky_green, sky_blue)
    pygame.draw.rect(screen, (sky_red, sky_green, sky_blue), (0, 0, WIDTH, HEIGHT))

    # draws all stars in stars list to the scene
    for star1 in stars:
        star1.star_change()
        star1.draw_star()

    #draw the sun and make it rise
    sun.sun_rise()
    sun.draw_sun()

    #draw the snowy foreground
    pygame.draw.rect(screen, WHITE, (0, HEIGHT//2, WIDTH, HEIGHT//2))
    sled.draw_sled()
    sled.move_sled(ySpeed)

    #draws the 2 mountains
    mountain1.draw_mountain()
    mountain2.draw_mountain()

    #draws all trees in trees list
    for tree1 in trees:
        tree1.draw_tree()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
import pygame
import random
import game_objects as go

class mountain():
    '''mountain class to place mountain, with snow cap, at the given
       x, y coordinates representing the lower left base of the 
       mountain'''

    def __init__(self, x, y, width, height, color1, color2,display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.display = display

    def draw_mountain(self):
        WHITE = (255, 255, 255)

        point_list = ((self.x, self.y),
                      (self.x+self.width//2+WIDTH//10, self.y),
                      (self.x+(self.width//2+WIDTH//10)//2, self.y-HEIGHT//3),
                      (self.x, self.y))
        snow_list = ()
        pygame.draw.polygon(self.display, self.color1, point_list)
        pygame.draw.polygon(self.display, self.color2, point_list, 4)

class tree():
    '''tree class to place a tree at a given x, y, location correponding 
       to the lower left part of the tree'''

    def __init__(self, x, y, width, height, color1, color2, display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.display = display

    def draw_tree(self):

        width_ratio = self.width*.1
        height_ratio = self.height*.1

        position1 = ((self.x, self.y),
                   (self.x+self.width//(width_ratio//4), self.y),
                   (self.x+(self.width//(width_ratio//2)), self.y-self.height//(height_ratio//6)),
                   (self.x, self.y))

        position2 = ((self.x, self.y+(width_ratio//4)),
                     (self.x + self.width //(width_ratio//4), self.y+20),
                     (self.x + (self.width //(width_ratio//2)), (self.y - self.height //(height_ratio//6))+(height_ratio//3)),
                     (self.x, self.y+(width_ratio//4)))
        '''
        stump = [self.x+(self.width*.019),
                 self.y + (width_ratio // 4),
                 self.width//(width_ratio),
                 self.height*.03]

        pygame.draw.rect(self.display, self.color2, stump)
        '''
        pygame.draw.polygon(self.display, self.color1, position1)
        pygame.draw.polygon(self.display, self.color1, position2)

class star ():
    '''place stars in the sky at x, y locations'''

    def __init__(self, width, height,display):
        self.width = width
        self.height = height
        self.red = 255
        self.green = 255
        self.blue = 255
        self.display = display
        self.rand_x = random.randint(0, self.width)
        self.rand_y = random.randint(0, self.height//2)
        self.position = (self.rand_x, self.rand_y)

    def draw_star(self):
        color = (self.red, self.green, self.blue)
        pygame.draw.circle(self.display, color, (self.position), 2)

    def star_change(self):
        """changes the color of the stars from white to sky blue (0, 128, 255)"""
        if self.red > 0:
            self.red -= 5
        if self.green > 128:
            self.green -= 3

class sun():
    '''creates the figure, kenny, and will handle his initial location and 
       movement in the scene'''

    def __init__(self, display, x, y, radius, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.radius = 2*radius
        self.width = width
        self.height = height

    def draw_sun(self):
        '''draws the sun to the display'''
        YELLOW = (247, 228, 12)
        pygame.draw.circle(self.display, YELLOW, (self.x, self.y), self.radius)

    def sun_rise(self):
        '''creates the illusion of a sun rising'''
        if self.y > 0+self.radius+10:
            self.y -= 1

class sled():
    '''class to create and move a snowmobile'''

    def __init__(self, display, x, y, width):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.speed_x = 5
        #self.height = height

    def draw_sled(self):
        BLACK = (0, 0, 0)
        point_list1 = [[self.x, self.y + 100], [self.x + 50, self.y + 100],
                       [self.x + 60, self.y + 90], [self.x + 10, self.y + 90]]
        point_list2 = [[self.x + 70, self.y + 100], [self.x + 130, self.y + 100],
                       [self.x + 160, self.y + 70], [self.x + 160, self.y + 60],
                       [self.x + 130, self.y + 90], [self.x + 80, self.y + 90]]
        point_list3 = [[self.x + 15, self.y + 80], [self.x + 120, self.y + 80],
                       [self.x + 145, self.y + 50],[self.x + 130, self.y + 40],
                       [self.x + 110, self.y + 35], [self.x + 100, self.y + 20],
                       [self.x + 90, self.y + 20], [self.x + 100, self.y + 35],
                       [self.x + 85, self.y + 55], [self.x + 30, self.y + 55]]
        person_list = [[self.x + 85, self.y + 55], [self.x + 75, self.y + 50],
                       [self.x + 75, self.y + 45], [self.x + 85, self.y + 45],
                       [self.x + 85, self.y + 35], [self.x + 75, self.y + 35],
                       [self.x + 75, self.y + 20], [self.x + 55, self.y + 20],
                       [self.x + 55, self.y + 45], [self.x + 60, self.y + 55]]
        pygame.draw.polygon(self.display, BLACK, point_list1)
        pygame.draw.polygon(self.display, BLACK, point_list2)
        pygame.draw.polygon(self.display, BLACK, point_list3)
        pygame.draw.polygon(self.display, BLACK, person_list)
        pygame.draw.circle(self.display, BLACK, (self.x + 70, self.y + 10), 10)

    def move_sled(self):
        self.x += self.speed_x

    def bounce_sled(self):
        if self.x < 0 or self.x > self.width - 100:
            self.speed_x *= -1
            #self.x += self.speed_x

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

#objects to be drawn to scene
stars = [star(WIDTH, HEIGHT, screen)for x in range(50)]

upper_range = HEIGHT*.5
lower_range = HEIGHT*.6
trees = [tree(random.randint(0, WIDTH), random.randint(upper_range, lower_range),
             WIDTH, HEIGHT, GREEN, SADDLE_BROWN, screen)for x in range(100)]

mountain1 = mountain(0, HEIGHT//2, WIDTH, HEIGHT,
                     SPRING_GREEN, SADDLE_BROWN, screen )
mountain2 = mountain(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT,
                     SPRING_GREEN, SADDLE_BROWN, screen )

sun = sun(screen, WIDTH//10, HEIGHT//2, WIDTH//40, WIDTH, HEIGHT)

sled = sled(screen, -300, 400, WIDTH)

#variables for sky color change
sky_red, sky_green, sky_blue = 0, 0, 0

running = True
x_coord = 10
y_coord = HEIGHT - .25*HEIGHT

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                y_speed = -3
            elif event.type == pygame.K_DOWN:
                y_speed = 3

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
    sled.move_sled()
    #sled.bounce_sled()

    #draws the 2 mountains
    mountain1.draw_mountain()
    mountain2.draw_mountain()

    #draws all trees in trees list
    for tree1 in trees:
        tree1.draw_tree()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
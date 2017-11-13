import pygame
import random

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
                      (self.x+self.width//2+self.width//10, self.y),
                      (self.x+(self.width//2+self.width//10)//2, self.y-self.height//3),
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
        self.speed_y = 0
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

    def move_sled(self, speed_y):
        self.y += speed_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


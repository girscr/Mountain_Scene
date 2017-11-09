import pygame

class sled():
    '''class to create and move a snowmobile'''

    def __init__(self, display, x, y, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.speed_x = 5
        self.height = height

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
import pygame

cardImage = [pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'), pygame.image.load('r4.png'), pygame.image.load('r5.png'),
            pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'), pygame.image.load('b4.png'), pygame.image.load('b5.png'),
            pygame.image.load('g1.png'), pygame.image.load('g2.png'), pygame.image.load('g3.png'), pygame.image.load('g4.png'), pygame.image.load('g5.png'),
            pygame.image.load('y1.png'), pygame.image.load('y2.png'), pygame.image.load('y3.png'), pygame.image.load('y4.png'), pygame.image.load('y5.png')]


class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num

cardList = [Card(1,1), Card(1,1), Card(1,1), Card(1,1), Card(1,1), Card(1,2), Card(1,2), Card(1,2), Card(1,3), Card(1,3), Card(1,3), Card(1, 4), Card(1, 4), Card(1, 5),
            Card(2,1), Card(2,1), Card(2,1), Card(2,1), Card(2,1), Card(2,2), Card(2,2), Card(2,2), Card(2,3), Card(2,3), Card(2,3), Card(2, 4), Card(2, 4), Card(2, 5),
            Card(3,1), Card(3,1), Card(3,1), Card(3,1), Card(3,1), Card(3,2), Card(3,2), Card(3,2), Card(3,3), Card(3,3), Card(3,3), Card(3, 4), Card(3, 4), Card(3, 5),
            Card(4,1), Card(4,1), Card(4,1), Card(4,1), Card(4,1), Card(4,2), Card(4,2), Card(4,2), Card(4,3), Card(4,3), Card(4,3), Card(4, 4), Card(4, 4), Card(4, 5),
            ]

def getCardlist():
    return cardList[:]

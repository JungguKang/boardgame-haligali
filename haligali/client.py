#-*- coding: utf-8 -*-

import pygame
from network import Network
import card
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x ,y ,color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

"""
wait for player
show each player if its his turn
"""
def redrawWindow(win, game, p):
    win.fill((128, 128, 128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Turn!", 1, (255, 0, 0))
        font = pygame.font.SysFont("comicsans", 60)
        text2 = font.render("Opponent's Turn...", 1, (255, 0, 0))

        for btn in btns:
            btn.draw(win)

        if game.p1Turn and p == 0:
            win.blit(text, (250, 650))
        elif game.p2Turn and p == 1:
            win.blit(text, (250, 650))
        else:
            win.blit(text2, (250, 650))

        if p == 0:
            text = font.render(str(game.p1Point), 1, (0,0,0))
            win.blit(text, (50, 600))
            if not game.p1Stack:
                pass
            else:
                card1 = game.p1Stack[-1]
                win.blit(card.cardImage[(card1.color-1)*5 + card1.num-1], (300, 500))
            if not game.p2Stack:
                pass
            else:
                card2 = game.p2Stack[-1]
                win.blit(card.cardImage[(card2.color-1)*5 + card2.num-1], (300, 100))

        else:
            text = font.render(str(game.p2Point), 1, (0, 0, 0))
            win.blit(text, (50, 600))
            if not game.p2Stack:
                pass
            else:
                card2 = game.p2Stack[-1]
                win.blit(card.cardImage[(card2.color - 1) * 5 + card2.num -1], (300, 500))
            if not game.p1Stack:
                pass
            else:
                card1 = game.p1Stack[-1]
                win.blit(card.cardImage[(card1.color - 1) * 5 + card1.num -1], (300, 100))

    pygame.display.update()

btns = [Button("Bell", 250, 300, (255, 255, 0)), Button("Flip!", 550, 500, (0 , 255, 0))]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if not game.winner() == -1:
            redrawWindow(win, game, player)
            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 0 and player == 0) or (game.winner() == 1 and player == 1):
                text = font.render("You Win!", 1, (255, 0, 0))
            else:
                text = font.render("Opponent Win", 1, (255, 0, 0))
            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)
            game = n.send("reset")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos):
                        if btn.text == "Flip!" and game.isTurn(player):
                            game = n.send("flip")

                        elif btn.text == "Bell":
                            game = n.send("bell")

        redrawWindow(win, game, player)

main()


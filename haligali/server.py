#-*- coding: utf-8 -*-
import socket
from _thread import *
from game import Game
import pickle
import card
import random

#wifi ipaddress
server = "172.30.1.29"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0
clists = {}

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()

                    if data == "flip":
                        if not clists[gameId]:
                            print("out of card")
                            break
                        game.firstRing = False
                        newcard = random.choice(clists[gameId])
                        clists[gameId].remove(newcard)
                        if p == 0:
                            game.p1Stack.append(newcard)
                        else:
                            game.p2Stack.append(newcard)
                        game.nextTurn()

                    elif data == "bell":
                        if game.soloFive():
                            if game.p1Stack[-1].num == 5:
                                game.p1Stack.pop()
                            else:
                                game.p2Stack.pop()
                            if p == 0:
                                game.p1Point += 1
                                game.p1Win = True
                            else:
                                game.p2Point += 1
                                game.p2Win = True

                        elif not game.isFive():
                            if p == 0:
                                game.p2Point += 1
                                game.p1Point -= 1
                            else:
                                game.p1Point += 1
                                game.p2Point -= 1
                        elif game.isFive() and not game.firstRing:
                            game.p1Stack.pop()
                            game.p2Stack.pop()
                            if p == 0:
                                game.p1Point += 1
                                game.p1Win = True
                            else:
                                game.p2Point += 1
                                game.p2Win = True
                            game.firstRing = False
                    reply = game
                    conn.sendall(pickle.dumps(reply))

            else:
                break
        except:
            break
    print("Lost connection")
    try:
        del games[gameId]
        del clists[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        clists[gameId] = card.getCardlist()
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))

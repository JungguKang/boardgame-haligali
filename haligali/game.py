class Game:
    def __init__(self, id):
        self.p1Turn = True
        self.p2Turn = False
        self.p1Stack = []
        self.p2Stack = []
        self.p1Point = 0
        self.p2Point = 0
        self.ready = False
        self.id = id
        self.moves = []
        self.firstRing = False
        self.p1Win = False
        self.p2Win = False

    def connected(self):
        return self.ready

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Turn = True
        else:
            self.p2Turn = True

    def isTurn(self, player):
        if player == 0:
            return self.p1Turn
        else:
            return self.p2Turn

    def nextTurn(self):
        if self.p1Turn:
            self.p1Turn = False
            self.p2Turn = True
        else:
            self.p1Turn = True
            self.p2Turn = False


    def isFive(self):
        if self.p1Stack[-1].color == self.p2Stack[-1].color and self.p1Stack[-1].num + self.p2Stack[-1].num == 5:
            return True

        else:
            return False

    def soloFive(self):
        if self.p1Stack[-1].color != self.p2Stack[-1].color:
            if self.p1Stack[-1].num == 5:
                return True
            elif self.p2Stack[-1].num == 5:
                return True
            else:
                return False
        else:
            return False

    def winner(self):
        if self.p1Win:
            return 0
        elif self.p2Win:
            return 1
        else:
            return -1


    def reset(self):
        self.p1Win = False
        self.p2Win = False

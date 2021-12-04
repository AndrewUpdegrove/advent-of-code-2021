import sys
import math

class Game:
    def __init__(self, boards, draw_order):
        self.boards = boards
        self.winner = -1
        self.drawOrder = draw_order
        self.drawQueue = draw_order.copy()

    def getNextNumber(self):
        num = self.drawQueue.pop(0)
        print(num)
        return num

    def updateBoards(self, num):
        for board in self.boards:
            if num in board:
                board[board.index(num)] = -1

    def checkForWinners(self):
        for itr, board in enumerate(self.boards):
            for i in range(0,5):
                j = i * 5
                hor = sum(board[j:j+5])
                vert = sum(board[i::5])
                if hor == -5 or vert == -5:
                    self.winner = itr
                    return 1
        return 0

with open(sys.argv[1], 'r') as in_file:
    draw_order = list(map(int, in_file.readline().rstrip().split(',')))
    
    blank_line = in_file.readline()

    boards = []
    while True:
        first_line = in_file.readline()
        if not first_line:
            break
        new_board = list(map(int, first_line.rstrip().split()))
        for i in range(4):
            new_board.extend(list(map(int, in_file.readline().rstrip().split())))

        assert len(new_board) == 25
        boards.append(new_board)
        blank_line = in_file.readline()

bingo = Game(boards, draw_order)

while bingo.winner == -1:
    draw = bingo.getNextNumber()
    bingo.updateBoards(draw)
    bingo.checkForWinners()

board_sum = sum([x for x in bingo.boards[bingo.winner] if x >= 0])
answer = board_sum * draw
print(bingo.winner)
print(draw)
print(bingo.boards[bingo.winner])
print(answer)

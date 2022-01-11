import random

class Game:
    @classmethod
    def deterministic_d100(cls):
        temp = cls.deterministic_die_val
        cls.deterministic_die_val += 1
        return temp

    @classmethod
    def random_die_throw(cls, sides):
        return random.randint(1, sides)

    class Die:
        def __init__(self, sides, is_deterministic):
            self.last_roll = sides
            self.times_rolled = 0
            self.deterministic = is_deterministic
            self.sides = sides

        def roll_die(self):
            if self.deterministic:
                roll = self.last_roll + 1
                if roll > self.sides: roll -= self.sides
            else:
                roll = random.randint(1, self.sides)

            self.last_roll = roll
            self.times_rolled += 1
            return self.last_roll

    class Player:
        def __init__(self, name, start_pos):
            self.name = name
            self.pos = start_pos
            self.score = 0
            self.turns_taken = 0

        def __str__(self):
            return f"{self.name} with a score of {self.score}"


    def __init__(self, player1_start, player2_start, board_size, winning_score, determ_die, die_size):
        Game.deterministic_die_val = 1
        self.p1 = self.Player("Player 1", player1_start % board_size)
        self.p2 = self.Player("Player 2", player2_start % board_size)
        self.board_size = board_size
        self.die = self.Die(die_size, determ_die)
        self.next = self.p1
        self.winning_score = winning_score
        self.winner = None

    def roll_die(self):
        return self.die.roll_die()

    def roll_three_sum(self):
        return sum([self.roll_die() for _ in range(3)])

    def take_next_turn(self):
        to_move = self.roll_three_sum()
        new_pos = (self.next.pos + to_move) % self.board_size
        self.next.pos = new_pos
        self.next.score += new_pos if new_pos != 0 else board_size
        if self.next.score >= self.winning_score:
            self.winner = self.next
        self.advance_turn()

    def advance_turn(self):
        self.next = self.p1 if self.next == self.p2 else self.p2

    def report_condition(self):
        loser = self.p1 if self.winner == self.p2 else self.p2
        return self.die.times_rolled * loser.score



p1_start_pos = 7
p2_start_pos = 9
'''
dirac = Game(p1_start_pos, p2_start_pos, 10, 1000, True, 100)
while not dirac.winner:
    dirac.take_next_turn()


print(f'The winner was {dirac.winner}')
print(f'The reporting value is {dirac.report_condition()}')
'''



# I stole this solution because I am a big dumb cheater. I was so close and should've though longer but no
rf = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

def wins(p1,t1,p2,t2):
    if t2 <= 0: return (0,1) # p2 has won (never p1 since p1 about to move)

    w1,w2 = 0,0
    for (r,f) in rf:
        c2,c1 = wins(p2,t2,(p1+r)%10,t1 - 1 - (p1+r)%10) # p2 about to move
        w1,w2 = w1 + f * c1, w2 + f * c2
    return w1,w2


print("Bigger winner universes:",max(wins(6,21,8,21)))

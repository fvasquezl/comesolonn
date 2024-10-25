import os
import random
import time
from libs.rules import Rule

class comesolo:
    def __init__(self, rows=5):
        self.rule = Rule(rows)
        self.tablero = self.create_board(rows)

    def create_board(self, rows):
        return [1] * rows * 3
    
    def get_board_length(self):
        return len(self.tablero)
    
    def get_rules(self):
        return self.rule.get_rules()

    def get_rule(self, rule=None):
        return self.rule.get_rule(rule)
    
    def validate(self, origin, destination):
        middle = (origin + destination) // 2
        if self.tablero[origin] == 1 and self.tablero[middle] == 1 and self.tablero[destination] == 0:
            return True
        return False
    
    def move(self, origin, destination):
        middle = (origin + destination) // 2
        if self.tablero[origin] == 1 and self.tablero[middle] == 1 and self.tablero[destination] == 0:
            self.tablero[origin] = 0
            self.tablero[middle] = 0
            self.tablero[destination] = 1
            return True
        return False

    def valid_moves(self):
        movements = []
        for index, value in enumerate(self.tablero):
            print(self.tablero)
            if value == 0:
                bytes_aleatorios = os.urandom(8)
                semilla = int.from_bytes(bytes_aleatorios, byteorder="big")
                random.seed(semilla)
                randpos = random.choice(self.get_rule(index))
                if self.validate(randpos, index):
                    movements.append(randpos)
                    self.move(randpos, index)
        print(movements)
        return movements
    
    def play(self):
        boards = []
        while sum(self.tablero) != 1:
            mov = self.valid_moves()
            if len(mov) == 0:
                print('break')
                break
            boards.append(self.tablero.copy())
        print(boards)
    

if __name__ == "__main__":
    game = comesolo(5)
    game.tablero[3] = 0  # Example of modifying the board
    game.play()

     
     # Example of getting the board length
    # print(game.get_rules())
    # print(game.get_rule(2))  # Example of getting a specific rule
    # print(game.get_rule(10))  # Example of getting a non-existent rule
    # print(game.get_rule())  # Example of getting all rules
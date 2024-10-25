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
        if origin in self.get_rules(destination):
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
        movimientos_validos = []
        for destino in range(0, 15):
            for origen in range(0, 15):
                if self.movimiento_valido(destino, origen):
                    movimientos_validos.append((origen, destino))
        return movimientos_validos
    
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
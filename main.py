import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random


#         0
#       1   2
#     3   4   5
#   6   7   8   9
# 10  11  12  13  14

#         1
#       1   1
#     1   1   0
#   1   1   1   1
# 1   1   1   1   1

# array = [0,1,2,3,4,5, 6 ,7,8,9,10, 11 ,12,13,14]
        # self.reglas = [
        #                [3, 1, 0], [5, 2, 0], 
        #                [6, 3, 1], [8, 4, 1], 
        #                [7, 4, 2], [9, 5, 2], 
        #                [10, 6, 3], [12, 7, 3], [5, 4, 3], [0, 1, 3],
        #                [11, 7, 4], [13, 8, 4], 
        #                [12, 8, 5], [14, 9, 5], [3, 4, 5], [0, 2, 5], 
        #                [1, 3, 6], [8, 7, 6], 
        #                [2, 4, 7], [9, 8, 7], 
        #                [1, 4, 8], [6, 7, 8], 
        #                [2, 5, 9], [7, 8, 9], 
        #                [3, 6, 10], [12, 11, 10], 
        #                [4, 7, 11], [13, 12, 11],
        #                [3, 7, 12], [5, 8, 12], [10, 11, 12], [14, 13, 12],
        #                [4, 8, 13], [11, 12, 13], 
        #                ]

# Clase Comesolo
class Comesolo:
    def __init__(self):

        self.reglas1 = [
                       [0, 1, 3], 
                       [0, 2, 5], 
                       [1, 3, 6], 
                       [1, 4, 8],
                       [2, 4, 7], 
                       [2, 5, 9],
                       [3, 4, 5],
                       [3, 7, 12], 
                       [3, 6, 10],
                       [4, 7, 11],
                       [4, 8, 13],
                       [5, 8, 12], 
                       [5, 9, 14],
                       [6, 7, 8], 
                       [7, 8, 9],
                       [10, 11, 12], 
                       [11, 12, 13],
                       [12, 13, 14],
                       ]

        self.movimientos = []
        self.tablero = []
        self.ini_tablero()

    def ini_tablero(self):
        self.tablero = [1] * 14


    def reglas_hijo(self):
        reglas = []
        for i in range(len(self.tablero)//3):
            inicio = i * (i + 1) // 2  # funcion para calcular numeros triangulares
            hijo = inicio
            reglas.append([hijo, hijo + 1, hijo + 2])
            reglas.append([hijo, hijo + 2, hijo + 3])
           
            fin = inicio + i 
            fila = self.tablero[inicio:fin]
            fila_str = []
            for valor in fila:
                if valor == 0:
                    fila_str.append(f"\033[33m{valor}\033[0m")  # Color amarillo
                else:
                    fila_str.append(str(valor))
            print("  " * (4 - i) + "   ".join(fila_str))


            
    
    def printTablero(self):
        print(self.tablero)

    def juego_terminado(self):
        return self.tablero.count(1) <= 1
        
    def add_movimiento(self):
         self.movimientos.append(self.tablero.copy())

    def primer_movimiento(self, movimiento: int) -> None:
        # Verifica que las posiciones sean válidas
        if not (0 <= movimiento <= 14):
            print("movimiento invalido")
            return
        else:
            self.tablero[movimiento] = 0
            self.add_movimiento()

    def update_tablero(self, movimiento):
        origen, intermedia, destino = movimiento
        self.tablero[origen] = 0
        self.tablero[intermedia] = 0
        self.tablero[destino] = 1

    def realizar_movimiento(self) -> None:
        while True:
            origen = 4
            destino = 1
            intermedia = (origen + destino) // 2
            movimiento = [origen, intermedia, destino]
            if self.movimiento_valido(movimiento):
                self.update_tablero(movimiento)
                self.add_movimiento()

            if self.juego_terminado():
                break
    

    def movimiento_valido(self,movimiento):
        origen , intermedia, destino = movimiento
        if not (0 <= destino <= 14 and 0 <= origen <= 14):       
            return movimiento in self.reglas
        return False

    def jugar(self):
        while True:
            bytes_aleatorios = os.urandom(8)
            semilla = int.from_bytes(bytes_aleatorios, byteorder="big")
            random.seed(semilla)
            
            # Obtener valores aleatorios entre 1 y 15 para origen y destino
            origen = random.randint(1, 15)
            destino = random.randint(1, 15)
            tablero = self.tablero

            nuevo_dato = tablero + [origen, (origen + destino) // 2, destino]
            nuevo_dato_tensor = torch.tensor(nuevo_dato, dtype=torch.float32).view(1, -1)

            with torch.no_grad():
                prediccion = self.modelo(nuevo_dato_tensor)
                prediccion = (prediccion > 0.5).float()

            if prediccion.item() == 1.0:
                if self.movimiento_valido(destino, origen):
                    self.realizar_movimiento(origen, destino)
                    print(f"Movimiento realizado: origen={origen}, destino={destino}")
                else:
                    print(f"Movimiento inválido según las reglas del juego: origen={origen}, destino={destino}")
            else:
                print(f"Predicción del modelo: movimiento no válido: origen={origen}, destino={destino}")
            
            # Condición de salida del bucle (ajusta según tu lógica)
            if self.juego_terminado():
                print("El juego ha terminado.")
                break

if __name__ == "__main__":

    juego = Comesolo()
    juego.reglas_hijo()
    # juego.realizar_movimiento()
    # print(juego.movimientos)
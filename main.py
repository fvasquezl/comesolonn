import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

# '''
# La inteligencia artificial son los intentos de replicar la inteligencia humana en sistemas artificiales.

# Machine learning son las técnicas de aprendizaje automático, en donde mismo sistema aprende como encontrar una respuesta sin que alguien lo este programando.

# Deep learning es todo lo relacionado a las redes neuronales. Se llama aprendizaje profundo porque a mayor capas conectadas ente sí se obtiene un aprendizaje más fino. __ En el Deep learning existen dos grandes problemas:
# Overfitting: Es cuando el algoritmo "memoriza" los datos y la red neuronal no sabe generalizar.
# Caja negra: Nosotros conocemos las entradas a las redes neuronales. Sim embargo, no conocemos que es lo que pasa dentro de las capas intermedias de la red
# '''

# class RedNeuronal(nn.Module):
#     def __init__(self):
#         super(RedNeuronal, self).__init__()
#         self.fc1 = nn.Linear(18, 64)  # Cambiado a 18 para incluir intermedia
#         self.fc2 = nn.Linear(64, 32)
#         self.fc3 = nn.Linear(32, 1)
#         self.sigmoid = nn.Sigmoid()

#     def forward(self, x):
#         x = torch.relu(self.fc1(x))
#         x = torch.relu(self.fc2(x))
#         x = self.sigmoid(self.fc3(x))
#         return x

# def generar_datos_entrenamiento(num_ejemplos):
#     datos = []
#     etiquetas = []
#     for _ in range(num_ejemplos):
#         tablero, origen, intermedia, destino = generar_movimiento_valido()
#         datos.append(np.concatenate((tablero, [origen, intermedia, destino])))
#         etiquetas.append(1)  # Todos los movimientos generados son válidos
#     return np.array(datos), np.array(etiquetas)

# def generar_movimiento_valido():
#     while True:
#         tablero = np.random.randint(2, size=15)
#         origen = np.random.randint(1, 16)
#         destino = np.random.randint(1, 16)
#         intermedia = (origen + destino) // 2
#         if movimiento_valido(tablero, destino, origen):
#             return tablero, origen, intermedia, destino

# def movimiento_valido(tablero, destino, origen):
#     if not (1 <= destino <= 15 and 1 <= origen <= 15):
#         return 0
#     intermedia = (destino + origen) // 2
#     if (
#         tablero[destino - 1] == 0
#         and tablero[intermedia - 1] != 0
#         and tablero[origen - 1] != 0
#     ):
#         reglas = [
#              [6, 4, 1],
#              [9, 7, 2],
#              [10, 8, 3],
#              [6, 1, 4],
#              [13, 11,4],
#              [14, 12,5],
#              [4, 1, 6],
#              [15, 13,6],
#              [9, 2, 7],
#              [10, 3, 8],
#              [7, 2, 9],
#              [8, 3, 10],
#              [13, 4, 11],
#              [14, 5, 12],
#              [6, 4, 13],
#              [15, 11,13],
#              [12, 5, 14],
#              [13, 6, 15],
#         ]
#         return 1 if origen in reglas[destino] else 0
#     return 0

# # Crear la red neuronal
# modelo = RedNeuronal()
# criterio = nn.BCELoss()
# optimizador = optim.Adam(modelo.parameters(), lr=0.001)

# # Generar datos de entrenamiento
# datos, etiquetas = generar_datos_entrenamiento(1000)

# # Convertir datos a tensores
# datos_tensor = torch.tensor(datos, dtype=torch.float32)
# etiquetas_tensor = torch.tensor(etiquetas, dtype=torch.float32).view(-1, 1)

# # Entrenar la red neuronal
# num_epochs = 100
# for epoch in range(num_epochs):
#     modelo.train()
#     optimizador.zero_grad()
#     salidas = modelo(datos_tensor)
#     perdida = criterio(salidas, etiquetas_tensor)
#     perdida.backward()
#     optimizador.step()
#     if (epoch + 1) % 10 == 0:
#         print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {perdida.item():.4f}')

# # Guardar el modelo entrenado
# torch.save(modelo.state_dict(), 'modelo_entrenado.pth')
# print("Modelo entrenado guardado como 'modelo_entrenado.pth'")

# modelo = RedNeuronal()
# modelo.load_state_dict(torch.load('modelo_entrenado.pth'))
# modelo.eval()

# # Datos de prueba
# tablero = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# origen = 3
# destino = 8
# intermedia = (origen + destino) // 2  # Calcular la posición intermedia
# nuevo_dato = tablero + [origen, intermedia, destino]
# nuevo_dato_tensor = torch.tensor(nuevo_dato, dtype=torch.float32).view(1, -1)

# # Realizar la predicción
# with torch.no_grad():
#     prediccion = modelo(nuevo_dato_tensor)
#     prediccion = (prediccion > 0.5).float()

# if prediccion.item() == 1.0:
#     print("El movimiento es válido.")
# else:
#     print("El movimiento no es válido.")
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




# Clase Comesolo
class Comesolo:
    def __init__(self):
        self.reglas = [
                       [3, 1, 0], [5, 2, 0], 
                       [6, 3, 1], [8, 4, 1], 
                       [7, 4, 2], [9, 5, 2], 
                       [10, 6, 3], [12, 7, 3], [5, 4, 3], [0, 1, 3],
                       [11, 7, 4], [13, 8, 4], 
                       [12, 8, 5], [14, 9, 5], [3, 4, 5], [0, 2, 5], 
                       [1, 3, 6], [8, 7, 6], 
                       [2, 4, 7], [9, 8, 7], 
                       [1, 4, 8], [6, 7, 8], 
                       [2, 5, 9], [7, 8, 9], 
                       [3, 6, 10], [12, 11, 10], 
                       [4, 7, 11], [13, 12, 11],
                       [3, 7, 12], [5, 8, 12], [10, 11, 12], [14, 13, 12],
                       [4, 8, 13], [11, 12, 13], 
                       ]
        self.movimientos = []
        self.tablero = []
        self.ini_tablero()

    def suma(self):
        for regla in self.reglas:
            print(sum(regla)//3)

    def ini_tablero(self):
        self.tablero = [1] * 15
    
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
    juego.suma()
    # juego.realizar_movimiento()
    # print(juego.movimientos)
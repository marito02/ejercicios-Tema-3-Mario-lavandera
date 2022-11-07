#Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], regla de Sarrus
#de forma recursiva y de forma iterativa

import numpy as np
from typing import Any

#forma iterativa

def constructor(matriz):
    matriz=np.array([[3,5,1],[7,4,9],[2,5,4]])
    determinante=np.linealg.det(matriz)
    return determinante

#forma recursiva

class Matrix():
    def __init__(self, rows:list[list[int]]):
        error=TypeError()
        if len(rows) !=0:
            cols = len(rows[0])
            if cols == 0:
                raise error
            for row in rows:
                if len(row) != cols:
                    raise error
                for value in row:
                    if not isinstance(value, (int, float())):
                        raise error
                self.rows = rows
        else:
            self.rows = []

#info de la matriz

    def columns(self) -> list[list[int]]:
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]
    def num_rows(self) -> int:
        return len(self.rows)
    def num_columns(self) -> int:
        return len(self.rows[0])
    def order(self) -> tuple[int, int]:
        return (self.num_rows, self.num_columns)
    def is_square(self) -> bool:
        return self.order[0] == self.order[1]
    def identity(self):
        values = [
            [0 if column_num != row_num else 1 for column_num in range(self.num_rows)]
            for row_num in range(self.num_rows)
        ]
        return Matrix(values)
    def determinante(self) -> int:
        if not self.is_square:
            return 0
        if self.order == (0, 0):
            return 1
        if self.order == (1, 1):
            return int(self.rows[0][0])
        if self.order == (2, 2):
            return int(
                (self.rows[0][0] * self.rows[1][1])
                - (self.rows[0][1] * self.rows[1][0])
            )
        else:
            return sum(
                self.rows[0][column] * self.cofactors().rows[0][column]
                for column in range(self.num_columns)
            )


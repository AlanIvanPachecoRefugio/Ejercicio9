class Robot:
    def __init__(self, rejilla):
        self.rejilla = rejilla
        self.filas = len(rejilla)
        self.columnas = len(rejilla[0])
        self.ruta = []

    def es_movimiento_valido(self, x, y, visitado):
        return (0 <= x < self.filas and 0 <= y < self.columnas and 
                not visitado[x][y] and self.rejilla[x][y] == 0)

    def encontrar_ruta(self):
        visitado = [[False for _ in range(self.columnas)] for _ in range(self.filas)]
        if self.dfs(0, 0, visitado):
            return self.ruta
        else:
            return None

    def dfs(self, x, y, visitado):
        if x == self.filas - 1 and y == self.columnas - 1:
            self.ruta.append((x, y))
            return True
        
        if self.es_movimiento_valido(x, y, visitado):
            visitado[x][y] = True
            self.ruta.append((x, y))

            # Movimiento a la derechaaa
            if self.dfs(x, y + 1, visitado):
                return True
            # Mover para abajo
            if self.dfs(x + 1, y, visitado):
                return True

            # se retrocede si no hay una ruta adecuada
            self.ruta.pop()
            visitado[x][y] = False

        return False

# Ejemplo de uso
rejilla = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0]
]

robot = Robot(rejilla)
ruta = robot.encontrar_ruta()

if ruta:
    print("Se encontró una ruta:)", ruta)
else:
    print("No se encontró una ruta :(")

class RubiksCube:
    def __init__(self):
        # Representación del cubo como una matriz tridimensional
        # Cada cara del cubo se representa con un número:
        # 0: Blanco, 1: Rojo, 2: Verde, 3: Azul, 4: Naranja, 5: Amarillo
        self.cube = [
            # Cara superior
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            # Cara frontal
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            # Cara derecha
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
     

    def __str__(self):
        # Representación visual del cubo
        result = ""
        for face in self.cube:
            result += "    " + " ".join([str(color) for row in face for color in row]) + "\n"
        return result

# Crear un cubo de Rubik y mostrar su estado inicial
cube = RubiksCube()
print(cube)
import json

class Cube:
    def __init__(self, file_path=None):
        if file_path:
            self.load_cube_from_file(file_path)
        else:
            print("No se cargó el cubo")

    def __str__(self):
        result = ""
        for i in range(3):
            result += '      ' + ' '.join(self.cube['U'][i]) + '\n'
        for i in range(3):
            result += ' '.join(self.cube['L'][i]) + ' ' + ' '.join(self.cube['F'][i]) + ' ' + ' '.join(self.cube['R'][i]) + ' ' + ' '.join(self.cube['B'][i]) + '\n'
        for i in range(3):
            result += '      ' + ' '.join(self.cube['D'][i]) + '\n'
        return result

    def load_cube_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.cube = data

    def is_solved(self):
      for face in self.cube.values():
          center_color = face[1][1]
          for row in face:
              for square in row:
                  if square != center_color:
                      return False
      return True
    def solve(self):
            # Algoritmo A* para resolver el cubo
            open_set = [(0, self.cube)]
            closed_set = set()

            while open_set:
                # Extraer el estado con el menor costo estimado
                current_cost, current_cube = heapq.heappop(open_set)

                # Verificar si el cubo actual es la solución
                if current_cube.is_solved():
                    return current_cube

                # Generar los posibles movimientos
                possible_moves = current_cube.generate_possible_moves()

                for move in possible_moves:
                    # Aplicar el movimiento al cubo actual
                    new_cube = copy.deepcopy(current_cube)
                    new_cube.apply_move(move)

                    # Calcular el costo del movimiento
                    cost = current_cost + 1  # Costo uniforme

                    # Agregar el nuevo estado al conjunto abierto si no está en el conjunto cerrado
                    if new_cube not in closed_set:
                        heapq.heappush(open_set, (cost, new_cube))
                        closed_set.add(new_cube)

    def rotate_face_clockwise(self, face):
        face_copy = [list(row) for row in face]
        for i in range(3):
            for j in range(3):
                face[i][j] = face_copy[2 - j][i]

    def rotate_face_counterclockwise(self, face):
        face_copy = [list(row) for row in face]
        for i in range(3):
            for j in range(3):
                face[i][j] = face_copy[j][2 - i]

    def U(self):
        print("Moving: Up face clockwise")
        self.rotate_face_clockwise(self.state['U'])
        temp = self.state['F'][0]
        self.state['F'][0] = self.state['R'][0]
        self.state['R'][0] = self.state['B'][0]
        self.state['B'][0] = self.state['L'][0]
        self.state['L'][0] = temp

    def U_r(self):
        print("Moving: Up face counterclockwise")
        self.rotate_face_counterclockwise(self.state['U'])
        temp = self.state['F'][0]
        self.state['F'][0] = self.state['L'][0]
        self.state['L'][0] = self.state['B'][0]
        self.state['B'][0] = self.state['R'][0]
        self.state['R'][0] = temp

    def F(self):
        print("Moving: Front face clockwise")
        self.rotate_face_clockwise(self.state['F'])
        temp = [row[0] for row in self.state['R']][::-1]
        for i in range(3):
            self.state['R'][i][0] = self.state['U'][2][i]
            self.state['U'][2][i] = self.state['L'][i][2]
            self.state['L'][i][2] = self.state['D'][0][i]
            self.state['D'][0][i] = temp[i]

    def F_r(self):
        print("Moving: Front face reverse clockwise")
        self.rotate_face_counterclockwise(self.state['F'])
        temp = [row[0] for row in self.state['R']]
        for i in range(3):
            self.state['R'][i][0] = self.state['D'][0][i]
            self.state['D'][0][i] = self.state['L'][i][2]
            self.state['L'][i][2] = self.state['U'][2][i]
            self.state['U'][2][i] = temp[i]

    def L(self):
        print("Moving: Left face clockwise")
        self.rotate_face_clockwise(self.state['L'])
        temp = [row[0] for row in self.state['F']]
        for i in range(3):
            self.state['F'][i][0] = self.state['U'][i][0]
            self.state['U'][i][0] = self.state['B'][2 - i][2]
            self.state['B'][2 - i][2] = self.state['D'][i][0]
            self.state['D'][i][0] = temp[i]

    def L_r(self):
        print("Moving: Left face reverse clockwise")
        self.rotate_face_counterclockwise(self.state['L'])
        temp = [row[0] for row in self.state['F']][::-1]
        for i in range(3):
            self.state['F'][i][0] = self.state['D'][i][0]
            self.state['D'][i][0] = self.state['B'][2 - i][2]
            self.state['B'][2 - i][2] = self.state['U'][i][0]
            self.state['U'][i][0] = temp[i]

    def R(self):
        print("Moving: Right face clockwise")
        self.rotate_face_clockwise(self.state['R'])
        temp = [row[0] for row in self.state['F']]
        for i in range(3):
            self.state['F'][i][2] = self.state['D'][i][2]
            self.state['D'][i][2] = self.state['B'][2 - i][0]
            self.state['B'][2 - i][0] = self.state['U'][i][2]
            self.state['U'][i][2] = temp[i]

    def R_r(self):
        print("Moving: Right face revert clockwise")
        self.rotate_face_counterclockwise(self.state['R'])
        temp = [row[2] for row in self.state['F']][::-1]
        for i in range(3):
            self.state['F'][i][2] = self.state['U'][i][2]
            self.state['U'][i][2] = self.state['B'][2 - i][0]
            self.state['B'][2 - i][0] = self.state['D'][i][2]
            self.state['D'][i][2] = temp[i]

    def D(self):
        print("Moving: Down face clockwise")
        self.rotate_face_clockwise(self.state['D'])
        temp = self.state['F'][2]
        self.state['F'][2] = self.state['L'][2]
        self.state['L'][2] = self.state['B'][2]
        self.state['B'][2] = self.state['R'][2]
        self.state['R'][2] = temp

    def D_r(self):
        print("Moving: Down face reverse clockwise")
        self.rotate_face_counterclockwise(self.state['D'])
        temp = self.state['F'][2]
        self.state['F'][2] = self.state['R'][2]
        self.state['R'][2] = self.state['B'][2]
        self.state['B'][2] = self.state['L'][2]
        self.state['L'][2] = temp

    def B(self):
        print("Moving: Back face clockwise")
        self.rotate_face_clockwise(self.state['B'])
        temp = [row[2] for row in self.state['L']][::-1]
        for i in range(3):
            self.state['L'][i][2] = self.state['U'][0][2 - i]
            self.state['U'][0][2 - i] = self.state['R'][2 - i][0]
            self.state['R'][2 - i][0] = self.state['D'][2][i]
            self.state['D'][2][i] = temp[i]

    def B_r(self):
        print("Moving: Back face reverse clockwise")
        self.rotate_face_counterclockwise(self.state['B'])
        temp = [row[2] for row in self.state['L']]
        for i in range(3):
            self.state['L'][i][2] = self.state['D'][2][i]
            self.state['D'][2][i] = self.state['R'][2 - i][0]
            self.state['R'][2 - i][0] = self.state['U'][0][2 - i]
            self.state['U'][0][2 - i] = temp[i]        
            return None

    def load_cube_from_lines(self, lines):
        cube_dict = {}
        for line in lines:
            line = line.strip()  # Eliminar espacios en blanco al inicio y al final
            if line:
                face_name, face_colors = line.split(':')
                face_name = face_name.strip()
                face_colors = face_colors.strip().replace('[', '').replace(']', '').replace("'", '').split(',')
                face = [face_colors[i:i+3] for i in range(0, len(face_colors), 3)]
                cube_dict[face_name] = face
        self.cube = cube_dict

    def validate_cube(self):
        colors_count = {}
        for face in self.cube.values():
            center_color = face[1][1]
            colors_count[center_color] = colors_count.get(center_color, 0) + 1

        if len(colors_count) != 6:
            print("El cubo no tiene exactamente 6 colores únicos en los centros.")
            return False

        for count in colors_count.values():
            if count != 1:
                print("El cubo tiene al menos un centro de color duplicado.")
                return False

        for face in self.cube.values():
            if len(face) != 3:
                print("Al menos una cara del cubo no tiene exactamente 3 filas.")
                return False
            for row in face:
                if len(row) != 3:
                    print("Al menos una fila del cubo no tiene exactamente 3 elementos.")
                    return False
        print("El cubo cumple con todas las validaciones.")
        return True

def main():
    cube = Cube()

    while True:
        print("\nMenu:")
        print("1. Cargar cubo desde un archivo")
        print("2. Mostrar cubo")
        print("3. Resolver cubo")
        print("4. Validaciones")
        print("5. Esta resuelto?")        
        print("6. Salir")

        option = input("Selecciona una opcion: ")

        if option == "1":
            filename = input("Ingrese el nombre del archivo: ")
            try:
                cube.load_cube_from_file(filename)
                print("¡Cubo cargado exitosamente!")
            except (FileNotFoundError, ValueError) as e:
                print(f"Error al cargar el cubo: {e}")
        elif option == "2":
            print(cube)
        elif option == "3":
            if cube.solve():
              print("se resolvio el cubo.")
            else:
              print("Aún no se implementa la función para resolver el cubo.")
        elif option == "4":
            if cube.validate_cube():
                print("El cubo cumple con todas las validaciones.")
            else:
                print("El cubo no cumple con todas las validaciones.")
        elif option == "5":
            if cube.is_solved():
                print("El cubo esta resuelto.")
            else:
                print("El cubo no esta resuelto.")
        elif option == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

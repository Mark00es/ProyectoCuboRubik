class RubiksCube:
    def __init__(self, file_path=None):
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.load_cube_from_lines(lines)  # Utilizar un método para cargar el cubo desde las líneas del archivo
        else:
            print("No se cargó el cubo")

    def __str__(self):
        cube_str = ""
        for face in self.cube:
            for row in face:
                cube_str += " ".join(row) + "\n"
            cube_str += "\n"
        return cube_str

    def is_solved(self):
        for face in self.cube:
            center_color = face[1][1]
            for row in face:
                for square in row:
                    if square != center_color:
                        return False
        return True

    def load_cube_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.load_cube_from_lines(lines)

    def load_cube_from_lines(self, lines):
        self.cube = eval(''.join(lines))

    def solve_cube(self):
        # Aquí implementa la lógica para resolver el cubo
        # Por ahora, solo imprimir un mensaje indicando que esta función aún no está implementada
        print("Función para resolver el cubo aún no implementada.")

    def validate_cube(self):
        # Verificar si hay más de un centro de un color
        colors_count = {}
        for face in self.cube:
            center_color = face[1][1]
            colors_count[center_color] = colors_count.get(center_color, 0) + 1

        for count in colors_count.values():
            if count != 1:
                return False

        # Verificar que no falte ni sobre alguna pieza o cara (color)
        if len(self.cube) != 6:
            return False

        for face in self.cube:
            if len(face) != 3:
                return False
            for row in face:
                if len(row) != 3:
                    return False

        return True


def main():
    cube = None  # Inicializamos la variable cube fuera del bucle

    while True:
        print("\nMenu:")
        print("1. Cargar cubo desde un archivo")
        print("2. Mostrar cubo")
        print("3. Resolver cubo")
        print("4. Validaciones")
        print("5. Salir")

        option = input("Selecciona una opcion: ")

        if option == "1":
            filename = input("Ingrese el nombre del archivo: ")
            try:
                cube = RubiksCube(filename)  # Almacenamos la instancia de RubiksCube creada en cube
                print("¡Cubo cargado exitosamente!")
            except (FileNotFoundError, ValueError) as e:
                print(f"Error al cargar el cubo: {e}")
        elif option == "2":
            if cube:  # Verificamos si el cubo ha sido cargado antes de mostrarlo
                print(cube)
            else:
                print("Primero debes cargar un cubo.")
        elif option == "3":
            if cube:  # Verificamos si el cubo ha sido cargado antes de resolverlo
                cube.solve_cube()
            else:
                print("Primero debes cargar un cubo.")
        elif option == "4":
            if cube:  # Verificamos si el cubo ha sido cargado antes de realizar las validaciones
                if cube.validate_cube():
                    print("El cubo cumple con todas las validaciones.")
                else:
                    print("El cubo no cumple con todas las validaciones.")
            else:
                print("Primero debes cargar un cubo.")
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

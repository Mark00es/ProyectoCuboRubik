# Cubo de Rubik Solver

Este proyecto es una implementación en Python de un solucionador de Cubo de Rubik utilizando el algoritmo A\*.

## Uso

1. Ejecuta el script `main.py`.
2. Selecciona las opciones del menú para cargar un cubo desde un archivo, mostrar el cubo, resolver el cubo, realizar validaciones o verificar si el cubo está resuelto.

## Archivos

- `cube.py`: El módulo que define la clase `Cube` para representar el Cubo de Rubik y sus operaciones.
- Otros archivos(cube_config.txt): Archivos de entrada de ejemplo para cargar el cubo en un estado.

## Autor

Marco Fernando Escobar Herrada

## Modelo

Se implemento el cubo en un diccionario 3x3x3 pero para poder realizar los movimientos se hizo una transformación a un tipo de 2D
mediante la forma:
W W W
W W W
W W W
O O O G G G R R R B B B
O O O G G G R R R B B B
O O O G G G R R R B B B
Y Y Y
Y Y Y
Y Y Y
Se intento implementar una heuristica con distancias, tambien se considero poner pesos a las esquias pero en ese intento no movia ni una pieza

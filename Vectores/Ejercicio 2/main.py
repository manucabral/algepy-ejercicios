"""
    Sean R(1, 1, 4) y S(3, 0, 2) dos puntos en R3, hallar los componentes del vector RS y calcular su distancia.
"""

from algepy import Point, Vector, Plot

# Definimos los puntos
R = Point(x=1, y=1, z=4)
S = Point(x=3, y=0, z=2)

# Obtenemos el vector a partir de los dos puntos
RS = R.find_vector(other=S)

# Utilizamos el método magnitude para calcular su distancia
distancia = RS.magnitude()

print(f'La distancia es {distancia}')

"""
    Sean R(1, 1, 4) y S(3, 0, 2) dos puntos en R3, hallar los componentes del vector RS.
"""

from algepy import Point, Vector, Plot

# Definimos los puntos
R = Point(x=1, y=1, z=4)
S = Point(x=3, y=0, z=2)

# Obtenemos el vector a partir de los dos puntos
RS = R.find_vector(other=S)

# Creamos un gráfico
grafico = Plot(projection='3d')

# Añadimos los puntos al gráfico
grafico.add_point(R, color='red')
grafico.add_point(S, color='blue')

# Añadimos al vector resultante al gráfico y le definimos su origen en el punto R
grafico.add_vector(RS, color='green', origin=R)

grafico.show()

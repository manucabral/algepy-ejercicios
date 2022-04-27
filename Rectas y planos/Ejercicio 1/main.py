"""
    Encuentre las ecuaciones paramétricas de la recta, si existe, que sea paralela
    al plano π: 3x -y -4z + 16 = 0 y al plano π2: xy que pase por el punto (2, 0, 3)
"""

from algepy import Line, Point, Vector, Plot, Plane

# Definimos los vectores normales de los planos
n1 = Vector(x=3, y=-1, z=-4)
n2 = Vector(x=0, y=0, z=1)

# Asignamos el punto por donde pasan los dos planos
p = Point(x=2, y=0, z=3)

# Definimos los planos y los identificamos con el punto p
π = Plane(normal=n1, point=p)
π2 = Plane(normal=n2, point=p)

"""
    Calculamos el producto vectorial entre los vectores normales con esto obtenemos el vector director 
    de la recta de intersección, este es paralela a los dos planos previamente definidos.
"""
v = n1.cross(n2)

# Definimos la recta mediante v y el punto p
r = Line(vector=v, point=p)

# Creamos un grafico con rango -5 a 5 en (x, y)
grafico = Plot(projection='3d', xrange=(-5, 5), yrange=(-5, 5))

# Añadimos los planos
grafico.add_plane(π, color='blue')
grafico.add_plane(π2, color='red')

# Añadimos los vectores normales de cada plano
grafico.add_vector(vector=n2, origin=p, color='red')
grafico.add_vector(vector=n1, origin=p, color='blue')

# Añadimos la recta y también su vector director
grafico.add_line(line=r, color='green')
grafico.add_vector(vector=v, origin=p, color='green')

grafico.show()

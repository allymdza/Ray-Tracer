from vectores import vectores
class plano:

    def __init__(self, punto, normal):
        self.punto = punto
        self.normal = normal

    def intersecciona(self, rayo)
        denom = rayo.direccion.producto_punto(self.normal) #si el rayo toca la normal (el producto punto es 0), es perpendicular al plano. no se tocan el rayo y plano
        if abs(denom) < (1e-8): #usamos abs para que no importe la direccion y un numero muy pequeño en vez de cero para prevenir los probelmas con el 0 y los decimales
            return False 

        """Dado la normal(A,B,C) y un vector en el plano (x,y,x) la formula de un plano Ax + By + Cz + D = 0 la podemos ver como n•v = D (nace de n•v = 0 pues son perpendiculares, D sigue siendo una const)
        Como el vector que nos interesa es el rayo sustituimos (con la parametrica) tal que n•(Q + td) = D.
        Despejamos para encontrar t y quedamos con t = D-n•Q/n•d"""

        """veamos que nos falta D. Tomamos el punto que sabemos esta en el plano tal que D = punto • normal"""

        D = self.punto.producto_punto(self.normal)
        t = D - (self.normal.producto_punto(rayo.origen)) / denom

       return t > 0.001 #0.001 para cuidar decimales
       """si es 0 estan justo en el mismo lugar, puede provocar errores
       si es menor que cero esta atras del rayo"""
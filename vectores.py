
import math

class vectores:
    # definimos un margen de error para realizar las comparaciones entre parámetros (0.00001)
    EPSILON = 1e-5

    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def suma_vectores(self, vector2):

        return vectores(self.x+vector2.x, self.y+vector2.y, self.z+vector2.z)

    def resta_vectores(self, vector2):

        return vectores(self.x-vector2.x, self.y-vector2.y, self.z-vector2.z)

    def producto_escalar(self, escalar: float):

        return vectores(self.x*escalar, self.y*escalar, self.z*escalar)

    def producto_punto(self, vector2):

        return (self.x*vector2.x) + (self.y*vector2.y) + (self.z*vector2.z)

    def norma_vector(self):

        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def normalizar_vector(self):

        return vectores(self.x / self.norma_vector(), self.y / self.norma_vector(), self.z / self.norma_vector())

    #metodo para poder comprar objetos de tipo vector
    def __eq__(self, otro):
        if isinstance(otro, vectores):
            return (
                math.isclose(self.x, otro.x, abs_tol=self.EPSILON)
                and math.isclose(self.y, otro.y, abs_tol=self.EPSILON)
                and math.isclose(self.z, otro.z, abs_tol=self.EPSILON)
            )
        return False

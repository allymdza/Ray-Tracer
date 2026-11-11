
import math

class vectores:

    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def suma_vectores(self, vector2):
        x1 = self.x
        y1 = self.y
        z1 = self.z

        x2 = vector2.x
        y2 = vector2.y
        z2 = vector2.z

        suma = vectores(x1 + x2, y1 + y2, z1 + z2)
        return suma

    def resta_vectores(self, vector2):
        x1 = self.x
        y1 = self.y
        z1 = self.z
    
        x2 = vector2.x
        y2 = vector2.y
        z2 = vector2.z
    
        resta = vectores(x1 - x2, y1 - y2, z1 - z2)
        return resta
    
    def producto_escalar(self, escalar: int):
        x = self.x
        y = self.y
        z = self.z

        resultado = vectores(x * escalar, y * escalar, z * escalar)
        return resultado

    def producto_punto(self, vector2):
        x1 = self.x
        y1 = self.y
        z1 = self.z
            
        x2 = vector2.x
        y2 = vector2.y
        z2 = vector2.z

        resultado = (x1 * x2) + (y1 * y2) + (z1 * z2)
        return resultado

    def norma_vector(self):
        x = self.x
        y = self.y
        z = self.z
        
        norma = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
        return norma
    
    def normalizar_vector(self):
        x = self.x
        y = self.y
        z = self.z

        norma = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))

        resultado = vectores(x / norma, y / norma, z / norma)
        return resultado

    #metodo para poder comprar objetos de tipo vector
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y and self.z == otro.z    

        
        

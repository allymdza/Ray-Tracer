
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
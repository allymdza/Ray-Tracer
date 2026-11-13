from vectores import vectores
class esfera:

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
        #self.color = color 

    def intersecciona(self, rayo):
        oc = self.centro.resta_vectores(rayo.origen) #vector distancia desde el origen del rayo al centro de la esfera
        """a,b,c con base a la formual general para t con t^2d•d - 2td•(C-Q)+(C-Q)•(C-Q)-r^2 = 0
        La formula sale de (C-P)•(C-P)=r^2 (la formula para ver si un vector pasa por la esfera) usando P(T) = Q + td (el rayo) como nuestro vector de interes
         """
        a = rayo.direccion.producto_punto(rayo.direccion)
        b = rayo.direccion.producto_punto(oc) * -2.0
        c = oc.producto_punto(oc) - (self.radio * self.radio) 
        discriminante = (b * b) - (4*a*c)

        return discriminante >= 0
        """si > 0, se tiene dos soluciones, entra y sale de la esfera
        si = 0 solo roza la esfera
        si < 0 no toca la esfera nunca"""
    
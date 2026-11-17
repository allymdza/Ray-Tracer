from vectores import vectores
from math import sqrt

class esfera:

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
        #self.color = color 

    def intersecciona(self, rayo, hit_info, tmin = 0.001, tmax= float("inf")):
        oc = self.centro.resta_vectores(rayo.origen) #vector distancia desde el origen del rayo al centro de la esfera
        """a,b,c con base a la formual general para t con t^2d•d - 2td•(C-Q)+(C-Q)•(C-Q)-r^2 = 0
        La formula sale de (C-P)•(C-P)=r^2 (la formula para ver si un vector pasa por la esfera) usando P(T) = Q + td (el rayo) como nuestro vector de interes
         """
        a = rayo.direccion.producto_punto(rayo.direccion)
        b = rayo.direccion.producto_punto(oc) * -2.00
        c = oc.producto_punto(oc) - (self.radio * self.radio) 
        discriminante = (b * b) - (4*a*c)

        if discriminante < 0:  #si esto pasa el rayo nunca toca la esfera
            return False

        raiz = sqrt(discriminante)

        t = (-b - raiz) / (2.00 * a)  #primera solucion: la entrada 
        if t < tmin or tmax < t: #si se pasa del limite
            t = (-b + raiz) / (2.00 * a) #vemos la segunda solucion: la salida. (puede pasar que el rayo solo salga y no entre a la esfera. cuando raiz = 0 sirve como doble comprobacion) 
            if t < tmin or tmax < t: #si se pasa del limite
                return False

        hit_info.t = t
        hit_info.p = rayo.parametrica(t)

        return True

        
        
    
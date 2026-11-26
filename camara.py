import math
from vectores import vectores

class imagen:

    def __init__(self, altura, ancho):
        if altura < 1 or ancho < 1:
            raise ValueError("No se puede generar la imagen")
        self.altura = altura
        self.ancho = ancho
        self.ratio = ancho/altura

class camara:

    def __init__(self, posicion, mirar_a, fov):
        self.posicion = posicion
        self.mirar_a = mirar_a
        self.fov = fov
        self.vup = vectores(0,1,0)

        self.viewport_delta_vertical = None
        self.viewport_delta_horizontal = None
        self.pixel_centro = None


    def calcular_viewport(self,imagen):

        #conviertiendo camara al origen
        w = self.posicion.resta_vectores(self.mirar_a).normalizar_vector() #atras, eje z. objeto -> camara
        u = self.vup.producto_cruz(w).normalizar_vector() #ortogonal con w, derecha, eje x
        v = w.producto_cruz(u) #arriba, eje y

        #dimensiones del viewport
        distancia = self.posicion.resta_vectores(self.mirar_a).norma_vector()
        rad = math.radians(self.fov)
        t = math.tan(rad/2) #solo una mitad para trig
        viewport_ancho = 2.0 * distancia * t  #trigonometria
        viewport_altura = viewport_ancho * (imagen.altura/imagen.ancho)

        #construir. de izq a der, de arriba a abajo por ppm 
        viewport_vertical = v.producto_escalar(-viewport_altura) #para emepzar arriba
        viewport_horizontal = u.producto_escalar(viewport_ancho)

        #para moverse pixel a pixel
        self.viewport_delta_vertical = viewport_vertical.producto_escalar(1.0/imagen.altura)
        self.viewport_delta_horizontal = viewport_horizontal.producto_escalar(1.0/imagen.ancho) 

        #movernos al primer pixel (esquina izquiera sup pues es ppm)
        viewport_centro = self.posicion.resta_vectores(w.producto_escalar(distancia))
        viewport_mover_izq = viewport_centro.resta_vectores(viewport_horizontal.producto_escalar(1.0/2.0))
        viewport_mover_arriba = viewport_mover_izq.resta_vectores(viewport_vertical.producto_escalar(1.0/2.0))

        #centro de pixel
        movimiento_deltas = self.viewport_delta_vertical.suma_vectores(self.viewport_delta_horizontal).producto_escalar(0.5)
        self.pixel_centro = viewport_mover_arriba.suma_vectores(movimiento_deltas)






        







    
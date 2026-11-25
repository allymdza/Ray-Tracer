from vectores import vectores


class hit_info:
    # Guarda la informacion del punto más cercano al rayo (el que se colorea)

    def __init__(self):
        self.punto = vectores(0, 0, 0)
        self.t = 0.0


class hit_lista:
    # Mira una lista de todas las figuras que toca el rayo y selecciona al que el rayo toca primero (el que se colorea)

    def __init__(self):
        self.figuras = []

    def agregar(self, obj):
        self.figuras.append(obj)

    """ Recordemos que si t < 0 el punto de impacto esta hacia atras, si t = 0 esta en el mismo punto
    tmin > 0.001 para que se pueda dar distancias cortas, pero no 0
    tmax(infinito, porque para ahi va el rayo que no choca con nada/dan al fondo"""
    def primer_hit(self, rayo, info_hit, tmin = 0.001, tmax = float("inf")):
        info_temporal = hit_info()
        toca_algo = False
        mas_cercano = tmax #todavia no checamos nada

        for obj in self.figuras:
            if obj.intersecciona(rayo, info_temporal, tmin, mas_cercano):
                toca_algo = True
                mas_cercano = info_temporal.t
                info_hit.punto = info_temporal.punto
                info_hit.t = info_temporal.t

        return toca_algo #si es falso el rayo va hasta el fondo



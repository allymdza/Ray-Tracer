class rayo: 

    def __init__(self, origen, direccion):
        self.origen = origen
        self.direccion = direccion.normalizar_vector() 

    def parametrica(self, t):
        return self.origen.suma_vectores(self.direccion.producto_escalar(t))
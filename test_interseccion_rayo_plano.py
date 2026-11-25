import pytest
from vectores import vectores
from rayo import rayo
from Figuras.plano import plano

def test_apunta_al_plano():
        punto = vectores(0,0,0)
        normal = vectores(0,1,0)

        plano1 = plano(punto,normal)

        origen = vectores(0,5,5)
        direccion = vectores(0,-5,5)
        rayo1 = rayo(origen,direccion)

        assert plano1.intersecciona(rayo1)

def test_esta_en_el_plano():
        punto = vectores(0,0,0)
        normal = vectores(0,1,0)

        plano1 = plano(punto,normal)

        origen = vectores(0,0,0)
        direccion = vectores(1,0,0)
        rayo1 = rayo(origen,direccion)

        assert not plano1.intersecciona(rayo1)

def test_plano_esta_atras():
        punto = vectores(0,0,0)
        normal = vectores(0,1,0)

        plano1 = plano(punto,normal)

        origen = vectores(0,5,0)
        direccion = vectores(0,6,0)
        rayo1 = rayo(origen,direccion)

        assert not plano1.intersecciona(rayo1)

def test_paralelo_fuera_plano():
        punto = vectores(0,0,0)
        normal = vectores(0,1,0)

        plano1 = plano(punto,normal)

        origen = vectores(0,5,0)
        direccion = vectores(1,0,0)
        rayo1 = rayo(origen,direccion)

        assert not plano1.intersecciona(rayo1)

def test_desde_abajo():
        punto = vectores(0,0,0)
        normal = vectores(0,1,0)

        plano1 = plano(punto,normal)

        origen = vectores(0,-5,0)
        direccion = vectores(0,1,0)
        rayo1 = rayo(origen,direccion)

        assert plano1.intersecciona(rayo1)
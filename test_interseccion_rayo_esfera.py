import pytest
from vectores import vectores
from rayo import rayo
from Figuras.esfera import esfera

def test_apunta_al_centro():
        centro = vectores(0,0,0)
        esfera1 = esfera(centro,1)
        vector1 = vectores(5,2,3)
        vector2 = vectores(-5,-2,-3)
        rayo1 = rayo(vector1, vector2)

        assert esfera1.intersecciona(rayo1)

def test_roza_orilla():
        centro = vectores(0,0,0)
        esfera1 = esfera(centro,1)
        vector1 = vectores(1,0,0)
        vector2 = vectores(0,5,0)
        rayo1 = rayo(vector1, vector2)

        assert esfera1.intersecciona(rayo1)


def test_no_pasa():
        centro = vectores(0,0,0)
        esfera1 = esfera(centro,1)
        vector1 = vectores(5,2,2)
        vector2 = vectores(0,5,0)
        rayo1 = rayo(vector1, vector2)

        assert not esfera1.intersecciona(rayo1)

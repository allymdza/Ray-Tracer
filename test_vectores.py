
import pytest
from vectores import vectores


def test_suma_vectores():
    vector1 = vectores(1, 2, 3)
    vector2 = vectores(1, 2, 3)

    suma = vector1.suma_vectores(vector2)
    resultado = vectores(2, 4, 6)
    assert suma == resultado

def test_resta_vectores():
    vector1 = vectores(1, 2, 3)
    vector2 = vectores(1, 2, 3)
    
    resta = vector1.resta_vectores(vector2)
    resultado = vectores(0, 0, 0)
    assert resta == resultado

def test_producto_escalar():
    vector = vectores(1, 2, 3)
    escalar = 5

    producto = vector.producto_escalar(escalar)
    resultado = vectores(5, 10, 15)
    assert producto == resultado

def test_producto_punto():
    vector1 = vectores(1, 2, 3)
    vector2 = vectores(1, 2, 3)

    producto = vector1.producto_punto(vector2)
    resultado = 14
    assert producto == resultado

def test_norma_vector():
    vector = vectores(1, 2, 3)

    norma = vector.norma_vector()
    resultado = pytest.approx(3.74, abs=0.1)
    #se coloca abs=0.1 pues estamos ocupando un redondeo de dos decimales
    #y es el margen de error que acepatmos
    assert norma == resultado   
import pytest
from vectores import vectores
from ppm import escribir_ppm
from ppm import colores_int

def test_negro():
    n = colores_int(vectores(0, 0, 0))
    assert n == (0,0,0)

def test_blanco():
    n = colores_int(vectores(1, 1, 1))
    assert n == (255,255,255)
    
def test_rojo():
    n = colores_int(vectores(1, 0, 0))
    assert n == (255,0,0)
    
def test_verde():
    n = colores_int(vectores(0, 1, 0))
    assert n == (0,255,0)

def test_azul():
    n = colores_int(vectores(0, 0, 1))
    assert n == (0,0,255)
    
def test_gris():
    n = colores_int(vectores(0.5, 0.5, 0.5))
    assert n == (128,128,128)

def test_fuera_de_rango():
    n = colores_int(vectores(1.5, -0.5, 0.5))
    assert n == (255, 0, 128)

def test_tamanio_error():
    pixeles = [
    vectores(1, 0, 0), vectores(0, 1, 0), vectores(0, 0, 1),
    vectores(1, 1, 0), vectores(0, 1, 1),
]
    with pytest.raises(ValueError):
        escribir_ppm("x.ppm", 3, 2, pixeles)

def test_imagen_3X2(tmp_path):
    ruta = tmp_path / "resultado.ppm"
    pixeles = [
        vectores(1, 0, 0), vectores(0, 1, 0), vectores(0, 0, 1),
        vectores(1, 1, 0), vectores(0, 1, 1), vectores(1, 0, 1),
    ]
    escribir_ppm(ruta, 3, 2, pixeles)
    r = ruta.read_text()
    assert r == (
        "P3\n"
        "3 2\n"
        "255\n"
        "255 0 0\n"
        "0 255 0\n"
        "0 0 255\n"
        "255 255 0\n"
        "0 255 255\n"
        "255 0 255\n"
    )

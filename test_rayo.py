import pytest
from rayo import rayo
from vectores import vectores

def test_parametrica():
	origen = vectores(1,2,3)
	direccion = vectores (1,0,0)

	ray = rayo(origen,direccion)
	par = ray.parametrica(3)

	resultado = vectores(4,2,3)

	assert par == resultado  
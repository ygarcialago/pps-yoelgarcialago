import pytest

from calculadora import es_par, calcular_descuento, clasificar_edad


# --- es_par -----------------------------------------------------

def test_es_par_numero_par():
    assert es_par(4) is True


def test_es_par_numero_impar():
    assert es_par(7) is False


# --- calcular_descuento ------------------------------------------

def test_calcular_descuento_normal():
    assert calcular_descuento(100, 20) == 80.0


def test_calcular_descuento_sin_descuento():
    assert calcular_descuento(50, 0) == 50.0


def test_calcular_descuento_total():
    assert calcular_descuento(50, 100) == 0.0


def test_calcular_descuento_precio_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(-10, 20)


def test_calcular_descuento_porcentaje_invalido():
    with pytest.raises(ValueError):
        calcular_descuento(100, 150)


# --- clasificar_edad ----------------------------------------------

def test_clasificar_edad_menor():
    assert clasificar_edad(10) == "menor"


def test_clasificar_edad_adulto():
    assert clasificar_edad(30) == "adulto"


def test_clasificar_edad_senior():
    assert clasificar_edad(70) == "sénior"


def test_clasificar_edad_negativa():
    with pytest.raises(ValueError):
        clasificar_edad(-5)

def test_es_multiplo():
    assert es_multiplo(10, 5) is True
    assert not es_multiplo(10, 3)

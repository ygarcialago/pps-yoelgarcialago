import pytest
from tienda import (
aplicar_descuento, es_par, media, normalizar_nombre,
password_segura, precio_con_iva, total_carrito,
)
# Ejemplo ya resuelto (tu punto de partida):
def test_es_par_con_un_par():
    assert es_par(4) is True
# A partir de aquí, escribe un test por cada tarea del apartado 4

@pytest.mark.parametrize("numero, esperado", [
    (0,True),
    (2, True),
    (3, False),
    pytest.param(-4, False, marks=pytest.mark.xfail(reason="Fuera de los límites"))
])
def test_es_par_parametrized(numero , esperado):
    assert es_par(numero) == esperado

def test_normalizar_nombre():
    assert normalizar_nombre(" ana lopez ") == "Ana Lopez"

def test_precio_con_iva():
    assert precio_con_iva(10) == pytest.approx(12.1)

def test_precio_con_iva_negativo():
    with pytest.raises(ValueError, match="negativo"):
        precio_con_iva(-10)

@pytest.fixture
def lista_descuentos():
    return [(100,20, False), (100, 0, True), (100, 100, True) (-1, 20, True), (150, 20, True)]

@pytest.mark.parametrize("precio, porcentaje, debe_dar_error", lista_descuentos)
def test_aplicar_descuento(precio, porcentaje, debe_dar_error):
    if debe_dar_error:
        with pytest.raises(ValueError):
            aplicar_descuento(precio, porcentaje)
    else:
        resultado = aplicar_descuento(precio, porcentaje)
        assert resultado == 80.0

@pytest.fixture
def lista_precios():
    return [
        ((100,20, 30), 150, False),
        ((), 0 , True)
    ]


def test_total_carrito(lista_precios):
    for items, esperado, da_error in lista_precios:
        if da_error:
            with pytest.raises(ValueError):
                total_carrito(items)
        assert total_carrito(items) == pytest.approx(esperado)

@pytest.mark.parametrize("password, valid", [
    ("adfghjhgj1", True),
    ("adfghjhgj", False)
    ("ad1", False)
])
def test_password_segura(password, valid):
    assert password_segura(password) == valid

def test_media():
    assert media([2,4,6]) == 4
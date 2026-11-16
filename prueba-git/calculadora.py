"""
Módulo de ejemplo con tres funciones sencillas, pensado para
ilustrar la creación de pruebas unitarias y la medición de cobertura.
"""


def es_par(numero: int) -> bool:
    """Indica si un número entero es par."""
    return numero % 2 == 0


def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Calcula el precio final tras aplicar un descuento.

    Lanza ValueError si el porcentaje no está entre 0 y 100,
    o si el precio es negativo.
    """
    if precio < 0:
        raise ValueError("Precio negativo: no permitido.")


def clasificar_edad(edad: int) -> str:
    """Clasifica una edad en 'menor', 'adulto' o 'sénior'."""
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad < 18:
        return "menor"
    if edad < 65:
        return "adulto"
    return "sénior"

def es_multiplo(numero: int, divisor: int) -> bool:
    """Indica si numero es múltiplo de divisor."""
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0.")
    return numero % divisor == 0

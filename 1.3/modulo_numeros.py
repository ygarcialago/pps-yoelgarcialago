#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de utilidades para la gestión de conjuntos de números.

Este módulo proporciona las funciones necesarias para solicitar al
usuario un conjunto de números, validarlos, ordenarlos de forma
descendente y calcular algunas estadísticas básicas sobre ellos.

Está pensado para ser importado desde un programa principal
(:mod:`programa_principal`) y documentado automáticamente con Sphinx
a partir de estos docstrings en formato reStructuredText.

:author: Departamento de Informática
:version: 1.0
"""

from typing import Dict, List

#: Cantidad de números que se solicitan en cada conjunto.
CANTIDAD_NUMEROS: int = 10


def solicitar_numero(posicion: int) -> float:
    """Solicita al usuario un único número por teclado.

    :param posicion: Número de orden (1-indexado) que ocupa el dato
        dentro del conjunto que se está introduciendo. Se usa
        únicamente para personalizar el mensaje mostrado al usuario.
    :type posicion: int
    :raises ValueError: si el texto introducido no puede convertirse
        a un número de tipo ``float``.
    :return: El número introducido, convertido a ``float``.
    :rtype: float
    """
    texto: str = input(f"Introduce el número {posicion}: ")
    # float() lanza ValueError si el texto no representa un número,
    # excepción que se propaga y se gestiona en la función llamante.
    return float(texto)


def solicitar_conjunto_numeros(cantidad: int = CANTIDAD_NUMEROS) -> List[float]:
    """Solicita al usuario un conjunto completo de números.

    Si el usuario introduce un valor que no es numérico, se muestra
    un mensaje de error y se reinicia la introducción de todo el
    conjunto desde el primer número.

    :param cantidad: Número de valores que se deben solicitar.
        Por defecto, :data:`CANTIDAD_NUMEROS`.
    :type cantidad: int
    :return: Lista (tipo de dato complejo) con los números
        introducidos por el usuario, en el orden en que se
        introdujeron.
    :rtype: List[float]
    """
    numeros: List[float] = []

    print(f"\nIntroduce un conjunto de {cantidad} números.")
    while len(numeros) < cantidad:
        """
        Elemento de tratamiento de excepciones
        """
        try:
            numero: float = solicitar_numero(len(numeros) + 1)
            numeros.append(numero)
        
        except ValueError:
            print(
                "\n⚠ Error: el valor introducido no es un número válido. "
                "Se reinicia la introducción del conjunto de números.\n"
            )
            numeros = []  # Se vuelve al principio del conjunto

    return numeros


def ordenar_descendente(numeros: List[float]) -> List[float]:
    """Ordena una lista de números de mayor a menor.

    :param numeros: Lista de números a ordenar.
    :type numeros: List[float]
    :return: Nueva lista con los mismos números ordenados en orden
        descendente.
    :rtype: List[float]
    """
    return sorted(numeros, reverse=True)

"""
Función
"""
def calcular_estadisticas(numeros: List[float]) -> Dict[str, float]:
    """Calcula estadísticas básicas sobre un conjunto de números.

    :param numeros: Lista de números sobre la que calcular las
        estadísticas.
    :type numeros: List[float]
    :return: Diccionario (tipo de dato complejo) con las claves
        ``"maximo"``, ``"minimo"`` y ``"media"`` y sus
        correspondientes valores numéricos.
    :rtype: Dict[str, float]
    """
    suma: float = sum(numeros)
    total: int = len(numeros)

    estadisticas: Dict[str, float] = {
        "maximo": max(numeros),
        "minimo": min(numeros),
        "media": suma / total,
    }
    return estadisticas


def mostrar_resultados(numeros_ordenados: List[float], estadisticas: Dict[str, float]) -> None:
    """Muestra por pantalla el conjunto ordenado y sus estadísticas.

    :param numeros_ordenados: Números ya ordenados de forma
        descendente.
    :type numeros_ordenados: List[float]
    :param estadisticas: Diccionario con las estadísticas calculadas
        por :func:`calcular_estadisticas`.
    :type estadisticas: Dict[str, float]
    :return: No devuelve ningún valor; el resultado se imprime en
        la consola.
    :rtype: None
    """
    print("\nNúmeros ordenados de forma descendente:")
    print(numeros_ordenados)
    print(f"\nMáximo: {estadisticas['maximo']}")
    print(f"Mínimo: {estadisticas['minimo']}")
    print(f"Media:  {estadisticas['media']:.2f}")

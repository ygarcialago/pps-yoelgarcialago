#!/usr/bin/env python3
"""
Programa principal: ordenación de conjuntos de números.

Este programa solicita al usuario conjuntos de 10 números, los
ordena de forma descendente y muestra el resultado junto con
algunas estadísticas. Al finalizar cada conjunto, pregunta al
usuario si desea introducir un nuevo conjunto o salir del programa.

La lógica de solicitud, validación, ordenación y cálculo de
estadísticas se encuentra delegada en el módulo
:mod:`modulo_numeros`, que este programa importa.

:author: Departamento de Informática
:version: 1.0
"""

from modulo_numeros import (
    calcular_estadisticas,
    mostrar_resultados,
    ordenar_descendente,
    solicitar_conjunto_numeros,
)


def preguntar_continuar() -> bool:
    """Pregunta al usuario si desea introducir un nuevo conjunto.

    Repite la pregunta hasta obtener una respuesta válida
    (``"s"`` o ``"n"``, en mayúsculas o minúsculas).

    :return: ``True`` si el usuario quiere continuar, ``False`` si
        quiere salir del programa.
    :rtype: bool
    """
    while True:
        respuesta: str = (
            input("\n¿Deseas introducir un nuevo conjunto de números? (s/n): ").strip().lower()
        )

        if respuesta == "s":
            return True
        if respuesta == "n":
            return False

        print("Respuesta no válida. Escribe 's' para sí o 'n' para no.")


def main() -> None:
    """Función principal: controla el bucle del programa.

    Mientras el usuario lo desee, solicita un conjunto de 10
    números, los ordena de forma descendente, calcula sus
    estadísticas y muestra los resultados por pantalla.

    :return: No devuelve ningún valor.
    :rtype: None
    """
    continuar: bool = True

    while continuar:
        numeros = solicitar_conjunto_numeros()
        numeros_ordenados = ordenar_descendente(numeros)
        estadisticas = calcular_estadisticas(numeros)

        mostrar_resultados(numeros_ordenados, estadisticas)

        continuar = preguntar_continuar()

    print("\nPrograma finalizado. ¡Hasta la próxima!")


if __name__ == "__main__":
    main()

import unittest
from unittest.mock import patch

import modulo_numeros


class TestUtilidadesNumeros(unittest.TestCase):

    @patch("modulo_numeros.input", return_value="15.5")
    def test_solicitar_numero_valido(self, mock_input):
        """Prueba que solicitar_numero convierte correctamente un input válido a float."""
        resultado = modulo_numeros.solicitar_numero(1)
        self.assertEqual(resultado, 15.5)
        self.assertIsInstance(resultado, float)
        mock_input.assert_called_once_with("Introduce el número 1: ")

    @patch("modulo_numeros.input", return_value="no_es_numero")
    def test_solicitar_numero_invalido(self, mock_input):
        """Prueba que solicitar_numero lanza ValueError si el input no es un número."""
        with self.assertRaises(ValueError):
            modulo_numeros.solicitar_numero(1)

    @patch(
        "modulo_numeros.input",
        side_effect=["10", "20", "30", "mal", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50"],
    )
    def test_solicitar_conjunto_numeros_con_reinicio(self, mock_input):
        """Prueba que solicitar_conjunto_numeros se reinicia al encontrar un valor inválido

        y completa la cantidad solicitada correctamente.
        """
        # Pedimos solo 5 números para que el test sea más ágil
        resultado = modulo_numeros.solicitar_conjunto_numeros(cantidad=5)
        self.assertEqual(resultado, [5.0, 10.0, 15.0, 20.0, 25.0])
        self.assertEqual(len(resultado), 5)

    def test_ordenar_descendente(self):
        """Prueba que la función ordena correctamente una lista de mayor a menor."""
        entrada = [3.5, 10.0, -2.0, 10.0, 7.1]
        resultado = modulo_numeros.ordenar_descendente(entrada)
        self.assertEqual(resultado, [10.0, 10.0, 7.1, 3.5, -2.0])

    def test_calcular_estadisticas_basicas(self):
        """Prueba el cálculo correcto del máximo, mínimo y media."""
        entrada = [2.0, 4.0, 6.0, 8.0]
        resultado = modulo_numeros.calcular_estadisticas(entrada)

        self.assertEqual(resultado["maximo"], 8.0)
        self.assertEqual(resultado["minimo"], 2.0)
        self.assertEqual(resultado["media"], 5.0)

    def test_calcular_estadisticas_negativos_y_decimales(self):
        """Prueba estadísticas con números negativos y decimales."""
        entrada = [-5.0, 0.0, 5.0]
        resultado = modulo_numeros.calcular_estadisticas(entrada)

        self.assertEqual(resultado["maximo"], 5.0)
        self.assertEqual(resultado["minimo"], -5.0)
        self.assertEqual(resultado["media"], 0.0)


if __name__ == "__main__":
    unittest.main()

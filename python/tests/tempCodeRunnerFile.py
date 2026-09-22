import unittest
from src.calculadora import calculadoraFisica

class TestecalculadoraFisica(unittest.TestCase):
    def teste_energiaPotencial(self):
        massa = 10.0
        altura = 5.0
        resultado_esperado = 490.5

        resultado_obtido = calculadoraFisica.energiaPotencial(massa, altura)

        self.assertAlmostEqual(resultado_obtido, resultado_esperado, places=3)

if __name__ == '__main__':
    unittest.main()
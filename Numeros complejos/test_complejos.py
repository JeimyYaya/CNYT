import unittest
import libreria_complejos as c
import math

class TestComplexFunctions(unittest.TestCase):
    def setUp(self):
        self.a = (3, 4)  # Representa el número complejo 3 + 4i
        self.b = (2, -1) # Representa el número complejo 2 - i

    def test_suma(self):
        # Prueba de la función suma
        self.assertEqual(c.suma(self.a, self.b), (5, 3))
        self.assertEqual(c.suma(self.b, self.a), (5, 3))

    def test_resta(self):
        # Prueba de la función resta
        self.assertEqual(c.resta(self.a, self.b), (1, 5))
        self.assertEqual(c.resta(self.b, self.a), (-1, -5))

    def test_multiplicacion(self):
        # Prueba de la función multiplicacion
        self.assertEqual(c.multiplicacion(self.a, self.b), (10, 5))
        self.assertEqual(c.multiplicacion(self.b, self.a), (10, 5))

    def test_division(self):
        # Definir números complejos a y b
        a = (2, 3)
        b = (1, 1)

        # Calcular la división de a y b
        resultado = c.division(a, b)

        # Verificar que la parte real e imaginaria del resultado sean aproximadamente iguales
        self.assertAlmostEqual(resultado[0], 2.5)
        self.assertAlmostEqual(resultado[1], 0.5)

    def test_modulo(self):
        # Prueba de la función modulo
        self.assertAlmostEqual(c.modulo(self.a), 5.0)
        self.assertAlmostEqual(c.modulo(self.b), math.sqrt(5))

    def test_conjugado(self):
        # Prueba de la función conjugado
        self.assertEqual(c.conjugado(self.a), (3, -4))
        self.assertEqual(c.conjugado(self.b), (2, 1))

    def test_fase(self):
        # Prueba de la función fase
        self.assertAlmostEqual(c.fase(self.a), 53.13010235415598)
        self.assertAlmostEqual(c.fase(self.b), -26.56505117707799)

    def test_polar_cartesiano(self):
        # Prueba de la función polar_cartesiano
        # Calcula las coordenadas cartesianas esperadas
        expected_coordinates = (1, math.sqrt(3))

        # Calcula las coordenadas cartesianas utilizando la función polar_cartesiano
        actual_coordinates = c.polar_cartesiano((2, 60))

        # Compara los valores de las coordenadas cartesianas
        self.assertAlmostEqual(actual_coordinates[0], expected_coordinates[0])
        self.assertAlmostEqual(actual_coordinates[1], expected_coordinates[1])

    def test_cartesiano_polar(self):
        # Prueba de la función cartesiano_polar
        self.assertAlmostEqual(c.cartesiano_polar(self.a), (5.0, 53.13010235415598))
        self.assertAlmostEqual(c.cartesiano_polar(self.b), (math.sqrt(5), -26.56505117707799))

if __name__ == '__main__':
    unittest.main()

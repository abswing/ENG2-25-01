import unittest
from calculadora import somar, dividir
#FROM aula-04.calculadora import somar, dividir


class TestCalcular(unittest.TestCase): 

    def test_somar(self):
        self.assertEqual(somar(1,2), 3)
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(2, 2), 4)


    def test_dividir(self): 
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(10, 0), "erro, nao pode 0")
        self.assertEqual(dividir(10, -2), -5)
        self.assertEqual(dividir(-10, -2), 5)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
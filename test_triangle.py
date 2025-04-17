import unittest
from delivery_service import check_triangle


class TestTriangleCheck(unittest.TestCase):
    def test_equilateral_triangle(self):
        """Тест для равностороннего треугольника"""
        self.assertEqual(check_triangle(10, 10, 10), "Равносторонний треугольник")
        self.assertEqual(check_triangle(5, 5, 5), "Равносторонний треугольник")

    def test_isosceles_triangle(self):
        """Тест для равнобедренного треугольника"""
        self.assertEqual(check_triangle(10, 10, 15), "Равнобедренный треугольник")
        self.assertEqual(check_triangle(15, 10, 10), "Равнобедренный треугольник")
        self.assertEqual(check_triangle(10, 15, 10), "Равнобедренный треугольник")

    def test_scalene_triangle(self):
        """Тест для разностороннего треугольника"""
        self.assertEqual(check_triangle(10, 12, 15), "Разносторонний треугольник")
        self.assertEqual(check_triangle(7, 10, 12), "Разносторонний треугольник")

    def test_nonexistent_triangle(self):
        """Тест для несуществующего треугольника"""
        self.assertEqual(check_triangle(10, 20, 30), "Треугольник не существует")
        self.assertEqual(check_triangle(10, 10, 20), "Треугольник не существует")
        self.assertEqual(check_triangle(0, 10, 20), "Треугольник не существует")
        self.assertEqual(check_triangle(-10, 10, 20), "Треугольник не существует")
        self.assertEqual(check_triangle(1, 2, 3), "Треугольник не существует")

    def test_invalid_values(self):
        """Тест для невалидных значений"""
        self.assertEqual(check_triangle(0, 0, 0), "Треугольник не существует")
        self.assertEqual(check_triangle(-1, -1, -1), "Треугольник не существует")


if __name__ == '__main__':
    unittest.main()
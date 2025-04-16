from unittest import TestCase, main
from delivery_service import check_age, check_auth, get_cost


class TestAgeControl(TestCase):
    def test_age_access(self):
        self.assertEqual(check_age(17), 'Доступ запрещён')
        self.assertEqual(check_age(18), 'Доступ разрешён')
        self.assertEqual(check_age(25), 'Доступ разрешён')
        self.assertEqual(check_age(0), 'Доступ запрещён')


class TestAuthControl(TestCase):
    def test_successful_auth(self):
        self.assertEqual(check_auth('admin', 'password'), 'Добро пожаловать')

    def test_failed_auth(self):
        cases = [('user', 'pass'), ('admin', 'wrong'), ('', ''), ('guest', '123')]
        for login, password in cases:
            with self.subTest(login=login, password=password):
                self.assertEqual(check_auth(login, password), 'Доступ ограничен')


class TestDeliveryCost(TestCase):
    def test_standard_weights(self):
        test_cases = [
            (5, '200'),
            (10, '200'),
            (11, '500'),
            (15, '500'),
            (100, '500')
        ]
        for weight, expected in test_cases:
            with self.subTest(weight=weight):
                self.assertIn(expected, get_cost(weight))

    def test_zero_weight(self):
        self.assertIn('200', get_cost(0))

    def test_negative_weight(self):
        with self.assertRaises(ValueError) as context:
            get_cost(-5)
        self.assertEqual(str(context.exception), "Вес не может быть отрицательным")

    def test_non_integer_weight(self):
        with self.assertRaises(TypeError) as context:
            get_cost(5.5)
        self.assertEqual(str(context.exception), "Вес должен быть целым числом")


if __name__ == '__main__':
    main()
def check_age(age: int) -> str:
    return 'Доступ разрешён' if age >= 18 else 'Доступ запрещён'


def check_auth(login: str, password: str) -> str:
    return 'Добро пожаловать' if login == 'admin' and password == 'password' else 'Доступ ограничен'


def get_cost(weight: int) -> str:
    if not isinstance(weight, int):
        raise TypeError("Вес должен быть целым числом")
    if weight < 0:
        raise ValueError("Вес не может быть отрицательным")
    return 'Стоимость доставки: 200 руб.' if weight <= 10 else 'Стоимость доставки: 500 руб.'


if __name__ == '__main__':
    print("=== Тестирование функций ===")

    # Демонстрация работы check_age
    print("\n1. Проверка возраста:")
    for age in [15, 18, 20]:
        print(f"{age} лет: {check_age(age)}")

    # Демонстрация работы check_auth
    print("\n2. Проверка авторизации:")
    for credentials in [('user', '123'), ('admin', 'password')]:
        print(f"{credentials[0]}/{credentials[1]}: {check_auth(*credentials)}")

    # Демонстрация работы get_cost
    print("\n3. Расчет стоимости доставки:")
    for weight in [5, 10, 11, 15]:
        try:
            print(f"{weight} кг: {get_cost(weight)}")
        except ValueError as e:
            print(f"{weight} кг: Ошибка - {e}")
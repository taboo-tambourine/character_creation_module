
from math import sqrt


def calculate_square_root(your_number: float) -> float:
    """Вычисляет квадратный корень."""
    if is_negative(your_number):
        your_number = float(input(
            'Ошибка! Число не может быть отрицательным. '
            'Введите другое число:'))
    if is_zero(your_number):
        return 0
    return sqrt(your_number)


def is_negative(n: float) -> bool:
    """Проверяет, если число меньше нуля."""
    return n < 0


def is_zero(n: float) -> bool:
    """Проверяет, если число равно нулю."""
    return n == 0


message = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа'
)
print(message)

your_number = float(input('Введите ваше число: '))
sqrt_your_number = calculate_square_root(your_number)

print(
    f'Мы вычислили квадратный корень из введённого вами числа. '
    f'Это будет: {sqrt_your_number}'
)

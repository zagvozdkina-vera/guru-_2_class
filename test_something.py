import math
import mpmath
from decimal import Decimal, getcontext
import random
from datetime import time
import selene


def test_dark_theme_by_time():
    current_time = 24
    if not 0 <= current_time <= 23:
        print("Ошибка: время должно быть от 0 до 23!")
        return

    if 6 <= current_time <= 22:
        print(current_time)
        print("Is dark theme is False")

    else:
        print(current_time)
        print("Is dark theme is True")





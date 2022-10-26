import random                                                               # импортируем модуль random
import string                                                               # импортируем модуль string
def get_random_password() -> str:                                           # создаем функцию
    x = string.digits + string.ascii_lowercase + string.ascii_uppercase     # разрешенные символы пароля
    try:                                                                    # проверяем значение n - длина пароля
        n = int(input("Введите длину пароля: "))                            # ввод значения n - длина пароля
        y = ''.join(random.sample(x, n))                                    # генерируем случайный пароль (количество символов == n)
        return(y)                                                           # возвращаем сгенерированный пароль
    except ValueError:                                                      # если в n введено не число, то получаем ошибку ValueError
        y = ''.join(random.sample(x, 8))                                    # генерируем пароль длиной 8 символов (по умолчанию)
        return(y)                                                           # возвращаем сгенерированный пароль
         # TODO написать функцию генерации случайных паролей

print(get_random_password())                                                # вызываем функцию


def is_prime(number: int) -> bool:
    """ Función que determina si un número es primo o no.

    :param number: Número a evaluar.
    :return: True si el número es primo, False en caso contrario.
    """
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(number**0.5)+1, 2):
            if number % current == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    # number = int(input('Ingrese un número: '))
    # print(is_prime(number))

    for number in range(1, 101):
        print(f'{number} es primo: {is_prime(number)}')
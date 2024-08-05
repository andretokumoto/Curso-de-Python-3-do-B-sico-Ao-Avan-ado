def div_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def _int_or_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    _int_or_float(n)
    _int_or_float(d)
    div_zero(d)
    return n / d


print(divide(8, '0'))
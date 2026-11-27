def add(z1: complex, z2: complex) -> complex:
    return complex(z1.real + z2.real, z1.imag + z2.imag)


def multiply(z1: complex, z2: complex) -> complex:
    re = z1.real * z2.real - z1.imag * z2.imag
    im = z1.real * z2.imag + z1.imag * z2.real
    return complex(re, im)


def divide(z1: complex, z2: complex) -> complex:
    denom = z2.real ** 2 + z2.imag ** 2
    if denom == 0:
        raise ZeroDivisionError("Деление на ноль (0 + 0i) невозможно.")
    re = (z1.real * z2.real + z1.imag * z2.imag) / denom
    im = (z1.imag * z2.real - z1.real * z2.imag) / denom
    return complex(re, im)

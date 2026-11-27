import math
def input_complex_number(prompt: str) -> complex:
    print(prompt)
    while True:
        try:
            re = float(input("  Действительная часть (a): "))
            im = float(input("  Мнимая часть (b): "))
            if not (math.isfinite(re) and math.isfinite(im)): raise ValueError
            return complex(re, im)
        except ValueError:
            print("Ошибка: введите корректные вещественные числа.")


def input_operation() -> str:
    valid_ops = ("+", "*", "/")
    while True:
        op = input("Выберите операцию (+, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Ошибка: допустимы только операции +, * или /.")

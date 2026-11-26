from input_module import input_complex_number, input_operation
from arithmetic_module import add, multiply, divide
from output_module import print_result


def main():
    print("=== Система работы с комплексными числами ===")
    
    z1 = input_complex_number("Введите первое число:")
    z2 = input_complex_number("Введите второе число:")
    op = input_operation()

    try:
        if op == "+":
            result = add(z1, z2)
        elif op == "*":
            result = multiply(z1, z2)
        elif op == "/":
            result = divide(z1, z2)
        else:
            print("Неизвестная операция.")
            return

        print_result(result)

    except ZeroDivisionError as e:
        print(f"Ошибка вычисления: {e}")


if __name__ == "__main__":
    main()
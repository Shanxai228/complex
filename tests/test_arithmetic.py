import pytest
from arithmetic_module import add, multiply, divide


class TestAdd:
    """Тесты функции сложения комплексных чисел."""

    @pytest.mark.parametrize(
        "z1, z2, expected",
        [
            (complex(3, 4), complex(1, 2), complex(4, 6)),          # обычный случай
            (complex(0, 0), complex(0, 0), complex(0, 0)),          # граница: оба нуля
            (complex(-3, -4), complex(3, 4), complex(0, 0)),        # взаимное уничтожение
            (complex(1e9, -1e9), complex(1e9, 1e9), complex(2e9, 0)),  # большие числа
        ],
    )
    def test_add_valid(self, z1, z2, expected):
        assert add(z1, z2) == expected

    def test_add_invalid_type(self):
        """Предположение об ошибке: передана строка вместо числа."""
        with pytest.raises(AttributeError):
            add("3+4i", complex(1, 1))


class TestMultiply:
    """Тесты функции умножения комплексных чисел."""

    @pytest.mark.parametrize(
        "z1, z2, expected",
        [
            (complex(1, 2), complex(3, 4), complex(-5, 10)),        # обычный случай
            (complex(5, -7), complex(0, 0), complex(0, 0)),         # граница: умножение на 0
            (complex(0, 1), complex(0, 1), complex(-1, 0)),         # граница: i * i = -1
            (complex(3, 4), complex(3, -4), complex(25, 0)),        # сопряжённые числа
            (complex(-1.5, 2.0), complex(2.0, -0.5), complex(-2.0, 4.75)),  # дроби
        ],
    )
    def test_multiply_valid(self, z1, z2, expected):
        assert multiply(z1, z2) == expected


class TestDivide:
    """Тесты функции деления (покрытие решений + комбинаторное покрытие условий)."""

    @pytest.mark.parametrize(
        "z1, z2, expected",
        [
            # Все комбинации условий (z2.real == 0 / != 0, z2.imag == 0 / != 0), кроме (0, 0):
            (complex(4, 2), complex(1, 1), complex(3, -1)),         # re != 0, im != 0
            (complex(6, 4), complex(2, 0), complex(3, 2)),          # re != 0, im == 0
            (complex(4, 2), complex(0, 2), complex(1, -2)),         # re == 0, im != 0
            (complex(0, 0), complex(3, 4), complex(0, 0)),          # граница: делимое = 0
        ],
    )
    def test_divide_valid(self, z1, z2, expected):
        """Ветка if denom == 0 -> False."""
        assert divide(z1, z2) == pytest.approx(expected)

    def test_divide_by_zero(self):
        """Предположение об ошибке + ветка if denom == 0 -> True (re == 0, im == 0)."""
        with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
            divide(complex(3, 4), complex(0, 0))

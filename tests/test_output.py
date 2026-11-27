import pytest
from output_module import format_algebraic, format_trigonometric, print_result


class TestFormatAlgebraic:
    """Тесты алгебраической формы (граничные значения + покрытие решений)."""

    def test_positive_imag(self):
        """Обычное число с положительной мнимой частью (ветка imag >= 0 -> '+')."""
        assert format_algebraic(complex(3, 4)) == "3.00 + 4.00i"

    def test_negative_imag(self):
        """Число с отрицательной мнимой частью (ветка imag < 0 -> '-')."""
        assert format_algebraic(complex(3, -4)) == "3.00 - 4.00i"

    def test_zero_complex(self):
        """Граничное значение: 0 + 0i (граница imag == 0)."""
        assert format_algebraic(complex(0, 0)) == "0.00 + 0.00i"

    def test_negative_floats(self):
        """Граничное значение: отрицательные дробные числа."""
        assert format_algebraic(complex(-2.5, -1.25)) == "-2.50 - 1.25i"

    def test_invalid_type_raises_error(self):
        """Предположение об ошибке: передана строка вместо complex."""
        with pytest.raises(AttributeError):
            format_algebraic("3+4i")


class TestFormatTrigonometric:
    """Тесты тригонометрической формы (граничные значения + покрытие решений)."""

    def test_zero_complex_branch(self):
        """Граничное значение и ветка if r == 0 (True)."""
        assert format_trigonometric(complex(0, 0)) == "0 (аргумент не определен)"

    @pytest.mark.parametrize(
        "z, expected",
        [
            (complex(3, 4), "5.00 * (cos(53.13°) + i * sin(53.13°))"),
            (complex(1, 0), "1.00 * (cos(0.00°) + i * sin(0.00°))"),
            (complex(0, 1), "1.00 * (cos(90.00°) + i * sin(90.00°))"),
            (complex(-1, 0), "1.00 * (cos(180.00°) + i * sin(180.00°))"),
            (complex(0, -1), "1.00 * (cos(-90.00°) + i * sin(-90.00°))"),
        ],
    )
    def test_nonzero_angles(self, z, expected):
        """Ветка r != 0 (False) и граничные углы на осях координат."""
        assert format_trigonometric(z) == expected

    def test_invalid_type_raises_error(self):
        """Предположение об ошибке: передано None вместо complex."""
        with pytest.raises(AttributeError):
            format_trigonometric(None)


class TestPrintResult:
    """Тесты консольного вывода результата."""

    def test_print_result_normal(self, capsys):
        """Проверка вывода для обычного комплексного числа."""
        print_result(complex(3, 4))
        captured = capsys.readouterr().out
        assert "--- Результат ---" in captured
        assert "3.00 + 4.00i" in captured
        assert "5.00 * (cos(53.13°) + i * sin(53.13°))" in captured

    def test_print_result_zero(self, capsys):
        """Граничное значение: вывод для 0 + 0i."""
        print_result(complex(0, 0))
        captured = capsys.readouterr().out
        assert "0.00 + 0.00i" in captured
        assert "0 (аргумент не определен)" in captured
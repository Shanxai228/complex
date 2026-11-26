import pytest
from input_module import input_complex_number, input_operation


class TestInputComplexNumber:
    """Тесты ввода комплексного числа (граничные значения + предположение об ошибке)."""

    def test_valid_positive_numbers(self, monkeypatch, capsys):
        """Нормальный тест: ввод положительных чисел."""
        inputs = iter(["3", "4"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        result = input_complex_number("Введите число:")
        out = capsys.readouterr().out

        assert result == complex(3.0, 4.0)
        assert "Введите число:" in out

    def test_boundary_zeros(self, monkeypatch):
        """Граничное значение: ввод нулей (0 + 0i)."""
        inputs = iter(["0", "0"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert input_complex_number("Тест") == complex(0.0, 0.0)

    def test_boundary_negative_floats(self, monkeypatch):
        """Граничное значение: отрицательные дробные числа."""
        inputs = iter(["-2.5", "-0.75"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        assert input_complex_number("Тест") == complex(-2.5, -0.75)

    def test_invalid_real_then_valid(self, monkeypatch, capsys):
        """Предположение об ошибке + ветка except: буквы в действительной части."""
        inputs = iter(["abc", "1", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        result = input_complex_number("Тест")
        out = capsys.readouterr().out

        assert result == complex(1.0, 2.0)
        assert "Ошибка: введите корректные вещественные числа." in out

    def test_invalid_imag_then_valid(self, monkeypatch, capsys):
        """Предположение об ошибке: ошибка при вводе мнимой части (повтор цикла)."""
        inputs = iter(["5", "xyz", "1", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        result = input_complex_number("Тест")
        out = capsys.readouterr().out

        assert result == complex(1.0, 2.0)
        assert "Ошибка: введите корректные вещественные числа." in out

    def test_empty_input_then_valid(self, monkeypatch, capsys):
        """Граничный случай / ошибка: пустой ввод (Enter)."""
        inputs = iter(["", "0", "1"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        result = input_complex_number("Тест")
        out = capsys.readouterr().out

        assert result == complex(0.0, 1.0)
        assert "Ошибка: введите корректные вещественные числа." in out


class TestInputOperation:
    """Тесты выбора операции (покрытие решений if/else + предположение об ошибке)."""

    @pytest.mark.parametrize("op", ["+", "*", "/"])
    def test_valid_operations(self, monkeypatch, op):
        """Нормальные тесты: все допустимые операции (ветка if -> True)."""
        monkeypatch.setattr("builtins.input", lambda _: op)
        assert input_operation() == op

    def test_operation_with_spaces(self, monkeypatch):
        """Граничный тест: операция с лишними пробелами (проверка .strip())."""
        monkeypatch.setattr("builtins.input", lambda _: "   +   ")
        assert input_operation() == "+"

    def test_invalid_operation_then_valid(self, monkeypatch, capsys):
        """Предположение об ошибке: неверная операция и пустая строка (ветка if -> False)."""
        inputs = iter(["-", "", "abc", "/"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        result = input_operation()
        out = capsys.readouterr().out

        assert result == "/"
        assert "Ошибка: допустимы только операции +, * или /." in out
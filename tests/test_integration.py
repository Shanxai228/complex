import main


class TestMainIntegration:
    """Интеграционные тесты и покрытие решений (ветвлений) для main.py."""

    def test_integration_addition(self, monkeypatch, capsys):
        """Сценарий 1: ввод двух чисел -> сложение -> вывод результата."""
        numbers = iter([complex(3, 4), complex(1, 2)])
        monkeypatch.setattr(main, "input_complex_number", lambda _: next(numbers))
        monkeypatch.setattr(main, "input_operation", lambda: "+")

        main.main()
        out = capsys.readouterr().out

        assert "--- Результат ---" in out
        assert "4.00 + 6.00i" in out

    def test_integration_multiplication(self, monkeypatch, capsys):
        """Сценарий 2: ввод двух чисел -> умножение -> вывод результата."""
        numbers = iter([complex(1, 2), complex(3, 4)])
        monkeypatch.setattr(main, "input_complex_number", lambda _: next(numbers))
        monkeypatch.setattr(main, "input_operation", lambda: "*")

        main.main()
        out = capsys.readouterr().out

        assert "--- Результат ---" in out
        assert "-5.00 + 10.00i" in out

    def test_integration_division(self, monkeypatch, capsys):
        """Сценарий 3: ввод двух чисел -> деление -> вывод результата."""
        numbers = iter([complex(4, 2), complex(1, 1)])
        monkeypatch.setattr(main, "input_complex_number", lambda _: next(numbers))
        monkeypatch.setattr(main, "input_operation", lambda: "/")

        main.main()
        out = capsys.readouterr().out

        assert "--- Результат ---" in out
        assert "3.00 - 1.00i" in out

    def test_integration_division_by_zero(self, monkeypatch, capsys):
        """Сценарий 4 (предположение об ошибке): деление на 0 + 0i."""
        numbers = iter([complex(5, 5), complex(0, 0)])
        monkeypatch.setattr(main, "input_complex_number", lambda _: next(numbers))
        monkeypatch.setattr(main, "input_operation", lambda: "/")

        main.main()
        out = capsys.readouterr().out

        assert "Ошибка вычисления:" in out

    def test_integration_unknown_operation(self, monkeypatch, capsys):
        """Сценарий 5 (предположение об ошибке): неизвестная операция."""
        numbers = iter([complex(2, 3), complex(1, 1)])
        monkeypatch.setattr(main, "input_complex_number", lambda _: next(numbers))
        monkeypatch.setattr(main, "input_operation", lambda: "-")

        main.main()
        out = capsys.readouterr().out

        assert "Неизвестная операция." in out

# Временная заглушка input_module.py
def input_complex_number(prompt: str) -> complex:
    return complex(2, 3)  # всегда возвращает (2 + 3i)

def input_operation() -> str:
    return "+"            # всегда возвращает сложение
import math


def format_algebraic(z: complex) -> str:
    sign = "+" if z.imag >= 0 else "-"
    return f"{z.real:.2f} {sign} {abs(z.imag):.2f}i"


def format_trigonometric(z: complex) -> str:
    r = math.hypot(z.real, z.imag)
    if r == 0:
        return "0 (аргумент не определен)"
    phi_rad = math.atan2(z.imag, z.real)
    phi_deg = math.degrees(phi_rad)
    return f"{r:.2f} * (cos({phi_deg:.2f}°) + i * sin({phi_deg:.2f}°))"


def print_result(z: complex) -> None:
    print("\n--- Результат ---")
    print(f"Алгебраическая форма:    {format_algebraic(z)}")
    print(f"Тригонометрическая форма: {format_trigonometric(z)}")
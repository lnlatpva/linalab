
"""
Вариант 13. Температурное расширение детали.
Главная программа с валидацией всех входных данных.
"""

import math

from constants import (
    L0_MIN, L0_MAX,
    T1_MIN, T1_MAX,
    T2_MIN, T2_MAX,
)

from menu import show_menu, material_name

from operations import (
    thermal_expansion,
    final_length,
    expansion_class,
)

from validation import validate_range
from logger import log_error


def input_material() -> float | None:
    """Выбор материала с проверкой правильности ввода."""

    materials = {
        "1": 1.2e-5,
        "2": 2.3e-5,
        "3": 1.7e-5,
    }

    while True:
        choice = input(
            "Введите номер материала (0..3): "
        ).strip()

        if choice == "0":
            return None

        elif choice in materials:
            return materials[choice]

        else:
            msg = "Ошибка: выберите материал от 1 до 3 или 0."
            print(msg)
            log_error(msg)


def input_valid_number(
    name: str,
    low: float,
    high: float,
) -> float:
    """Проверка типа и допустимого диапазона числа."""

    while True:
        raw = input(
            f"Введите {name} ({low}..{high}): "
        ).strip()

        try:
            value = float(raw)

        except ValueError:
            msg = f"Ошибка: '{raw}' не является числом."
            print(msg)
            log_error(msg)
            continue

        if not math.isfinite(value):
            msg = "Ошибка: введите конечное число."
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)

        if not ok:
            print(msg)
            log_error(msg)
            continue

        return value


def main() -> None:
    """Главный сценарий работы программы."""

    print("=== Температурное расширение детали ===")

    while True:
        show_menu()

        # 1. Валидация материала
        alpha = input_material()

        if alpha is None:
            print("Работа завершена.")
            break

        # 2. Валидация начальной длины
        l0 = input_valid_number(
            "начальную длину L0, мм",
            L0_MIN,
            L0_MAX,
        )

        # 3. Валидация начальной температуры
        t1 = input_valid_number(
            "начальную температуру t1, °C",
            T1_MIN,
            T1_MAX,
        )

        # 4. Валидация конечной температуры
        while True:
            t2 = input_valid_number(
                "конечную температуру t2, °C",
                T2_MIN,
                T2_MAX,
            )

            if t2 > t1:
                break

            else:
                msg = (
                    "Ошибка: конечная температура t2 "
                    "должна быть больше t1."
                )
                print(msg)
                log_error(msg)

        # 5. Расчёты
        delta_l = thermal_expansion(
            l0, alpha, t1, t2
        )

        length = final_length(
            l0, delta_l
        )

        cls = expansion_class(delta_l)

        # 6. Вывод результата
        print("\n--- Результаты расчёта ---")
        print(f"Материал:           {material_name(alpha)}")
        print(f"Коэффициент α:      {alpha}")
        print(f"Начальная длина:    {l0:.3f} мм")
        print(f"Температура t1:     {t1:.2f} °C")
        print(f"Температура t2:     {t2:.2f} °C")
        print(f"Изменение ΔL:       {delta_l:.4f} мм")
        print(f"Конечная длина L:   {length:.4f} мм")
        print(f"Класс расширения:   {cls}")
        print("\nРасчёт завершён.")


if __name__ == "__main__":
    main()
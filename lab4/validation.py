
"""
Проверка пользовательского ввода.
"""

from __future__ import annotations

import math

from constants import (
    L0_MIN,
    L0_MAX,
    T1_MIN,
    T1_MAX,
    T2_MIN,
    T2_MAX,
)

from logger import log_error


def validate_range(
    value: float,
    low: float,
    high: float,
) -> tuple[bool, str]:
    """Проверить попадание числа в заданный диапазон."""

    if not math.isfinite(value):
        return False, "Ошибка: число должно быть конечным."

    if value < low:
        return False, (
            f"Ошибка: значение меньше нижней границы ({low})."
        )

    elif value > high:
        return False, (
            f"Ошибка: значение больше верхней границы ({high})."
        )

    else:
        return True, ""


def input_number(
    prompt: str,
    low: float,
    high: float,
) -> float:
    """Повторять ввод до получения корректного числа."""

    while True:
        raw = input(prompt).strip()

        try:
            value = float(raw)

        except ValueError:
            msg = f"Ошибка: введено не число ('{raw}')."
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)

        if ok:
            return value

        print(msg + " Повторите ввод.")
        log_error(msg)


def input_length() -> float:
    """Ввод начальной длины L0 (1..10000 мм)."""

    return input_number(
        "Введите начальную длину L0, мм (1..10000): ",
        L0_MIN,
        L0_MAX,
    )


def input_initial_temperature() -> float:
    """Ввод начальной температуры t1 (-60..200 °C)."""

    return input_number(
        "Введите начальную температуру t1, °C (-60..200): ",
        T1_MIN,
        T1_MAX,
    )


def input_final_temperature(t1: float) -> float:
    """
    Ввод конечной температуры t2 (-60..800 °C).

    Обязательное условие: t2 > t1.
    """

    while True:
        t2 = input_number(
            "Введите конечную температуру t2, °C (-60..800): ",
            T2_MIN,
            T2_MAX,
        )

        if t2 > t1:
            return t2

        msg = (
            "Ошибка: конечная температура t2 "
            "должна быть больше начальной t1."
        )

        print(msg + " Повторите ввод.")
        log_error(msg)


"""
Расчёт температурного расширения детали.
"""

from typing import Annotated

from constants import (
    EXPANSION_SMALL_LIMIT,
    EXPANSION_LARGE_LIMIT,
)


def thermal_expansion(
    l0: Annotated[float, "Начальная длина, мм"],
    alpha: Annotated[float, "Коэффициент расширения"],
    t1: Annotated[float, "Начальная температура, °C"],
    t2: Annotated[float, "Конечная температура, °C"],
) -> float:
    """
    Рассчитать изменение длины детали.

    Формула:
        ΔL = L0 * alpha * (t2 - t1)

    Returns:
        Изменение длины ΔL, мм.
    """
    return l0 * alpha * (t2 - t1)


def final_length(
    l0: Annotated[float, "Начальная длина, мм"],
    delta_l: Annotated[float, "Изменение длины, мм"],
) -> float:
    """
    Рассчитать конечную длину детали.

    Формула:
        L = L0 + ΔL
    """
    return l0 + delta_l


def expansion_class(
    delta_l: Annotated[float, "Изменение длины, мм"],
) -> str:
    """
    Классификация температурного расширения.

    ΔL < 0.1 — пренебрежимое;
    0.1 <= ΔL <= 2 — учитываемое;
    ΔL > 2 — значительное.
    """

    if delta_l < EXPANSION_SMALL_LIMIT:
        return "пренебрежимое"

    elif delta_l <= EXPANSION_LARGE_LIMIT:
        return "учитываемое"

    else:
        return "значительное"
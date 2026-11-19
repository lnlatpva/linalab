from typing import Dict, Sequence
import math

def _ensure_not_empty(data: Sequence[float]) -> None:

    if not data:

        raise ValueError("Ряд пуст: расчёт статистики невозможен")

def mean(data: Sequence[float]) -> float:

    """Среднее арифметическое."""

    _ensure_not_empty(data)

    return sum(data) / len(data)

def median(data: Sequence[float]) -> float:

    """Медиана."""

    _ensure_not_empty(data)

    s = sorted(data)

    k = len(s) // 2

    if len(s) % 2:

        return float(s[k])

    return (s[k - 1] + s[k]) / 2.0

def spread(data: Sequence[float]) -> float:

    """Размах ряда: max - min."""

    _ensure_not_empty(data)

    return float(max(data) - min(data))

def summarize(data: Sequence[float]) -> Dict[str, float]:

    """Сводный отчёт: count, mean, median, spread, min, max."""

    _ensure_not_empty(data)

    return {

        "count": len(data),

        "mean": mean(data),

        "median": median(data),

        "spread": spread(data),

        "min": float(min(data)),

        "max": float(max(data)),

    }

# Вариант 13. Асимметрия и эксцесс

def _central_moment(
    data: Sequence[float],
    order: int
) -> float:
    """Вычисление центрального момента заданного порядка."""
    _ensure_not_empty(data)

    avg = mean(data)
    n = len(data)

    return sum(
        (x - avg) ** order
        for x in data
    ) / n


def skewness(data: Sequence[float]) -> float:
    """Коэффициент асимметрии распределения.

    skewness = m3 / m2 ** 1.5
    """
    _ensure_not_empty(data)

    m2 = _central_moment(data, 2)
    m3 = _central_moment(data, 3)

    if m2 == 0:
        return 0.0

    result = m3 / (m2 ** 1.5)

    if not math.isfinite(result):
        raise ValueError("Асимметрия содержит NaN или inf")

    return result


def kurtosis(data: Sequence[float]) -> float:
    """Эксцесс распределения.

    kurtosis = m4 / m2 ** 2 - 3
    """
    _ensure_not_empty(data)

    m2 = _central_moment(data, 2)
    m4 = _central_moment(data, 4)

    if m2 == 0:
        return 0.0

    result = m4 / (m2 ** 2) - 3

    if not math.isfinite(result):
        raise ValueError("Эксцесс содержит NaN или inf")

    return result


def check_exponential_series(
    data: Sequence[float]
) -> bool:
    """Проверка краевого случая варианта 13.

    Все элементы ряда должны быть строго положительными.
    Значения и результаты статистики должны быть конечными.
    """
    _ensure_not_empty(data)

    if not all(
        math.isfinite(x) and x > 0
        for x in data
    ):
        return False

    stats_values = [
        mean(data),
        median(data),
        spread(data),
        skewness(data),
        kurtosis(data),
    ]

    return all(
        math.isfinite(value)
        for value in stats_values
    )
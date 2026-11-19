"""Скользящие средние на основе collections.deque.

Отдельный модуль, не заменяющий moving_average.py:
- сохраняет публичный контракт (Sequence[float] -> list[float]);
- реализует SMA, CMA и EMA через deque(maxlen=...);
- удобен для потоковой обработки и сравнения с индексной версией.
"""

from __future__ import annotations
from collections import deque
from typing import Deque, List, Sequence

# Валидация (единая точка отказа — fail fast)

def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError(
            "Ряд пуст: расчёт скользящей средней невозможен"
        )

def _check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(
            f"window должен быть целым, получено: {window!r}"
        )

    if window < 1:
        raise ValueError(
            f"window должен быть >= 1, получено: {window}"
        )

    if window > n:
        raise ValueError(
            f"window ({window}) больше длины ряда ({n}) — SMA невозможна"
        )

def _check_alpha(alpha: float) -> None:
    if not isinstance(alpha, (int, float)) or isinstance(alpha, bool):
        raise ValueError(
            f"alpha должен быть числом, получено: {alpha!r}"
        )

    if not (0 < alpha <= 1):
        raise ValueError(
            f"alpha должен быть в (0, 1], получено: {alpha}"
        )

# Простая скользящая средняя (SMA) через deque

def simple_moving_average_deque(
    data: Sequence[float],
    window: int,
) -> List[float]:
    """SMA через deque(maxlen=window).

    Сложность: O(n) по времени, O(window) по памяти.

    Пример:
    >>> simple_moving_average_deque([1, 2, 3, 4, 5], 3)
    [2.0, 3.0, 4.0]
    """
    _ensure_not_empty(data)
    _check_window(window, len(data))

    buf: Deque[float] = deque(maxlen=window)
    running = 0.0
    result: List[float] = []

    for i, x in enumerate(data):
        if len(buf) == window:
            running -= buf[0]

        buf.append(x)
        running += x

        if i >= window - 1:
            result.append(running / window)

    return result

# Центрированное MA через deque

def centered_moving_average_deque(
    data: Sequence[float],
    window: int,
) -> List[float]:
    """Центрированное MA: окно нечётное, значения выровнены по центру."""
    _ensure_not_empty(data)
    _check_window(window, len(data))

    if window % 2 == 0:
        raise ValueError(
            f"Центрированное MA требует нечётного window, "
            f"получено: {window}"
        )

    half = window // 2
    buf: Deque[float] = deque(maxlen=window)
    running = 0.0
    result: List[float] = []

    for x in data:
        if len(buf) == window:
            running -= buf[0]

        buf.append(x)
        running += x

        if len(buf) == window:
            result.append(running / window)

    # Результат содержит n - window + 1 значений.
    # Первое значение соответствует центру с индексом half.
    return result

# Экспоненциальная скользящая средняя (EMA) через deque

def exponential_moving_average_deque(
    data: Sequence[float],
    alpha: float,
) -> List[float]:
    """EMA через deque для хранения последнего сглаженного значения.

    EMA[0] = data[0]
    EMA[i] = alpha * data[i] + (1 - alpha) * EMA[i-1]
    """
    _ensure_not_empty(data)
    _check_alpha(alpha)

    prev = float(data[0])
    buf: Deque[float] = deque([prev], maxlen=1)
    result: List[float] = [prev]

    for x in data[1:]:
        prev = alpha * x + (1.0 - alpha) * buf[-1]
        buf.append(prev)
        result.append(prev)

    return result

# Публичный список функций модуля

__all__ = [
    "simple_moving_average_deque",
    "centered_moving_average_deque",
    "exponential_moving_average_deque",
]
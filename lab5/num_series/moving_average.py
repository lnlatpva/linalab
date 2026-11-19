import time
from collections import deque
from typing import List, Sequence

def _check_window(window: int, n: int) -> None:

    """Проверка размера окна."""

    try:

        is_valid = (

            isinstance(window, int)

            and not isinstance(window, bool)

            and window >= 1

            and window <= n

        )

    except TypeError as err:

        raise ValueError(

            f"window должно быть целым числом от 1 до {n}"

        ) from err

    if not is_valid:

        raise ValueError(

            f"window должно быть целым числом от 1 до {n} "

            f"(получено: {window!r})"

        )

def simple_moving_average(

    data: Sequence[float],

    window: int

) -> List[float]:

    """Простая скользящая средняя через бегущую сумму."""

    _check_window(window, len(data))

    running = sum(data[:window])

    result = [running / window]

    for i in range(window, len(data)):

        running += data[i] - data[i - window]

        result.append(running / window)

    return result

def centered_moving_average(

    data: Sequence[float],

    window: int

) -> List[float]:

    """Центрированная скользящая средняя."""

    _check_window(window, len(data))

    if window % 2 == 0:

        raise ValueError("Для центрированной MA окно должно быть нечётным")

    sma = simple_moving_average(data, window)

    result = [0.0] * len(data)

    offset = window // 2

    for i, value in enumerate(sma):

        result[i + offset] = value

    return result

def exponential_moving_average(

    data: Sequence[float],

    alpha: float

) -> List[float]:

    """Экспоненциальная скользящая средняя."""

    if not data:

        raise ValueError("Ряд пуст: расчёт EMA невозможен")

    if not isinstance(alpha, (int, float)) or isinstance(alpha, bool):

        raise ValueError("alpha должно быть числом от 0 до 1")

    if not 0 < alpha <= 1:

        raise ValueError(

            f"alpha должно быть в диапазоне (0, 1] (получено: {alpha})"

        )

    result = [float(data[0])]

    for i in range(1, len(data)):

        value = alpha * data[i] + (1 - alpha) * result[-1]

        result.append(value)

    return result

# Простая скользящая средняя через deque

def simple_moving_average_deque(
    data: Sequence[float],
    window: int
) -> List[float]:
    """SMA с использованием deque (двусторонней очереди)."""
    _check_window(window, len(data))

    result = []
    d = deque()
    running_sum = 0.0

    for x in data:
        d.append(x)
        running_sum += x

        if len(d) > window:
            running_sum -= d.popleft()

        if len(d) == window:
            result.append(running_sum / window)

    return result

# Замер времени выполнения SMA

def benchmark_moving_average(
    data: Sequence[float],
    window: int,
    repeats: int = 1000
) -> dict:
    """Замеряет среднее время SMA для list и deque.

    Возвращает словарь с ключами 'list' и 'deque'.
    Значения — время выполнения в секундах.
    """
    _check_window(window, len(data))

    if not isinstance(repeats, int) or isinstance(repeats, bool) or repeats < 1:
        raise ValueError("repeats должен быть положительным целым числом")

    # Замер для list-реализации
    t0 = time.perf_counter()

    for _ in range(repeats):
        simple_moving_average(data, window)

    t_list = (time.perf_counter() - t0) / repeats

    # Замер для deque-реализации
    t0 = time.perf_counter()

    for _ in range(repeats):
        simple_moving_average_deque(data, window)

    t_deque = (time.perf_counter() - t0) / repeats

    return {
        "list": t_list,
        "deque": t_deque
    }
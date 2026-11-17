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
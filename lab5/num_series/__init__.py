
"""Пакет алгоритмической обработки числовых рядов."""

from .generator import (
    random_series,
    sine_series,
    trend_series,
    exponential_series,
)

from .stats import (
    mean,
    median,
    spread,
    summarize,
    skewness,
    kurtosis,
    check_exponential_series,
)

from .moving_average import (
    simple_moving_average,
    simple_moving_average_deque,
    centered_moving_average,
    exponential_moving_average,
    benchmark_moving_average,
)

from .deque_average import (
    simple_moving_average_deque as deque_sma,
    centered_moving_average_deque,
    exponential_moving_average_deque,
)

from .io_json import (
    save_series_json,
    load_series_json,
)

from .io_file import (
    load_series_txt,
    load_series_csv,
    load_series_auto,
)


__all__ = [
    # генерация
    "random_series",
    "sine_series",
    "trend_series",
    "exponential_series",

    # статистика
    "mean",
    "median",
    "spread",
    "summarize",
    "skewness",
    "kurtosis",
    "check_exponential_series",

    # скользящие средние
    "simple_moving_average",
    "simple_moving_average_deque",
    "centered_moving_average",
    "exponential_moving_average",
    "benchmark_moving_average",

    # отдельный модуль deque
    "deque_sma",
    "centered_moving_average_deque",
    "exponential_moving_average_deque",

    # ввод-вывод
    "save_series_json",
    "load_series_json",
    "load_series_txt",
    "load_series_csv",
    "load_series_auto",
    
]

__version__ = "1.3.0"
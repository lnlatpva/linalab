import math

# --- Коэффициенты температурного расширения (Вариант 13) ---
ALPHA_STEEL: float = 1.2 * math.e-5
ALPHA_ALUMINUM: float = 2.3 * math.e-5
ALPHA_COPPER: float = 1.7 * math.e-5

# --- Допустимые диапазоны входных данных ---
L0_MIN: float = 1.0
L0_MAX: float = 10000.0

T1_MIN: float = -60.0
T1_MAX: float = 200.0

T2_MIN: float = -60.0
T2_MAX: float = 800.0

# --- Границы классификации расширения ---
EXPANSION_SMALL_LIMIT: float = 0.1
EXPANSION_LARGE_LIMIT: float = 2.0

# --- Файл журнала ошибок ---
LOG_FILE: str = "input_errors.log"

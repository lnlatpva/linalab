
"""
Меню выбора материала через match-case.
"""

from __future__ import annotations

from constants import (
    ALPHA_STEEL,
    ALPHA_ALUMINUM,
    ALPHA_COPPER,
)


def show_menu() -> None:
    """Вывести меню выбора материала."""
    print("\nВыберите материал детали:")
    print("  1 — сталь     (α = 1.2e-5)")
    print("  2 — алюминий  (α = 2.3e-5)")
    print("  3 — медь      (α = 1.7e-5)")
    print("  0 — выход")


def select_material() -> float | None:
    """
    Запросить материал и вернуть коэффициент alpha.
    None возвращается при выборе выхода.
    """
    while True:
        choice = input(
            "Введите номер материала (от 0 до 3): "
        ).strip()

        match choice:
            case "1":
                return ALPHA_STEEL
            case "2":
                return ALPHA_ALUMINUM
            case "3":
                return ALPHA_COPPER
            case "0":
                return None
            case _:
                print(
                    "Ошибка: неверный пункт меню. "
                    "Повторите ввод."
                )


def material_name(alpha: float) -> str:
    """Вернуть название материала по коэффициенту."""

    match alpha:
        case 1.2e-5:
            return "сталь"
        case 2.3e-5:
            return "алюминий"
        case 1.7e-5:
            return "медь"
        case _:
            return "неизвестный материал"
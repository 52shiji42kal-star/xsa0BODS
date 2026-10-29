# lib3
# python -m venv .venv
# .venv\Scripts\activate
# pip install colorama
# pip freeze > requirements.txt
# echo .venv/ >> .gitignore

# lib4
try:
    import colorama
    COLOR = True
except ImportError:
    COLOR = False

status = "Система работает нормально"
print(colorama.Fore.GREEN + status if COLOR else status)

# lib5
# Fore: RED, BLUE, MAGENTA
# Style: BRIGHT, DIM

try:
    import colorama
    win_str = colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "Вы победили врага!" + colorama.Style.RESET_ALL
except ImportError:
    win_str = "Вы победили врага!"

print(win_str)

# lib6
"""Модуль dungeon.py реализует логику текстового приключения в подземном лабиринте."""

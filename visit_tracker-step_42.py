# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: VisitTracker
import sys

ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
}

COLORS = {
    'info': 'cyan',
    'success': 'green',
    'warning': 'yellow',
    'error': 'red',
    'heading': 'bold',
    'dim': 'dim',
}


def _colorize(text, color_name):
    code = ANSI.get(color_name, '')
    if not code:
        return text
    return f'{code}{text}{ANSI["reset"]}'


def info(msg):
    print(_colorize(f'  ┌─ {msg}', 'info'))


def success(msg):
    print(_colorize(f'  ✓ {msg}', 'success'))


def warning(msg):
    print(_colorize(f'  ⚠ {msg}', 'warning'))


def error(msg):
    print(_colorize(f'  ✗ {msg}', 'error'))


def heading(text):
    print(_colorize(f'══════ {text} ══════', 'heading'))


def dim(text):
    print(_colorize(f'  {text}', 'dim'))

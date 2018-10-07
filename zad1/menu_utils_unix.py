import sys,tty,termios
import readline

# Skopiowane z internetu, pobiera strzalki w konsoli
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch != '\r':
                ch += sys.stdin.read(2)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# -1 - up
# 2 - enter
# 1 - down
# 0 - other
# https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples
def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    if k=='\r':
        return 2
    elif k=='\x1b[A':
        return -1
    elif k=='\x1b[B':
        return +1
    else:
        return 0

def print_menu_option(label, isSelected):
    arrow = '=> ' if isSelected else ''
    colorStart = '\033[95m' if isSelected else ''
    colorEnd = '\033[0m' if isSelected else ''
    print(colorStart + arrow + label + colorEnd)

def print_menu(selectedOption):
    print_menu_option('Dodawanie', selectedOption == 0)
    print_menu_option('Odejmowanie', selectedOption == 1)
    print_menu_option('Mnożenie', selectedOption == 2)
    print_menu_option('Dzielenie', selectedOption == 3)
    print_menu_option('Modulo', selectedOption == 4)
    print_menu_option('Wyjście', selectedOption == 5)

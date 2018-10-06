#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from menu_utils import print_menu, get

def clear_console():
    print('\033[H\033[J')

def main():
    option = 0
    shouldBeRunning = True
    while(shouldBeRunning):
        #print menu
        clear_console()
        print_menu(option)
        #get option
        key = get()
        if (key == 2):
            shouldBeRunning = handle_option(option)
        else:
            option += key
        option = max(0, min(option, 5)) 

def load_numbers():
    x = float(input('Podaj pierwszą liczbę: '))
    y = float(input('Podaj drugą liczbę: '))
    return x, y

def handle_calculator_option(option):
    x, y = load_numbers()
    # TODO: Handle exceptions
    if option == 0:
        result = add(x, y)
    elif option == 1:
        result = subtract(x, y)
    elif option == 2:
        result = mulitply(x, y)
    elif option == 3:
        result = divide(x, y)
    elif option == 4:
        result = modulo(x, y)

    print('Wynik: ' + str(result))

# returns true if app should still be running
def handle_option(option):
    clear_console()
    if option < 5:
        handle_calculator_option(option)
    elif option == 5:
        return False
    
    input('Naciśnij [Enter] aby kontynuować...')
    return True

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mulitply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

if __name__ == '__main__':
  main()

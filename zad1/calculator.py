#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from menu_utils_windows import print_menu, get

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

operationSymbols = ['+', '-', '*', '/', '%']
operationNames = ['Dodawanie', 'Odejmowanie', 'Mnozenie', 'Dzielenie', 'Modulo']
functions = [add, subtract, mulitply, divide, modulo]

def clear_console():
    print('\033[H\033[J')

# main UNIX
# def main():
#     option = 0
#     shouldBeRunning = True
#     while(shouldBeRunning):
#         #print menu
#         clear_console()
#         print_menu(option)
#         #get option
#         key = get()
#         if (key == 2):
#             shouldBeRunning = handle_option(option)
#         else:
#             option += key
#         option = max(0, min(option, 5)) 

#main WINDOWS
def main():
    import os
    shouldBeRunning = True
    while(shouldBeRunning):
        #print menu
        os.system("cls")
        print_menu()
        #get option
        key = get()
        shouldBeRunning = handle_option(key - 1) # - 1 because indexing starts from 0 

def load_numbers():
    x = float(input('Podaj pierwszą liczbę: '))
    y = float(input('Podaj drugą liczbę: '))
    return x, y

def handle_calculator_option(option):
    x, y = load_numbers()
    # TODO: Handle exceptions
    result = functions[option](x, y)
    log = '[Wynik] ' + str(x) + ' ' + operationSymbols[option] + ' ' + str(y) + ' = ' + str(result)

    print(log)

# returns true if app should still be running
def handle_option(option):
    clear_console()
    if option < 5:
        handle_calculator_option(option)
    elif option == 5:
        return False
    
    input('Naciśnij [Enter] aby kontynuować...')
    return True

if __name__ == '__main__':
  main()

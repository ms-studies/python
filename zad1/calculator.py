#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from menu_utils_windows import print_menu, get
from file_utils import write_line_to_file
import os

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mulitply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        handle_zero_division_error()

def modulo(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        handle_zero_division_error()
        
def handle_zero_division_error():
    print('Nie można dzielić przez 0')
    return None
    
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

def start_session():
    import datetime
    now = datetime.datetime.now()
    write_line_to_file("== " + now.strftime("%Y-%m-%d") + " ==")

#main WINDOWS
def main():
    start_session()
    shouldBeRunning = True
    while(shouldBeRunning):
        #print menu
        os.system("cls")
        print_menu()
        #get option
        key = get()
        shouldBeRunning = handle_option(key - 1) # - 1 because indexing starts from 0 

def load_numbers():
    return load_number(), load_number()

def load_number():
    number = None
    while(number == None):
        try:
            number = float(input('Podaj liczbę: '))
        except ValueError:
            print('To nie jest liczba :(')
            number = None
    return number

def handle_calculator_option(option):
    x, y = load_numbers()
    result = functions[option](x, y)
    if (result != None):
        result_to_save = str(x) + ' ' + operationSymbols[option] + ' ' + str(y) + ' = ' + str(result)
        write_line_to_file(result_to_save)
        log = '[Wynik] ' + result_to_save
        print(log)
    
# returns true if app should still be running
def handle_option(option):
    clear_console()
    if option < 5:
        handle_calculator_option(option)
    elif option == 5:
        show_current_session()
    elif option == 6:
        handle_current_date()
    elif option == 7:
        return False
    
    input('Naciśnij [Enter] aby kontynuować...')
    return True

if __name__ == '__main__':
  main()

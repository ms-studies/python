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

# returns true if app should still be running
def handle_option(option):
    clear_console()
    if option < 5:
        x = input('Podaj pierwszą liczbę: ')
        y = input('Podaj drugą liczbę: ')

    result = 0
    if option == 0:
        result = add(x, y)
    elif option == 1:
        subtract()
    elif option == 2:
        mulitply()
    elif option == 3:
        divide()
    elif option == 4:
        modulo()
    elif option == 5:
        return False
    
    print('Wynik: '+result)
    input('Naciśnij [Enter] aby kontynuować...')
    return True

def add(x, y):
    return x + y

def subtract():
    return 0

def mulitply():
    return 0

def divide():
    return 0

def modulo():
    return 0

if __name__ == '__main__':
  main()

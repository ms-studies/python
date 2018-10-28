import numpy as np
from collections import Counter

def main():
    load_data()

def load_data():
    data = np.loadtxt("iris.data",
    dtype={'names': ('sepal length', 'sepal width', 'petal length', 'petal width', 'label'),
            'formats': (np.float, np.float, np.float, np.float, '|S15')},
    delimiter=',', skiprows=0)
    print(data)
    find_medians(data)
    find_maximums(data)
    find_minimums(data)
    find_dominant(find_column_elements(data, 4))

def find_column_elements(data, column):
    columnElements = []
    for row in range(len(data)):
        columnElements.append(data[row][column])
    return columnElements

def find_median(columnData):
    return np.median(columnData)

def find_medians(data):
    print('\nMediana dla kolumny sepal length: ' + str(find_median(find_column_elements(data, 0))))
    print('Mediana dla kolumny sepal width: ' + str(find_median(find_column_elements(data, 1))))
    print('Mediana dla kolumny petal length: ' + str(find_median(find_column_elements(data, 2))))    
    print('Mediana dla kolumny petal width: ' + str(find_median(find_column_elements(data, 3))))

def find_max(columnData):
    return np.amax(columnData)

def find_maximums(data):
    print('\nMaximum dla kolumny sepal length: ' + str(find_max(find_column_elements(data, 0))))
    print('Maximum dla kolumny sepal width: ' + str(find_max(find_column_elements(data, 1))))
    print('Maximum dla kolumny petal length: ' + str(find_max(find_column_elements(data, 2))))    
    print('Maximum dla kolumny petal width: ' + str(find_max(find_column_elements(data, 3))))

def find_min(columnData):
    return np.amin(columnData)

def find_minimums(data):
    print('\nMinimum dla kolumny sepal length: ' + str(find_min(find_column_elements(data, 0))))
    print('Minimum dla kolumny sepal width: ' + str(find_min(find_column_elements(data, 1))))
    print('Minimum dla kolumny petal length: ' + str(find_min(find_column_elements(data, 2))))    
    print('Minimum dla kolumny petal width: ' + str(find_min(find_column_elements(data, 3))))

def find_dominant(columnData):
    count_map = Counter(columnData) # count_map przechowuje mape zawierajaca element i liczbe wystapien elementu
    freqency_list = [list(count_map.values()).count(x) for x in count_map] # lista przechowujaca ile razy dany element wystapil
    max_count = max(freqency_list) # wyznaczenie maksymalnej liczby wystapien
    most_frequent_elements_counter = freqency_list.count(max_count) # wyznaczenie liczby elementow z maksymalna liczba wystapien
    most_common = count_map.most_common(most_frequent_elements_counter)
    print('\nDominanta dla kolumny label: ' + str([elem[0] for elem in most_common]) + ', liczba wystąpień: ' + str(most_common[0][1]))
    ## TODO Zastanowic sie, czy chcemy dla wiecej niz jednej wartosci dominujacej nie wyswietlac zadnej wartosci czy wyswietlac wszystkie

if __name__ == '__main__':
  main()
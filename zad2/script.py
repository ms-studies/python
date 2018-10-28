import numpy as np
from collections import Counter
import pandas as pd  #trzeba zrobic pip install wheel pip install pandas
import matplotlib.pyplot as plt #trzeba zrobic pip install matplotlib
from matplotlib import colors

def main():
    data = load_data()
    find_medians(data)
    find_maximums(data)
    find_minimums(data)
    find_dominant(find_column_elements(data, 4))
    correlated_column_1, correlated_column_2 = find_most_correlated_columns(data)
    draw_histogram(data, correlated_column_1, correlated_column_2)

def load_data():
    data = np.loadtxt("iris.data",
    dtype={'names': ('sepal length', 'sepal width', 'petal length', 'petal width', 'label'),
            'formats': (np.float, np.float, np.float, np.float, '|S15')},
    delimiter=',', skiprows=0)
    print(data)
    return data

def draw_histogram(data, col1, col2):
    plt.scatter(find_column_elements(data, col1), find_column_elements(data, col2))
    plt.xlabel(data.dtype.names[col1])
    plt.ylabel(data.dtype.names[col2])
    plt.show()

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

def find_most_correlated_columns(data):
    data_frame = pd.DataFrame(data)
    data_frame.drop(data_frame.columns[4], axis=1, inplace=True)
    correlaton_matrix = data_frame.corr().abs()
    correlated_values = (correlaton_matrix.where(np.triu(np.ones(correlaton_matrix.shape), k=1).astype(np.bool))
                 .stack()
                 .sort_values(ascending=False))

    for row in range(correlaton_matrix.shape[0]): # df is the DataFrame
         for col in range(correlaton_matrix.shape[1]):
             if correlaton_matrix.iloc[row][col] == correlated_values.iloc[0]:
                 return row, col

if __name__ == '__main__':
  main()
import numpy as np
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import colors
from utils import find_column_elements, load_irys_data

def main():
    data = load_irys_data()
    find_medians(data)
    find_maximums(data)
    find_minimums(data)
    find_dominant(find_column_elements(data, 4))
    correlated_column_1, correlated_column_2 = find_most_correlated_columns(data)
    draw_histograms(data, correlated_column_1, correlated_column_2)

def draw_histograms(data, col1, col2):
    attribute1 = find_column_elements(data, col1)
    normalized_attribute_1 = (attribute1 - np.min(attribute1)) / (np.amax(attribute1) - np.amin(attribute1))
    plt.hist(normalized_attribute_1, bins = 50, label=data.dtype.names[col1])

    attribute2 = find_column_elements(data, col2)
    normalized_attribute_2 = (attribute2 - np.amin(attribute2)) / (np.amax(attribute2) - np.amin(attribute2))
    plt.hist(normalized_attribute_2, bins = 50, label=data.dtype.names[col2])
    plt.legend()
    plt.ylabel('Liczba wystąpień')
    plt.xlabel('Znormalizowany rozkład wystąpień')
    plt.show()


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

def find_most_correlated_columns(data):
    data_frame = pd.DataFrame(data)
    data_frame.drop(data_frame.columns[4], axis=1, inplace=True)
    correlaton_matrix = data_frame.corr().abs()
    print(correlaton_matrix)
    correlated_values = (correlaton_matrix.where(np.triu(np.ones(correlaton_matrix.shape), k=1).astype(np.bool))
                 .stack()
                 .sort_values(ascending=False))

    for row in range(correlaton_matrix.shape[0]): # df is the DataFrame
         for col in range(correlaton_matrix.shape[1]):
             if correlaton_matrix.iloc[row][col] == correlated_values.iloc[0]:
                 return row, col

if __name__ == '__main__':
  main()
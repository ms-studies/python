import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
from utils import find_column_elements, load_irys_data

def main():
    data = load_irys_data()
    test_hypothesis(data)
    draw_histogram(data)

def draw_histogram(data):
    versicolour = extract_one_species(data, 'Iris-versicolor')
    virginica = extract_one_species(data, 'Iris-virginica')

    by_sepal_width = [
        find_column_elements(versicolour, 1),
        find_column_elements(virginica, 1),
    ]
    labels = ['Versicolor', 'Virginica']
    colors = ['red', 'blue']
    for arr in by_sepal_width:
        mean = np.mean(arr)
        variance = np.var(arr)
        sigma = np.sqrt(variance)
        x = np.linspace(min(arr), max(arr), 100)
        plt.plot(x, mlab.normpdf(x, mean, sigma)*5, color=colors[by_sepal_width.index(arr)])

    plt.hist(by_sepal_width, bins=25, color=colors, label=labels)                                                                    
    plt.legend()
    plt.xlabel('Sepal width [cm]')
    plt.show()

def extract_one_species(data, species):
    return [a for a in data if a[4].decode() == species]

def test_hypothesis(data):
    print('Badam hipoteze czy można użyć parametru "sepal width" do rozróżnienia klas kwiatów Iris Versicolour oraz Iris Virginica z poziom istotności statystycznej 5%')
    versicolour = extract_one_species(data, 'Iris-versicolor')
    virginica = extract_one_species(data, 'Iris-virginica')
    value, pvalue = stats.ttest_ind(find_column_elements(versicolour, 1), find_column_elements(virginica, 1))
    print(value, pvalue)
    # Hipoteza zerowa: nie można można rozróżnić zbiorów na podstawie parametru "sepal width", hipoteza alternatywna: można rozróżnić zbiory na podstawie parametru "sepal width"
    if pvalue < 0.05:
	    print('Odrzucamy hipotezę zerową - można rozróżnić zbiory na podstawie parametru "sepal width"')
    else:
	    print('Nie ma podstaw do odrzucenia hipotezy zerowej - nie można można rozróżnić zbiorów na podstawie parametru "sepal width"')

if __name__ == '__main__':
  main()
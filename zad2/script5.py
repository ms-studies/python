import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from utils import find_column_elements, load_irys_data

def main():
    data = load_irys_data()
    draw_histogram(data)

def draw_histogram(data):
    versicolour = extract_one_species(data, 'Iris-versicolor')
    virginica = extract_one_species(data, 'Iris-virginica')
    setosa = extract_one_species(data, 'Iris-setosa')

    by_sepal_width = [
        find_column_elements(versicolour, 1),
        find_column_elements(virginica, 1),
        find_column_elements(setosa, 1)
    ]

    labels = ['Versicolor', 'Virginica', 'Setosa']
    colors = ['red', 'blue', 'orange']

    for arr in by_sepal_width:
        mean = np.mean(arr)
        variance = np.var(arr)
        sigma = np.sqrt(variance)
        x = np.linspace(min(arr), max(arr), 100)
        plt.plot(x, mlab.normpdf(x, mean, sigma)*5, color=colors[by_sepal_width.index(arr)]) #uwaga - tutaj mnoze razy piec zeby lepiej bylo widac na histogramie, nie wiem czy to jest ok 
    

    plt.hist(by_sepal_width, bins=25, color=colors, label=labels)                                                                    
    plt.legend()
    plt.xlabel('Sepal width [cm]')
    plt.show()

def extract_one_species(data, species):
    return [a for a in data if a[4].decode() == species]


if __name__ == '__main__':
  main()
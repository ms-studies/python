import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from utils import find_column_elements, load_births_data

def main():
    data = load_births_data()
    mean = test_hypothesis(data, 1000)
    draw_histogram(data, mean)

def draw_histogram(data, mean):
    births = find_column_elements(data, 2)
    plt.hist(births, bins=100)
    plt.ylabel('Number of days')
    plt.xlabel('Number of births')
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=1)
    plt.show()

def test_hypothesis(data, size):
    print('Badam hipoteze czy dzienna srednia urodzen wynosi 10000 na losowej probie ' + str(size) + ' krotek z poziom istotności statystycznej 5%')
    births = find_column_elements(data, 2)
    np.random.shuffle(births)
    
    mean = np.mean(births[1:size])
    print('Dzienna srednia urodzin wynosi ' + str(mean) + '.')
    if mean >= 0.95*10000 and mean <= 1.05*10000:
        print('Hipoteza potwierdzona.')
    else:
        print('Hipoteza obalona.')
    
    return mean

if __name__ == '__main__':
  main()
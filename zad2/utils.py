import numpy as np

def find_column_elements(data, column):
    columnElements = []
    for row in range(len(data)):
        columnElements.append(data[row][column])
    return columnElements

def load_irys_data():
    data = np.loadtxt("iris.data",
    dtype={'names': ('sepal length', 'sepal width', 'petal length', 'petal width', 'label'),
            'formats': (np.float, np.float, np.float, np.float, '|S15')},
    delimiter=',', skiprows=0)
    return data

def load_births_data():
    data = np.loadtxt("Births.csv",
    dtype={'names': ('id','date', 'births', 'wday', 'year', 'month', 'day', 'day_of_year', 'day_of_week'),
            'formats': ('|S15', '|S15', np.int, '|S15', np.int, np.int, np.int, np.int, np.int)},
    delimiter=',', skiprows=1)
    return data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = pd.read_csv('winequality-red.csv')
    data = addMissingData(data)
    print(calculatePercentage(data))
    dataWithoutMissingValues = data.dropna()
    drawRegressionCurve(dataWithoutMissingValues)

def addMissingData(data):
    data.sample(frac=1)
    for i in range(100):
        data.iat[i,0] = None
    return data

def calculatePercentage(data):
    columns = data.columns
    percent_missing = data.isnull().sum() * 100 / len(data)
    missing_value = pd.DataFrame({'column_name': columns,
                                 'percent_missing': percent_missing})
    missing_value.sort_values('percent_missing', inplace=True)
    return missing_value

def drawRegressionCurve(data):
    plt.plot(data['pH'], data['fixed acidity'],'o',markersize=2)
    plt.show()

if __name__ == '__main__':
  main()

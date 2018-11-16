import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import statistics 
import math

def main():
    data = pd.read_csv('winequality-red.csv')
    data = addMissingData(data)

    print(calculatePercentage(data))
    dataWithoutMissingValues = data.dropna()
    
    #linear regression
    print("\n========= Without missing values ==========")
    drawRegressionCurve(dataWithoutMissingValues)
    printDatasetCharacteristics(dataWithoutMissingValues['fixed acidity'])

    #filling with mean
    print("\n========= Filled with mean ==========")
    filledDataWithMean = fillMissingValuesWithMeanValue(data.copy())
    printDatasetCharacteristics(filledDataWithMean['fixed acidity'])
    drawRegressionCurve(filledDataWithMean)

    #filling with regression
    print("\n========= Filled with regression ==========")
    filledDataWithRegression = fillMissingValuesRegression(data.copy())
    printDatasetCharacteristics(filledDataWithRegression['fixed acidity'])
    drawRegressionCurve(filledDataWithRegression)

    #filling with interpolation
    print("\n========= Filled with interpolation ==========")
    filledDataWithInterpolation = fillMissingValuesInterpolation(data.copy())
    printDatasetCharacteristics(filledDataWithInterpolation['fixed acidity'])
    drawRegressionCurve(filledDataWithInterpolation)

    plt.show()


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

def createLinearRegressionModel(data):
    model = LinearRegression()
    x = data[['pH']]
    y = data[['fixed acidity']]
    model.fit(x, y)
    return model, x, y

def drawRegressionCurve(data):
    model, x, y = createLinearRegressionModel(data)

    # predict y from the data
    x_new = np.linspace(2.7, 4.1, 100) # arguments: beginning of x range, end of x range, number of samples to generate
    y_new = model.predict(x_new[:, np.newaxis]) 

    # plot the results
    plt.figure(figsize=(7, 5))
    ax = plt.axes()
    ax.scatter(x, y, s=6) # s - size of dots
    ax.plot(x_new, y_new)

    ax.set_xlabel('pH')
    ax.set_ylabel('fixed acidity')

    ax.axis('tight')

def printDatasetCharacteristics(column):
    print("Standard Deviation of sample is % s " 
                % (statistics.stdev(column))) 
    print("Mean of sample is % s " 
                % (statistics.mean(column)))
    print("Quartiles of sample are \n% s " 
                % (column.quantile([0.25,0.5,0.75]))) 
    

    #TODO dodac kwartyle

def fillMissingValuesWithMeanValue(data):
    mean = data['fixed acidity'].mean()
    data.fillna(value=mean, inplace=True)
    return data

def fillMissingValuesRegression(data):
    dataWithoutMissingValues = data.dropna()
    regressionModel, x, y = createLinearRegressionModel(dataWithoutMissingValues)

    for index, row in data.iterrows():
        if math.isnan(row['fixed acidity']):
            prediction = regressionModel.predict(np.array([[row['pH']]]))
            data.at[index, 'fixed acidity'] = prediction[0][0]
    return data

def fillMissingValuesInterpolation(data):
    data = data.sort_values(['pH'])
    data = data.interpolate()
    return data

if __name__ == '__main__':
  main()

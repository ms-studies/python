import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import statistics 
import math

def main():
    data = pd.read_csv('winequality-red.csv')
    data = addMissingData(data, 100)

    print(calculatePercentage(data))
    dataWithoutMissingValues = data.dropna()
    
    #linear regression
    print("\n========= Without missing values ==========")
    drawRegressionCurve(dataWithoutMissingValues, 'Missing data: 0%')
    printDatasetCharacteristics(dataWithoutMissingValues['fixed acidity'])

    #filling with mean
    print("\n========= Filled with mean ==========")
    filledDataWithMean = fillMissingValuesWithMeanValue(data.copy())
    printDatasetCharacteristics(filledDataWithMean['fixed acidity'])
    drawRegressionCurve(filledDataWithMean, 'Missing data: 6.25%, filling method: mean')

    print("\n=======================GRADE 4==================================")
    #filling with regression
    print("\n========= Filled with regression ==========")
    filledDataWithRegression = fillMissingValuesRegression(data.copy())
    printDatasetCharacteristics(filledDataWithRegression['fixed acidity'])
    drawRegressionCurve(filledDataWithRegression, 'Missing data: 6.25%, filling method: regression')

    #filling with hot-deck
    print("\n========= Filled with hot-deck ==========")
    filledWithHotDeck = fillMissingValuesHotDeck(data.copy())
    printDatasetCharacteristics(filledWithHotDeck['fixed acidity'])
    drawRegressionCurve(filledWithHotDeck, 'Missing data: 6.25%, filling method: hot-deck')

    # #filling with interpolation
    print("\n========= Filled with interpolation ==========")
    filledDataWithInterpolation = fillMissingValuesInterpolation(data.copy())
    printDatasetCharacteristics(filledDataWithInterpolation['fixed acidity'])
    drawRegressionCurve(filledDataWithInterpolation, 'Missing data: 6.25%, filling method: interpolation')

    print("\n=======================GRADE 5==================================")
    title = 'Missing data: 15%, filling method: regression'
    print("\n========= " + title + " ==========")
    runRegressionForDatasetWithMissingValues(data.copy(), 240, title)

    title = 'Missing data: 30%, filling method: regression'
    print("\n========= " + title + " ==========")
    runRegressionForDatasetWithMissingValues(data.copy(), 480, title)

    title = 'Missing data: 45%, filling method: regression'
    print("\n========= " + title + " ==========")
    runRegressionForDatasetWithMissingValues(data.copy(), 720, title)

    plt.show()


def addMissingData(data, missingSamplesCounter):
    data.sample(frac=1)
    for i in range(missingSamplesCounter):
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

def drawRegressionCurve(data, title):
    model, x, y = createLinearRegressionModel(data)

    print('\nRegression curve parameters: ')
    print('Intercept: b0 =' + str(model.intercept_))
    print('Slope: b1 =' + str(model.coef_))

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
    ax.set_title(title)

    ax.axis('tight')

def printDatasetCharacteristics(column):
    print("Standard Deviation of sample is % s " 
                % (statistics.stdev(column))) 
    print("Mean of sample is % s " 
                % (statistics.mean(column)))
    print("Quartiles of sample are \n% s " 
                % (column.quantile([0.25,0.5,0.75]))) 
    
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

def fillMissingValuesHotDeck(data):
    dataWithoutMissingValues = data.dropna()
    dataWithMissingValues = data[data.isnull().any(axis=1)]

    for index1, row1 in dataWithMissingValues.iterrows(): # for each Nan row
        maxSameValues = 0
        predictedAcidity = 0
        for index2, row2 in dataWithoutMissingValues.iterrows():
            sameValues = 0

            for column in dataWithMissingValues: #for each column
                if column != 'fixed acidity':
                    diff = row2[column] - row1[column]
                    if diff == 0:
                        sameValues += 1

            if sameValues > maxSameValues:
                maxSameValues = sameValues
                predictedAcidity = row2['fixed acidity']
                
        data.at[index1, 'fixed acidity'] = predictedAcidity

    return data

def runRegressionForDatasetWithMissingValues(data, missingSamplesCounter, plotTitle):
    data = addMissingData(data, missingSamplesCounter)
    print(calculatePercentage(data))
    dataWithoutMissingValues = data.dropna()
    print("\n==== Before filling missing data =====")
    printDatasetCharacteristics(dataWithoutMissingValues['fixed acidity'])
    filledDataWithRegression = fillMissingValuesRegression(data.copy())
    print("\n==== After filling missing data =====")
    printDatasetCharacteristics(filledDataWithRegression['fixed acidity'])
    drawRegressionCurve(filledDataWithRegression, plotTitle)

if __name__ == '__main__':
  main()

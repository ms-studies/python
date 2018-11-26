import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

def main():
    data = pd.read_csv('data.csv')
    class_column = data.iloc[:, 34]
    data_without_class = data.iloc[:,0:34]

    # classification with all attributes
    runClassification(data_without_class, class_column)
    
    # classification with two attributes chosen by PCA
    X_transformed_PCA = transformWithPCA(data_without_class, class_column)
    runClassification(X_transformed_PCA, class_column)

def runClassification(data_without_class, class_column):
    X_train, X_test, y_train, y_test = train_test_split(data_without_class, class_column, random_state=42)

    mlp = MLPClassifier(max_iter = 10000)
    mlp.fit(X_train,y_train)
    print("Accuracy score: " + str(accuracy_score(y_test,mlp.predict(X_test)))
    # nie zrobic tego wykresu tak jak doszlismy do wniosku, ze powinno byc to zrobione
    # bo mi sie jednak wydaje, ze to dla roznej liczby iteracji to trzeba zrobic
)

def transformWithPCA(data_without_class, class_column):
    pca_1 = PCA()
    data_without_class_1 = pca_1.fit_transform(data_without_class)  
    explained_variance_1 = pca_1.explained_variance_ratio_  
    print("Variance for all components: " + str(explained_variance_1)) # prints variance for all components 

    pca_2 = PCA(n_components = 2)
    data_without_class_2 = pca_2.fit_transform(data_without_class)  
    explained_variance_2 = pca_2.explained_variance_ratio_ 
    X_transformed = pca_2.transform(data_without_class) 
    print("Two principal components variance: " + str(explained_variance_2)) # prints two components with biggest variance

    return X_transformed    

if __name__ == '__main__':
  main()

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def main():
	colnames = ['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13',
				'col14','col15','col16','col17','col18','col19','col20','col21','col22','col23','col24','col25','col26','col27','col28','col29','col30','col31','col32','col33','col34','col35']

	data = pd.read_csv('data.csv', names = colnames)
	class_column = data.iloc[:, 34]
	data_without_class = data.iloc[:,0:34]

	# classification with all attributes
	runClassification(data_without_class, class_column, 0.001, 1000)

	# classification with two attributes chosen by PCA
	X_transformed_PCA = transformWithPCA(data_without_class, class_column)
	runClassification(X_transformed_PCA, class_column, 0.001, 1000)

	plt.show()

def runClassification(data_without_class, class_column, initLearningRate, epochs):
	X_train, X_test, y_train, y_test = train_test_split(data_without_class, class_column, random_state=42)

	mlp = MLPClassifier(hidden_layer_sizes=(100,), learning_rate_init=initLearningRate)
    
	scores_train = []
	scores_test = []

	# LEARNING
	for _ in range(epochs):
		mlp.partial_fit(X_train, y_train, classes=np.unique(y_train))
		scores_train.append(mlp.score(X_train, y_train))
		scores_test.append(mlp.score(X_test, y_test))

	# VISUALISATION
	drawScoresPlot(scores_train, scores_test)
	print("Accuracy score: " + str(accuracy_score(y_test,mlp.predict(X_test))))

def drawScoresPlot(scores_train, scores_test):
	plt.figure()
	plt.plot(scores_train, color='green', alpha=0.8, label='Train')
	plt.plot(scores_test, color='magenta', alpha=0.8, label='Test')
	plt.title("Accuracy over epochs", fontsize=14)
	plt.xlabel('Epochs')
	plt.legend(loc='upper left')

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

    # proby znalezienia innych dwoch cech oprocz tych z najwieksza wariancja - nieudane
    # print(type(pca_1.components_))
    # temp_df = pd.DataFrame(pca_1.components_.transpose(),index=data_without_class.columns)
    # colnames = temp_df.columns.values.tolist()
    # print(colnames)
    # sorted = temp_df.sort_values(by=colnames[:33], ascending = False)
    # koniec prob

    return X_transformed

if __name__ == '__main__':
  main()

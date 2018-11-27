import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import time

def main():
	colnames = ['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13',
				'col14','col15','col16','col17','col18','col19','col20','col21','col22','col23','col24','col25','col26','col27','col28','col29','col30','col31','col32','col33','col34','col35']

	data = pd.read_csv('data.csv', names = colnames)
	class_column = data.iloc[:, 34]
	data_without_class = data.iloc[:,0:34]

	# classification with all attributes
	runClassification(data_without_class, class_column, 0.001, 1000, "Full data")

	# classification with two attributes chosen by PCA
	X_transformed_PCA = transformWithPCA(data_without_class, class_column)
	runClassification(X_transformed_PCA, class_column, 0.001, 1000, "PCA, 2 best")

	X_transformed_PCA_2 = transformWithPCAWorst(data_without_class, class_column)
	runClassification(X_transformed_PCA_2, class_column, 0.001, 1000, "PCA, 2 worst")

	plt.show()

def runClassification(data_without_class, class_column, initLearningRate, epochs, name):
	start = time.process_time()
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
	drawScoresPlot(scores_train, scores_test, name)
	print("Accuracy score: " + str(accuracy_score(y_test,mlp.predict(X_test))))
	print("Classification took "+str(time.process_time()-start)+" units(?)")

def drawScoresPlot(scores_train, scores_test, name):
	plt.figure()
	plt.plot(scores_train, color='green', alpha=0.8, label='Train')
	plt.plot(scores_test, color='magenta', alpha=0.8, label='Test')
	plt.title(name+": accuracy over epochs", fontsize=14)
	plt.xlabel('Epochs')
	plt.legend(loc='upper left')

def transformWithPCA(data_without_class, class_column):
	print("\n===== PCA with all parameters=====")
	pca_1 = PCA(copy=True)
	pca_1.fit(data_without_class)  
	explained_variance_1 = pca_1.explained_variance_ratio_  
	print("Variance for all components: " + str(explained_variance_1)) # prints variance for all components
	print("Sum of importance: " + str(sum(explained_variance_1)))
	
	print("\n===== PCA with 2 best parameters=====")	
	pca_2 = PCA(n_components = 2, copy=True)
	pca_2.fit(data_without_class)  
	explained_variance_2 = pca_2.explained_variance_ratio_ 
	X_transformed = pca_2.transform(data_without_class)
	print("Two principal components variance: " + str(explained_variance_2)) # prints two components with biggest variance
	print("Sum of importance: " + str(sum(explained_variance_2)))

	return X_transformed

def transformWithPCAWorst(data_without_class, class_column):
	print("\n===== PCA with 2 worst parameters=====")
	pca = PCA(copy=True) 
	pca.fit(data_without_class)
	explained_variance = pca.explained_variance_ratio_[-2:]
	X_transformed = pca.transform(data_without_class)[:, -2:]
	print("Two worst components variance: " + str(explained_variance)) # prints two components with lowest variance
	print("Sum of importance: " + str(sum(explained_variance)))

	return X_transformed

if __name__ == '__main__':
  main()

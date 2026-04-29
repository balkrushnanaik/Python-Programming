import pandas as pd # type: ignore
import numpy as np # type: ignore


data = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(data.head())

data.info() # This gives us information about the dataset, including the number of non-null entries and the data types of each column.
np.unique(data['class']) # This gives us the unique classes in the dataset, which are the different types of iris flowers.

data.describe() # This gives us statistical information about the dataset, such as the mean, standard deviation, and quartiles for each numerical column.
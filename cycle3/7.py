print("JACOB K M : 23MCA032")

import pandas as pd

df = pd.read_csv('iris.csv')


print("Shape of the dataset is : ", df.shape)

print("First 5 rows of the dataset:\n", df.head())

print("Last 5 rows of the dataset:\n", df.tail())


print("Size of dataset : ", df.size)


print("No. of samples available for each variety:\n", df['species'].value_counts())

print("Description of the data set:\n", df.describe())

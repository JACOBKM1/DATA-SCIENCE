import numpy as np
print("SJC23MCA032 : JACOB K M")
array_2d = np.array([
    [1, 3, 5],
    [7, 9, 11]
     ])
print("2D Array:")
print(array_2d)
rows, columns = array_2d.shape
print("\nNumber of Rows:", rows)
print("Number of Columns:", columns)
dimensions = array_2d.ndim
print("\nDimensions of the Array:", dimensions)
reshaped_array = array_2d.reshape(3, 2)
print("\nReshaped Array (3x2):")
print(reshaped_array)
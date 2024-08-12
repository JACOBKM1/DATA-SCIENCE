import numpy as np
print("SJC23MCA032 : JACOB K M")
X = np.array([[1, 2],
[3, 4]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2 * Y
print(result)
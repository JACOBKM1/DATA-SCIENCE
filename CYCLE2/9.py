import numpy as np
print("SJC23MCA032 : JACOB K M")
arr_id = np.array([1,2,3,4,5])
dia_mul=np.diag(arr_id)
print("id array")
print(arr_id)
print("Diagonal matrix")
print(dia_mul)
arr_2d=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
dia_ele=np.diag(arr_2d)
print("2d non square")
print(arr_2d)
print("diagonal elemets(non square):")
print(dia_ele)
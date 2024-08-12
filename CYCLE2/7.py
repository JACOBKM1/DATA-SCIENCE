print("SJC23MCA032 : JACOB K M")
import numpy as np
matrix1=np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
matrix2=np.array([[9,8,7],
                  [6,5,4],
                  [3,2,1]])
mat_sum=matrix1+matrix2
mat_diff=matrix1-matrix2
mar_div=matrix1/matrix2
mat_mul=np.dot(matrix1,matrix2)
mat_trans=np.transpose(matrix1)
dio_s=np.trace(matrix1)
print("matrix 1:\n",matrix1)
print("\nmatrix 2:\n",matrix2)
print("\nMatrix sum\n",mat_sum)
print("\nmatrix difference\n",mat_diff)
print("\nmatrix else wise product of :\n",mat_mul)
print("\n matrix divsion:\n",mar_div)
print("\n matrix transpose \n",mat_trans)
print("\n matrix diagonal sum of mat1\n",dio_s)

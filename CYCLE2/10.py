import numpy as np
print("SJC23MCA032 : JACOB K M")
mal_s=3
mat=np.random.randint(10,20,size=(mal_s,mal_s))
print("original matrix")
print(mat)
if np.linalg.matrix_rank(mat)==mal_s:
    inverse_matrix=np.linalg.inv(mat)
    print("inverse matrix")
    print(inverse_matrix)
else:
    print("matirx is inreversable")
rank=np.linalg.matrix_rank(mat)
print("Rank of matrix1:",rank)
deter=np.linalg.det(mat)
print("determinannt of matrix",deter)
mat_id=mat.flatten()
print("matrix as 1d array")
print(mat_id)
eigenvalues, eigenvectors=np.linalg.eig(mat)
print("Eigen values")
print(eigenvalues)
print("eigen vectors")
print(eigenvectors)
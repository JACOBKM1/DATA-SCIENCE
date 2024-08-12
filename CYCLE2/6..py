import numpy as np
print("SJC23MCA032 : JACOB K M")
two = np.array([[1,2,3,4,],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
excluding_first_row = two[1:]
excluding_last_colum = two[:, :-1]
column1and2inrow2and3 =two[1:3, 0:2]
colum2and3 = two[:, 1:3]
element2and3infirstrow = two[0, 1:3]
desc = two.ravel()[::-1][4:11]

print("Original 2D array: \n",two)
print("Elements excluding the first row:\n",excluding_first_row)
print("Element exccluding the last column:\n",excluding_last_colum)
print("Elements of the 1st and 2nd column in the 2nd and 3rd row:\n",
      column1and2inrow2and3)
print("Elements of the 2nd and 3 rd column:\n",colum2and3)
print("2nd and 3rd element of the 1st row:\n",
      element2and3infirstrow)
print("Elements from indices 4 to 10 in desceding order:\n",desc)
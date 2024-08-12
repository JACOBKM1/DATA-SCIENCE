import numpy as np
print("SJC23MCA032 : JACOB K M")
even = np.arange(2,31,2)
silce_result = even[2:9:2]
last_3 = even[-3:]
alter_element=even[::2]
last_3_alter=alter_element[-3:]
print("original array",even)
print("element from index 2 to 8 wth step 2 :",silce_result)
print("last 3 elements of the array using negative index",last_3)
print("alternative elemet of the array",alter_element)
print("last 3 alter elememt",last_3_alter)
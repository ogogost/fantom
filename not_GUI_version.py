import numpy as np
import random

#
# a = np.array([[1, 1, 1],[2, 2, 2]])
# print(a)
# print('id(a)=', id(a))
# # b = a + [1,2,2]
# # b = np.insert([2,3,4])
# a = np.append(a, [[3,3,3]], axis=0)
# print(a)
# print('a[0]=', a[0])
# print('id(a)=', id(a))

n = 5
m = 10

b = np.ones((5,n))
# print(b)

# for i in range(0,9):
#     b[1,i] = random.randint(0,m)
# b[2] = random.randint(0,m)
# print(b)

b[0,2] = 10
b[2] = [5,5,5,5,5]
b = np.ndarray
b = np.append(b, [[6,6,6,6,6]], axis=0)
print(b)

# if b[0][6] == 6:
#     b = np.delete(b, 0, 0)
# else:
    # print(b[0][4])
print(b[2][2])

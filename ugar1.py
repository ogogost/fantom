import random
import time

start_time = time.time()
print('start time = ', start_time)

i = 100000

num_z = 0
num_x = 0
num_c = 0

while i > 0:
    word = random.choice(['z', 'x', 'c'])
    # print('random word = ', word)
    if word == 'z':
        num_z = num_z + 1
    if word == 'x':
        num_x = num_x + 1
    if word == 'c':
        num_c = num_c + 1

    i = i -1

print('Z = ', num_z, 'X = ', num_x, 'C = ', num_c, 'total = ', num_z + num_x + num_c)
print('Percent of Z =', num_z / (num_z + num_x + num_c) * 100)
print('Percent of X =', num_x / (num_z + num_x + num_c) * 100)
print('Percent of C =', num_c / (num_z + num_x + num_c) * 100)
finish_time = time.time()
print('finish time = ', finish_time)
print('execution time = ', finish_time - start_time)
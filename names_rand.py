import random

names = []

with open('names.csv') as f:
    for line in f:
        names.append(line.strip())

print(random.choice(names))

print(names)

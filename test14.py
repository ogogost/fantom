data = [(1, 'xxx', 90), (2, 'ccc', 60), (3, 'eee', 70)]
print(data)
prices = []
for i in data:
    prices.append(i[2])

print(prices)

amount = min(prices)
print(amount)

print(any(e[2] == amount for e in data))


for i in data:
    if i[2] == amount:
        print(i[0])
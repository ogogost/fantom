import random

clients_names = []
with open('names.csv') as f: # read names
    for line in f: #
        clients_names.append(line.strip()) # remove \n

# for i in range(10):
#    print(random.choice(clients_names))

clients = []

for i in range(len(clients_names)):
    clients.append([clients_names[i], random.randint(0, 1000000), random.randint(0, 1000)])

print(clients)

for i in range(len(clients)):
    print(clients[i][0], clients[i][1], clients[i][2])

money_total = 0
for i in range(len(clients)):
    money_total += clients[i][1]
print(money_total)

stocks_total = 0
for i in range(len(clients)):
    stocks_total += clients[i][2]
print(stocks_total)
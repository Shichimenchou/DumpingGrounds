import random

land = []

for i in range(0, 100):
    row = []
    for j in range(0, 100):
        row.append(random.randint(0,100))
    land.append(row)




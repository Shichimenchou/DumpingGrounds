threebythree = [['1', '2', '3'], ['a', 'b', 'c']]
weird = [['1','2', '3'], ['a', 'b'], ['!', '?', '@', '$']]

combs = []
for i in weird[0]:
    for j in weird[1]:
        for k in weird[2]:
            combs.append(i + j + k)
print(combs)

cmbs = []
for i in threebythree[0]:
    for j in threebythree[1]:
        cmbs.append(i + j)
print(cmbs)

def generateCombinations(array, row):
    combinations = []
    if row == len(array) - 1:
        for i in array[row]:
            combinations.append(i)
    else: 
        lowerCombs = generateCombinations(array, row + 1)
        for i in array[row]:
            for j in lowerCombs:
                combinations.append(i + j)
    return combinations

print(generateCombinations(weird, 0))
print(generateCombinations(threebythree, 0))

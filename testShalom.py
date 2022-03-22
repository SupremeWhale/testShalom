import random

testFam = [1, 2, 3, 4, 5]
rate = 1
temp =[]
for i in range(len(testFam)):
    x = random.randint(1,100)
    temp.append(testFam[i])
    if rate == x:
        temp.append(x)
     #   fuck python
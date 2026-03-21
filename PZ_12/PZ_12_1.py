import random

i = int(input())
j = int(input())

matrix = [[random.randint(1, 10) for _ in range(j)] for _ in range(i)]

for row in matrix:
    print(row)

row = matrix[0]
row = [i**3 for i in row ]
print(row)
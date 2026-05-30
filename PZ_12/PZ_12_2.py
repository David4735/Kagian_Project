#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random

m1 = [[random.randint(0, 20) for _ in range(5)] for _ in range(4)]

print("Исходная матрица:")
list(map(lambda r: print(r), m1))

m2 = list(map(lambda row: list(map(lambda x: 0 if x > 10 else x, row)), m1))

print("Результат:")
list(map(lambda r: print(r), m2))

print("Результат:")
for r in m2:
    print(r)

#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random

m1 = [[random.randint(0, 20) for i in range(5)] for i in range(4)]

print("Исходная матрица:")
for r in m1:
    print(r)

m2 = []
for r in m1:
    n = []
    for x in r:
        if x > 10:
            n.append(0)
        else:
            n.append(x)
    m2.append(n)

print("Результат:")
for r in m2:
    print(r)
#В матрице элементы первого столбца возвести в куб.
import random

m = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

print("Исходная матрица:")
for r in m:
    print(r)

m = list(map(lambda row: [row[0]**3 if j == 0 else row[j] for j in range(len(row))], m))

print("Результат:")
for r in m:
    print(r)

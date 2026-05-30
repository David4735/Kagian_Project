#В матрице элементы первого столбца возвести в куб.
import random

m = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

print("Исходная матрица:")
list(map(lambda r: print(r), m))

m = list(map(lambda row, i: [row[0]**3 if j == 0 else row[j] for j in range(len(row))], m, range(3)))

print("Результат:")
list(map(lambda r: print(r), m))

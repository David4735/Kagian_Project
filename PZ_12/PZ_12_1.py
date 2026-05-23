#В матрице элементы первого столбца возвести в куб.
import random

m = [[random.randint(1, 10) for i in range(4)] for i in range(3)]

print("Исходная матрица:")
for r in m:
    print(r)

for i in range(3):
    m[i][0] = m[i][0] ** 3 #возводим в 3 степень

print("Результат:")
for r in m:
    print(r)
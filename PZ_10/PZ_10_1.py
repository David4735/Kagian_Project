# Вариант 6.
# Задание 1.
# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать новый
# текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Повторяющиеся элементы:
# Количество повторяющихся элементов:
# Элементы больше 5 увеличены в два раза:

import random

n = []
a = random.randint(1, 11)

for i in range(a):
    n.append(random.randint(-99, 100))

f1 = open('data_1.txt', 'w')
for i in n:
    f1.write(str(i) + ' ')
f1.close()

f1 = open('data_1.txt')
k = f1.read().split()

for i in range(len(k)):
    k[i] = int(k[i])

f1.close()

c = len(k)
p = 1
for i in k:
    p = p * i

d = []
for i in range(len(k)):
    t = 0
    for j in range(len(k)):
        if k[i] == k[j]:
            t += 1
    if t > 1:
        u = 0
        for l in range(len(d)):
            if k[i] == d[l]:
                u = 1
        if u == 0:
            d.append(k[i])

b = []
for i in k:
    if i > 5:
        b.append(i * 2)
    else:
        b.append(i)

f2 = open('data_2.txt', 'w', encoding='utf-16')

f2.write('Исходные данные: ')
f2.write(str(k))
f2.write('\n')

f2.write('Количество элементов: ')
f2.write(str(c))
f2.write('\n')

f2.write('Произведение элементов: ')
f2.write(str(p))
f2.write('\n')

f2.write('Повторяющиеся элементы: ')
f2.write(str(d))
f2.write('\n')

f2.write('Количество повторяющихся элементов: ')
f2.write(str(len(d)))
f2.write('\n')

f2.write('Элементы больше 5 увеличены в два раза: ')
f2.write(str(b))

f2.close()

for i in open('data_2.txt', encoding='utf-16'):
    print(i, end='')

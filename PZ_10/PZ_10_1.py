#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

#Исходные данные:
#Количество элементов:
#Произведение элементов:
#Повторяющиеся элементы:
#Количество повторяющихся элементов:
#Элементы больше 5 увеличены в два раза:

import random;

n = 15
d = ''

for i in range(n):
    a = random.randint(-20, 20)
    d = d + str(a)
    if i < n - 1:
        d = d + ''
b = open('chisla.txt', 'w')
b.write(d)
b.close()

b = open('chisla.txt', 'r')
s = b.read()
b.close()

s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])

p = 1
for i in range(len(s)):
    p = p * s[i]
pov = []
for i in range(len(s)):
    l = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            l = l + 1
    if l > 1:
        o = 0
        for k in range(len(pov)):
            if s[i] == pov[k]:
                o = 1
        if o == 0:
            pov.append(s[i])

kpov = len(pov)

bolshe = []
for i in range(len(s)):
    if s[i] > 5:
        bolshe.append(s[i] * 2)
    else:
        bolshe.append(s[i])

r = open('result.txt', 'w')
r.write('Исходные данные: ')
r.write(d)
r.write('\n')
r.write('Количество элементов')
r.write(str(len(s)))
r.write('\n')
r.write('Произведение элементов: ')
r.write(str(p))
r.write('\n')
r.write('Повторяющееся элементы: ')
if len(pov) > 0:
    for i in range(len(pov)):
        r.write(str(pov[i]))
        if i < len(pov) - 1:
            r.write(' ')
else:
    r.write('нет')
r.write('\n')
r.write('Количество повторяющихся элементов: ')
r.write(str(kpov))
r.write('\n')
r.write('Элементы более 5 увеличены в два раза: ')
for i in range(len(bolshe)):
    r.write(str(bolshe[i]))
    if i < len(bolshe) - 1:
        r.write(' ')
r.close()
print('1 задание готово')

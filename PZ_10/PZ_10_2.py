# ========== ВАРИАНТ 6, ЗАДАНИЕ 2 ==========
import random

# Создаём файл text18-6.txt со случайным стихотворением (если его нет)
stihi = [
    'В лесу родилась ёлочка,\n',
    'В лесу она росла.\n',
    'Зимой и летом стройная,\n',
    'Зелёная была.\n',
    'Метель ей пела песенку:\n',
    'Спи, ёлочка, бай-бай!\n',
    'Мороз снежком укутывал:\n',
    'Смотри, не замерзай!\n'
]

# Выбираем случайные 6 строк
random.shuffle(stihi)  # перемешиваем
vybannye = stihi[:6]   # берём первые 6

# Записываем в файл
a = open('text18-6.txt', 'w', encoding='UTF-8')
for i in range(len(vybannye)):
    a.write(vybannye[i])
a.close()

# ========== ВЫПОЛНЯЕМ ЗАДАНИЕ ==========

# Выводим содержимое на экран
a = open('text18-6.txt', 'r', encoding='UTF-8')
l = a.readlines()
a.close()

print('Содержимое файла:')
print('-' * 30)
for i in range(len(l)):
    print(l[i], end='')
print('-' * 30)

# Считаем количество пробельных символов (пробелы, табуляции, переводы строк)
prob = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == ' ' or l[i][j] == '\t' or l[i][j] == '\n':
            prob = prob + 1

print('Количество пробельных символов:', prob)

# Заменяем все знаки пунктуации на «!»
# Знаки пунктуации: . , ! ? ; : - ( ) " '
znaki = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'"]

for i in range(len(l)):
    novaya_stroka = ''
    for j in range(len(l[i])):
        if l[i][j] in znaki:
            novaya_stroka = novaya_stroka + '!'
        else:
            novaya_stroka = novaya_stroka + l[i][j]
    l[i] = novaya_stroka

# Записываем в новый файл
w = open('text18-6_new.txt', 'w', encoding='UTF-8')
for i in range(len(l)):
    w.write(l[i])
w.close()

print('2 задание готово! Смотри text18-6_new.txt')

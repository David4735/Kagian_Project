# Вариант 6.
# Задание 2.
# Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

p = 0

for i in open('text18-6.txt', encoding='utf-16'):
    print(i, end='')
    for j in i:
        if j == ' ' or j == '\n':
            p += 1

print(end='\n\n')
print('Количество пробельных символов: ', p, end='\n\n')

f1 = open('text18-6.txt', encoding='utf-16')
l = f1.readlines()
f1.close()

z = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'"]

f2 = open('new_text18-6.txt', 'w', encoding='utf-16')

for i in l:
    s = ''
    for j in i:
        if j in z:
            s += '!'
        else:
            s += j
    f2.write(s)

f2.close()

for i in open('new_text18-6.txt', encoding='utf-16'):
    print(i, end='')

#Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».
a = open('text10-2.txt', 'r', encoding='UTF-8')
l = a.readlines()
a.close()

print('Содержимое файла:')
print('-' * 30)
for i in range(len(l)):
    print(l[i], end='')
print('-' * 30)

prob = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == ' ' or l[i][j] == '\t' or l[i][j] == '\n':
            prob = prob + 1

print('Количество пробельных символов:', prob)

znaki = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'"]

for i in range(len(l)):
    novaya_stroka = ''
    for j in range(len(l[i])):
        if l[i][j] in znaki:
            novaya_stroka = novaya_stroka + '!'
        else:
            novaya_stroka = novaya_stroka + l[i][j]
    l[i] = novaya_stroka

w = open('text10-2_new.txt', 'w', encoding='UTF-8')
for i in range(len(l)):
    w.write(l[i])
w.close()

print('2 задание готово! Смотри text10-2_new.txt')

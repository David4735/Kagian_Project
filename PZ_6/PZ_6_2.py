#Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).
import random;
try:
    n = random.randint(5, 15)
    lst = [random.randint(1, 100) for _ in range(n)]
    print("N =", n)
    print("Список: ", lst)

    max = 0
    for i in range(1, n-1):
        if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
            if max == 0 or lst[i] > max:
                max = lst[i]

    if max != 0:
        print("Максимальный локальный минимум:", max)
    else:
        print("Нет локальных минимумов")
except ValueError:
    print("Ошибка! Введено не число!")  # если ввели что то кроме чисел выходит ошибка

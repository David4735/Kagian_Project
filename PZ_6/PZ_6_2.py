#Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).
import random;
try:
    n = random.randint(5, 15)
    lst = [random.randint(1, 100) for _ in range(n)]
    print(f"\n2. N={n}")
    print(f"   Список: {lst}")

    max_min = None
    for i in range(1, n-1):
        if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
            if max_min is None or lst[i] > max_min:
                max_min = lst[i]

    if max_min is not None:
        print(f"   Максимальный локальный минимум: {max_min}")
    else:
        print("   Нет локальных минимумов")
except ValueError:
    print("Ошибка! Введено не число!")  # если ввели что то кроме чисел выходит ошибка

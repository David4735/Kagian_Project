a = int(input("Введите число: "))
def abc(a):
    a1 = a
    c = 0
    c1 = 1
    b = 0
    while a1 > c:
        b = c * c1
        c = b * c1
        c1 += 1
    return(c)
print(abc(a))
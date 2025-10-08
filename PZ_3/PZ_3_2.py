try:
    a = float(input("Введите первое число: "))
    c = str(input("Введите операцию: "))
    b = float(input("Введите второе число: "))

    if(c == "+"):
        d = a + b
        print(d)
    elif(c == "-"):
        d = a - b
        print(d)
    elif(c == "/"):
        d = a / b
        print(d)
    elif(c == "*"):
        d = a * b
        print(d)
    else: print("Такой операции не существует")
except ValueError:
    print("Ошибка! Введено не число!")  # если ввели что то кроме чисел выходит ошибка
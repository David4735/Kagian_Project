#сгенерировать таблицу в которой элементы больше 10 заменяются на нуль
i = int(input())
j = int(input())

matrix = [[random.randint(1, 15) for _ in range(j)] for _ in range(i)]

for row in matrix:
    print(row)

row = [[0 if x > 10 else x for x in row] for row in matrix ]
for i in row:
  print(i)

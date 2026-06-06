# Вариант 6.
# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
# адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
# а во второй – все остальные. Посчитать количество полученных строк в каждом файле.

import re

with open('ip_address.txt', 'r', encoding='utf-8') as f:
    section = re.search(r'Зарезервированные адреса\s+((?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?\s*)+)', f.read())

addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?', section.group(1))

# Отбираем адреса, у которых первый И второй октеты ненулевые
nonzero = [a for a in addresses if not a.startswith('0.') and not re.match(r'\d+\.0\.', a)]
zero = [a for a in addresses if a not in nonzero]

with open('file1.txt', 'w') as f:
    f.write('\n'.join(nonzero))
with open('file2.txt', 'w') as f:
    f.write('\n'.join(zero))

print(f"Строки с ненулевыми первым и вторым октетами: {len(nonzero)}")
print(f"Строки с нулевым первым или вторым октетом: {len(zero)}")
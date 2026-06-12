import re

i = "ip_address.txt"
o1 = "reserved_nonzero.txt"
o2 = "reserved_other.txt"

with open(i, "r", encoding="utf-8") as f:
    l = f.readlines()

p = re.compile(r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")

r1 = []
r2 = []
c1 = 0
c2 = 0
s = False

for n in l:
    if "Зарезервированные адреса" in n:
        s = True
        continue
    if not s:
        continue
    if n.strip() == "":
        continue
    m = p.search(n)
    if m:
        o1v = int(m.group(1))
        o2v = int(m.group(2))
        if o1v != 0 and o2v != 0:
            r1.append(n)
            c1 += 1
        else:
            r2.append(n)
            c2 += 1
    else:
        r2.append(n)
        c2 += 1

with open(o1, "w", encoding="utf-8") as f:
    f.writelines(r1)

with open(o2, "w", encoding="utf-8") as f:
    f.writelines(r2)

print(f"Первый файл ({o1}): {c1} строк")
print(f"Второй файл ({o2}): {c2} строк")
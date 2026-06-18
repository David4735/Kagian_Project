#Создание базового класса "Фигура" и его наследование для создания классов
#"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
#такие как вычисление площади и периметра, а классы-наследники будут иметь
#специфичные методы и свойства. 
import math
import random

class Figure:
    def set_square(self, a):
        self.type = "квадрат"
        self.a = a
    
    def set_rectangle(self, a, b):
        self.type = "прямоугольник"
        self.a = a
        self.b = b
    
    def set_circle(self, r):
        self.type = "круг"
        self.r = r
    
    def area(self):
        if self.type == "квадрат":
            return self.a ** 2
        elif self.type == "прямоугольник":
            return self.a * self.b
        elif self.type == "круг":
            return math.pi * self.r ** 2
    
    def perimeter(self):
        if self.type == "квадрат":
            return self.a * 4
        elif self.type == "прямоугольник":
            return 2 * (self.a + self.b)
        elif self.type == "круг":
            return 2 * math.pi * self.r
    
    def info(self):
        if self.type == "квадрат":
            return f"Квадрат со стороной {self.a}"
        elif self.type == "прямоугольник":
            return f"Прямоугольник {self.a}x{self.b}"
        elif self.type == "круг":
            return f"Круг радиусом {self.r}"

s = Figure()
s.set_square(random.randint(1, 20))

r = Figure()
r.set_rectangle(random.randint(1, 20), random.randint(1, 20))

c = Figure()
c.set_circle(random.randint(1, 20))

print(s.info())
print(f"Площадь: {s.area()}")
print(f"Периметр: {s.perimeter()}\n")

print(r.info())
print(f"Площадь: {r.area()}")
print(f"Периметр: {r.perimeter()}\n")

print(c.info())
print(f"Площадь: {c.area():.2f}")
print(f"Периметр: {c.perimeter():.2f}")
#Создание базового класса "Фигура" и его наследование для создания классов
#"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
#такие как вычисление площади и периметра, а классы-наследники будут иметь
#специфичные методы и свойства. 
import math

class Figure:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def info(self):
        return f"{self.name}: площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"

class Square(Figure):
    def __init__(self, side):
        super().__init__("Квадрат")
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4
    
    def diagonal(self):
        return self.side * math.sqrt(2)

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height

class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return self.radius * 2

s = Square(5)
r = Rectangle(4, 6)
c = Circle(3)

print(s.info())
print(f"Диагональ: {s.diagonal():.2f}\n")

print(r.info())
print(f"Это квадрат: {r.is_square()}\n")

print(c.info())
print(f"Диаметр: {c.diameter()}")

#Создание базового класса "Фигура" и его наследование для создания классов
#"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
#такие как вычисление площади и периметра, а классы-наследники будут иметь
#специфичные методы и свойства. 
import math

class Figure:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def info(self):
        return f"Фигура: {self.__class__.__name__}"

class Square(Figure):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4
    
    def info(self):
        return f"Квадрат со стороной {self.side}"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def info(self):
        return f"Прямоугольник {self.width}x{self.height}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def info(self):
        return f"Круг радиусом {self.radius}"

s = Square(5)
r = Rectangle(4, 6)
c = Circle(3)

print(s.info())
print(f"Площадь: {s.area()}")
print(f"Периметр: {s.perimeter()}")
print()

print(r.info())
print(f"Площадь: {r.area()}")
print(f"Периметр: {r.perimeter()}")
print()

print(c.info())
print(f"Площадь: {c.area():.2f}")
print(f"Периметр: {c.perimeter():.2f}")

#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, n):
        self.current_page += n
        if self.current_page > self.pages:
            self.current_page = self.pages
        print(f"Прочитано {self.current_page} из {self.pages} страниц")

    def write(self, text):
        print(f"Запись в книгу '{self.title}': {text}")

b = Book("1984", "Джордж Оруэлл", 328)
b.read(50)
b.read(100)
b.write("Важная заметка")

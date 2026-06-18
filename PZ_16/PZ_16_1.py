title = ""
author = ""
pages = 0
page = 0

def book(t, a, p):
    global title, author, pages, page
    title = t
    author = a
    pages = p
    page = 0

def read(n):
    global page, pages
    page = page + n
    if page > pages:
        page = pages
    print(page, "из", pages)

def write(text):
    print(text)

book("1984", "Оруэлл", 328)
read(50)
read(100)
write("заметка")
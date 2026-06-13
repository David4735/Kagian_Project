#Приложение для туристического агентства ТУР. Таблица Турист должна
#содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
#(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
#путевки.
import sqlite3
import sys

def create_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(f"Ошибка подключения к БД: {e}")
        sys.exit(1)

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Турист (
            Код_клиента INTEGER PRIMARY KEY AUTOINCREMENT,
            Фамилия TEXT NOT NULL,
            Телефон TEXT NOT NULL,
            Страна TEXT NOT NULL,
            Регион TEXT NOT NULL,
            Продолжительность INTEGER NOT NULL,
            Стоимость REAL NOT NULL
        )
    """)

def insert_sample_data(conn):
    if conn.execute("SELECT COUNT(*) FROM Турист").fetchone()[0] == 0:
        sample_data = [
            ("Иванов", "89123456789", "Турция", "Анталья", 7, 35000.0),
            ("Петров", "89234567890", "Египет", "Хургада", 10, 45000.0),
            ("Сидоров", "89345678901", "Таиланд", "Пхукет", 14, 65000.0),
            ("Кузнецова", "89456789012", "Турция", "Алания", 5, 28000.0),
            ("Смирнов", "89567890123", "ОАЭ", "Дубай", 8, 55000.0),
            ("Васильева", "89678901234", "Египет", "Шарм-эль-Шейх", 12, 52000.0),
            ("Михайлов", "89789012345", "Россия", "Сочи", 4, 18000.0),
            ("Федорова", "89890123456", "Турция", "Стамбул", 6, 32000.0),
            ("Морозов", "89901234567", "Италия", "Рим", 9, 78000.0),
            ("Волков", "89012345678", "Испания", "Барселона", 11, 72000.0)
        ]
        conn.executemany("INSERT INTO Турист (Фамилия, Телефон, Страна, Регион, Продолжительность, Стоимость) VALUES (?,?,?,?,?,?)", sample_data)
        conn.commit()
        print("Добавлено 10 записей")

def search_queries(conn):
    print("\n=== ПОИСК ===")
    surname = input("Фамилия: ")
    for row in conn.execute("SELECT * FROM Турист WHERE Фамилия LIKE ?", (f"%{surname}%",)):
        print(row)
    
    country = input("Страна: ")
    days = int(input("Мин. дней: "))
    for row in conn.execute("SELECT * FROM Турист WHERE Страна=? AND Продолжительность>=?", (country, days)):
        print(row)
    
    min_p, max_p = float(input("Мин. цена: ")), float(input("Макс. цена: "))
    for row in conn.execute("SELECT * FROM Турист WHERE Стоимость BETWEEN ? AND ?", (min_p, max_p)):
        print(row)

def delete_queries(conn):
    print("\n=== УДАЛЕНИЕ ===")
    code = int(input("Код клиента: "))
    print(f"Удалено: {conn.execute('DELETE FROM Турист WHERE Код_клиента=?', (code,)).rowcount}")
    country = input("Страна: ")
    print(f"Удалено: {conn.execute('DELETE FROM Турист WHERE Страна=?', (country,)).rowcount}")
    days = int(input("Удалить короче (дней): "))
    print(f"Удалено: {conn.execute('DELETE FROM Турист WHERE Продолжительность<?', (days,)).rowcount}")
    conn.commit()

def update_queries(conn):
    print("\n=== РЕДАКТИРОВАНИЕ ===")
    code, price = int(input("Код клиента: ")), float(input("Новая цена: "))
    print(f"Обновлено: {conn.execute('UPDATE Турист SET Стоимость=? WHERE Код_клиента=?', (price, code)).rowcount}")
    country, dur = input("Страна: "), int(input("Новая длительность: "))
    print(f"Обновлено: {conn.execute('UPDATE Турист SET Продолжительность=? WHERE Страна=?', (dur, country)).rowcount}")
    region, percent = input("Регион: "), float(input("Процент увеличения: "))
    print(f"Обновлено: {conn.execute('UPDATE Турист SET Стоимость=Стоимость*(1+?/100) WHERE Регион=?', (percent, region)).rowcount}")
    conn.commit()

def show_all(conn):
    print("\n=== ВСЕ ЗАПИСИ ===")
    for row in conn.execute("SELECT * FROM Турист"):
        print(row)

def main():
    conn = create_connection("tour_agency.db")
    create_table(conn)
    insert_sample_data(conn)
    
    menu = {"1": show_all, "2": search_queries, "3": delete_queries, "4": update_queries}
    while True:
        print("\n1-Все 2-Поиск 3-Удаление 4-Редактирование 0-Выход")
        choice = input("Выберите: ")
        if choice == "0":
            break
        menu.get(choice, lambda x: print("Неверно"))(conn)
    conn.close()

if __name__ == "__main__":
    main()

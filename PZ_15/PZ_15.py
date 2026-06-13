#Приложение для туристического агентства ТУР. Таблица Турист должна
#содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
#(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
#путевки.
import sqlite3
import sys

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка подключения к БД: {e}")
        sys.exit(1)

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
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
    conn.commit()

def insert_sample_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Турист")
    count = cursor.fetchone()[0]
    if count == 0:
        sample_data = [
            ("Иванов", "89123456789", "Турция", "Анталья", 7, 35000),
            ("Петров", "89234567890", "Египет", "Хургада", 10, 45000),
            ("Сидоров", "89345678901", "Таиланд", "Пхукет", 14, 65000),
            ("Кузнецова", "89456789012", "Турция", "Алания", 5, 28000),
            ("Смирнов", "89567890123", "ОАЭ", "Дубай", 8, 55000),
            ("Васильева", "89678901234", "Египет", "Шарм-эль-Шейх", 12, 52000),
            ("Михайлов", "89789012345", "Россия", "Сочи", 4, 18000),
            ("Федорова", "89890123456", "Турция", "Стамбул", 6, 32000),
            ("Морозов", "89901234567", "Италия", "Рим", 9, 78000),
            ("Волков", "89012345678", "Испания", "Барселона", 11, 72000)
        ]
        cursor.executemany("""
            INSERT INTO Турист (Фамилия, Телефон, Страна, Регион, Продолжительность, Стоимость)
            VALUES (?, ?, ?, ?, ?, ?)
        """, sample_data)
        conn.commit()
        print("Добавлено 10 записей")
    else:
        print(f"В таблице уже есть {count} записей")

def show_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Турист")
    for row in cursor.fetchall():
        print(row)

def search_menu(conn):
    cursor = conn.cursor()
    print("\n1. Поиск по фамилии")
    print("2. Поиск по стране")
    print("3. Поиск по стоимости")
    choice = input("Выберите: ")
    if choice == "1":
        name = input("Введите фамилию: ")
        cursor.execute("SELECT * FROM Турист WHERE Фамилия LIKE ?", (f"%{name}%",))
    elif choice == "2":
        country = input("Введите страну: ")
        cursor.execute("SELECT * FROM Турист WHERE Страна = ?", (country,))
    elif choice == "3"):
        min_p = float(input("Мин. цена: "))
        max_p = float(input("Макс. цена: "))
        cursor.execute("SELECT * FROM Турист WHERE Стоимость BETWEEN ? AND ?", (min_p, max_p))
    else:
        print("Неверный выбор")
        return
    for row in cursor.fetchall():
        print(row)

def delete_menu(conn):
    cursor = conn.cursor()
    print("\n1. Удалить по коду клиента")
    print("2. Удалить по стране")
    print("3. Удалить по продолжительности")
    choice = input("Выберите: ")
    if choice == "1":
        code = int(input("Введите код: "))
        cursor.execute("DELETE FROM Турист WHERE Код_клиента = ?", (code,))
    elif choice == "2":
        country = input("Введите страну: ")
        cursor.execute("DELETE FROM Турист WHERE Страна = ?", (country,))
    elif choice == "3":
        days = int(input("Меньше дней: "))
        cursor.execute("DELETE FROM Турист WHERE Продолжительность < ?", (days,))
    else:
        print("Неверный выбор")
        return
    conn.commit()
    print(f"Удалено строк: {cursor.rowcount}")

def update_menu(conn):
    cursor = conn.cursor()
    print("\n1. Изменить стоимость по коду")
    print("2. Изменить продолжительность по стране")
    print("3. Увеличить стоимость на % для региона")
    choice = input("Выберите: ")
    if choice == "1":
        code = int(input("Введите код: "))
        new_price = float(input("Новая цена: "))
        cursor.execute("UPDATE Турист SET Стоимость = ? WHERE Код_клиента = ?", (new_price, code))
    elif choice == "2":
        country = input("Введите страну: ")
        new_days = int(input("Новая продолжительность: "))
        cursor.execute("UPDATE Турист SET Продолжительность = ? WHERE Страна = ?", (new_days, country))
    elif choice == "3":
        region = input("Введите регион: "))
        percent = float(input("Процент увеличения: "))
        cursor.execute("UPDATE Турист SET Стоимость = Стоимость * (1 + ? / 100) WHERE Регион = ?", (percent, region))
    else:
        print("Неверный выбор")
        return
    conn.commit()
    print(f"Обновлено строк: {cursor.rowcount}")

def main():
    conn = create_connection("tour_agency.db")
    create_table(conn)
    insert_sample_data(conn)
    while True:
        print("\n1 - Все записи")
        print("2 - Поиск")
        print("3 - Удаление")
        print("4 - Редактирование")
        print("0 - Выход")
        choice = input("Выберите: ")
        if choice == "1":
            show_all(conn)
        elif choice == "2":
            search_menu(conn)
        elif choice == "3":
            delete_menu(conn)
        elif choice == "4":
            update_menu(conn)
        elif choice == "0":
            break
    conn.close()

if __name__ == "__main__":
    main()

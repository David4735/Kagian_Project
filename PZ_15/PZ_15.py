#Приложение для туристического агентства ТУР. Таблица Турист должна
#содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
#(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
#путевки.
import sqlite3
import sys

def data_from_txt():
    with open("text.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split("|")
                фамилия = parts[0]
                телефон = parts[1]
                страна = parts[2]
                регион = parts[3]
                продолжительность = int(parts[4])
                стоимость = float(parts[5])
                
                print(f"Обработана запись: {фамилия}")

def data(conn):
    if conn.execute("SELECT COUNT(*) FROM Турист").fetchone()[0] == 0:
        with open("text.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    # Распаковываем в отдельные переменные
                    фамилия = parts[0]
                    телефон = parts[1]
                    страна = parts[2]
                    регион = parts[3]
                    продолжительность = int(parts[4])
                    стоимость = float(parts[5])
                    
                    conn.execute("""
                        INSERT INTO Турист (Фамилия, Телефон, Страна, Регион, Продолжительность, Стоимость)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (фамилия, телефон, страна, регион, продолжительность, стоимость))
        conn.commit()
        print("Данные добавлены из text.txt (по одной записи)")
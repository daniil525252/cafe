import pymysql

name_db = "bd"
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database=name_db,
    charset='utf8mb4'
)

users = [
    ("admin1@example.com", "password123", True),
    ("admin2@example.com", "password123", True),
    ("user1@example.com", "password123", False),
    ("user2@example.com", "password123", False),
    ("user3@example.com", "password123", False),
    ("user4@example.com", "password123", False),
    ("user5@example.com", "password123", False),
    ("user6@example.com", "password123", False),
    ("user7@example.com", "password123", False),
    ("user8@example.com", "password123", False),
]

try:
    with connection.cursor() as cursor:
        insert_query = """
        INSERT INTO users (email, password, is_admin)
        VALUES (%s, %s, %s);
        """
        cursor.executemany(insert_query, users)
        print("Таблица 'users' успешно заполнена.")

    connection.commit()
except pymysql.MySQLError as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    connection.close()

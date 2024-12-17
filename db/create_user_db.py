import pymysql

name_db = "bd"
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database=name_db,
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            is_admin BOOLEAN NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Таблица 'users' успешно создана.")

    connection.commit()
except pymysql.MySQLError as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    connection.close()

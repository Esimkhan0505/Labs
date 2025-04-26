import psycopg2

# Функция для установления соединения с базой данных
def create_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="Lab works",
        user="postgres",
        password="Qwertyeska12"
    )

# Поиск по шаблону
def search_by_pattern(conn, pattern):
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR phone ILIKE %s
    """, (f"%{pattern}%", f"%{pattern}%"))
    
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")
    
    cur.close()

# Вставка или обновление пользователя
def insert_or_update_user(conn, name, phone):
    cur = conn.cursor()
    cur.execute("""
        DO $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = %s) THEN
                UPDATE phonebook SET phone = %s WHERE name = %s;
            ELSE
                INSERT INTO phonebook (name, phone) VALUES (%s, %s);
            END IF;
        END;
        $$;
    """, (name, phone, name, name, phone))
    
    conn.commit()
    cur.close()

# Массовое добавление пользователей
def insert_multiple_users(conn, users):
    for user in users:
        name, phone = user
        if not phone.isdigit() or len(phone) != 10:
            print(f"Invalid phone number for {name}: {phone}")
        else:
            insert_or_update_user(conn, name, phone)

# Получение пользователей с пагинацией
def get_users_with_pagination(conn, limit, offset):
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM phonebook
        LIMIT %s OFFSET %s
    """, (limit, offset))
    
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No more records.")
    
    cur.close()

# Удаление пользователя по имени или телефону
def delete_user(conn, identifier):
    cur = conn.cursor()
    if "@" in identifier:  # Если в строке есть "@", то это телефон
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (identifier,))
    else:
        cur.execute("DELETE FROM phonebook WHERE name = %s", (identifier,))
    
    conn.commit()
    cur.close()

# Меню
def show_menu():
    conn = create_connection()  # Соединение с БД происходит один раз в начале

    while True:
        print("""
1. Search by pattern
2. Insert or Update user
3. Insert multiple users
4. Get users with pagination
5. Delete user
6. Exit
        """)
        choice = input("Enter choice: ")

        if choice == '1':
            pattern = input("Enter pattern to search: ")
            search_by_pattern(conn, pattern)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            insert_or_update_user(conn, name, phone)
        elif choice == '3':
            users_input = input("Enter users (name, phone) separated by comma: ")
            users = [tuple(user.split(',')) for user in users_input.split(';')]
            insert_multiple_users(conn, users)
        elif choice == '4':
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            get_users_with_pagination(conn, limit, offset)
        elif choice == '5':
            identifier = input("Enter name or phone to delete: ")
            delete_user(conn, identifier)
        elif choice == '6':
            conn.close()  # Закрываем соединение с БД при выходе
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()

import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(
    host="localhost",
    dbname="Lab works",
    user="postgres",
    password="Qwertyeska12",
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(20)
    );
""")
conn.commit()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Inserted successfully.\n")

def insert_from_csv():
    path = input("Enter CSV file path: ")
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV data inserted.\n")

def update_data():
    name = input("Enter existing name to update: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Data updated.\n")

def delete_data():
    phone = input("Enter phone number to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Deleted successfully.\n")

def query_data():
    name = input("Enter name to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Phone"], tablefmt="grid"))

def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Phone"], tablefmt="fancy_grid"))

while True:
    print("""
1. Insert data (console)
2. Insert data (CSV)
3. Update phone by name
4. Delete by phone
5. Search by name
    """)
    choice = input("Enter choice: ")
    if choice == '1':
        insert_from_console()
    elif choice == '2':
        insert_from_csv()
    elif choice == '3':
        update_data()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        query_data()
    else:
        print("Exiting program.")
        break

cur.close()
conn.close()

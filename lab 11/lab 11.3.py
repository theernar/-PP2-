import psycopg2
import csv

#PostgreSQL-ге қосылу!
def connect():
    return psycopg2.connect(
        host="localhost", 
        dbname="postgres", 
        user="postgres",
        password="ERNAR4iK001&" 
    )

#Кесте жасау: create table
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Кесте дайын!")

#Деректерді енгізу орны: 
def insert_manual():
    conn = connect()
    cur = conn.cursor()
    name = input("Input your name: ")
    phone = input("Input your phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("All informations added.")

#CSV файл арқылы енгізу
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    file_path = input("Input your CSV file name (example, contacts.csv): ")
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                name, phone = row
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Informations added from CSV file")

#Дерек жаңарту
def update_data():
    conn = connect()
    cur = conn.cursor()
    name = input("What kind of name do you want to change?")
    new_phone = input("New phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Phone number updated")

#Дерек оқу (фильтрмен)
def query_data():
    conn = connect()
    cur = conn.cursor()
    name_filter = input("Input the name: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name_filter,))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    if not rows:
        print("Nothing found")
    cur.close()
    conn.close()

#Дерек жою
def delete_data():
    conn = connect()
    cur = conn.cursor()
    name = input("What kind of name do you want to delete?")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Information deleted")
    
#3-ші функция: көп қолданушыны енгізу, phone тексеру, қате мәліметтерді қайтару
def insert_many_users():
    conn = connect()
    cur = conn.cursor()
    
    count = int(input("How many people do you want to add? "))
    errors = []  # Қате мәліметтерді жинау үшін

    for _ in range(count):
        name = input("Name: ")
        phone = input("Phone number: ")
        
        try:
            cur.execute("SELECT insert_user_check(%s, %s)", (name, phone))
            result = cur.fetchone()[0]
            if result != 'OK':
                errors.append(result)
        except Exception as e:
            errors.append(f"Exception: {e}")

    conn.commit()
    cur.close()
    conn.close()
    
    print("\n All informations updated! ")
    if errors:
        print("The list of error informations:")
        for err in errors:
            print(err)
    else:
        print("Error informations not founded.")




#Меню
def menu():
    create_table()  # Бірінші рет қосылғанда кесте жасап қояды
    while True:
        print("\n PHONEBOOK:")
        print("1. Adding information by myself")
        print("2. Adding informations from CSV file.")
        print("3. Updating informations.")
        print("4. Search the information")
        print("5. Delete information")
        print("6. Adding usernames and return error informations")
        print("0. Exist")

        choice = input("Choose the option: ")
        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            insert_many_users()
        elif choice == "0":
            print("The code stopped. Thank you!")
            break
        else:
            print("ERROR. Please, try again.")

#Кодты іске қосу
if __name__ == "__main__":
    menu()
    
    

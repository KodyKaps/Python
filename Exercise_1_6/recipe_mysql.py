import mysql.connector
import os
# Definition for operation A
def operation_A():
    # ...
    print("operation_A")

# Definition for operation B
def operation_B():
    # ...
    print("operation_B")

# Definition for operation C
def operation_C():
    # ...
    print("operation_C")


def main():
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3306)),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', '')
    }

    try:
        #connect to db using our config
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        #prove the database has tables
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        if(len(tables) > 0):
            print("connected to db")
        print("Tables in the database:")
        for table in tables:
            print(table[0])
        #show there is data in the table
        cursor.execute("SELECT * FROM Recipes;")
        recipes = cursor.fetchall()
        print("rows in the recipes:")
        for r in recipes:
            print(r)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

    #allows ytou to execute queries
    #cursor = conn.cursor()

    print("")
    #This is our loop running the main menu.
    # It continues to loop as long as the user
    # doesn't choose to quit.
    choice = ''
    while(choice != 'quit'):
        print("What would you like to do? Pick a choice!")
        print("1. Perform Operation A")
        print("2. Perform Operation B")
        print("3. Perform Operation C")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == '1':
            operation_A()
        elif choice == '2':
            operation_B()
        elif choice == '3':
            operation_C()

if __name__ == "__main__":
    main()
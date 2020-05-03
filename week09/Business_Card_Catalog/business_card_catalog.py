import sqlite3


def create_users_table():
    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(30) UNIQUE NOT NULL,
        email VARCHAR(30) UNIQUE NOT NULL,
        age INTEGER NOT NULL,
        phone VARCHAR(10) NOT NULL,
        additional_info TEXT);
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


def add():
    name = input('Enter user name: ')
    email = input('Enter e-mail: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional_info = input('Enter additional info(optional): ')

    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()

    query = '''
    INSERT INTO users (full_name, email, age, phone, additional_info)
        VALUES(?, ?, ?, ?, ?)
    '''

    if additional_info == '':
        cursor.execute(query, (name, email, age, phone, "NULL"))
    else:
        cursor.execute(query, (name, email, age, phone, additional_info))

    connection.commit()
    connection.close()


def list():
    print('#############\n###Contacts###\n#############')

    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()

    query = '''
    SELECT * FROM users;
    '''

    cursor.execute(query)

    for user in cursor.fetchall():
        print(f'ID: {user[0]}, Email: {user[2]}, Full name: {user[1]}')

    connection.commit()
    connection.close()


def get():
    id = input('Enter id: ')

    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()

    query = '''
    SELECT * FROM users WHERE id = ?;
    '''

    cursor.execute(query, id)

    user = cursor.fetchone()

    print('Contact info:')

    print('###############')
    print(f'Id: {user[0]}')
    print(f'Full name: {user[1]}')
    print(f'Email: {user[2]}')
    print(f'Age: {user[3]}')
    print(f'Phone: {user[4]}')
    if user[5] != 'NULL':
        print(f'Additional info: {user[5]}')
    print('##############')

    connection.close()


def delete():
    id = input('Enter id: ')

    connection = sqlite3.connect('business_card_catalog.db')
    cursor = connection.cursor()

    query = '''
    SELECT * FROM users WHERE id = ?;
    '''

    cursor.execute(query, id)

    user = cursor.fetchone()

    delete_query = '''
    DELETE FROM users WHERE id = ?
    '''

    cursor.execute(delete_query, id)
    connection.commit()
    connection.close()

    print('\nFollowing contact is deleted successfully:\n')

    print('###############')
    print(f'Id: {user[0]}')
    print(f'Full name: {user[1]}')
    print(f'Email: {user[2]}')
    print(f'Age: {user[3]}')
    print(f'Phone: {user[4]}')
    print(f'Additional info: {user[5]}')
    print('##############')


def help_():
    print('#############\n###Options###\n#############\n')

    print('1. `add` - insert new business card')
    print('2. `list` - list all business cards')
    print('3. `delete` - delete a certain business card (`ID` is required)')
    print('4. `get` - display full information for a certain business card (`ID` is required)')
    print('5. `help` - list all available options')
    print('6. `close` - close')


def main():
    create_users_table()

    print('Hello! This is your business card catalog.')
    print('What would you like? (enter "help" to list all available options)')

    command = ''

    while command != 'close':
        command = input('>>> Enter command: ')

        if command == 'add':
            add()
        elif command == 'list':
            list()
        elif command == 'delete':
            delete()
        elif command == 'get':
            get()
        elif command == 'close':
            exit()
        elif command == 'help':
            help_()
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()

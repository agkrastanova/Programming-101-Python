import sqlite3


def create_base_user_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS BaseUser(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(50),
        email VARCHAR(30),
        phone_number VARCHAR(10),
        address VARCHAR(50));
    '''

    cursor.execute(query)

    connection.commit()
    connection.close()


def add_new_client():
    name = input('Provide user name: ')
    email = input('Provide e-mail: ')
    phone = input('Provide phone: ')
    address = input('Provide address: ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    INSERT INTO BaseUser (user_name, email, phone_number, address)
        VALUES(?, ?, ?, ?)
    '''

    cursor.execute(query, (name, email, phone, address))

    connection.commit()
    connection.close()


def create_client_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS Client(
        base_id INTEGER NOT NULL,
        FOREIGN KEY base_id REFERENCES BaseUser(id)
    );
    '''

    cursor.execute(query)

    connection.commit()
    connection.close()


def create_mechanic_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS Mechanic(
    FOREIGN KEY base_id REFERENCES BaseUser(id)
    );
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


def create_vehicle_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS Vehicle(
        id INTEGER PRIMARY KEY,
        category VARCHAR(20) NOT NULL,
        make VARCHAR(20) NOT NULL,
        model VARCHAR(20) NOT NULL,
        register_number VARCHAR(20) UNIQUE NOT NULL,
        gear_box VARCHAR(20) NOT NULL,
        owner INTEGER NOT NULL,
        FOREIGN KEY owner REFERENCES Client(base_id)
        );
    '''

    cursor.execute(query)

    connection.commit()
    connection.close()


def create_repair_hour_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS RepairHour():
        id INTEGER PRIMARY KEY,
        date VARCHAR(10) NOT NULL,
        start_hour VARCHAR(5) NOT NULL,
        vehicle INTEGER,
        bill REAL,
        mechanic_service INTEGER,
        FOREIGN KEY vehicle REFERENCES Vehicle(id),
        FOREIGN KEY mechanic_service REFERENCES MechanicService(id)
    );
    '''

    cursor.execute(query)

    connection.commit()
    connection.close()


def create_mechanic_service():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS MechanicService(
        id INTEGER PRIMARY KEY,
        mechanic_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        FOREIGN KEY mechanic_id REFERENCES Mechanic(base_id),
        FOREIGN KEY service_id REFERENCES Service(id)
        );
    '''

    cursor.execute(query)

    connection.commit()
    connection.close()


def create_service_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS Service(
        id INTEGER PRIMARY KEY,
        name VARCHAR(30)
    );
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()


# def print_message(name):
#     print(f'Thank you, {name}!')
#     print('Welcome to Vehicle Services!')
#     print('Next time you try to login, provide your user_name!')

#     print('You can choose from the following commands:')
#     print('list_all_free_hours')
#     print('list_free_hours <date>')
#     print('save_repair_hour <hour_id>')
#     print('update_repair_hour <hour_id>')
#     print('delete_repair_hour <hour_id>')
#     print('add_vehicle')
#     print('update_vehicle <vehicle_id>')
#     print('delete_vehicle <vehicle_id>')
#     print('exit')


def main():
    pass


if __name__ == '__main__':
    main()

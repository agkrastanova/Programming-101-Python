import sqlite3


def list_all_free_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    SELECT id, date, start_hour FROM RepairHour WHERE vehicle IS NULL AND mechanic_service IS NULL;
    '''

    cursor.execute(query)

    free_hours = cursor.fetchall()

    print('\n|  ID  |  date  |  start hour  |')
    print('--------------------------------')
    for hours in free_hours:
        print(f'|  {hours[0]}  |  {hours[1]}  |  {hours[2]}  |')

    connection.close()


def list_free_hours_date():
    today = input('Enter date:(dd-mm-yyyy) ')
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    SELECT id, date, start_hour FROM RepairHour WHERE date = ? AND vehicle IS NULL;
    '''

    cursor.execute(query, (today,))

    free_hours = cursor.fetchall()

    print('\n|  ID  |  date  |  start hour  |')
    print('--------------------------------')
    for hours in free_hours:
        print(f'|  {hours[0]}  |  {hours[1]}  |  {hours[2]}  |')

    connection.close()


def save_repair_hour():
    pass


def update_repair_hour():
    pass


def delete_repair_hour():
    pass


def add_vehicle(client):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    category = input('Enter category: ')
    make = input('Enter make: ')
    model = input('Enter model: ')
    register_number = input('Enter registration number: ')
    gear_box = input('Enter gearbox type: ')

    query = '''
    SELECT user_name FROM BaseUser WHERE user_name = ?;
    '''
    cursor.execute(query, (client,))

    owner = cursor.fetchone()

    add_query = '''
    INSERT INTO Vehicle(category, make, model, register_number, gear_box, owner) VALUES(?,?,?,?,?,?);
    '''

    cursor.execute(add_query, (category, make, model, register_number, gear_box, owner[0]))

    connection.commit()
    connection.close()

    print('You added new vehicle successfully!\n')


def update_vehicle():
    pass


def delete_vehicle(owner):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    DELETE FROM Vehicle WHERE owner = ?;
    '''

    cursor.execute(query, (owner,))

    connection.commit()
    connection.close()

    print('You deleted vehicle successfully!\n')


def list_all_busy_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    SELECT id, date, start_hour FROM RepairHour WHERE vehicle IS NOT NULL AND mechanic_service IS NOT NULL;
    '''

    cursor.execute(query)

    free_hours = cursor.fetchall()

    print('\n|  ID  |  date  |  start hour  |')
    print('--------------------------------')
    for hours in free_hours:
        print(f'|  {hours[0]}  |  {hours[1]}  |  {hours[2]}  |')

    connection.close()


def list_busy_hours_date():
    today = input('Enter date:(dd-mm-yyyy) ')
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    SELECT id, date, start_hour FROM RepairHour WHERE date = ? AND vehicle IS NOT NULL;
    '''

    cursor.execute(query, (today,))

    free_hours = cursor.fetchall()

    print('\n|  ID  |  date  |  start hour  |')
    print('--------------------------------')
    for hours in free_hours:
        print(f'|  {hours[0]}  |  {hours[1]}  |  {hours[2]}  |')

    connection.close()


def add_new_repair_hour():
    date = input('Enter date(dd-mm-yyyy): ')
    hour = input('Enter hour(hh-mm): ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    INSERT INTO RepairHour(date, start_hour) VALUES(?,?)
    '''

    cursor.execute(query, (date, hour))

    connection.commit()
    connection.close()

    print('You added new repair hour successfully!\n')


def add_new_service():
    service = input('Provide service name: ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    INSERT INTO Service(name) VALUES(?);
    '''

    cursor.execute(query, (service,))

    connection.commit()
    connection.close()

    print('You added new service successfully!\n')


def add_new_client_to_BaseUser_table():
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

    print(f'Thank you, {name}!\nWelcome to Vehicle Services!\nNext time you try to login, provide your user_name!')


def check_if_user_in_database(name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
        SELECT * FROM BaseUser WHERE user_name = ?;
    '''

    cursor.execute(query, (name,))

    user = cursor.fetchone()

    connection.close()

    if user is None:
        return False
    else:
        return True


def main():
    pass


if __name__ == '__main__':
    main()

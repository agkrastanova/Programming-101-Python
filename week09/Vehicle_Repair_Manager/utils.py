import sqlite3


def add_mechanic():
    add_new_client_to_BaseUser_table()
    title = input('Enter title: ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    INSERT INTO Mechanic(title) VALUES(?);
    '''
    cursor.execute(query, (title,))

    connection.commit()
    connection.close()


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


def save_repair_hour(client):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    print('Choose vehicle to repair: ')

    query1 = '''
    SELECT id, make, register_number FROM Vehicle WHERE owner = ?;
    '''
    cursor.execute(query1, (client,))

    vehicles = cursor.fetchall()

    if vehicles == '' or vehicles is None:
        print('No vehicles to repair!\n')
        return None

    print('\n|    ID    |           Vehicle           |')
    print('------------------------------------------')
    for vehicle in vehicles:
        print(f'|  {vehicle[0]}  | {vehicle[1]} with Register number {vehicle[2]} |')

    print('\n')
    car_id = input('Vehicle id: ')

    print('\nChoose service: ')

    query2 = '''
    SELECT * FROM Service;
    '''

    cursor.execute(query2)

    services = cursor.fetchall()

    print('\n|  ID  |     Service     |')
    print('--------------------------')

    for s in services:
        print(f'| {s[0]} |    {s[1]}    ')

    print('\n')
    service_id = input('Service id: ')

    print('\n')
    add_new_repair_hour(car_id, service_id)

    print(f'Thank you! You saved an hour for {services[int(service_id)-1][1]}')
    print(f'Vehicle: {vehicles[int(car_id)-1][1]} with Register number: {vehicles[int(car_id)-1][2]}')


def update_repair_hour():
    pass


def delete_repair_hour():
    list_all_busy_hours()

    print('Choose hour id to delete: ')
    hour = input('Hour id: ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    DELETE FROM RepairHour WHERE id = ?;
    '''
    cursor.execute(query, (hour,))

    connection.commit()
    connection.close()

    print('You deleted repair hour successfully!')


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


def add_new_repair_hour(vehicle_id, service_id):
    date = input('Enter date(dd-mm-yyyy): ')
    hour = input('Enter hour(hh-mm): ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    INSERT INTO RepairHour(date, start_hour, vehicle, mechanic_service) VALUES(?, ?, ?, ?);
    '''

    cursor.execute(query, (date, hour, vehicle_id, service_id))

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
    add_mechanic()


if __name__ == '__main__':
    main()

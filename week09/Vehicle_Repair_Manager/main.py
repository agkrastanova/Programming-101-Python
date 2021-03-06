import sqlite3
from create_tables import create_all_tables
from utils import (add_new_client_to_BaseUser_table,
                   check_if_user_in_database,
                   list_all_free_hours,
                   list_free_hours_date,
                   save_repair_hour,
                   update_repair_hour,
                   delete_repair_hour,
                   add_vehicle,
                   update_vehicle,
                   delete_vehicle,
                   list_all_busy_hours,
                   list_busy_hours_date,
                   add_new_repair_hour,
                   add_new_service,
                   add_mechanic
                   )

client_list = ['list all free hours',
               'list free hours for date',
               'save repair hour',
               'update repair hour',
               'delete repair hour',
               'add vehicle',
               'update vehicle',
               'delete vehicle',
               'exit']

mechanic_list = ['list_all_free_hours',
                 'list_free_hours <date>',
                 'list_all_busy_hours',
                 'list_busy_hours <date>',
                 'add_new_repair_hour',
                 'add_new_service',
                 'update_repair_hour <hour_id>',
                 'exit']


def print_command_list(command_list):
    for command in command_list:
        print(command)


def client_choose_command_list(client):
    command = ''
    while command != 'exit':
        command = input('command> : ')
        if command == 'list all free hours':
            list_all_free_hours()
        if command == 'list free hours for date':
            list_free_hours_date()
        if command == 'save repair hour':
            save_repair_hour()
        if command == 'update repair hour':
            update_repair_hour()
        if command == 'delete repair hour':
            delete_repair_hour()
        if command == 'add vehicle':
            add_vehicle(client)
        if command == 'update vehicle':
            update_vehicle()
        if command == 'delete vehicle':
            delete_vehicle(client)

    print('Goodbye!')


def mechanic_choose_command_list():
    command = ''
    while command != 'exit':
        command = input('command> : ')
        if command == 'list all free hours':
            list_all_free_hours()
        if command == 'list free hours for date':
            list_free_hours_date()
        if command == 'list all busy hours':
            list_all_busy_hours()
        if command == 'list busy hours for date':
            list_busy_hours_date()
        if command == 'add new repair hour':
            add_new_repair_hour()
        if command == 'add new service':
            add_new_service()
        if command == 'update repair hour':
            update_repair_hour()


def login(user_name):
    if not check_if_user_in_database(user_name):
        print('Unknown user!\nWould you like to create new user?(yes/no)')
        answer = ''
        answer = input('(yes/no)>> ')
        if answer == 'yes':
            print('Are you a client or mechanic?')
            client_or_mehanic = input()
            if client_or_mehanic.lower() == 'client':
                add_new_client_to_BaseUser_table()
            elif client_or_mehanic.lower() == 'mechanic':
                add_mechanic()
        if answer == 'no':
            return
        else:
            return


def is_client(user_name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    SELECT user_name FROM BaseUser WHERE BaseUser.user_name = ?;
    '''

    cursor.execute(query, (user_name,))

    client = cursor.fetchone()

    if client is None:
        return False

    if client[0] == user_name:
        return True
    else:
        return False

    connection.close()


def is_mechanic(user_name):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    SELECT * FROM Mechanic WHERE title = ?;
    '''
    cursor.execute(query, (user_name,))

    mechanic = cursor.fetchone()

    connection.close()
    if mechanic is None:
        return False

    if mechanic[1] == user_name:
        return True
    else:
        return False


def main():
    create_all_tables()
    print('Hello!\nProvide user name: ')
    user_name = input()

    login(user_name)

    if is_client(user_name) and not is_mechanic(user_name):
        print('\nChoose command: ')
        print('----------------')
        print_command_list(client_list)
        print('----------------\n')
        client_choose_command_list(user_name)

    if is_mechanic(user_name):
        print('\nChoose command: ')
        print('----------------')
        print_command_list(mechanic_list)
        print('----------------\n')
        mechanic_choose_command_list(user_name)


if __name__ == '__main__':
    main()

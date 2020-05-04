import sqlite3
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
                   add_new_service
                   )


client_list = ['list_all_free_hours',
               'list_free_hours <date>',
               'save_repair_hour <hour_id>',
               'update_repair_hour <hour_id>',
               'delete_repair_hour <hour_id>',
               'add_vehicle',
               'update_vehicle <vehicle_id>',
               'delete_vehicle <vehicle_id>',
               'exit']

mechanic_list = ['list_all_free_hours',
                 'list_free_hours <date>',
                 'list_all_busy_hours',
                 'list_busy_hours <date>',
                 'add_new_repair_hour',
                 'add_new_service',
                 'update_repair_hour <hour_id>',
                 'exit']


def client_choose_command_list(client):
    command = ''
    while command != 'exit':
        command = input('command> : ')
        if command == 'list_all_free_hours':
            list_all_free_hours()
        if command == 'list_free_hours <date>':
            list_free_hours_date()
        if command == 'save_repair_hour <hour_id>':
            save_repair_hour()
        if command == 'update_repair_hour <hour_id>':
            update_repair_hour()
        if command == 'delete_repair_hour <hour_id>':
            delete_repair_hour()
        if command == 'add_vehicle':
            add_vehicle(client)
        if command == 'update_vehicle <vehicle_id>':
            update_vehicle()
        if command == 'delete_vehicle <vehicle_id>':
            delete_vehicle(client)


def mechanic_choose_command_list():
    command = ''
    while command != 'exit':
        command = input('command> : ')
        if command == 'list_all_free_hours':
            list_all_free_hours()
        if command == 'list_free_hours <date>':
            list_free_hours_date()
        if command == 'list_all_busy_hours':
            list_all_busy_hours()
        if command == 'list_busy_hours <date>':
            list_busy_hours_date()
        if command == 'add_new_repair_hour':
            add_new_repair_hour()
        if command == 'add_new_service':
            add_new_service()
        if command == 'update_repair_hour <hour_id>':
            update_repair_hour()


def main():
    pass
    # print('Hello!\nProvide user name: ')
    # user_name = input()

    # if not check_if_user_in_database(user_name):
    #     print('Unknown user!\nWould you like to create new user?(yes/no)')
    #     answer = ''
    #     while answer != 'yes' or answer != 'no':
    #         answer = input()
    #         if answer == 'yes':
    #             add_new_client_to_BaseUser_table()
    #         if answer == 'no':
    #             return None
    #         else:
    #             print('yes or no, please: ')
    # elif check_if_user_in_database(user_name):
    #     print('You can choose from the following commands:')
    #     pass


if __name__ == '__main__':
    main()

import sqlite3


def create_all_tables():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS BaseUser(
        id INTEGER PRIMARY KEY,
        user_name VARCHAR(50),
        email VARCHAR(30),
        phone_number VARCHAR(10),
        address VARCHAR(50)
    );

    CREATE TABLE IF NOT EXISTS Client(
        base_id INTEGER NOT NULL,
        FOREIGN KEY (base_id) REFERENCES BaseUser(id)
    );

    CREATE TABLE IF NOT EXISTS Mechanic(
        base_id INTEGER NOT NULL,
        title VARCHAR(30),
        FOREIGN KEY (base_id) REFERENCES BaseUser(id)
    );

    CREATE TABLE IF NOT EXISTS Vehicle(
        id INTEGER PRIMARY KEY,
        category VARCHAR(20) NOT NULL,
        make VARCHAR(20) NOT NULL,
        model VARCHAR(20) NOT NULL,
        register_number VARCHAR(20) UNIQUE NOT NULL,
        gear_box VARCHAR(20) NOT NULL,
        owner INTEGER NOT NULL,
        FOREIGN KEY (owner) REFERENCES Client(base_id)
    );

    CREATE TABLE IF NOT EXISTS MechanicService(
        id INTEGER PRIMARY KEY,
        mechanic_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        FOREIGN KEY (mechanic_id) REFERENCES Mechanic(base_id),
        FOREIGN KEY (service_id) REFERENCES Service(id)
    );

    CREATE TABLE IF NOT EXISTS RepairHour(
        id INTEGER PRIMARY KEY,
        date VARCHAR(10) NOT NULL,
        start_hour VARCHAR(5) NOT NULL,
        vehicle INTEGER,
        bill REAL,
        mechanic_service INTEGER,
        FOREIGN KEY (vehicle) REFERENCES Vehicle(id),
        FOREIGN KEY (mechanic_service) REFERENCES MechanicService(id)
    );


    CREATE TABLE IF NOT EXISTS Service(
        id INTEGER PRIMARY KEY,
        name VARCHAR(30)
    );
    '''

    cursor.executescript(query)

    connection.commit()
    connection.close()


def main():
    create_all_tables()


if __name__ == '__main__':
    main()

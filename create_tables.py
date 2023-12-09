
import sqlite3


def main():
    create_roles_table()
    create_hero_table()
    create_hero_roles_relation()



#Функция создает таблицу Hero в базе данных dota_counter_picks.db
def create_hero_table():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Heroes(
                        id INTEGER PRIMARY KEY,
                        Name TEXT,
                        Attribute TEXT,
                        Description TEXT
        )''')


        print('Таблица данных "Heroes" создана')
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ',err)
    finally:
        if conn != None:
            conn.close()




# Функция создает таблицу Roles в базе данных dota_counter_picks.db
def create_roles_table():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Roles (
                        id INTEGER PRIMARY KEY,
                        Name TEXT,
                        Description TEXT
        )''')

        print('Таблица данных "Roles" создана')
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()



#Функция создает связь между Героем и его Ролями в игре
def create_hero_roles_relation():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS HeroRoles(
                        id INTEGER PRIMARY KEY,
                        hero_id INTEGER,
                        role_id INTEGER,
                        FOREIGN KEY (hero_id) REFERENCES Heroes(id),
                        FOREIGN KEY (role_id) REFERENCES Roles(id)
                        )''')
        print('Связующая таблица для Heroes and Roles создана')
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()






if __name__ == '__main__':
    main()


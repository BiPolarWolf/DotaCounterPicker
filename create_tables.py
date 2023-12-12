
import sqlite3


def main():
    create_hero_table()
    create_feature_table()
    create_hero_feature_relation()
    create_feature_vs_feature()

#Функция создает таблицу Hero в базе данных dota_counter_picks.db
def create_hero_table():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Heroes(
                        id INTEGER PRIMARY KEY,
                        Name TEXT UNIQUE,
                        Attribute TEXT,
                        Attack TEXT,
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
def create_feature_table():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Feature(
                        id INTEGER PRIMARY KEY,
                        Name TEXT UNIQUE,
                        Description TEXT
        )''')

        print('Таблица данных "Feature" создана')
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()



#Функция создает связь между Героем и его Ролями в игре
def create_hero_feature_relation():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Hero_feature(
                        id INTEGER PRIMARY KEY,
                        hero_id INTEGER,
                        feature_id INTEGER,
                        level INTEGER,
                        FOREIGN KEY (hero_id) REFERENCES Heroes(id),
                        FOREIGN KEY (feature_id) REFERENCES Feature(id)
                        
                        )''')
        print('Связующая таблица для Heroes and Feature создана')
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()


#создает связующую таблицу для
def create_feature_vs_feature():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Feature_vs_feature(
                        id INTEGER PRIMARY KEY,
                        winner_id INTEGER,
                        loser_id INTEGER,
                        FOREIGN KEY (winner_id) REFERENCES Feature(id),
                        FOREIGN KEY (loser_id) REFERENCES Feature(id)

                        )''')
        print('Связующая таблица для Feature and Feature создана')
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()

if __name__ == '__main__':
    main()


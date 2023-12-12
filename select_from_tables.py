
import sqlite3


def main():
    pass
   # feature_name = input('Введите имя персонажа :')
   # hero_name= input('Введите имя персонажа :')
   # loser_id = None
   # select_hero_info(hero_name)
   # select_counter_heroes()
   # select_heroes_names()
   # select_features()
   # select_feature_info(feature_name)
   # select_counter_features(loser_id)


def  select_counter_features(loser_id):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Feature_vs_feature WHERE loser_id == ?''',(loser_id,))

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()

        return results


def select_hero_info(hero_name):
    conn = None
    result = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT * FROM Heroes WHERE Name == ?''',(hero_name,))

        result = cur.fetchone()
    except sqlite3.Error as err:
        print('Ошибка базы данных ',err)
    finally:
        if conn != None:
            conn.close()
        return result


def select_counter_heroes():
    pass

def select_heroes_names():
    conn = None
    result = []
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT id,Name FROM Heroes ''')

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()
        return results



def select_feature_info(feature_name):
    conn = None
    result = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT * FROM Feature WHERE Name == ?''', (feature_name,))

        result = cur.fetchone()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()
        return result



def select_features():
    conn = None
    result = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT id,Name FROM Feature ''')

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()
        return results

if __name__ == '__main__':
    main()

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

#выбирает все оссобенности определенного персонажа по его айди
def select_hero_features(hero_id):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()
        cur.execute('''SELECT hero_id,feature_id,level FROM Hero_feature WHERE hero_id == ?''',(hero_id,))

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()

        return results

def select_hero_features1(hero_id):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()
        cur.execute('''SELECT Heroes.Name,Heroes.Description,Feature.Name,Feature.Description,level
         FROM Hero_feature
         JOIN Heroes ON Hero_feature.hero_id = Heroes.id
         JOIN Feature ON Hero_feature.feature_id == Feature.id
         
         WHERE hero_id == ?''',(hero_id,))

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()

        return results


#Выбирает все записи о конкурирующих между собой способностях по id оссобенности которая слабее
def  select_counter_features(loser_id):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Feature_vs_feature WHERE loser_id == ?''',(loser_id,))

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()

        return results

# возвращает полное описание Персонажа  по его id
def select_hero_info(hero_id):
    conn = None
    result = None
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT * FROM Heroes WHERE id == ?''',(hero_id,))

        result = cur.fetchone()
    except sqlite3.Error as err:
        print('Ошибка базы данных ',err)
    finally:
        if conn != None:
            conn.close()
        return result

# должна подбирать контр пики для определенного Героя
def select_counter_heroes():
    pass



# выбирает все id и Имена персонажей из таблицы Heroes
def select_heroes():
    conn = None
    result = []
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT id,Name FROM Heroes ORDER BY id ''')

        results = cur.fetchall()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()
        return results


# возвращает полное описание оссобенности по ее id
def select_feature_info(feature_id):
    conn = None
    result = None
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''SELECT * FROM Feature WHERE id == ?''', (feature_id,))

        result = cur.fetchone()
    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()
        return result


# выбирает список всех оссобеностей которые только могут быть
def select_features():
    conn = None
    result = None
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
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
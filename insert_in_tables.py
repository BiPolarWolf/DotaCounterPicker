import requests
import sqlite3

Hero_obj =requests.get('https://api.opendota.com/api/heroes')

#json список из словарей в которых есть информация о персонаже
Heroes = Hero_obj.json()

#Функция перебирает все записи о героях из API и добавляет каждого в базу через фунцкию hero_insert
def insert_all_heroes(Heroes):
    for hero in Heroes:
        hero_insert(hero_info=hero)


#Функция добавляет персонажа в базу данных таблицу Heroes
def hero_insert(hero_info:dict):
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Heroes(Name,Attribute,Attack)
                        VALUES (?,?,?)''',
                    (hero_info['localized_name'],
                                hero_info['primary_attr'],
                                hero_info['attack_type']))
        print('Герой занесен в базу')

        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)

    finally:
        if conn != None:
            conn.close()


#Функция для добавления оссобенности с ее названием и описанием
def feature_insert(feature_info):
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Feature(Name,Description) VALUES (?,?)''',
                    (feature_info[0],feature_info[1]))
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)

    finally:
        if conn != None:
            conn.close()

#Функция для добавления Герою оссобенности из списка и указанию силы этой оссобенности
def Hero_feature_insert(hero_feature_info:dict):
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Hero_feature(hero_id,feature_id,level)
                            VALUES (?,?,?)''',
                    (hero_feature_info['hero_id'],
                     hero_feature_info['feature_id'],
                     hero_feature_info['level']))
        print('К Герою добавлена новая оссобенность')

        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)

    finally:
        if conn != None:
            conn.close()


#срабатывает функция для добавления всех персонажей.

if __name__ == '__main__':
    insert_all_heroes(Heroes)

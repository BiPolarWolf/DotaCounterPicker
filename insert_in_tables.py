import requests
import sqlite3

Hero_obj =requests.get('https://api.opendota.com/api/heroes')
Heroes = Hero_obj.json()

def insert_all_heroes(Heroes):
    for hero in Heroes:
        hero_insert(hero_info=hero)

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

if __name__ == '__main__':
    insert_all_heroes(Heroes)


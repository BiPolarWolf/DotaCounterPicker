import sqlite3

def delete_heroes():
    conn = None
    try:
        conn = sqlite3.connect('dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute(''' DROP TABLE IF EXISTS Heroes''')

        print('Таблица данных "Heroes" удалена')
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)
    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    delete_heroes()
import sqlite3


def update_feature_description(feature_name,feature_descr):
    conn = None
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Feature
        SET Description = ?
        WHERE Name == ?''',(feature_descr,feature_name))
        conn.commit()
        print('Описание для способности было обновлено')

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)

    finally:
        if conn != None:
            conn.close()
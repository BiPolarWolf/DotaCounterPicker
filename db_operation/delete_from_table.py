
import sqlite3



def delete_from_hero_feature(hero_id,feature_id):
    conn = None
    try:
        conn = sqlite3.connect('../dota_counter_picks.db')
        cur = conn.cursor()

        cur.execute('''DELETE FROM Hero_Feature WHERE hero_id == ? AND feature_id == ?''',(hero_id,feature_id))
        conn.commit()

    except sqlite3.Error as err:
        print('Ошибка базы данных ', err)

    finally:
        if conn != None:
            conn.close()

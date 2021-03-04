# pip install psycopg2
# pip install psycopg2-binary (UNIX)

import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor

#conn = psycopg2.connect(dbname='postgres',
                        # user='postgres',
                        # password='123',
                        # host='localhost',
                        # port='5433')

# cursor = conn.cursor()

# cursor.execute('select * from "user"')

#cursor.fetchone()  возвращает одну строку
#cursor.fetchall() вовзращает список всех строк
#cursor.fetchmany(size = 2)  возвращает заданное количество строк

# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()

with closing(psycopg2.connect(dbname='postgres',user='postgres',password='123',host='localhost',port='5433')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('select * from "user"')
        for row in curs:
            print(row)
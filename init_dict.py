import os
import psycopg2

database_url = os.environ.get('DATABASE_URL')

with psycopg2.connect(database_url) as conn:
    with conn.cursor() as cur:
        sql = '''
            CREATE TABLE dictionary (
                guildId BIGINT,
                word TEXT,
                kana TEXT,
                UNIQUE (guildId, word)
            )
            '''
        cur.execute(sql)

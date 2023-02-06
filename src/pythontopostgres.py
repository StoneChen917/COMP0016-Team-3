import psycopg2



hostname = "localhost"
database = "postgres"
username = "postgres"
pwd = "Abc123456"
port_id = 5433
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL)'''
    cur.execute(create_script)

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
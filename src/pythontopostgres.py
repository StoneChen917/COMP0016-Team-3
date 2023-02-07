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

    create_script = '''   CREATE TABLE IF NOT EXISTS Admin0 (
                            admin_0_code              varchar(40) PRIMARY KEY,
                            name                      varchar(40) NOT NULL);

                          CREATE TABLE IF NOT EXISTS Admin1 (
                            admin_1_code              varchar(40) PRIMARY KEY,
                            name                      varchar(40) NOT NULL,
                            admin_0_code              varchar(40) REFERENCES Admin0);

                          CREATE TABLE IF NOT EXISTS Admin2 (
                            admin_2_code              varchar(40) PRIMARY KEY,
                            name                      varchar(40) NOT NULL,
                            admin_1_code              varchar(40) REFERENCES Admin1);

                          CREATE TABLE IF NOT EXISTS Disaster (
                            operation_number          varchar(40) PRIMARY KEY,
                            glide_number              varchar(40) NOT NULL,
                            host_national_society     varchar(40) NOT NULL,
                            operation_budget          varchar(40) NOT NULL,
                            operation_start_date      DATE,
                            operation_end_date        DATE,
                            number_of_people_affected INT,
                            number_of_people_assisted INT,
                            admin_2_code varchar(40)  REFERENCES Admin2)'''                    
    cur.execute(create_script)

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
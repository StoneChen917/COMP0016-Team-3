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

    create_script_1 = ''' CREATE TABLE IF NOT EXISTS Admin2 (
                            admin_2_code     varchar(40) PRIMARY KEY,
                            name           varchar(40) NOT NULL);

                          CREATE TABLE IF NOT EXISTS Disaster (
                            operation_number          varchar(40) PRIMARY KEY,
                            glide_number              varchar(40) NOT NULL,
                            host_national_society     varchar(40) NOT NULL,
                            operation_budget          varchar(40) NOT NULL,
                            operation_start_date      DATE,
                            operation_end_date        DATE,
                            number_of_people_affected INT,
                            number_of_people_assisted INT,
                            CONSTRAINT fk_admin_2_code
                                FOREIGN KEY(admin_2_code) 
	                            REFERENCES Admin2(admin_2_code))'''
    create_script_2 = ''' CREATE TABLE IF NOT EXISTS Admin0 (
                            admin0code     varchar(40) PRIMARY KEY,
                            name    varchar(40) NOT NULL)'''
    create_script_3 = ''' CREATE TABLE IF NOT EXISTS Admin2 (
                            admin2code     varchar(40) PRIMARY KEY,
                            name    varchar(40) NOT NULL)'''                       
    cur.execute(create_script_1)

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
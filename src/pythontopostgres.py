import psycopg2



hostname = "localhost"
database = "cifrc"
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
                            admin_0_code              varchar PRIMARY KEY,
                            name                      varchar NOT NULL);

                          CREATE TABLE IF NOT EXISTS Admin1 (
                            admin_1_code              varchar PRIMARY KEY,
                            name                      varchar NOT NULL,
                            admin_0_code              varchar REFERENCES Admin0);

                          CREATE TABLE IF NOT EXISTS Admin2 (
                            admin_2_code              varchar PRIMARY KEY,
                            name                      varchar NOT NULL,
                            admin_1_code              varchar REFERENCES Admin1);

                          CREATE TABLE IF NOT EXISTS Disaster (
                            operation_number          varchar PRIMARY KEY,
                            glide_number              varchar NOT NULL,
                            host_national_society     varchar NOT NULL,
                            operation_budget          varchar NOT NULL,
                            operation_start_date      DATE,
                            operation_end_date        DATE,
                            number_of_people_affected INT,
                            number_of_people_assisted INT,
                            admin_2_code              varchar REFERENCES Admin2)'''                    
    cur.execute(create_script)

    admin_0_insert_script = ''' INSERT INTO Admin0 (admin_0_code, name) VALUES (%s, %s)'''
    admin_1_insert_script = ''' INSERT INTO Admin1 (admin_1_code, name, admin_0_code) VALUES (%s, %s, %s)'''
    admin_2_insert_script = ''' INSERT INTO Admin2 (admin_2_code, name, admin_1_code) VALUES (%s, %s, %s)'''
    disaster_insert_script = ''' INSERT INTO Disaster (operation_number, glide_number, host_national_society, operation_budget, 
                          operation_start_date, operation_end_date, number_of_people_affected, number_of_people_assisted,
                          admin_2_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    admin_0_insert_value = ("1", "Turkey")
    admin_1_insert_value = ("1", "Turkey1", "1")
    admin_2_insert_value = ("1", "Turkey2", "1")
    disaster_insert_value = ("MDRJM004", "1", "The Jamaica Red Cross (JRC) has 400 volunteers at the national level",
                      "130,149 Swiss francs (CHF)", "2016-10-1", "2016-12-1", 150000, 2620, "1")
    
    cur.execute(admin_0_insert_script, admin_0_insert_value)
    cur.execute(admin_1_insert_script, admin_1_insert_value)
    cur.execute(admin_2_insert_script, admin_2_insert_value)
    cur.execute(disaster_insert_script, disaster_insert_value)

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
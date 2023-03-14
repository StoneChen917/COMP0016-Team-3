import psycopg2



hostname = "localhost"
database = "cifrc"
username = "postgres"
pwd = "Abc123456"
port_id = 5433
conn = None
cur = None

def save_to_table(op_num, ad0, ad1, ad2, iso, glide, hns, ob, osd, oed, npaf, npas):
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    
    cur = conn.cursor()

    disaster_insert_script = ''' INSERT INTO Disaster (operation_number, admin_0_code, admin_1_code, admin_2_code, iso_info, glide_number, host_national_society, operation_budget, 
                          operation_start_date, operation_end_date, number_of_people_affected, number_of_people_assisted) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    disaster_insert_value = (op_num, ad0, ad1, ad2, iso, glide, hns, ob, osd, oed, npaf, npas)
    
    cur.execute(disaster_insert_script, disaster_insert_value)

    conn.commit()
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()



def create_script():
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

    cur = conn.cursor()

    create_script = '''   CREATE TABLE IF NOT EXISTS Disaster (
                            operation_number          varchar PRIMARY KEY,
                            admin_0_code              varchar NOT NULL,
                            admin_1_code              varchar NOT NULL,
                            admin_2_code              varchar NOT NULL,
                            iso_info                  varchar NOT NULL,
                            glide_number              varchar NOT NULL,
                            host_national_society     varchar NOT NULL,
                            operation_budget          varchar NOT NULL,
                            operation_start_date      DATE,
                            operation_end_date        DATE,
                            number_of_people_affected INT,
                            number_of_people_assisted INT)'''                    
    cur.execute(create_script)
    conn.commit()
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
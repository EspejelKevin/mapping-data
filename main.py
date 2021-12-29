from mappingData import mapping
import psycopg2


def getConnection():
    conn = psycopg2.connect("dbname=testbackend user=kevin")

    return conn

def insertSett(settlements):
    try:
        conn = getConnection()
        cur = conn.cursor()

        query = """
            insert into settlements(name, codepostal, zone, id_asenta_munici, id_typesett, id_munici, id_city, id_postal) 
            values(%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur.executemany(query, settlements)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
        

settlements, typeSettlements, postalAdministrations, states, municipalities, cities = mapping()

insertSett(settlements)
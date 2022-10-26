import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                password="IADica26129",
                                host="node36962-pawaris.proen.app.ruk-com.cloud",
                                port="5432",
                                database="postgres")
    
    connection.autocommit = True
    
    #
    cursor = connection.cursor()

    #
    sql = '''CREATE database HW'''

    #
    cursor.execute(sql)
    print("Database created successfully........")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
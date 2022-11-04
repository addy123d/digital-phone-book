import psycopg2


def options():
    print('''
          1. Create Database
          2. Drop Database
          ''')

    user_option = int(input("Option: "))

    if (user_option == 1):
        create_db()
    else:
        drop_db()


def default_config():
    connection = psycopg2.connect(
        host='127.0.0.1',
        port='5432',
        database='postgres',
        user='postgres',
        password='postgres'
    )

    connection.autocommit = True
    
    # Create a cursor
    cursor = connection.cursor()
    
    # Ask user for database name
    dbname = str(input("Enter DBName: "))
    
    return (dbname, cursor)
    


def create_db():
    '''
      Asks User for a database name, and creates the database with the same name.
      Use:
        1. psql -U database_name
        2. \l (This will list all databases)
    '''

    dbname, cursor = default_config() 
    
    # Execute a query
    create_db_query = f'CREATE DATABASE {dbname}'
    
    cursor.execute(create_db_query) #Database will be created
    
    
    
    
def drop_db():
    '''
      Asks User for a database name, and creates the database with the same name.
      Use:
        1. psql -U database_name
        2. \l (This will list all databases)
    '''

    dbname, cursor = default_config() 
    
    # Execute a query
    drop_db_query = f'DROP DATABASE {dbname}'
    
    cursor.execute(drop_db_query) #Database will be created
    
    

if __name__ == "__main__":
    options()
    
    
    
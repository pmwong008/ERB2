# pip install mysql-connector-python

from mysql.connector import connect, Error
load_dotenv()

if __name__ == "__main__":
    try:
        with connect(
            host="localhost",
            user="root", # shouldn't be here, should be saved as Environmental variable
            password="password", # shouldn't be here, should be saved as Environmental variable
            database="erb_demo"
        ) as connection:
            print(connection)
            show_table_query = """
            DESCRIBE movies
            """

            with connection.cursor() as cursor:
                cursor.execute(show_table_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

    except Error as e:
        print(e)
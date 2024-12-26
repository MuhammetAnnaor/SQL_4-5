def create_database_and_tables(cursor):

    cursor.execute('''CREATE DATABASE IF NOT EXISTS Cars''')
    cursor.execute("""USE Cars""")

    query = """CREATE TABLE IF NOT EXISTS brands (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL UNIQUE,
                country VARCHAR(50) NOT NULL
                 );"""
    cursor.execute(query)

    query = """CREATE TABLE IF NOT EXISTS models (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                year INT NOT NULL CHECK (year >= 1886),
                brand_id INT NOT NULL,
                FOREIGN KEY (brand_id) REFERENCES brands(id) ON DELETE CASCADE
    );"""
    cursor.execute(query)
    print("База данных и таблицы успешно созданы.")


def connect_to_cars_detabase(cursor):
    cursor.execute("""USE Cars""")
    print('Подключились к базе данных о машине')


def add_brands(cursor,connection):
    new_brand = input("Имя производителя машины: ")
    country = input('Страна: ')
    query = """INSERT INTO brands (name, country) VALUES (%s, %s)"""
    cursor.execute(query, (new_brand, country))
    connection.commit()
    print(f"Марка {new_brand} успешно добавлена")


def add_models(cursor,connection):
    new_model = input("Модель машины: ")
    year = int(input('Год: '))
    get_brands_info(cursor)
    brand_id = int(input('id производителя машин: '))
    query = """INSERT INTO models (name, year, brand_id) VALUES (%s, %s, %s)"""
    cursor.execute(query, (new_model, year, brand_id))
    connection.commit()
    print(f"Марка {new_model} успешно добавлена")

def del_model(cursor,connection):
    get_full_model_info(cursor)
    model_id = int(input('id модели надо удалить'))
    query = '''DELETE FROM models WHERE id = %s'''
    cursor.execute(query, model_id)
    connection.commit()
    print("Машина удалена")
def upddate_model (cursor,connection):
    get_full_model_info(cursor)
    model_id = int(input("id модели, которую надо изменить"))
    new_name = input("Новое название модели: ")
    new_year = int(input("Новый год создания: "))
    query = '''UPDATE models 
                SET name = %s, year = %s
                WHERE id = %s
                '''
    cursor.execute(query, (new_name, new_year, model_id))
    connection.commit()
    print("Данные успешно обновлены!")

def get_full_model_info(cursor):
    query = """SELECT m.id, m.name, m.year, b.name, b.country FROM models m 
                JOIN brands b ON m.brand_id = b.id    """
    cursor.execute(query)
    for i, row in enumerate(cursor, start=1):
        print (f'{i}. id:{row[0]}; name:{row[1]}; year:{row[2]}; brand:{row[3]}; country:{row[4]}.')

def get_brands_info(cursor):
    cursor.execute(''' SELECT * FROM brands''')
    for row in cursor:
        print (f'id: {row[0]}; {row[1]}; {row[2]}')


import pymysql
import sql

try:
    with pymysql.connect(host="localhost", port=3307, user="root", password="") as connection:  # с помощью модуля подключаемся к базе данных
        print('Успешно подключено')

        with connection.cursor() as cursor:
            while True:
                print('+. Подключиться к базе данных о машинах')
                print("0. Выход")
                print("1. Создать базу данных и таблицы")
                print("2. Добавить производителя машин")
                print("3. Добавить модель машины")
                print("4. Удалить модель машины")
                print("5. Обновить информацию о модели машины")
                print("6. Показать информацию о машине")

                user_choice = input("Введите номер действия: ")

                match user_choice:
                    case "+": sql.connect_to_cars_detabase(cursor)
                    case "0": break
                    case "1": sql.create_database_and_tables(cursor)
                    case "2": sql.add_brands(cursor, connection)
                    case "3": sql.add_models(cursor,connection)
                    case "4": sql.del_model(cursor,connection)
                    case "5": sql.upddate_model(cursor,connection)
                    case "6": sql.get_full_model_info(cursor)
except pymysql.Error as e:
    print(e)
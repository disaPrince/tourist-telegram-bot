import mysql.connector
from mysql.connector import Error
from aiogram import types
from create_bot import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_connection(host_name, user_name, user_password, db_name):
    global connection
    global cur
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        cur = connection.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tour(img TEXT, name VARCHAR(24) PRIMARY KEY, description TEXT, '
                       'rating INT, from_city TEXT, to_city TEXT, when_date DATE, days INT, price INT)')
        connection.commit()
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    # return connection


# connection = create_connection("localhost", "root", "", "tour_bot")


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


async def db_add_tour(tour):
    cur.execute('INSERT INTO tour (img, name, description, rating, from_city, to_city, when_date, days, price)'
                   'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                   (tour.photo, tour.name, tour.description, int(tour.rating), tour.from_city,
                    tour.to_city, tour.when_date.date().isoformat(), int(tour.days), int(tour.price)))
    connection.commit()


async def db_get_tour(message: types.Message):
    cur.execute('select img, name, description, price from tour')
    for ret in cur.fetchall():
        await bot.send_photo(message.chat.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}',
                             reply_markup=InlineKeyboardMarkup().
                             add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))
    connection.commit()

async def sql_read(message: types.Message):
    cur.execute('select * from tour')
    for ret in cur.fetchall():
        await bot.send_photo(message.chat.id, ret[0], f'{ret[1]}, {ret[2]}, {ret[3]}, {ret[4]}, {ret[5]}, {ret[6]}, {ret[7]}, {ret[8]}')
    connection.commit()

async def db_delete_tour(data):
    cur.execute('delete from tour where name = %s', (data, ))
    connection.commit()





import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('tourist.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS tour(from_city TEXT primary key, mon TEXT, to_city TEXT, day TEXT, budget TEXT, adults TEXT, children TEXT)')
    # cur.execute("""INSERT INTO tour VALUES ('Алматы', 'Январь', 'Дубай', '8', '200000 - 500000', '4', '3');""")
    base.commit()


# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO tours VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
#         base.commit()


# async def sql_read(message):
#     for ret in cur.execute('SELECT * FROM tour').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], ret[1], ret[2], ret[3], ret[4], ret[5], ret[6], parse_mode='Markdown')


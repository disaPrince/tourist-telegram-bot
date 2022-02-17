import sqlite3 as sq
from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('tourist.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS tours(from_city TEXT primary key, mon TEXT, to_city TEXT, day int, budget int, adults int, children int)')
    # cur.execute("""INSERT INTO tours VALUES ('Алматы', 'Январь', 'Дубай', '8', '200000 - 500000', '4', '3');""")
    base.commit()



# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO tours VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
#         base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[1], ret[2], ret[3], ret[4], ret[5], ret[6], ret[7])
    # cur.execute('SELECT * FROM tours')
    # query_results = cur.fetchall()
    # text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
    # return (str(text))



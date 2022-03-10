from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin
from database import db_connect


async def on_startup(_):
	print('Бот работает!')
	db_connect.create_connection("localhost", "root", "", "test")

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



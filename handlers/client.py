from aiogram import bot, types
from create_bot import dp
from aiogram.dispatcher import Dispatcher
from keyboards import client_kb
from aiogram.dispatcher.filters import Text
from database import sqlite_db
import tracemalloc

tracemalloc.start()



async def url_command(message: types.Message):
    await message.answer(message.from_user.first_name, reply_markup=client_kb.kb)
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.urlkb)

    await message.delete()

async def menu(message: types.Message):
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.urlkb)
    await message.delete()

async def button1_call(callback: types.CallbackQuery):
    await callback.message.answer('Туристическая компания для нахождения очень выгодных туров по всему миру 🍹')
    await callback.message.answer('Для подробной информацией перейдите на <a href="https://www.youtube.com/">сайт компании</a>', parse_mode=types.ParseMode.HTML)
    await callback.answer()

async def button2_call(callback: types.CallbackQuery):
    await callback.message.answer('Откуда вылетаете?📲', reply_markup=client_kb.urlb)
    await callback.answer()

async def button6_call(callback: types.CallbackQuery):
    await callback.message.answer('Выберите месяц:📆', reply_markup=client_kb.urlmon)
    await callback.answer()

async def button7_call(callback: types.CallbackQuery):
    await callback.message.answer('Выберите страну:🌃', reply_markup=client_kb.urlto)
    await callback.answer()

async def button_day(callback: types.CallbackQuery):
    await callback.message.answer('Выберите день:📅', reply_markup=client_kb.bday)
    await callback.answer()

async def button5_call(callback: types.CallbackQuery):
    await callback.message.delete()

async def button3_call(callback: types.CallbackQuery):
    await callback.message.answer('Адиль: 8708 111 62 02')
    await callback.answer()

async def button4_call(callback: types.CallbackQuery):
    await callback.message.delete()

async def budget(callback: types.CallbackQuery):
    await callback.message.answer('Какой ваш бюджет: 💳', reply_markup=client_kb.budg)
    await callback.answer()

async def button_adults(callback: types.CallbackQuery):
    await callback.message.answer('Количество взрослых(старше 16 лет): 👨‍👦‍👦', reply_markup=client_kb.adults)
    await callback.answer()

async def button_children(callback: types.CallbackQuery):
    await callback.message.answer('Количество детей(младше 16 лет):👨‍👦‍👦', reply_markup=client_kb.children)
    await callback.answer()

async def result(callback: types.CallbackQuery):
    await callback.answer("Ваш запрос обрабатывается, ожидайте ответа 💻",show_alert=True)
    await callback.message.answer('Подходящий тур по вашему запросу:')
    # await callback.answer(sqlite_db.sql_read('Подходящий тур по вашему запросу:'))
    await callback.answer()


# # @dp.message_handler(commands=['Меню'])
# async def JDam_menu_command(message : types.Message):
#         await message.answer('Подходящий тур по вашему запросу:')
#         await message.answer(sqlite_db.sql_read())





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(url_command, commands=['start'])
    dp.register_callback_query_handler(button1_call, text='button1')
    dp.register_callback_query_handler(button2_call, text='button2')
    dp.register_callback_query_handler(button3_call, text='button3')
    dp.register_callback_query_handler(button4_call, text='button4')
    dp.register_callback_query_handler(button5_call, text='button5')
    dp.register_callback_query_handler(button6_call, text='button6')
    dp.register_callback_query_handler(button7_call, text='button')
    dp.register_message_handler(menu, Text(equals='Главное меню', ignore_case=True))
    dp.register_callback_query_handler(button_day, text='button7')
    dp.register_callback_query_handler(budget, text='button8')
    dp.register_callback_query_handler(button_adults, text='button9')
    dp.register_callback_query_handler(button_children, text='button10')
    dp.register_callback_query_handler(result,  text='button11')



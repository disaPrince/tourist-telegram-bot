from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import client_kb
from aiogram.dispatcher.filters import Text
from database import db_connect


async def start(message: types.Message):
    await message.answer(message.from_user.first_name, reply_markup=client_kb.kb)
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.menu_b)
    await message.delete()


async def menu(message: types.Message):
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.menu_b)
    await message.delete()


async def information(callback: types.CallbackQuery):
    await callback.message.answer('Туристическая компания для нахождения очень выгодных туров по всему миру 🍹')
    await callback.message.answer(r'Для подробной информацией перейдите на <a href="C:\Users\JDam\Desktop\travel website\index.html">сайт компании</a>',
        parse_mode=types.ParseMode.HTML)
    await callback.answer()


async def func_from(callback: types.CallbackQuery):
    await callback.message.answer('Откуда вылетаете?📲', reply_markup=client_kb.from_b)
    await callback.answer()


async def month(callback: types.CallbackQuery):
    await callback.message.answer('Выберите месяц:📆', reply_markup=client_kb.mon_b)
    await callback.answer()


async def func_to(callback: types.CallbackQuery):
    await callback.message.answer('Выберите страну:🌃', reply_markup=client_kb.to_b)
    await callback.answer()


async def day(callback: types.CallbackQuery):
    await callback.message.answer('Выберите день:📅', reply_markup=client_kb.day_b)
    await callback.answer()

async def contacts(callback: types.CallbackQuery):
    await callback.message.answer('Адиль: 8708 111 62 02')
    await callback.answer()


async def back(callback: types.CallbackQuery):
    await callback.message.delete()


async def budget(callback: types.CallbackQuery):
    await callback.message.answer('Какой ваш бюджет: 💳', reply_markup=client_kb.budg_b)
    await callback.answer()
    await callback.message.delete()


async def adults(callback: types.CallbackQuery):
    await callback.message.answer('Количество взрослых(старше 16 лет): 👨‍👦‍👦', reply_markup=client_kb.adults_b)
    await callback.answer()
    await callback.message.delete()


async def children(callback: types.CallbackQuery):
    await callback.message.answer('Количество детей(младше 16 лет):👨‍👦‍👦', reply_markup=client_kb.child_b)
    await callback.answer()
    await callback.message.delete()


async def result(callback: types.CallbackQuery):
    await callback.answer("Ваш запрос обрабатывается, ожидайте ответа 💻", show_alert=True)
    await callback.message.answer('Подходящий тур по вашему запросу:')
    await callback.answer()
    await callback.message.delete()
    await db_connect.sql_read(callback.message)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_callback_query_handler(information, text='button1')
    dp.register_callback_query_handler(func_from, text='button2')
    dp.register_callback_query_handler(contacts, text='button3')
    dp.register_callback_query_handler(back, text='button4')
    dp.register_callback_query_handler(back, text='button5')
    dp.register_callback_query_handler(month, text='button6')
    dp.register_callback_query_handler(func_to, text='button')
    dp.register_message_handler(menu, Text(equals='Главное меню', ignore_case=True))
    dp.register_callback_query_handler(day, text='button7')
    dp.register_callback_query_handler(budget, text='button8')
    dp.register_callback_query_handler(adults, text='button9')
    dp.register_callback_query_handler(children, text='button10')
    dp.register_callback_query_handler(result, text='button11')



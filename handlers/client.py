from aiogram import bot, types
from create_bot import dp
from aiogram.dispatcher import Dispatcher
from keyboards import client_kb
from aiogram.dispatcher.filters import Text



async def url_command(message: types.Message):
    await message.answer(message.from_user.first_name, reply_markup=client_kb.kb)
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.urlkb)
    await message.delete()

async def menu(message: types.Message):
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.urlkb)

async def button1_call(callback: types.CallbackQuery):
    await callback.message.answer('Информация')
    await callback.answer()

async def button2_call(callback: types.CallbackQuery):
    await callback.message.answer('Откуда вылетаете?', reply_markup=client_kb.urlb)
    await callback.answer()

async def button6_call(callback: types.CallbackQuery):
    await callback.message.answer('Выберите месяц:', reply_markup=client_kb.urlmon)
    await callback.answer()

async def button7_call(callback: types.CallbackQuery):
    await callback.message.answer('Выберите страну:', reply_markup=client_kb.urlto)
    await callback.answer()

async def button8_call(callback: types.CallbackQuery):
    await callback.message.answer('Выберите день:', reply_markup=client_kb.urlDate)
    await callback.answer()

async def button5_call(callback: types.CallbackQuery):
    await callback.message.delete()

async def button3_call(callback: types.CallbackQuery):
    await callback.message.answer('Контактные данные')
    await callback.answer()

async def button4_call(callback: types.CallbackQuery):
    await callback.message.delete()






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
    dp.register_callback_query_handler(button8_call, text='button3')


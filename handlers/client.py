from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp
from keyboards import client_kb
from aiogram.dispatcher.filters import Text
from database import db_connect
from domain import Tours
from aiogram_calendar import DialogCalendar, dialog_cal_callback
from aiogram.types import CallbackQuery
from aiogram_calendar import simple_cal_callback, SimpleCalendar

tour = Tours.Tour

async def start(message: types.Message):
    await message.answer(message.from_user.first_name, reply_markup=client_kb.kb)
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.menu_b)

async def menu(message: types.Message):
    await message.answer('Давайте выберем поездку в Tour Bot!', reply_markup=client_kb.menu_b)


async def contacts(callback: types.CallbackQuery):
    await callback.message.answer('Адиль: 8 708 111 62 02')
    await callback.answer()

async def information(callback: types.CallbackQuery):
    await callback.message.answer('Туристическая компания для нахождения очень выгодных туров по всему миру 🍹')
    await callback.message.answer(r'Для подробной информацией перейдите на <a href=" ">сайт компании</a>', parse_mode=types.ParseMode.HTML)
    await callback.answer()

async def func_from(callback: types.CallbackQuery):
    await callback.message.answer('Откуда вылетаете?📲', reply_markup=client_kb.from_b)
    await callback.answer()

async def func_to(callback: types.CallbackQuery):
    await callback.message.answer('Выберите страну:🌃', reply_markup=client_kb.to_b)
    from_c = callback.data
    tour.parameters = [from_c.replace('b_', '', 1)]
    await callback.answer()

async def data(callback: types.CallbackQuery):
        await callback.message.reply("Дата начало тура: ", reply_markup=await SimpleCalendar().start_calendar())
        to_c = callback.data
        tour.parameters.append(to_c.replace('bu_', '', 1))
        await callback.answer()

@dp.callback_query_handler(simple_cal_callback.filter())
async def day(callback_query: CallbackQuery, callback_data: dict):
    selects, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selects:
        await callback_query.message.answer(f'Вы выбрали дату: {date.strftime("%d/%m/%Y")}')
        tour.parameters.append(date.strftime("%Y/%m/%d"))
        await callback_query.message.answer("Длителность днях: ", reply_markup=client_kb.days_b)

# async def price(message: types.Message):
#     tour.days = message.text
#     await Tour.next()
#     await message.answer("Цена: ")

# async def price(message: types.Message, state: FSMContext):
#     tour.price = message.text
#     await state.finish()

async def budget(callback: types.CallbackQuery):
    day = callback.data
    tour.parameters.append(int(day.replace('but_', '', 1)))
    await callback.message.answer('Какой ваш бюджет: 💳', reply_markup=client_kb.budg_b)
    await callback.answer()
    await callback.message.delete()

async def back(callback: types.CallbackQuery):
    await callback.message.delete()

async def result(callback: types.CallbackQuery):
    await callback.answer("Ваш запрос обрабатывается, ожидайте ответа 💻", show_alert=True)
    await callback.message.answer('Подходящий тур по вашему запросу:')
    await callback.answer()
    await callback.message.delete()
    await db_connect.sql_read(callback.message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_callback_query_handler(information, text='information')
    dp.register_callback_query_handler(contacts, text='contacts')
    dp.register_callback_query_handler(func_from, text='tours')
    dp.register_callback_query_handler(func_to, Text(startswith=('b_')))
    dp.register_callback_query_handler(data, Text(startswith=('bu_')))
    dp.register_callback_query_handler(budget, Text(startswith=('but_')))
    dp.register_callback_query_handler(back, text='back')
    dp.register_message_handler(menu, Text(equals='Главное меню', ignore_case=True))
    dp.register_callback_query_handler(result, text='button9')